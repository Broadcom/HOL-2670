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

echo "Temporary Password for SSP and SSPI is: $tmpPW"

echo "Setting TMP password on SSP"
# Step 1- Change to temporary pass:
curl -k -w "\n%{http_code}\n" --location 'https://ssp.site-a.vcf.lab/ssp/auth/change-password' \
-H "Content-Type: application/json" \
-u "$vPodUID:$vPodPW" \
-d "{
    \"username\": \"$vPodUID\",
    \"old_password\": \"$vPodPW\",
    \"password\": \"$tmpPW\"
}"

echo "Setting TMP password on SSPi"
# Step 3 - Change SSPI to have a temporary Password
curl -k -w "\n%{http_code}\n" --location --request POST 'https://ssp-i.site-a.vcf.lab/sspi/operations/accounts' \
-H "Content-Type: application/json" \
-u "$vPodUID:$vPodPW" \
-d "{
    \"account_name\": \"$vPodUID\",
    \"current_password\": \"$vPodPW\",
    \"new_password\": \"$tmpPW\"
}"

sleep 2m

echo "Setting Lab password on SSP"
# Step 2- change back to same password with extension of 180days:
 curl -k -w "\n%{http_code}\n" --location 'https://ssp.site-a.vcf.lab/ssp/auth/change-password' \
-H "Content-Type: application/json" \
-u "$vPodUID:$tmpPW" \
-d "{
    \"username\": \"$vPodUID\",
    \"old_password\": \"$tmpPW\",
    \"password\": \"$vPodPW\"
}"

echo "Setting Lab password on SSPi"
# Step 4 - Chage SSPI to have the Lab Password
curl -k -w "\n%{http_code}\n" --location --request POST 'https://ssp-i.site-a.vcf.lab/sspi/operations/accounts' \
-H "Content-Type: application/json" \
-u "$vPodUID:$tmpPW" \
-d "{
    \"account_name\": \"$vPodUID\",
    \"current_password\": \"$tmpPW\",
    \"new_password\": \"$vPodPW\"
}"