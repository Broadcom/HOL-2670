#!/bin/bash

. /home/holuser/.bashrc

#cleanup existing VMflowgen Configuration
/bin/bash /vpodrepo/2026-labs/2670/lab-startup/cleanup-vmflowgen.sh | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

#Execute and Ansible tasks to prepare the lab
ansible-playbook /vpodrepo/2026-labs/2670/lab-startup/lab-update.yml | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

#Update vmflogen topologies and libraries
/bin/bash /vpodrepo/2026-labs/2670/lab-startup/update-vmflowgen.sh | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

# Clear the GEO IP data for the lab
/bin/bash /vpodrepo/2026-labs/2670/lab-startup/clear-geo.sh | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

#Deploy the DFW policy for the management domain
ansible-playbook /vpodrepo/2026-labs/2670/mgmt-seg-pso/vDefend_DFW_Configuration.yml | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

#Deploy VMflowgen configuration
/bin/bash /vpodrepo/2026-labs/2670/lab-startup/enable-vmflowgen.sh | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1