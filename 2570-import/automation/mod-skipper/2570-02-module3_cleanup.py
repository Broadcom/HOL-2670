'''
Python Script to FastFoward
2570-02 Module 3 - NTA
Netowrk Traffic Analysis
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



class Nta:

  def __init__(self,name='0'):
    self.name = name

  def enable(self):
    data = {'sites':['c32e766f-b5f9-42e9-be6e-c503b98f12e8'], 'detectors':['DNS_TUNNELING', 'HORIZONTAL_PORT_SCAN', 'SERVER_PORT_PROFILER', 'LLMNR_NBTNS', 'DGA', 'PORT_PROFILER', 'REMOTE_SERVICES', 'DATA_UPDOWNLOADER', 'NETWORK_TRAFFIC_DROP', 'DEST_IP_PROFILER', 'UPDOWNLOADER_TIMESERIES', 'FLOW_BEACONING', 'UNCOMMONLY_USED_PORT', 'VERTICAL_PORT_SCAN']}
    requests.post('https://{}/napp/api/v1/intelligence/nta/detectors/configuration/activate'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))

  def disable(self):
    data = {'sites':['c32e766f-b5f9-42e9-be6e-c503b98f12e8'], 'detectors':['DNS_TUNNELING', 'HORIZONTAL_PORT_SCAN', 'SERVER_PORT_PROFILER', 'LLMNR_NBTNS', 'DGA', 'PORT_PROFILER', 'REMOTE_SERVICES', 'DATA_UPDOWNLOADER', 'NETWORK_TRAFFIC_DROP', 'DEST_IP_PROFILER', 'UPDOWNLOADER_TIMESERIES', 'FLOW_BEACONING', 'UNCOMMONLY_USED_PORT', 'VERTICAL_PORT_SCAN']}
    requests.post('https://{}/napp/api/v1/intelligence/nta/detectors/configuration/deactivate'.format(nsxmgr), auth=basic, verify=False, headers=headers, data=json.dumps(data))



#Deactivating NTA

print('Deactivating NTA')

nta = Nta()

nta.disable()

print('NTA has been deactivated')

