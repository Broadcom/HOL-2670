#!/bin/bash

vPodPW=$(</home/holuser/creds.txt) 

# Malware Demo
curl -s -k -X POST -u 'admin:$vPodPW' https://vmflowgen.site-a.vcf.lab/apply?config_name=malwarepreventiondemo

# IPS Demo
curl -s -k -X POST -u 'admin:$vPodPW' https://vmflowgen.site-a.vcf.lab/apply?config_name=ipsdemo

# Intelligence Demo
curl -s -k -X POST -u 'admin:$vPodPW' https://vmflowgen.site-a.vcf.lab/apply?config_name=intelligence-hol

# vDefend Firewall demo
curl -s -k -X POST -u 'admin:$vPodPW' https://vmflowgen.site-a.vcf.lab/apply?config_name=vdefendfirewalldemo