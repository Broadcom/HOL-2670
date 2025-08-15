#!/bin/bash

. /home/holuser/.bashrc

# /bin/bash /vpodrepo/2026-labs/2670/lab-startup/enable-vmflowgen.sh | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

# ansible-playbook /vpodrepo/2026-labs/2670/lab-startup/lab-update.yml | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

ansible-playbook /vpodrepo/2026-labs/2670/mgmt-seg-pso/vDefend_DFW_Configuration.yml | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

/bin/bash /vpodrepo/2026-labs/2670/lab-startup/clear-geo.sh | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1