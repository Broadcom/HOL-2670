#!/bin/bash

. /home/holuser/.bashrc
ansible-playbook /vpodrepo/2025-labs/2572/lab-startup/lab-update.yml | tee -a /wmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1