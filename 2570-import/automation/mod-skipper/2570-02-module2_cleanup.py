'''
Python Script to Cleanup
2570-02 Module 2 - Malware Prevention Configuration
NAPP Service, Distributed and GWFW
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

t1list = ['Tier-1-gateway-mars','Tier-1-gateway-VDI','Tier-1-gateway-Production','Tier-1-gateway-01','Tier-1-gateway-Development']

malwareprofilename = 'MalwareProfile'



class MalwarePrevention:

  def __init__(self,mpstatus='unknown',ccstatus='unknown',precheckstatus='unknown'):
    self.mpstatus = mpstatus
    self.ccstatus = ccstatus
    self.precheckstatus = precheckstatus

  def status(self):
    mpscall = requests.get('https://{}/napp/api/v1/platform/features/malware-prevention/status'.format(nsxmgr), auth=basic, verify=False)
    self.mpstatus = mpscall.json()
    return self.mpstatus

  def disable(self):
    data = {'action': 'UNDEPLOY'} 
    requests.post('https://{}/napp/api/v1/platform/features/malware-prevention'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))



class MpSvm:

  def __init__(self,mpsvmstatus='unknown'):
    self.mpsvmstatus = mpsvmstatus

  def status(self):
    mpsvmstatuscall = requests.get('https://{}/api/v1/malware-prevention/compute-collection/c1da5ddb-6a0c-410f-8cd9-91040f49e030%3Adomain-c1006/status'.format(nsxmgr), auth=basic, verify=False)
    self.mpsvmstatus = mpsvmstatuscall.json()
    return self.mpsvmstatus

  def delete(self):
    requests.delete('https://{}/api/v1/malware-prevention/compute-collection/c1da5ddb-6a0c-410f-8cd9-91040f49e030%3Adomain-c1006/svm-deployment'.format(nsxmgr), auth=basic, verify=False)


class AtpT1:

  def __init__(self,t1id):
    self.t1id = t1id

  def disable_idps_mp(self):
    data = {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'{}'.format(self.t1id), 'target_type':'Tier1', 'children':[{'SecurityFeatures':{'resource_type':'SecurityFeatures', 'features':[{'feature':'IDPS', 'enable':'false'}, {'feature':'MALWAREPREVENTION', 'enable':'false'}, {'feature':'TLS', 'enable':'false'}, {'feature':'IDFW', 'enable':'false'}]}, 'resource_type':'ChildSecurityFeatures'}]}]}
    requests.patch('https://{}/policy/api/v1/infra'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))



class MpGeneral:

  def __init__(self,name='0'):
    self.name = name

  def profile_delete(self):
    requests.delete('https://{}/policy/api/v1/infra/settings/firewall/security/malware-prevention-service/profiles/{}'.format(nsxmgr,malwareprofilename), auth=basic, verify=False)

  def rule_delete(self):
    data = {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'default', 'target_type':'Domain', 'children':[{'resource_type':'ChildIdsSecurityPolicy', 'marked_for_delete':'true', 'IdsSecurityPolicy':{'resource_type':'IdsSecurityPolicy', 'id':'Distributed-Malware', 'marked_for_delete':'true', 'children':[]}}]}]}
    requests.patch('https://{}/policy/api/v1/infra?enforce_revision_check=true'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))

  def rule_deletet1(self):
    data = {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'default', 'target_type':'Domain', 'children':[{'resource_type':'ChildIdsGatewayPolicy', 'marked_for_delete':'true', 'IdsGatewayPolicy':{'resource_type':'IdsGatewayPolicy', 'display_name':'Gateway-ATP', 'id':'Gateway-ATP', 'marked_for_delete':'false', 'stateful':'true', 'locked':'false', 'category':'SharedPreRules', 'sequence_number':10, 'children':[{'resource_type':'ChildIdsRule', 'marked_for_delete':'true', 'IdsRule':{'display_name':'Gateway-IDPS-Malware', 'id':'Gateway-IDPS-Malware', 'resource_type':'IdsRule', 'marked_for_delete':'true', 'source_groups':['ANY'], 'sequence_number':10, 'destination_groups':['ANY'], 'services':['ANY'], 'scope':['/infra/tier-1s/Tier-1-gateway-Production', '/infra/tier-1s/Tier-1-gateway-VDI'], 'action':'DETECT', 'direction':'IN_OUT', 'logged':'false', 'disabled':'false', 'notes':'', 'tag':'', 'ip_protocol':'IPV4_IPV6', 'ids_profiles':['/infra/settings/firewall/security/malware-prevention-service/profiles/MalwareProfile', '/infra/settings/firewall/security/intrusion-services/profiles/DefaultIDSProfile']}}]}}]}]}
    requests.patch('https://{}/policy/api/v1/infra?enforce_revision_check=true'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))

#Delete MP Rules

print('Deleting Malware Prevention Distributed Rules')

mpdemo = MpGeneral()

mpdemo.rule_delete()

time.sleep(2)



print('Deleting Malware Prevention GWFW Rules')

mpdemo.rule_deletet1()

time.sleep(2)



#Delete MP Profile

print('Deleting Malware Prevention Profile')

mpdemo.profile_delete()

time.sleep(5)



#Disabling MP and IDPS on GWFW

print('Disabling Malware Prevention and IDPS on T1s')

for tier1 in t1list:
  print('Configuring Tier-1 {}'.format(tier1))
  tier1gw = AtpT1(tier1)
  tier1gw.disable_idps_mp()
  time.sleep(5)



#Delete Malware Prevention SVM

mpsvm = MpSvm()

print('Deleting Malware Prevention SVM')

mpsvm.delete()

time.sleep(20)

print('Getting Malware Prevention SVM removal status')

mpsvmstatus = mpsvm.status()

while 'compute_collection_deployment_status' in mpsvmstatus:
  print('Cluster level MP SVM status is {}'.format(mpsvmstatus['compute_collection_deployment_status']))
  time.sleep(20)
  mpsvmstatus = mpsvm.status()

print('SVM has been deleted')



#Disable MalwarePrevention

print('Deactivating Malware-Prevention Service in NAPP')

mpsvc = MalwarePrevention()

mpsvc.disable()

checkmpsvc = mpsvc.status()

#Check if Malware-Prevention has been enabled

while checkmpsvc['status'] != 'NOT_DEPLOYED':
  print('Malware Prevention status is {}'.format(checkmpsvc['status']))
  time.sleep(20) 
  checkmpsvc = mpsvc.status() 

print('Malware-Prevention Service Deactivation Complete')


