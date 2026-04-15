#!/bin/bash

#Every 180 the admin password for SSPI will expire and will need to be renewed.
#This script will reset the timer for the expired SSPI admin passwored in Production HOL Evironment.
#It will execute on every vPod Boot and will result in the password being new

vPodPW=$(</home/holuser/creds.txt) 
tmpPW=$(tr -dc 'A-Za-z0-9!#$@' < /dev/urandom | head -c 16)
tmpPW+="!"

echo $tmpPW

sshpass -p $vPodPW ssh -t sysadmin@ssp-i.site-a.vcf.lab "echo $tmpPW | echo $tmpPW | echo $vPodPW | sudo -S /opt/vmware/vsx-operator/bin/reset_user_cred.py -u 'admin'"

echo "\nPassword set to the temporary Password listed above\n"

sleep 1m

sshpass -p $vPodPW ssh -t sysadmin@ssp-i.site-a.vcf.lab "echo $vPodPW | echo $vPodPW | echo $vPodPW | sudo -S /opt/vmware/vsx-operator/bin/reset_user_cred.py -u 'admin'"