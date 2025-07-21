'''
Python Script to FastFoward
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



class IdpsTn:

  def __init__(self,name=0):
    self.name = name

  def enable(self):
    data = {'ids_enabled':'true', 'cluster':{'target_id':'c1da5ddb-6a0c-410f-8cd9-91040f49e030:domain-c1006'}}
    requests.patch('https://{}/policy/api/v1/infra/settings/firewall/security/intrusion-services/cluster-configs/c1da5ddb-6a0c-410f-8cd9-91040f49e030%3Adomain-c1006'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))



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


  def enable(self):
    data = {'action': 'DEPLOY'} 
    requests.post('https://{}/napp/api/v1/platform/features/ndr'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))



class IdpsGeneral:

  def __init__(self,name='0'):
    self.name = name

  def enable(self):
    data = {'auto_update':'true', 'ids_events_to_syslog':'true', 'oversubscription':'BYPASSED'}
    requests.patch('https://{}/policy/api/v1/infra/settings/firewall/security/intrusion-services'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))

  def update(self):
    requests.post('https://{}/policy/api/v1/infra/settings/firewall/security/intrusion-services/signatures?action=update_signatures'.format(nsxmgr), auth=basic, verify=False, headers=headers)

  def profile(self):
    data = {'display_name':'{}'.format(idpsprofilename), 'profile_severity':['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'SUSPICIOUS'], 'pcap_config':{'pcap_enabled':'true', 'pcap_byte_count':10000, 'pcap_packet_count':5}}
    requests.put('https://{}/policy/api/v1/infra/settings/firewall/security/intrusion-services/profiles/{}'.format(nsxmgr,idpsprofilename), auth=basic, verify=False, headers=headers, data=json.dumps(data))

  def rule_create(self):
    data = {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'default', 'target_type':'Domain', 'children':[{'resource_type':'ChildIdsSecurityPolicy', 'marked_for_delete':'false', 'IdsSecurityPolicy':{'resource_type':'IdsSecurityPolicy', 'lock_modified_time':0, 'overridden':'true', 'marked_for_delete':'false', 'id':'Distributed_IDPS', 'locked':'false', 'stateful':'true', 'display_name':'Distributed IDPS', 'is_default':'false', 'sequence_number':5, 'category':'ThreatRules', 'children':[{'resource_type':'ChildIdsRule', 'marked_for_delete':'false', 'IdsRule':{'display_name':'ATP Demo', 'id':'ATP_Demo', 'resource_type':'IdsRule', 'marked_for_delete':'false', 'source_groups':['ANY'], 'sequence_number':5, 'destination_groups':['ANY'], 'services':['ANY'], 'action':'DETECT', 'direction':'IN_OUT', 'logged':'false', 'disabled':'false', 'notes':'', 'tag':'', 'ip_protocol':'IPV4_IPV6', 'ids_profiles':['/infra/settings/firewall/security/intrusion-services/profiles/Lateral-Profile'], 'scope':['/infra/domains/default/groups/ATP']}}]}}]}]} 
    requests.patch('https://{}/policy/api/v1/infra'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))



#Enable NDR 

ndr = Ndr()


#Enabling the pre-checks

ndr.prechecks_enable()

checkpc = [0,0,0]
#checkpc = [1,1,1]

#Validating the pre-checks are met

while checkpc != [1,1,1]:
  ndr.prechecks_status()
  pcsresults = ndr.precheckstatus['results'] 
  pcscounter = 0

  for check in pcsresults:
    if check['status'] != 'SUCCESS':
      print('{} is {}'.format(check['id'],check['status']))
      pcscounter = pcscounter + 1
    else:
      print('{} is {}'.format(check['id'],check['status']))
      checkpc[pcscounter] = 1
      pcscounter = pcscounter + 1
  time.sleep(10) 

print('NDR Pre-Checks done! Activating NDR')



#Enable NDR

ndr.enable()

checkndr = ndr.status()

#Check if NDR has been enabled

while checkndr['status'] != 'DEPLOYMENT_SUCCESSFUL':
  print('NDR status is {}'.format(checkndr['status']))
  time.sleep(20) 
  checkndr = ndr.status() 

print('NDR Deployment Successful')
 
  

#Enable IDPS Features

print('Enabling IDPS at the ESXi Cluster Level')

tncluster = IdpsTn()

tncluster.enable()

time.sleep(5)



print('Enabling IDPS Auto Update and Syslog')

idpsdemo = IdpsGeneral()

idpsdemo.enable()

idpsdemo.update()

time.sleep(3)



print('Creating IDPS Profile')

idpsdemo.profile()

time.sleep(3)

print('Creating IDPS Distributed Rules')

idpsdemo.rule_create()


