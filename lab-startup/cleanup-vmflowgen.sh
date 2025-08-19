#!/bin/bash

#This script will decomision each of the required topologies for HOL2670 all associated VMs will be deleted as well.
#The PW variable requires the file listed to be present as it is on the manager VM.
#This script will not work on the LMC

vPodUID="admin"
vPodPW=$(</home/holuser/creds.txt)

curl -s -k -X POST -u ${vPodUID}:${vPodPW} https://vmflowgen.site-a.vcf.lab/destroy?config_name=malwarepreventiondemo

curl -s -k -X POST -u ${vPodUID}:${vPodPW} https://vmflowgen.site-a.vcf.lab/destroy?config_name=vdefendfirewalldemo

curl -s -k -X POST -u ${vPodUID}:${vPodPW} https://vmflowgen.site-a.vcf.lab/destroy?config_name=idpsdemo

curl -s -k -X POST -u ${vPodUID}:${vPodPW} https://vmflowgen.site-a.vcf.lab/destroy?config_name=intelligence-hol