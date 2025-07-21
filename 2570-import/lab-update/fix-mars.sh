#!/bin/bash

#Verify existing netplan information:

echo "Existing MARS-Gateway Netplan" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh nsxatp@192.168.100.200 -o StrictHostKeyChecking=accept-new 'cat /etc/netplan/01-netcfg.yaml' | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
echo "Existing MARS-Worker 1 Netplan" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh nsxatp@192.168.100.201 -o StrictHostKeyChecking=accept-new 'cat /etc/netplan/01-netcfg.yaml' | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
echo "Existing MARS-Worker 2 Netplan" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh nsxatp@192.168.100.202 -o StrictHostKeyChecking=accept-new 'cat /etc/netplan/01-netcfg.yaml' | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
echo "Existing MARS-Worker 3 Netplan" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh nsxatp@192.168.100.203 -o StrictHostKeyChecking=accept-new 'cat /etc/netplan/01-netcfg.yaml' | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

############# Gateway #################

#copy existing config file to gateway node
sshpass -p *** scp /vpodrepo/2025-labs/2570/lab-update/gateway.01-netcfg.yaml nsxatp@192.168.100.200:01-netcfg.yaml

#copy file from home directory to netplan directory and apply the netplan 
sshpass -p *** ssh nsxatp@192.168.100.200 "sudo rm /etc/netplan/01-netcfg.yaml; sudo cp 01-netcfg.yaml /etc/netplan/01-netcfg.yaml; sudo netplan apply"

#verify the ip address has been updated
echo "MARS-Gateway Configured" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh nsxatp@192.168.100.200 'ip a show dev ens192 | grep inet' | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

############# Worker 1 #################

#copy existing config file to worker node
sshpass -p *** scp /vpodrepo/2025-labs/2570/lab-update/worker1.01-netcfg.yaml nsxatp@192.168.100.201:01-netcfg.yaml

#copy file from home directory to netplan directory and apply the netplan 
sshpass -p *** ssh nsxatp@192.168.100.201 "sudo rm /etc/netplan/01-netcfg.yaml; sudo cp 01-netcfg.yaml /etc/netplan/01-netcfg.yaml; sudo netplan apply"

#verify the ip address has been updated
echo "MARS-Worker 1 Configured" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh nsxatp@192.168.100.201 'ip a show dev ens192 | grep inet' | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

############# Worker 2 #################

#copy existing config file to worker node
sshpass -p *** scp /vpodrepo/2025-labs/2570/lab-update/worker2.01-netcfg.yaml nsxatp@192.168.100.202:01-netcfg.yaml

#copy file from home directory to netplan directory and apply the netplan 
sshpass -p *** ssh nsxatp@192.168.100.202 "sudo rm /etc/netplan/01-netcfg.yaml; sudo cp 01-netcfg.yaml /etc/netplan/01-netcfg.yaml; sudo netplan apply"

#verify the ip address has been updated
echo "MARS-Worker 2 Configured" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh nsxatp@192.168.100.202 'ip a show dev ens192 | grep inet' | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

############# Worker 3 #################

#copy existing config file to worker node
sshpass -p *** scp /vpodrepo/2025-labs/2570/lab-update/worker3.01-netcfg.yaml nsxatp@192.168.100.203:01-netcfg.yaml

#copy file from home directory to netplan directory and apply the netplan 
sshpass -p *** ssh nsxatp@192.168.100.203 "sudo rm /etc/netplan/01-netcfg.yaml; sudo cp 01-netcfg.yaml /etc/netplan/01-netcfg.yaml; sudo netplan apply"

#verify the ip address has been updated
echo "MARS-Worker 3 Configured" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh nsxatp@192.168.100.203 'ip a show dev ens192 | grep inet' | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1