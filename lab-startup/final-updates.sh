#!/bin/bash

#This script will execute all final bash commands needed for the vPod to be ready
#The PW variable requires the file listed to be present as it is on the manager VM.
#This script will not work on the LMC

vPodPW=$(</home/holuser/creds.txt) 
sshpass -p $vPodPW scp /vpodrepo/2026-labs/2670/lab-startup/svmsshkey.txt holuser@10.1.10.130:Desktop/svmsshkey.txt