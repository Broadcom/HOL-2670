# Lab Standup Automation for HOL-2572: Securing VCF with vDefend

**This section will provide the needed automation to stand up the the lab based on a single site VCF template.**

In this section you will find ansible scripts and other modules to secure a VCF management domain within the HOL environment. 

The content presented here is inline with ANSBU best practices.

---
##  Requirements for the automation


---
## DFW Configuration Setup

### Group Definitions
| Group Name | Description |
| ---------- | ---------- |
| Main_Console | HOL Only IP Set for the main console, which is outside the SDDC Framework | 
| Bastion_Zone | IP based security group that covers the IP addresses or ranges of the lab jump hosts |
| SDDC_Zone | Security group containing the SDDC Manager(s) |
| Mgmt_WLD_Zone | Security group contianing the Management components (apart from Aria) for the Mgmt WLD |
| vCenter_Zone | Security group contianing the vCenters deployed as part of a SDDC implementaiton |
| VI_WLD1_Zone | Security group contianing the Management components (apart from Aria) for the first VI WLD inclusive of IPs for ESXi Hosts |
| Aria_Zone | Security group containing the Aria suite componentes |
| InfraSvc_Zone | Security group containing the infrastructure services such as DNS, AD, Loging etc... |
| Tools_Zone | Security group containing 3rd party autoamtion tools that will be used for workloads |

### Tag Definitions
| Tag | Scope | Description |
| --- | --- | --------|
| Bastion | Zone | Tag to be applied to Identify virtual Jump Hosts | 
| SDDC | Zone | Tag to be applied to all SDDC Managers |
| vCeter | Zone | Tag to be applied to all vCenters |
| Aria | Zone | Tag to be applied to all components of the Aria Suite (Governed by LCM) |
| Mgmt_WLD | Zone | Tag to be applied to all compoents of the Mgmt WLD |
| VI_WLD1 | Zone | Tag to be applied to all virtual components of WLD 1 |
| InfraSvc | Zone | Tag to be applied to all virtual infrastructure services |
| Tools | Zone | Tag to be applied to any 3rd pary Tools |

### Policy Configruatin

**Infrastructure Section**
| Name                                      | Source                                         | Destination                                    | Service        | Context Profile | Applied To                                     | Action / Log |
|-------------------------------------------|------------------------------------------------|------------------------------------------------|----------------|-----------------|------------------------------------------------|--------------|
| Allow Bastion Zone to VCF                 | JumpHost                                       | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone ARia_Zone | HTPPS SSH 5480 |                 | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone Aria_Zone | Allow        |
| Allow VCF to InfraSvc                     | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone ARia_Zone | InfraSvc_Zone                                  |                |                 | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone ARia_Zone | Allow        |
| Allow VCF to AD                           | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone ARia_Zone | InfraSvc_Zone                                  |                | ACTIVDIR        | VCF_Zone                                       | Allow        |
| Allow 3rd Automation and Management Tools |                                                | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone ARia_Zone |                |                 | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone ARia_Zone | Allow        |

**Environment Section**
| Name                                           | Source                                         | Destination                           | Service          | Context Profile | Applied To                                     | Action / Log |
|------------------------------------------------|------------------------------------------------|---------------------------------------|------------------|-----------------|------------------------------------------------|--------------|
| Allow VCF Management                           | SDDC_Zone                                      | Mgmt_WLD_Zone  VI_WLD1_Zone ARia_Zone | HTPPS SSH        |                 | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone Aria_Zone | Allow        |
| Allow VCF ELM                                  | vCenter_Zone                                   | vCenter_Zone                          | TCP/389          |                 | vCenter_Zone                                   | Allow        |
| Allow WLD1 to WLD1                             | VI_WLD1_Zone                                   | VI_WLD1_Zone                          | Any              |                 | VI_WLD1_Zone                                   | Allow        |
| Allow 3rd Automation and Management Tools      | Aria_Zone                                      | Mgmt_WLD_Zone VI_WLD1_Zone            | HTTPS SSH        |                 | Mgmt_WLD_Zone VI_WLD1_Zone  ARia_Zone          | Allow        |
| Allow VCF WLDs to Aria Suite (for LI and vRNI) | Mgmt_WLD_Zone VI_WLD1_Zone                     | Aria_Zone                             | HTTPS SSH Syslog |                 | Mgmt_WLD_Zone VI_WLD1_Zone ARia_Zone           | Allow        |
| Allow VCF Management Outbound                  | SDDC_Zone Mgmt_WLD_Zone VI_WLD1_Zone ARia_Zone | Any                                   | HTTPS            | TLS 1.2         |                                                | Allow        |

---
## Standup procedure

The following is the order that the above ansible playbooks will need to be run in order to stand up the lab: 

1. create-edge-dpgs.yml
2. deploy-edge-nodes.yml
3. create-nsx-topology.yml
4. deploy-l2-vms.yml
5. tag-vms.yml
6. create-app-sec-groups.yml
7. create-security-groups.yml
8. create-app-policy.yml
9. create-mgmt-domain-policy.yml

