#!/bin/bash

#Every 180 the admin password for SSPI will expire and will need to be renewed.
#This script will reset the timer for the expired SSPI admin passwored in Production HOL Evironment.
#It will execute on every vPod Boot and will result in the password being new

vPodPW=$(</home/holuser/creds.txt) 

sshpass -p $vPodPW ssh admin@ssp-i.site-a.vcf.lab '/opt/vmware/vsx-operator/bin/reset_user_cred.py -u "admin"'
