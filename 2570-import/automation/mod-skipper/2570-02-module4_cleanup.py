'''
Python Script to Cleanup
2570-02 Module 4 - NDR Configuration
Network Detection and Response
'''


import requests

import json

import time

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

from requests.auth import HTTPBasicAuth

basic = HTTPBasicAuth('admin', '******')

nsxmgr = 'nsx-mgr.vcf.sddc.lab'

headers = {'Content-type': 'application/json'}

idpsprofilename = 'Lateral-Profile'



class Ndr:

  def __init__(self,ndrstatus='unknown',precheckstatus='unknown'):
    self.ndrstatus = ndrstatus
    self.precheckstatus = precheckstatus

  def status(self):
    ndrscall = requests.get('https://{}/napp/api/v1/platform/features/ndr/status'.format(nsxmgr), auth=basic, verify=False)
    self.ndrstatus = ndrscall.json()
    return self.ndrstatus


  def prechecks_enable(self):
    requests.post('https://{}/napp/api/v1/platform/features/ndr/pre-checks'.format(nsxmgr), auth=basic, verify=False)

  def prechecks_status(self):
    pcscall = requests.get('https://{}/napp/api/v1/platform/features/ndr/pre-checks/status'.format(nsxmgr), auth=basic, verify=False)
    self.precheckstatus = pcscall.json()
    return self.precheckstatus


  def disable(self):
    data = {'action': 'UNDEPLOY'} 
    requests.post('https://{}/napp/api/v1/platform/features/ndr'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))



class IdpsGeneral:

  def __init__(self,name='0'):
    self.name = name

  def disable(self):
    data = {'auto_update':'false', 'ids_events_to_syslog':'false', 'oversubscription':'BYPASSED'}
    requests.patch('https://{}/policy/api/v1/infra/settings/firewall/security/intrusion-services'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))

  def update(self):
    requests.post('https://{}/policy/api/v1/infra/settings/firewall/security/intrusion-services/signatures?action=update_signatures'.format(nsxmgr), auth=basic, verify=False, headers=headers)

  def profile_delete(self):
    requests.delete('https://{}/policy/api/v1/infra/settings/firewall/security/intrusion-services/profiles/{}'.format(nsxmgr,idpsprofilename), auth=basic, verify=False, headers=headers)

  def rule_delete(self):
    data = {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'default', 'target_type':'Domain', 'children':[{'resource_type':'ChildIdsSecurityPolicy', 'marked_for_delete':'false', 'IdsSecurityPolicy':{'resource_type':'IdsSecurityPolicy', 'lock_modified_time':0, 'overridden':'true', 'marked_for_delete':'false', 'id':'Distributed_IDPS', 'locked':'false', 'stateful':'true', 'display_name':'Distributed IDPS', 'is_default':'false', 'sequence_number':5, 'category':'ThreatRules', 'children':[{'resource_type':'ChildIdsRule', 'marked_for_delete':'true', 'IdsRule':{'display_name':'ATP Demo', 'id':'ATP_Demo', 'resource_type':'IdsRule', 'marked_for_delete':'true', 'source_groups':['ANY'], 'sequence_number':5, 'destination_groups':['ANY'], 'services':['ANY'], 'action':'DETECT', 'direction':'IN_OUT', 'logged':'false', 'disabled':'false', 'notes':'', 'tag':'', 'ip_protocol':'IPV4_IPV6', 'ids_profiles':['/infra/settings/firewall/security/intrusion-services/profiles/Lateral-Profile'], 'scope':['/infra/domains/default/groups/ATP']}}]}}]}]} 
    requests.patch('https://{}/policy/api/v1/infra'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))



#Deleting IDPS Distributed Rule

print('Deleting IDPS Distributed Rules')

idpsdemo = IdpsGeneral()

idpsdemo.rule_delete()

time.sleep(3)



print('Deleting IDPS Profile')

idpsdemo.profile_delete()

time.sleep(3)


#Disable NDR 

print('Deactivating NDR')

ndr = Ndr()

ndr.disable()

time.sleep(3)

checkndr = ndr.status()

#Check if NDR has been deactivated

while checkndr['status'] != 'NOT_DEPLOYED':
  print('NDR status is {}'.format(checkndr['status']))
  time.sleep(20) 
  checkndr = ndr.status() 

print('NDR has been deactivated Successfully')
 
  



