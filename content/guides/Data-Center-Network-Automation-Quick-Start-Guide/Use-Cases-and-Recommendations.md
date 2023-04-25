---
title: Use Cases and Recommendations
author: Cumulus Networks
weight: 30
product: Cumulus Networks Guides
imgData: guides
---
In the world of data center automation and deployment, Day-0, Day-1, Day-2 and Day-N are widely used terms to determine the stage of the device configuration and usage. The classification determines when the configurations are applied.

Day-0 configuration is the initial minimal configuration with which the switch starts up, based on the topology and network architecture that has been designed.

Day-1 configuration includes setting up of common services like NTP, syslog, and so on.

Day-2 to Day-N are the configurations pushed to the device for day-to-day operations. This also includes patching and upgrading based on the changing needs of the environment.

## Automation options

| Options | Recommendations |
| ------- | --------------- |
| Flat File automation | NVUE must be explicitly told to ignore flat files pushed with automation methods outside of NVUE |
| REST API driven automation | NVUE is one hundred percent API driven and all features are accessible with the API. You can use the API for automation by any tool or script that can interacts with REST, such as Ansible, Python, Postman, and so on. |
| NVUE Configuration file automation | You can automate and apply the startup.yaml file. You can do this today using PRA, as mentioned above. |

## Integrate with Existing Tools

| Tools | Recommendation |
| ----- | -------------- |
| Ansible |For Day-0 configurations, you can use the PRA package to automate startup.yaml file generation or use the Ansible modules to set up the configuration as desired and run it across all the switches.</br>For Day-1..N configurations, you can leverage the Ansible modules that are available to make configuration changes on the go. |
| Salt | For Day-0 configurations, you can automate startup.yaml file generation.</br>For Day-1..N configurations, you can automate startup.yaml file updates and apply them on the switches. |
| Puppet |For Day-0 configurations, you can automate startup.yaml file generation.</br>For Day-1..N configurations, you can use the http_request module to interact with NVUE API. |
| Scripts | Most programming languages support making REST API calls. Use the RESTful NVUE API to integrate into your existing automation scripts. |

## Code Snippets

Using the REST API to make any updates (PATCH) is a three step process:
1. Create a new revision ID.
2. Make the change using a PATCH request against the revision ID recorded in the previous step.
3. Apply the changes to the revision changeset.
4. Optionally, review the status of the applied revision.

You can combine multiple PATCH requests into one revision.

You can change configuration settings either at the root level or the object level. With a root patch, you can push all configurations to the switch in bulk. With a targeted configuration patch, you can control individual resources.

The examples below use curl. You can do this with any tool or programming language.

### Revisions

1. View the current applied configuration.

   {{< tabs "TabID51 ">}}
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

{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config show
```

{{< /tab >}}
{{< /tabs >}}

2. Create a new revision ID.

     {{< tabs "TabID116 ">}}
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
Note: Cumulus Linux applies but does not save the configuration; the configuration does not persist after a reboot.

     {{< tabs "TabID144 ">}}
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

{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

4. Review the revision.

     {{< tabs "TabID176 ">}}
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

     {{< tabs "TabID201 ">}}
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

{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config save
```

{{< /tab >}}
{{< /tabs >}}

### Day 0: Set Up Basic Connectivity

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

{< /tab >}}
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

{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv show interface lo ip address
```

{{< /tab >}}
{{< /tabs >}}

### Day 1: Set Up Common Services

**System Hostname and time zone**

