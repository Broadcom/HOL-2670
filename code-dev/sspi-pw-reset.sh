#!/bin/bash

#Every 180 the admin password for SSP will expire and will need to be renewed.
#This script will refresh the expired Password in the Production HOL Evironment.
#It will execute on every vPod Boot and will result in the password being new


vPodUID="admin"
vPodPW=$(</home/holuser/creds.txt) 
tmpPW=$(tr -dc 'A-Za-z0-9!#$@' < /dev/urandom | head -c 16)
tmpPW+="!"

vPodTOKEN=$(echo -n "${vPodUID}:${vPodPW}" | base64)
tmpTOKEN=$(echo -n "${vPodUID}:${tmpPW}" | base64)

echo $tmpPW
echo $vPodTOKEN
echo $tmpTOKEN

echo "Setting TMP password on SSPi"
# Step 3 - Change SSPI to have a temporary Password
curl -k 'https://ssp-i.site-a.vcf.lab/sspi/operations/accounts' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic "'"${tmpTOKEN}"'"' \
--data '{
    'username': "'"${vPodUID}"'",
    'old_password': "'"${vPodPW}"'",
    'password': "'"${tmpPW}"'"
}'

echo "Setting Lab password on SSPi"
# Step 4 - Chage SSPI to have the Lab Password
curl -k 'https://ssp-i.site-a.vcf.lab/sspi/operations/accounts' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic "'"${tmpTOKEN}"'"' \
--data '{
    'username': "'"${vPodUID}"'",
    'old_password': "'"${tmpPW}"'",
    'password': "'"${vPodPW}"'"
}'