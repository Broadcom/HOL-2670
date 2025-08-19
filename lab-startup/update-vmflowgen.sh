#!/bin/bash

#This script will update VMflowgen for HOL2670
#The PW variable requires the file listed to be present as it is on the manager VM.
#This script will not work on the LMC

vPodPW=$(</home/holuser/creds.txt) 

#Copy over the updated vdefend firewall demo topology

sshpass -p $vPodPW ssh root@vmflowgen.site-a.vcf.lab  'rm /opt/vmware/vmflowgen/topologies/vdefendfirewalldemo.yaml'
sshpass -p $vPodPW scp /vpodrepo/2026-labs/2670/vmflowgen/vdefendfirewalldemo.yaml root@vmflowgen.site-a.vcf.lab:/opt/vmware/vmflowgen/topologies/vdefendfirewalldemo.yaml

#Download and copy over the update libray.yaml
#gpg --pinentry-mode=loopback --passphrase 'VMware123!VMware123!' --output /vpodrepo/2026-labs/2670/vmflowgen/library.yaml.tar.gz --decrypt /vpodrepo/2026-labs/2670/vmflowgen/library.yaml.tar.gz.gpg
#tar -xvzf /vpodrepo/2026-labs/2670/vmflowgen/library.yaml.tar.gz -C /vpodrepo/2026-labs/2670/vmflowgen

#Copy the library file to the flowgen VM
#sshpass -p $vPodPW ssh root@vmflowgen.site-a.vcf.lab  'rm /opt/vmware/vmflowgen/library.yaml'
#sshpass -p $vPodPW scp /vpodrepo/2026-labs/2670/vmflowgen/library.yaml root@vmflowgen.site-a.vcf.lab:/opt/vmware/vmflowgen/library.yaml
##sshpass -p $vPodPW ssh root@vmflowgen.site-a.vcf.lab  'systemctl restart vmflowgen'