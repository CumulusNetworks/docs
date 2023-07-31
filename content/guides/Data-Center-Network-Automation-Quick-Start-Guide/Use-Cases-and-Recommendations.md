---
title: Use Cases and Recommendations
author: NVIDIA
weight: 40
product: Technical Guides
imgData: guides
---
In the world of data center automation and deployment, Day 0, Day 1, Day 2 and Day N are widely used terms to determine the stage of the device configuration and usage. The classification determines when the configurations are applied.

- **Day 0** configuration is the initial minimal configuration with which the switch starts up, based on the topology and network architecture that has been designed.
- **Day 1** configuration includes setting up common services like NTP, syslog, and so on.
- **Day 2** to **Day N** are the configurations you push to the device for day-to-day operations. This also includes patching and upgrading based on the changing needs of the environment.

## Automation Options

| Options | Recommendations |
| ------- | --------------- |
| Flat file automation | You must explicitly tell NVUE to ignore flat files pushed with automation methods outside of NVUE. |
| REST API driven automation | NVUE is one hundred percent API driven and all features are accessible with the API. You can use the API for automation by any tool or script that can interacts with REST, such as Ansible, Python, Postman, and so on. |
| NVUE configuration file automation | You can automate and apply the startup.yaml file. You can do this today using PRA, as mentioned above. |

## Integrate with Existing Tools

| Tools | Recommendation |
| ----- | -------------- |
| **Ansible** |For Day 0 configurations, you can use the PRA package to automate `startup.yaml` file generation or use the Ansible modules to set up the configuration as desired and run it across all the switches.</br>For Day 1 through day N configurations, you can leverage the Ansible modules that are available to make configuration changes on the go. |
| **Salt** | For Day 0 configurations, you can automate `startup.yaml` file generation.</br>For Day 1 through day N configurations, you can automate startup.yaml file updates and apply them on the switches. |
| **Puppet** |For Day 0 configurations, you can automate `startup.yaml` file generation.</br>For Day 1 through day N configurations, you can use the `http_request` module to interact with NVUE API. |
| **Scripts** | Most programming languages support making REST API calls. Use the RESTful NVUE API to integrate into your existing automation scripts. |

## Code Snippets

Using the REST API to make any updates (PATCH) is a multi step process:
1. Create a new revision ID.
2. Make the change using a PATCH request against the revision ID recorded in the previous step.
3. Apply the changes to the revision changeset.
4. Review the status of the applied revision. This step is optional.

You can combine multiple PATCH requests into one revision.

You can change configuration settings either at the root level or the object level. With a root patch, you can push all configurations to the switch in bulk. With a targeted configuration patch, you can control individual resources.

The examples below use curl. You can use any tool or programming language.

### Revisions

