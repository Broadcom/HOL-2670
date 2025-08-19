#!/bin/bash

#This script will deploy each of the required topologies for HOL2670
#The PW variable requires the file listed to be present as it is on the manager VM.
#This script will not work on the LMC


vPodUID="admin"
vPodPW=$(</home/holuser/creds.txt) 

# Malware Demo
curl -s -k -X POST -u ${vPodUID}:${vPodPW} https://vmflowgen.site-a.vcf.lab/apply?config_name=malwarepreventiondemo

# IPS Demo
curl -s -k -X POST -u ${vPodUID}:${vPodPW} https://vmflowgen.site-a.vcf.lab/apply?config_name=idpsdemo

# Intelligence Demo
curl -s -k -X POST -u ${vPodUID}:${vPodPW} https://vmflowgen.site-a.vcf.lab/apply?config_name=intelligence-hol

# vDefend Firewall demo
curl -s -k -X POST -u ${vPodUID}:${vPodPW} https://vmflowgen.site-a.vcf.lab/apply?config_name=vdefendfirewalldemo