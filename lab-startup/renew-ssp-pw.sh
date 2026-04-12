#!/bin/bash

#Every 180 the admin password for SSP will expire and will need to be renewed.
#This script will refresh the expired Password in the Production HOL Evironment.
#It will execute on every vPod Boot and will result in the password being new


vPodUID="admin"
vPodPW=$(</home/holuser/creds.txt) 
tmpPW=pwgen -y 16 2

echo $tmpPW

# Step 1- Change to temporary pass:
curl --location 'https://ssp.ans.lab/ssp/auth/change-password' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic YWRtaW46Vk13YXJlMTIzIVZNd2FyZTEyMyE=' \
--data "{
    'username': ${vPodUID},
    'old_password': ${vPodPW},
    'password': ${tmpPW}
}"

# Step 2- change back to same password with extension of 180days:
 curl --location 'https://ssp.ans.lab/ssp/auth/change-password' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic YWRtaW46Vk13YXJlMSFWTXdhcmUxIQ==' \
--data "{
    'username': ${vPodUID},
    'old_password': ${tmpPW},
    'password': ${vPodPW}
}"