1. View the current applied configuration.

   {{< tabs "TabID49 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -k -X GET "https://127.0.0.1:8765/nvue_v1/?rev=applied&filled=false" 
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
"acl": {}, 
  "bridge": { 
    "domain": { 
      "br_default": { 
        "encap": "802.1Q", 
        "mac-address": "auto", 
        "multicast": { 
          "snooping": { 
            "enable": "off" 
          } 
        }, 
        "stp": { 
          "priority": 32768, 
          "state": { 
            "up": {} 
          } 
        }, 
        "type": "vlan-aware", 
        "untagged": 1, 
        "vlan": { 
          "10": { 
            "multicast": { 
              "snooping": { 
                "querier": { 
                  "source-ip": "0.0.0.0" 
                } 
              } 
            }, 
            "ptp": { 
              "enable": "off" 
            }, 
            "vni": { 
              "10": { 
                "flooding": { 
                  "enable": "auto" 
                }, 
                "mac-learning": "auto" 
              } 
.... 
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config show
```

{{< /tab >}}
{{< /tabs >}}

2. Create a new revision ID.

     {{< tabs "TabID113 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -k -X POST https://127.0.0.1:8765/nvue_v1/revision
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{ 

"changeset/cumulus/2023-04-06_20.22.44_T2XP": { 
    "state": "pending", 
    "transition": { 
      "issue": {}, 
      "progress": "" 
    } 
} 
}
```

{{< /tab >}}
{{< /tabs >}}

3. Apply the revision changeset after you push all the configurations.

   {{%notice note%}}
Cumulus Linux applies but does not save the configuration; the configuration does not persist after a reboot.
{{%/notice%}}

     {{< tabs "TabID142 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"state":"apply","auto-prompt":{"ays":"ays_yes"}}' -H 'Content-Type:application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/revision/changeset%2Fcumulus%2F2023-04-06_20.22.44_T2XP
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{ 
  "state": "apply", 
  "transition": { 
    "issue": {}, 
    "progress": "" 
  } 
} 
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

4. Review the revision.

     {{< tabs "TabID174 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -k -X GET https://127.0.0.1:8765/nvue_v1/revision/changeset%2Fcumulus%2F2023-04-06_20.22.44_T2XP
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{ 
  "state": "applied", 
  "transition": { 
    "issue": {}, 
    "progress": "" 
  } 
} 
```

{{< /tab >}}
{{< /tabs >}}

5. Save a revision. Save an applied configuration change to the startup configuration (`/etc/nvue.d/startup.yaml`) so that the changes persist after a reboot.

     {{< tabs "TabID199 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -k -X PATCH -d '{"state": "save", "auto-prompt": {"ays": "ays_yes"}}' -H 'Content-Type: application/json'  https://127.0.0.1:8765/nvue_v1/revision/applied 
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{ 
  "state": "save", 
  "transition": { 
    "issue": {}, 
    "progress": "" 
  } 
} 
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config save
```

{{< /tab >}}
{{< /tabs >}}

### Day 0 - Set Up Basic Connectivity

**Interfaces**

1. Set the loopback interface IP address.

     {{< tabs "TabID237 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"99.99.99.99/32": {}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/interface/lo/ip/address?rev=changeset%2Fcumulus%2F2023-04-06_20.22.44_T2XP
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{   
"99.99.99.99/32": {}  
}
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv set interface lo ip address 99.99.99.99/32
```

{{< /tab >}}
{{< /tabs >}}

2. Review the IP address after you apply the revision.

   {{< tabs "TabID265 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -k -X GET https://127.0.0.1:8765/nvue_v1/interface/lo/ip/address
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{   
"127.0.0.1/8": {},   
"99.99.99.99/32": {}, 
"::1/128": {}  
}
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv show interface lo ip address
```

{{< /tab >}}
{{< /tabs >}}

### Day 1 - Set Up Common Services

**System Hostname and time zone**

{{< tabs "TabID297 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"hostname":"switch01","timezone":"America/Los_Angeles"}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/system?rev=changeset%2Fcumulus%2F2023-04-06_20.31.58_T2XR
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{}  
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv set system hostname switch01 
cumulus@switch:~$ nv set system timezone America/Los_Angeles
```

{{< /tab >}}
{{< /tabs >}}

**NTP**

{{< tabs "TabID324 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"default":{"server:{"4.cumulusnetworks.pool.ntp.org":{"iburst":"on"}}}}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/service/ntp?rev=changeset%2Fcumulus%2F2023-04-06_20.31.58_T2XR
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{} 
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv set service ntp default server 4.cumulusnetworks.pool.ntp.org iburst on 
```

{{< /tab >}}
{{< /tabs >}}

**DNS**

{{< tabs "TabID350 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"mgmt":{"server:{"192.168.1.100":{}}}}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/service/dns?rev=changeset%2Fcumulus%2F2023-04-06_20.31.58_T2XR
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{} 
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv set service dns mgmt server 192.168.1.100
```

{{< /tab >}}
{{< /tabs >}}

**Syslog**

{{< tabs "TabID376 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"mgmt":{"server:{"192.168.1.120":{"port":8000}}}}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/service/syslog?rev=changeset%2Fcumulus%2F2023-04-06_20.31.58_T2XR
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{} 
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv set service syslog mgmt server 192.168.1.120 port 8000
```

{{< /tab >}}
{{< /tabs >}}

**All services at the root level**

{{< tabs "TabID402 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"system": {"hostname":"switch01","timezone":"America/Los_Angeles"}, "service": { "ntp": {"default":{"server:{"4.cumulusnetworks.pool.ntp.org":{"iburst":"on"}}}}, "dns": {"mgmt":{"server:{"192.168.1.100":{}}}}, "syslog": {"mgmt":{"server:{"192.168.1.120":{"port":8000}}}}}}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/?rev=changeset%2Fcumulus%2F2023-04-06_20.31.58_T2XR
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{} 
```

{{< /tab >}}
{{< /tabs >}}

### Day 2 through Day N - Setup Configuration

**Bond**

{{< tabs "TabID421 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"bond0": {"type":"bond","bond":{"member":{"swp1":{},"swp2":{},"swp3":{},"swp4":{}}}}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/interface?rev=changeset%2Fcumulus%2F2023-04-06_21.08.10_T2XV
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{ 
  "bond0": { 
    "bond": { 
      "member": { 
        "swp1": {}, 
        "swp2": {}, 
        "swp3": {}, 
        "swp4": {} 
      } 
    }, 
    "type": "bond" 
  }, 
  "bond1": { 
    "bond": { 
      "lacp-bypass": "on", 
      "member": { 
        "swp1": {} 
      }, 
      "mlag": { 
        "enable": "on", 
        "id": 1 
      }, 
      "mode": "lacp" 
    }, 
    "bridge": { 
      "domain": { 
        "br_default": { 
          "access": 10, 
          "stp": { 
            "admin-edge": "on", 
            "auto-edge": "on", 
            "bpdu-guard": "on" 
          } 
        } 
      } 
    }, 
    "link": { 
      "mtu": 9000 
    }, 
    "type": "bond" 
  }, 
  "eth0": { 
    "ip": { 
      "address": { 
        "192.168.200.6/24": {} 
      }, 
      "vrf": "mgmt" 
    }, 
    "type": "eth" 
  }, 
  "lo": { 
    "ip": { 
      "address": { 
        "10.10.10.1/32": {} 
      } 
    }, 
    "type": "loopback" 
  } 
}  
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv set interface bond0 bond member swp1-4
```

{{< /tab >}}
{{< /tabs >}}

**Bridge**

{{< tabs "TabID505 ">}}
{{< tab "Sample API Call ">}}

```
curl -u 'cumulus:CumulusLinux!' -d '{"swp1": {"bridge":{"domain":{"br_default":{}}},"swp2": {"bridge":{"domain":{"br_default":{}}}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/interface?rev=changeset%2Fcumulus%2F2023-04-06_21.08.10_T2X 

curl -u 'cumulus:CumulusLinux!' -d '{"untagged":1,"vlan":{"10":{},"20":{}}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/bridge/domain/br_default?rev=changeset%2Fcumulus%2F2023-04-06_21.08.10_T2XVResourcesResources
```

{{< /tab >}}
{{< tab "Sample Output ">}}

```
{} 
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 10,20
cumulus@switch:~$ nv set bridge domain br_default untagged 1
```

{{< /tab >}}
{{< /tabs >}}

## Resources

- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-55/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVIDIA User Experience Documentation">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/production-ready-automation/" text="Production Ready Automation">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/Data-Center-Network-Automation-Ansible-Deployment-Guide/" text="Data Center Network Automation with Ansible">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-soft" text="NVUE API Swagger Documentation">}}