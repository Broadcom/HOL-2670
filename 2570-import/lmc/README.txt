##################################################################
#                    Welcome to Hands-on-Labs                    #
##################################################################
   _   _  ___  _         ____  ____  ____  ___     __  ____  __
  | | | |/ _ \| |       |___ \| ___||___ |/ _ \     \ \/ /\ \/ /
  | |_| | | | | |   _____ __) |___ \  / /| | | |_____\  /  \  / 
  |  _  | |_| | |__ _____/ __/ ___) |/ / | | | |_____/  \  /  \ 
  |_| |_|\___/|____|    |_____|____//_/   \___/     /_/\_\/_/\_\
 
##################################################################
#             vDefend Firewal for VCF Private Clouds             #
##################################################################

About This Lab:

This lab environment is configured for vDfend Firewall and Advanced Threat Prevention.

This lab includes the following VMware software (including versions):

* VMware vCenter 8.0u2a
* VMware ESXi 8.0u2
* VMware NSX v4.2.0
* VMware NSX NAPP Autoamtion Appliance v4.2.0
* VMware Aria Operations for Logs 8.14.1

Lab Credentials:

+---------------------------------+-----------------------------+--------------+-----------------------------+----------------------------+
|  Application/Service            |           FQDN              |    Type      |          Username           |           Password         |
+---------------------------------+-----------------------------+--------------+-----------------------------+----------------------------+
| VMware vCenter Server           | vcenter-mgmt.vcf.sddc.lab   | sso admin    | administrator@vsphere.local | ***                 |
| VMware vCenter Server           | vcenter-mgmt.vcf.sddc.lab   | appliance    | root                        | ***                 |
| VMware ESXi                     | esxi-XX.vcf.sddc.lab        | appliance    | root                        | ***                 |
+---------------------------------+-----------------------------+--------------+-----------------------------+----------------------------+
| VMware NSX                      | nsx-mgmt.vcf.sddc.lab       | admin UI     | admin                       | ******       |
| VMware NAPP Automation          | nappa.vcf.sddc.lab          | admin UI     | admin                       | ******       |
| haproxy                         | haproxy.vcf.sddc.lab        | user         | root                        | ******       |
+---------------------------------+-----------------------------+--------------+-----------------------------+----------------------------+
| VMware Aria Operations for Logs | logs.vcf.sddc.lab           | appliance    | root                        | ***                 |
| VMware Aria Operations for Logs | logs.vcf.sddc.lab           | local admin  | admin                       | ***                 |
+---------------------------------+-----------------------------+--------------+-----------------------------+----------------------------+
| MARS                            | mars.vcf.sddc.lab           | admin UI     | N/A                         | N/A                        |
|                                 | mars-gateway-1.vcf.sddc.lab | user         | nsxatp                      | ***                   |
|                                 | mars-worker-1.vcf.sddc.lab  | user         | nsxatp                      | ***                   |
|                                 | mars-worker-2.vcf.sddc.lab  | user         | nsxatp                      | ***                   |
|                                 | mars-worker-3.vcf.sddc.lab  | user         | nsxatp                      | ***                   |
+---------------------------------+-----------------------------+--------------+-----------------------------+----------------------------+
| Application VMs                 | web-01a.vcf.sddc.lab        | user         | root                        | ***                   |
|                                 | web-02a.vcf.sddc.lab        | user         | root                        | ***                   |
|                                 | app-01a.vcf.sddc.lab        | user         | root                        | ***                   |
|                                 | db-01a.vcf.sddc.lab         | user         | root                        | ***                   |
+---------------------------------+-----------------------------+--------------+-----------------------------+----------------------------+
| vmflowgen VMS  (Linked Clones)  | flowgen (Template VM)       | N/A          | No SSH                      | No SSH                     |
|                                 | DEV-AD-01                   | N/A          | No SSH                      | No SSH                     |
|                                 | DEV-APP01                   | N/A          | No SSH                      | No SSH                     |
|                                 | DEV-DB01                    | N/A          | No SSH                      | No SSH                     |
|                                 | DEV-DNS-01                  | N/A          | No SSH                      | No SSH                     |
|                                 | dev-user01                  | N/A          | No SSH                      | No SSH                     |
|                                 | dev-user02                  | N/A          | No SSH                      | No SSH                     |
|                                 | dev-user03                  | N/A          | No SSH                      | No SSH                     |
|                                 | dev-vdi01                   | N/A          | No SSH                      | No SSH                     |
|                                 | DEV-WEB01                   | N/A          | No SSH                      | No SSH                     |
|                                 | frontend-webapp             | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-AD-01                  | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-AD-02                  | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-CRM-APP01              | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-CRM-APP02              | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-CRM-DB02               | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-CRM-WEB01              | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-CRM-WEB02              | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-DNS-01                 | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-DNS-02                 | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-eCOMM-APP01            | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-eCOMM-APP02            | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-eCOMM-DB02             | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-eCOMM-WEB01            | N/A          | No SSH                      | No SSH                     |
|                                 | PROD-eCOMM-WEB02            | N/A          | No SSH                      | No SSH                     |
|                                 | prod-user01                 | N/A          | No SSH                      | No SSH                     |
|                                 | prod-user02                 | N/A          | No SSH                      | No SSH                     |
|                                 | prod-user03                 | N/A          | No SSH                      | No SSH                     |
|                                 | VDI-001                     | N/A          | No SSH                      | No SSH                     |
|                                 | vdi01                       | N/A          | No SSH                      | No SSH                     |
|                                 | vdi02                       | N/A          | No SSH                      | No SSH                     |
+---------------------------------+-----------------------------+--------------+-----------------------------+----------------------------+
