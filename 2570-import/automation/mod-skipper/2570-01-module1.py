'''
Python Script to FastFoward 
2570-01 Module 1 - DFW Configuration
Distributed FW Layer 4
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



class Dfw:

  def __init__(self,name='0'):
    self.name = name

  def rule_enable(self):
    data = {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'default', 'target_type':'Domain', 'children':[{'resource_type':'ChildSecurityPolicy', 'marked_for_delete':'false', 'SecurityPolicy':{'resource_type':'SecurityPolicy', 'lock_modified_time':0, 'overridden':'false', 'logging_enabled':'false', 'marked_for_delete':'false', 'scope':['ANY'], 'id':'3-tier-app', 'locked':'false', 'stateful':'true', 'tcp_strict':'true', 'target_type':'DFW', 'display_name':'3-tier-app', 'is_default':'false', 'sequence_number':10, 'category':'Application', 'children':[{'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-web-servers'], 'action':'ALLOW', 'disabled':'false', 'id':'3-tier-client-access', 'tag':'3-tier-client-access', 'direction':'IN_OUT', 'source_groups':['ANY'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/HTTPS', '/infra/services/HTTP'], 'display_name':'3-tier-client-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'rule_id':4100, 'sequence_number':10, 'sources_excluded':'false'}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-app-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-app-servers', '/infra/domains/default/groups/3-tier-web-servers'], 'action':'ALLOW', 'disabled':'false', 'id':'web-to-app-access', 'tag':'web-to-app-access', 'direction':'IN_OUT', 'source_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/TCP-8443'], 'display_name':'web-to-app-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'rule_id':4101, 'sequence_number':15, 'sources_excluded':'false'}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-db-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-app-servers', '/infra/domains/default/groups/3-tier-db-servers'], 'action':'ALLOW', 'disabled':'false', 'id':'app-to-db-access', 'tag':'app-to-db-access', 'direction':'IN_OUT', 'source_groups':['/infra/domains/default/groups/3-tier-app-servers'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/MySQL'], 'display_name':'app-to-db-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'rule_id':4102, 'sequence_number':20, 'sources_excluded':'false'}}]}}, {'resource_type':'ChildSecurityPolicy', 'marked_for_delete':'false', 'SecurityPolicy':{'resource_type':'SecurityPolicy', 'lock_modified_time':0, 'overridden':'false', 'logging_enabled':'false', 'marked_for_delete':'false', 'scope':['ANY'], 'id':'default-layer3-section', 'locked':'false', 'stateful':'true', 'tcp_strict':'false', 'display_name':'Default Layer3 Section', 'is_default':'true', 'sequence_number':2147483647, 'internal_sequence_number':2147483647, 'category':'Application', 'children':[{'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'destination_groups':['ANY'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'false', 'scope':['ANY'], 'action':'DROP', 'disabled':'false', 'id':'default-layer3-rule', 'direction':'IN_OUT', 'source_groups':['ANY'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['ANY'], 'display_name':'Default Layer3 Rule', 'is_default':'true', 'ip_protocol':'IPV4_IPV6', 'rule_id':2, 'sequence_number':2147483647, 'sources_excluded':'false'}}]}}]}]} 
    requests.patch('https://{}/policy/api/v1/infra'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))

  def rule_disable(self):
    data = {'resource_type':'Infra', 'children':[{'resource_type':'ChildResourceReference', 'id':'default', 'target_type':'Domain', 'children':[{'resource_type':'ChildSecurityPolicy', 'marked_for_delete':'false', 'SecurityPolicy':{'resource_type':'SecurityPolicy', 'lock_modified_time':0, 'overridden':'false', 'logging_enabled':'false', 'marked_for_delete':'false', 'scope':['ANY'], 'id':'3-tier-app', 'locked':'false', 'stateful':'true', 'tcp_strict':'true', 'target_type':'DFW', 'display_name':'3-tier-app', 'is_default':'false', 'sequence_number':10, 'category':'Application', 'children':[{'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-web-servers'], 'action':'ALLOW', 'disabled':'true', 'id':'3-tier-client-access', 'tag':'3-tier-client-access', 'direction':'IN_OUT', 'source_groups':['ANY'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/HTTPS', '/infra/services/HTTP'], 'display_name':'3-tier-client-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'rule_id':4100, 'sequence_number':10, 'sources_excluded':'false'}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-app-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-app-servers', '/infra/domains/default/groups/3-tier-web-servers'], 'action':'ALLOW', 'disabled':'true', 'id':'web-to-app-access', 'tag':'web-to-app-access', 'direction':'IN_OUT', 'source_groups':['/infra/domains/default/groups/3-tier-web-servers'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/TCP-8443'], 'display_name':'web-to-app-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'rule_id':4101, 'sequence_number':15, 'sources_excluded':'false'}}, {'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'notes':'', 'destination_groups':['/infra/domains/default/groups/3-tier-db-servers'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'true', 'scope':['/infra/domains/default/groups/3-tier-app-servers', '/infra/domains/default/groups/3-tier-db-servers'], 'action':'ALLOW', 'disabled':'true', 'id':'app-to-db-access', 'tag':'app-to-db-access', 'direction':'IN_OUT', 'source_groups':['/infra/domains/default/groups/3-tier-app-servers'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['/infra/services/MySQL'], 'display_name':'app-to-db-access', 'is_default':'false', 'ip_protocol':'IPV4_IPV6', 'rule_id':4102, 'sequence_number':20, 'sources_excluded':'false'}}]}}, {'resource_type':'ChildSecurityPolicy', 'marked_for_delete':'false', 'SecurityPolicy':{'resource_type':'SecurityPolicy', 'lock_modified_time':0, 'overridden':'false', 'logging_enabled':'false', 'marked_for_delete':'false', 'scope':['ANY'], 'id':'default-layer3-section', 'locked':'false', 'stateful':'true', 'tcp_strict':'false', 'display_name':'Default Layer3 Section', 'is_default':'true', 'sequence_number':2147483647, 'internal_sequence_number':2147483647, 'category':'Application', 'children':[{'resource_type':'ChildRule', 'marked_for_delete':'false', 'Rule':{'destination_groups':['ANY'], 'overridden':'false', 'marked_for_delete':'false', 'logged':'false', 'scope':['ANY'], 'action':'ALLOW', 'disabled':'false', 'id':'default-layer3-rule', 'direction':'IN_OUT', 'source_groups':['ANY'], 'destinations_excluded':'false', 'resource_type':'Rule', 'profiles':['ANY'], 'services':['ANY'], 'display_name':'Default Layer3 Rule', 'is_default':'true', 'ip_protocol':'IPV4_IPV6', 'rule_id':2, 'sequence_number':2147483647, 'sources_excluded':'false'}}]}}]}]} 
    requests.patch('https://{}/policy/api/v1/infra'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))




print('Enabling DFW Default Rule to Drop and 3-Tier-App Security Policy')

dfwdemo = Dfw()

dfwdemo.rule_enable()

time.sleep(3)

print('DFW configurations have been finished')

