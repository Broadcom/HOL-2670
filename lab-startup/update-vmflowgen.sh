#!/bin/bash

#This script will update VMflowgen for HOL2670
#The PW variable requires the file listed to be present as it is on the manager VM.
#This script will not work on the LMC

vPodPW=$(</home/holuser/creds.txt) 

#Copy over the updated vdefend firewall demo topology

sshpass -p $vPodPW ssh root@vmflowgen.site-a.vcf.lab  'rm /opt/vmware/vmflowgen/topologies/vdefendfirewalldemo.yaml'
sshpass -p $vPodPW scp /vpodrepo/2026-labs/2670/vmflowgen/vdefendfirewalldemo.yaml root@vmflowgen.site-a.vcf.lab:/opt/vmware/vmflowgen/topologies/vdefendfirewalldemo.yaml

#Download and copy over the update libray.yaml
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1gTZJhDqQLg7Q6A6Oe3_JveTysgvQh3JL' -O /home/holuser/library.yaml.tar.gz.gpg
gpg --pinentry-mode=loopback --passphrase 'VMware123!VMware123!' --output /home/holuser/library.yaml.tar.gz --decrypt /home/holuser/library.yaml.tar.gz.gpg
tar -xvzf /home/holuser/vmflowgen/library.yaml.tar.gz -C /home/holuser/vmflowgen

Copy the library file to the flowgen VM
sshpass -p $vPodPW ssh root@vmflowgen.site-a.vcf.lab  'rm /opt/vmware/vmflowgen/library.yaml'
sshpass -p $vPodPW scp /home/holuser/library.yaml root@vmflowgen.site-a.vcf.lab:/opt/vmware/vmflowgen/library.yaml
sshpass -p $vPodPW ssh root@vmflowgen.site-a.vcf.lab  'systemctl restart vmflowgen'