#!/bin/bash

####################################################
###             Update ModuleSwitcher            ###
####################################################

echo "Starting ModuleSwitcher Corrections" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

cp /vpodrepo/2025-labs/2570/lab-update/fsginstall.sh /lmchol/tmp/fsginstall.sh
sshpass -p *** ssh holuser@mainconsole '/usr/bin/sh /tmp/fsginstall.sh'
cp /vpodrepo/2025-labs/2570/lab-update/main_ui.py /lmchol/hol/ModuleSwitcher/main_ui.py
echo "Finished ModuleSwitcher Corrections. Review /tmp/fsginstall.out on the LMC." | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

####################################################
###               Correct MARS VMS               ###
####################################################

echo "Starting MARS VM Corrections" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
. /vpodrepo/2025-labs/2570/lab-update/fix-mars.sh
echo "MARS VM Corrections Complete" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1

####################################################
###               Correct NAPP VMS               ###
####################################################

echo "Starting NAPP VM Corrections" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
python3 /vpodrepo/2025-labs/2570/lab-update/fix-napp.py | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
echo "Completing NAPP VM Corrections" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1


####################################################
###                Update Firefox                ###
####################################################

sshpass -p *** scp /vpodrepo/2025-labs/2570/lab-update/prefs.js holuser@10.0.0.2:/home/holuser/.mozilla/firefox/jx0nv8m0.default-release/prefs.js
sshpass -p *** scp /vpodrepo/2025-labs/2570/lab-update/content-prefs.sqlite holuser@10.0.0.2:/home/holuser/.mozilla/firefox/jx0nv8m0.default-release/content-prefs.sqlite


####################################################
###             Update ModuleSwitcher            ###
####################################################

echo "Starting ModuleSwitcher Corrections" | tee -a /lmchol/hol/labstartup.log >> /home/holuser/hol/labstartup.log 2>&1
sshpass -p *** ssh holuser@mainconsole pip3 install FreeSimpleGUI
cp /vpodrepo/2025-labs/2570/lab-update/main_ui.py /lmchol/hol/ModuleSwitcher/main_ui.py

