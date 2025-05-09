#!/bin/bash

#Pull password from the creds.txt file in the manager home directory.
file="/home/holuser/creds.txt"
read -d $'\x04' password < "$file"
echo $password

sshpass -p $password scp /home/holuser/vpodrepo/2026-labs/2670/lab-standup/dnsmasq_configmap.yml root@router:/holodeck-runtime/dnsmasq/dnsmasq_configmap.yml
sshpass -p $password ssh root@router 'kubectl apply -f /holodeck-runtime/dnsmasq/dnsmasq_configmap.yaml'
sshpass -p $password ssh root@router 'kubectl rollout restart deployment/dnsmasq-deployment'