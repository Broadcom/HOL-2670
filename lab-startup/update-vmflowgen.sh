#!/bin/bash

#This script will update VMflowgen for HOL2670
#The PW variable requires the file listed to be present as it is on the manager VM.
#This script will not work on the LMC

vPodPW=$(</home/holuser/creds.txt) 

#Copy over the updated vdefend firewall demo topology

sshpass -p $vPodPW ssh root@vmflowgen.site-a.vcf.lab  'rm /opt/vmware/vmflowgen/topologies/defendfirewalldemo.yaml'
sshpass -p $vPodPW scp /vpodrepo/2026-labs/2670/vmflowgen/vdefendfirewalldemo.yaml root@vmflowgen.site-a.vcf.lab:/opt/vmware/vmflowgen/topologies/defendfirewalldemo.yaml

#Download and copy over the update libray.yaml