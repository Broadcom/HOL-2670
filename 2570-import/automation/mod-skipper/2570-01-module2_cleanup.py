'''
Python Script to FastFoward 
2570-01 Module 1 - DFW Configuration
Distributed FW and Context Profile
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

cpl7id = 'tlsv12'
cpl7displayname = 'TLS 1.2'
cptlsversion = 'TLS_V12' 

cpl7id2 = 'tls-insecure'
cpl7displayname2 = 'tls-insecure'
cptlsversion2 = 'TLS_V11' 


class ContextProfile:

  def __init__(self,l7id=0,l7displayname=0,tlsversion=0):
    self.l7id = l7id
    self.l7displayname = l7displayname
    self.tlsversion = tlsversion

  def create(self):
    data = {'display_name':'{}'.format(self.l7displayname), 'attributes':[{'key':'APP_ID', 'datatype':'STRING', 'sub_attributes':[{'key':'TLS_VERSION', 'value':['{}'.format(self.tlsversion)], 'datatype':'STRING'}], 'value':['SSL']}], 'id':'{}'.format(self.l7id)} 
    requests.put('https://{}/policy/api/v1/infra/context-profiles/{}'.format(nsxmgr,self.l7id), auth=basic, verify=False, headers=headers, data=json.dumps(data))

  def delete(self):
    requests.delete('https://{}/policy/api/v1/infra/context-profiles/{}'.format(nsxmgr,self.l7id), auth=basic, verify=False, headers=headers)



class Dfw:

  def __init__(self,name='0'):
    self.name = name

  def rule_enable(self):
    data =  {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'default', 'target_type':'Domain', 'children':[{'resource_type':'ChildSecurityPolicy', 'marked_for_delete':'false', 'SecurityPolicy':{'resource_type':'SecurityPolicy', 'lock_modified_time':0, 'overridden':'false', 'logging_enabled':'false', 'marked_for_delete':'false', 'scope':['ANY'], 'id':'3-tier-app', 'locked':'false', 'stateful':'true', 'tcp_strict':'true', 'target_type':'DFW', 'display_name':'3-tier-app', 'is_default':'false', 'sequence_number':10, 'category':'Application', 'children':[{'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'display_name':'block-3-tier-client-access-insecure', 'id':'block-3-tier-client-access-insecure', 'resource_type':'Rule', 'marked_for_delete':'false', 'source_groups':['ANY'], 'sequence_number':5, 'destination_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'services':['/infra/services/HTTPS'], 'profiles':['/infra/context-profiles/tls-insecure'], 'scope':['/infra/domains/default/groups/3-tier-web-servers'], 'action':'DROP', 'direction':'IN_OUT', 'logged':'true', 'disabled':'false', 'notes':'', 'tag':'3-tier-client-access', 'ip_protocol':'IPV4_IPV6', 'overridden':'false', 'destinations_excluded':'false', 'is_default':'false', 'sources_excluded':'false', 'service_entries':[]}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-web-servers'], 'action':'ALLOW', 'disabled':'false', 'id':'3-tier-client-access', 'tag':'3-tier-client-access', 'direction':'IN_OUT', 'source_groups':['ANY'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['/infra/context-profiles/tlsv12'], 'services':['/infra/services/HTTPS'], 'display_name':'3-tier-client-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'sequence_number':10, 'sources_excluded':'false', 'service_entries':[]}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-app-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-app-servers', '/infra/domains/default/groups/3-tier-web-servers'], 'action':'ALLOW', 'disabled':'false', 'id':'web-to-app-access', 'tag':'web-to-app-access', 'direction':'IN_OUT', 'source_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['/infra/context-profiles/SSL'], 'services':['/infra/services/TCP-8443'], 'display_name':'web-to-app-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'sequence_number':15, 'sources_excluded':'false'}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-db-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-app-servers', '/infra/domains/default/groups/3-tier-db-servers'], 'action':'ALLOW', 'disabled':'false', 'id':'app-to-db-access', 'tag':'app-to-db-access', 'direction':'IN_OUT', 'source_groups':['/infra/domains/default/groups/3-tier-app-servers'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['/infra/context-profiles/MYSQL'], 'services':['/infra/services/MySQL'], 'display_name':'app-to-db-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'sequence_number':20, 'sources_excluded':'false'}}]}}, {'resource_type':'ChildSecurityPolicy', 'marked_for_delete':'false', 'SecurityPolicy':{'resource_type':'SecurityPolicy', 'lock_modified_time':0, 'overridden':'false', 'logging_enabled':'false', 'marked_for_delete':'false', 'scope':['ANY'], 'id':'default-layer3-section', 'locked':'false', 'stateful':'true', 'tcp_strict':'false', 'display_name':'Default Layer3 Section', 'is_default':'true', 'sequence_number':2147483647, 'internal_sequence_number':2147483647, 'category':'Application', 'children':[{'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'destination_groups':['ANY'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'false', 'scope':['ANY'], 'action':'DROP', 'disabled':'false', 'id':'default-layer3-rule', 'direction':'IN_OUT', 'source_groups':['ANY'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['ANY'], 'display_name':'Default Layer3 Rule', 'is_default':'true', 'ip_protocol':'IPV4_IPV6', 'rule_id':2, 'sequence_number':2147483647, 'sources_excluded':'false'}}]}}]}]}
    requests.patch('https://{}/policy/api/v1/infra'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))

  def rule_disable(self):
    data = {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'default', 'target_type':'Domain', 'children':[{'resource_type':'ChildSecurityPolicy', 'marked_for_delete':'false', 'SecurityPolicy':{'resource_type':'SecurityPolicy', 'lock_modified_time':0, 'overridden':'false', 'logging_enabled':'false', 'marked_for_delete':'false', 'scope':['ANY'], 'id':'3-tier-app', 'locked':'false', 'stateful':'true', 'tcp_strict':'true', 'target_type':'DFW', 'display_name':'3-tier-app', 'is_default':'false', 'sequence_number':10, 'category':'Application', 'children':[{'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-web-servers'], 'action':'ALLOW', 'disabled':'true', 'id':'3-tier-client-access', 'tag':'3-tier-client-access', 'direction':'IN_OUT', 'source_groups':['ANY'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/HTTPS', '/infra/services/HTTP'], 'display_name':'3-tier-client-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'sequence_number':10, 'sources_excluded':'false', 'service_entries':[]}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-app-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-app-servers', '/infra/domains/default/groups/3-tier-web-servers'], 'action':'ALLOW', 'disabled':'true', 'id':'web-to-app-access', 'tag':'web-to-app-access', 'direction':'IN_OUT', 'source_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/TCP-8443'], 'display_name':'web-to-app-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'sequence_number':15, 'sources_excluded':'false'}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-db-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-app-servers', '/infra/domains/default/groups/3-tier-db-servers'], 'action':'ALLOW', 'disabled':'true', 'id':'app-to-db-access', 'tag':'app-to-db-access', 'direction':'IN_OUT', 'source_groups':['/infra/domains/default/groups/3-tier-app-servers'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/MySQL'], 'display_name':'app-to-db-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'sequence_number':20, 'sources_excluded':'false'}}, {'resource_type':'ChildRule', 'marked_for_delete':'true', 'Rule':{'id':'block-3-tier-client-access-insecure', 'marked_for_delete':'true', 'resource_type':'Rule'}}]}}, {'resource_type':'ChildSecurityPolicy', 'marked_for_delete':'false', 'SecurityPolicy':{'resource_type':'SecurityPolicy', 'lock_modified_time':0, 'overridden':'false', 'logging_enabled':'false', 'marked_for_delete':'false', 'scope':['ANY'], 'id':'default-layer3-section', 'locked':'false', 'stateful':'true', 'tcp_strict':'false', 'display_name':'Default Layer3 Section', 'is_default':'true', 'sequence_number':2147483647, 'internal_sequence_number':2147483647, 'category':'Application', 'children':[{'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'destination_groups':['ANY'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'false', 'scope':['ANY'], 'action':'ALLOW', 'disabled':'false', 'id':'default-layer3-rule', 'direction':'IN_OUT', 'source_groups':['ANY'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['ANY'], 'display_name':'Default Layer3 Rule', 'is_default':'true', 'ip_protocol':'IPV4_IPV6', 'sequence_number':2147483647, 'sources_excluded':'false'}}]}}]}]}  
    requests.patch('https://{}/policy/api/v1/infra'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))




print('Setting DFW Default Rule to Allow and Disabling 3-Tier-App Security Policy')

dfwdemo = Dfw()

dfwdemo.rule_disable()

time.sleep(3)



#Delete L7 Context Profiles

print('Deleting L7 Application Context Profile {}'.format(cpl7displayname))

l7tls12 = ContextProfile(l7id=cpl7id,l7displayname=cpl7displayname,tlsversion=cptlsversion)

l7tls12.delete()

time.sleep(3)



print('Deleting L7 Application Context Profile {}'.format(cpl7displayname2))

l7tls11 = ContextProfile(l7id=cpl7id2,l7displayname=cpl7displayname2,tlsversion=cptlsversion2)

l7tls11.delete()

time.sleep(3)



print('DFW configurations have been finished')


