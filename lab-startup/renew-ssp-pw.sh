#!/bin/bash

#Every 180 the admin password for SSP will expire and will need to be renewed.
#This script will refresh the expired Password in the Production HOL Evironment.
#It will execute on every vPod Boot and will result in the password being new


vPodUID="admin"
vPodPW=$(</home/holuser/creds.txt) 
tmpPW=pwgen -y 16 2

vPodTOKEN=$(echo -n "${vPodUID}:${vPodPW}" | base64)
tmpTOKEN=$(echo -n "${vPodUID}:${tmpPW}" | base64)

echo $tmpPW

# Step 1- Change to temporary pass:
curl --location 'https://ssp.site-a.vcf.lab/ssp/auth/change-password' \
--header 'Content-Type: application/json' \
--header "Authorization: Basic ${vPodTOKEN}" \
--data "{
    'username': ${vPodUID},
    'old_password': ${vPodPW},
    'password': ${tmpPW}
}"

# Step 2- change back to same password with extension of 180days:
 curl --location 'https://ssp.site-a.vcf.lab/ssp/auth/change-password' \
--header 'Content-Type: application/json' \
--header "Authorization: Basic ${tmpTOKEN}" \
--data "{
    'username': ${vPodUID},
    'old_password': ${tmpPW},
    'password': ${vPodPW}
}"

# Step 3 - Change SSPI to have a temporary Password
curl 'https://sspi.site-a.vcf.lab/sspi/operations/accounts' \
--header 'Content-Type: application/json' \
--header "Authorization: Basic ${tmpTOKEN}" \
--data "{
    'username': ${vPodUID},
    'old_password': ${vPodPW},
    'password': ${tmpPW}
}"

# Step 4 - Chage SSPI to have the Lab Password
curl 'https://sspi.site-a.vcf.lab/sspi/operations/accounts' \
--header 'Content-Type: application/json' \
--header "Authorization: Basic ${tmpTOKEN}" \
--data "{
    'username': ${vPodUID},
    'old_password': ${tmpPW},
    'password': ${vPodPW}
}"