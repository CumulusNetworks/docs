---
title: NVUE API
author: NVIDIA
weight: 125
toc: 3
---
<style>
  .scroll{
    height: 500px;
    overflow-y: auto;
  }
</style>
{{%notice warning%}}
When you upgrade to Cumulus Linux 5.6 or later, the switch overwrites any manual configuration you performed by editing files in Cumulus Linux 5.5 or earlier, such as configuring the listening address, port, TLS, or certificate.
{{%/notice%}}

In addition to the CLI, NVUE supports a REST API. Instead of accessing Cumulus Linux using SSH, you can interact with the switch using an HTTP client, such as cURL or a web browser.

The `nvued` service provides access to the NVUE REST API. Cumulus Linux exposes the HTTP endpoint internally, which makes the NVUE REST API accessible locally within the Cumulus Linux switch. The NVUE CLI also communicates with the `nvued` service using internal APIs. To provide external access to the NVUE REST API, Cumulus Linux uses an HTTP reverse proxy server, and supports HTTPS and TLS connections from external REST API clients.

The following illustration shows the NVUE REST API architecture and illustrates how Cumulus Linux forwards the requests internally.

{{< img src = "/images/cumulus-linux/nvue-api-arch.png" >}}

## Supported HTTP Methods

The NVUE REST API supports the following methods:
- The **GET** method displays configuration and operational data, and is equivalent to the `nv show` commands.
- The **POST** method creates and submits operations. You typically use this method for `nv action` commands and for the `nv config` command to create revisions.
- The **PATCH** method replaces or unsets a configuration. You use this method for the `nv set` and `nv config apply` commands. You can either perform:
  - A *targeted* configuration patch to make a configuration change, where you run a specific NVUE REST API targeted at a particular OpenAPI end-point URI. Based on the NVUE schema definition, you need to direct the PATCH REST API request at a particular endpoint (for example, `/nvue_v1/vrf/<vrf-id>/router/bgp`) and provide the payload that conforms to the schema. With a targeted configuration patch, you can control individual resources.
  - A *root* patch, where you run the NVUE PATCH API on the root node of the schema so that a single PATCH operation can change one, some, or the entire configuration in a single payload. The payload of the PATCH method must be aware of the entire NVUE object model schema because you make the configuration changes relative to the root node `/nvue_v1`. You typically perform a *root patch* to push all configurations to the switch in bulk; for example, if you use an SDN controller or a network management system to push the entire switch configuration every time you need to make a change, regardless of how small or large. A root patch can also make configuration changes with fewer round trips to the switch.
- The **DELETE** method deletes a configuration and is equivalent to the `nv unset` commands.

## Secure the API

The NVUE REST API supports HTTP basic authentication, and the same underlying authentication methods for username and password that the NVUE CLI supports. User accounts work the same on both the API and the CLI.

### Certificates
<!-- vale off -->
Cumulus Linux includes a self-signed certificate and private key to use on the server so that it works out of the box. The switch generates the self-signed certificate and private key when it boots for the first time. The X.509 certificate with the public key is in `/etc/ssl/certs/cumulus.pem` and the corresponding private key is in `/etc/ssl/private/cumulus.key`.
<!-- vale on -->
NVIDIA recommends you use your own certificates and keys. Certificates must be in PEM format. For the steps to generate self-signed certificates and keys, and to install them on the switch, refer to the {{<exlink url="https://help.ubuntu.com/lts/serverguide/certificates-and-security.html" text="Ubuntu Certificates and Security documentation">}}.

To use your own certificate chain:
1. Import the certificate and private key onto the Cumulus Linux switch using secure channels, such as SCP or SFTP.
2. Store the certificate and private key on the filesystem in a location of you choice or use the same location; for example, `/etc/ssl/certs` and `/etc/ssl/private`.
3. Update the `/etc/nginx/sites-enabled/nvue.conf` file to set the `ssl_certificate` and the `ssl_certificate_key` values to your keys.
4. Restart NGINX with the `sudo systemctl restart nginx` command.
<!-- vale off -->
### API-only User
<!-- vale on -->
To create an API-only user without SSH permissions, use Linux group permissions. You can create the API-only user in the ZTP script.

```
# Create the dedicated automation user 
adduser --disabled-password --gecos "Automation User,,,," --shell /usr/bin/nologin automation

# Set the password
echo 'automation:password!' | chpasswd

# Add the user to nvapply group to make NVUE config changes
adduser automation nvapply
```

### Control Plane ACLs

You can secure the API by configuring:
- A listening address; see {{<link url="#api-port-and-listening-address" text="API Port and Listening Address">}} below.
- Control plane ACLs; see the following example.

This example shows how to create ACLs to allow users from the management subnet and the local switch to communicate with the switch using REST APIs, and restrict all other access.

```
cumulus@switch:~$ nv set acl API-PROTECT type ipv4 
cumulus@switch:~$ nv set acl API-PROTECT rule 10 action permit
cumulus@switch:~$ nv set acl API-PROTECT rule 10 match ip .protocol tcp .dest-port 8765 .source-ip 192.168.200.0/24
cumulus@switch:~$ nv set acl API-PROTECT rule 10 remark "Allow the Management Subnet to talk to API"

cumulus@switch:~$ nv set acl API-PROTECT rule 20 action permit
cumulus@switch:~$ nv set acl API-PROTECT rule 20 match ip .protocol tcp .dest-port 8765 .source-ip 127.0.0.1
cumulus@switch:~$ nv set acl API-PROTECT rule 20 remark "Allow the local switch to talk to the API"

cumulus@switch:~$ nv set acl API-PROTECT rule 30 action deny
cumulus@switch:~$ nv set acl API-PROTECT rule 30 match ip .protocol tcp .dest-port 8765
cumulus@switch:~$ nv set acl API-PROTECT rule 30 remark "Block everyone else from talking to the API"

cumulus@switch:~$ nv set system control-plane acl API-PROTECT inbound
```

## Supported Objects

The NVUE object model supports most features on the Cumulus Linux switch. The following list shows the supported objects. The NVUE API supports more objects within each of these objects. You can find a full listing of the supported API endpoints {{<mib_link url="cumulus-linux-56/api/index.html" text="here.">}}

| High-level Objects | Description |
| ------------------ | ----------- |
| acl | Access control lists. |
| bridge | Bridge domain configuration. |
| evpn | EVPN configuration. |
| interface | Interface configuration. |
| mlag | MLAG configuration. |
| nve | Network virtualization configuration, such as VXLAN-specfic MLAG configuration and VXLAN flooding. |
| platform | Platform configuration, such as hardware and software components. |
| qos | QoS RoCE configuration. |
| router | Router configuration, such as router policies, global BGP and OSPF configuration, PBR, PIM, IGMP, VRR, and VRRP configuration. |
| service | DHCP relays and server, NTP, PTP, LLDP, and syslog configuration. |
| system | Global system settings, such as the reserved routing table range for PBR and the reserved VLAN range for layer 3 VNIs, system login messages and switch reboot history. |
| vrf | VRF configuration. |

## Use the API

The NVUE CLI and the REST API are equivalent in functionality; you can run all management operations from the REST API or from the CLI. The NVUE object model drives both the REST API and the CLI management operations. All operations are consistent; for example, the CLI `nv show commands` reflect any PATCH operation (create and update) you run through the REST API.
<!-- vale off -->
NVUE follows a declarative model, removing context-specific commands and settings. The structure of NVUE is like a big tree that represents the entire state of a Cumulus Linux instance. At the base of the tree are high level branches representing objects, such as router and interface. Under each of these branches are more branches. As you navigate through the tree, you gain a more specific context. At the leaves of the tree are actual attributes, represented as key-value pairs. The path through the tree is similar to a filesystem path.
<!-- vale on -->

Cumulus Linux enables the NVUE REST API by default. To disable the NVUE REST API, run the `nv set system api state disabled` command.

{{%notice note%}}
To use the NVUE REST API in Cumulus Linux 5.6, you must {{<link url="/User-Accounts" text="change the password for the cumulus user">}}; otherwise you see 403 responses when you run commands.
{{%/notice%}}

### API Port and Listening Address

This section shows how to:
- Set the NVUE REST API port. If you do not set a port, Cumulus Linux uses the default port 8765.
- Specify the NVUE REST API listening address; you can specify an IPv4 address, IPv6 address, or `localhost`. If you do not specify a listening address, NGINX listens on all addresses for the target port.

{{< tabs "TabID129 ">}}
{{< tab "Curl Command ">}}

The following example uses NVUE REST API port 8888 and listening address localhost:

```
cumulus@switch:~$ curl  -u 'cumulus:cumulus' --insecure https://localhost:8888/nvue_v1/...
...
```

You can listen on multiple interfaces by specifying different listening addresses.

If you configure a VRF for an interface, NGINX listens on the VRF configured for that interface. The following example uses the default NVUE REST API port 8765 on eth0, which has IP address 172.0.24.0 and uses the management VRF by default:

```
cumulus@switch:~$ curl  -u 'cumulus:cumulus' --insecure https://172.0.24.0:8765/nvue_v1/...
...
```

{{< /tab >}}
{{< tab "Python Code ">}}

The following example uses NVUE REST API port 8888 and listening address localhost:

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://localhost:8888/nvue_v1"
mime_header = {"Content-Type": "application/json"}
...
```

You can listen on multiple interfaces by specifying different listening addresses.

If you configure a VRF for an interface, NGINX listens on the VRF configured for that interface. The following example uses the default NVUE REST API port 8765 on eth0, which has IP address 172.0.24.0 and uses the management VRF by default:

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://172.0.24.0:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}
...
```

{{</ tab >}}
{{< tab "NVUE CLI ">}}

The following example sets the NVUE REST API port to 8888 and the listening address to localhost:

```
cumulus@switch:~$ nv set system api port 8888
cumulus@switch:~$ nv set system api listening-address localhost
cumulus@switch:~$ nv config apply
```

You can listen on multiple interfaces by specifying different listening addresses:

```
cumulus@switch:~$ nv set system api listening-address 10.10.10.1
cumulus@switch:~$ nv set system api listening-address 10.10.20.1
cumulus@switch:~$ nv config apply
```

If you configure a VRF for an interface, NGINX listens on the VRF configured for that interface. The following example configures VRF BLUE on swp1, which has IP address 10.10.20.1, then sets the API listening address to the IP address for swp1 (configured for VRF BLUE).

```
cumulus@switch:~$ nv set interface swp1 ip address 10.10.10.1/24
cumulus@switch:~$ nv set interface swp1 ip vrf BLUE
cumulus@switch:~$ nv config apply

cumulus@switch:~$ nv set system api listening-address 10.10.10.1
cumulus@switch:~$ nv config apply
```

To configure NGINX to listen on eth0, which has IP address 172.0.24.0 and uses the management VRF by default:

```
cumulus@switch:~$ nv set system api listening-address 172.0.24.0
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

### Show NVUE REST API Information

To show REST API port configuration, state (enabled or disabled), and connection information, run the `nv show system api` command:

```
cumulus@switch:~$ nv show system api
                  operational     applied
--------------    -----------     -------
port                 8888         8888     
state                enabled      enabled  
[listening-address]  localhost    localhost
connections
  accepted        31
  active          1
  handled         33
  reading         0
  requests        28
  waiting         0
  writing         1
```

To show connection information only, run the `nv show system api connections` command:

```
cumulus@switch:~$ nv show system api connections
          operational  applied
--------  -----------  -------
accepted  31                  
active    1                   
handled   33                  
reading   0                   
requests  28                   
waiting   0                   
writing   1     
```

To show the configured listening address, run the `nv show system api listening-address` command:

```
cumulus@switch:~$ nv show system api listening-address

---------
localhost
```
<!--
### Access the NVUE REST API from a Front Panel Port

To access the NVUE REST API from a front panel port (swp) on the switch:

1. Ensure that the `nvue.conf` file is present in the `/etc/nginx/sites-enabled` directory.

   Either copy the packaged template file `nvue.conf` from the `/etc/nginx/sites-available` directory to the `/etc/nginx/sites-enabled` directory or create a symbolic link.

2. Edit the `nvue.conf` file and add the `listen` directive with the IPv4 or IPv6 address of the swp interface you want to use.

   The default `nvue.conf` file includes a single `listen localhost:8765 ssl;` entry. Add an entry for each swp interface with its IP address. Make sure to use an accessible HTTP (TCP) port (subject to any ACL or firewall rules). For information on the NGINX `listen` directive, see {{<exlink url="http://nginx.org/en/docs/http/ngx_http_core_module.html#listen" text="the NGINX documentation" >}}.

3. Restart the `nginx` service:

   ```
   cumulus@switch:~$ sudo systemctl reload-or-restart nginx
   ```

{{%notice note%}}
- The swp interfaces must be part of the default VRF on the Cumulus Linux switch or virtual appliance.
- To access the REST API from the switch running `curl` locally, invoke the REST API client from the default VRF from the Cumulus Linux shell by prefixing the command with `ip vrf exec default curl`.
- To access the NVUE REST API from a client on a peer Cumulus Linux switch or virtual appliance, or any other off-the-shelf Linux server or virtual machine, make sure the switch or appliance has the correct IP routing configuration so that the REST API HTTP packets arrive on the correct target interface and VRF.
{{%/notice%}}
-->
### Run cURL Commands

You can run the cURL commands from the command line. Use the username and password for the switch. For example:

```
cumulus@switch:~$ curl  -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/interface
{
  "eth0": {
    "ip": {
      "address": {
        "192.168.200.12/24": {}
      }
    },
    "link": {
      "mtu": 1500,
      "state": {
        "up": {}
      },
      "stats": {
        "carrier-transitions": 2,
        "in-bytes": 184151,
        "in-drops": 0,
        "in-errors": 0,
        "in-pkts": 2371,
        "out-bytes": 117506,
        "out-drops": 0,
        "out-errors": 0,
        "out-pkts": 762
      }
...
```

## API Use Cases

The following examples show the primary API uses cases.

### View a Configuration

Use the following example to obtain the current applied configuration on the switch. Change the `rev` argument to view any revision. Possible options for the `rev` argument include `startup`, `pending`, `operational`, and `applied`.

{{< tabs "ViewConfig">}}
{{< tab "Curl Command ">}}

```
cumulus@switch:~$ curl -k -u cumulus:cumulus -X GET "https://127.0.0.1:8765/nvue_v1/?rev=applied&filled=false"
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
...  
```

{{< /tab >}}
{{< tab "Python Code ">}}

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

if __name__ == "__main__":
    r = requests.get(url=nvue_end_point + "/?rev=applied&filled=false",
                     auth=auth,
                     verify=False)
    print("=======Current Applied Revision=======")
    print(json.dumps(r.json(), indent=2))
```

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config show
- set: 
    bridge: 
      domain: 
        br_default: 
          type: vlan-aware 
          vlan: 
            '10': 
              vni: 
                '10': {} 
            '20': 
              vni: 
                '20': {} 
            '30': 
              vni: 
                '30': {} 
    evpn: 
      enable: on 
    mlag: 
      backup: 
        10.10.10.2: {} 
      enable: on 
      init-delay: 10 
      mac-address: 44:38:39:BE:EF:AA 
... 
```

{{< /tab >}}
{{< /tabs >}}

### Replace an Entire Configuration

To replace an entire configuration:

1. Create a new revision ID with a POST:

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure -X POST https://127.0.0.1:8765/nvue_v1/revision
   {
    "1": {
      "state": "pending",
      "transition": {
        "issue": {},
        "progress": ""
      }
    }
   }
   ```

2. Record the revision ID. In the above example, the revision ID is `"1"`.

3. Do a root patch to delete the whole configuration.
   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{}' -H 'Content-Type: application/json' -k -X DELETE https://127.0.0.1:8765/nvue_v1/?rev=1
   {}
   ```

4. Do a root patch to update the switch with the new configuration.

   <div class=scroll>

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{
      "system": {
        "hostname": "switch01"
      },
      "bridge": {
        "domain": {
          "br_default": {
            "type": "vlan-aware",
            "vlan": {
              "10": {
                "vni": {
                  "10": {}
                  }
                },
              "20": {
                "vni": {
                  "20": {}
                }
              },
              "30": {
                "vni": {
                  "30": {}
                }
              }
            }
          }
        }
      },
      "interface": {
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
        },
        "swp51": {
          "link": {
            "state": {
              "up": {}
            }
          },
          "type": "swp"
        },
        "swp52": {
          "link": {
            "state": {
              "up": {}
            }
          },
          "type": "swp"
        },
        "swp53": {
          "link": {
            "state": {
              "up": {}
            }
          },
          "type": "swp"
        },
        "swp54": {
          "link": {
            "state": {
              "up": {}
            }
          },
          "type": "swp"
        }
      },
      "mlag": {
        "backup": {
          "10.10.10.2": {}
        },
        "enable": "on",
        "init-delay": 10,
        "mac-address": "44:38:39:BE:EF:AA",
        "peer-ip": "linklocal",
        "priority": 1000
      }
      "router": {
        "bgp": {
          "enable": "on"
        },
        "vrr": {
          "enable": "on"
        }
      },
      "service": {},
      "vrf": {
        "mgmt": {
          "router": {
            "static": {
              "0.0.0.0/0": {
                "address-family": "ipv4-unicast",
                "via": {
                  "192.168.200.1": {
                    "type": "ipv4-address"
                  }
                }
              }
            }
          }
        }
      }
    }' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/?rev=1
   {}
   ```
   </div>

5. Apply the changes with a PATCH to the revision changeset.

   {{< tabs "ApplyRootPatchConfigChange">}}
{{< tab "Curl Command ">}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -H 'Content-Type:application/json' -d '{"state": "apply", "auto-prompt": {"ays": "ays_yes"}}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/revision/1
{
  "state": "apply",
  "transition": {
    "issue": {},
    "progress": ""
  }
}
```

{{</ tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config apply
```

{{</ tab >}}
{{</ tabs>}}

6. Review the status of the apply and the configuration:

   {{< tabs "ReviewRootPatchConfigChange">}}
{{< tab "Curl Command ">}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -k -X GET https://127.0.0.1:8765/nvue_v1/revision/1
{
  "state": "applied",
  "transition": {
    "issue": {},
    "progress": ""
  }
}
```

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/system
{
 "build": "Cumulus Linux 5.4.0",
 "hostname": "switch01",
 "timezone": "Etc/UTC",
 "uptime": 763
}
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/bridge/domain/br_default/vlan/10
{
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
     "mac-learning": "off"
   }
 }
```

{{</ tab >}}
{{< tab "Python Code ">}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)
        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    payload = {
      "system": {
        "hostname": "switch01"
      },
      "bridge": {
        "domain": {
          "br_default": {
            "type": "vlan-aware",
            "vlan": {
              "10": {
                "vni": {
                  "10": {}
                  }
                },
              "20": {
                "vni": {
                  "20": {}
                }
              },
              "30": {
                "vni": {
                  "30": {}
                }
              }
            }
          }
        }
      },
      "interface": {
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
        },
        "swp51": {
          "link": {
            "state": {
              "up": {}
            }
          },
          "type": "swp"
        },
        "swp52": {
          "link": {
            "state": {
              "up": {}
            }
          },
          "type": "swp"
        },
        "swp53": {
          "link": {
            "state": {
              "up": {}
            }
          },
          "type": "swp"
        },
        "swp54": {
          "link": {
            "state": {
              "up": {}
            }
          },
          "type": "swp"
        }
      },
      "mlag": {
        "backup": {
          "10.10.10.2": {}
        },
        "enable": "on",
        "init-delay": 10,
        "mac-address": "44:38:39:BE:EF:AA",
        "peer-ip": "linklocal",
        "priority": 1000
      }
      "router": {
        "bgp": {
          "enable": "on"
        },
        "vrr": {
          "enable": "on"
        }
      },
      "service": {},
      "vrf": {
        "mgmt": {
          "router": {
            "static": {
              "0.0.0.0/0": {
                "address-family": "ipv4-unicast",
                "via": {
                  "192.168.200.1": {
                    "type": "ipv4-address"
                  }
                }
              }
            }
          }
        }
      }
    }
    apply_new_config("/",payload)
    time.sleep(DUMMY_SLEEP)
    print("=====Verifying some of the configurations=====")
    nvue_get("/system")
    nvue_get("/bridge/domain/br_default/vlan/10")
```

</div>

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv show system
            operational          applied
--------  -------------------  -------
hostname  switch01             cumulus
build     Cumulus Linux 5.4.0
uptime    0:12:59
timezone  Etc/UTC
```

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10

                 operational  applied  pending  description
---------------  -----------  -------  -------  ------------------------------------------------------
[vni]            10           10       10       L2 VNI
multicast
  snooping
    querier
      source-ip  0.0.0.0      0.0.0.0  0.0.0.0  Source IP to use when sending IGMP/MLD queries.
ptp
  enable         off          off      off      Turn the feature 'on' or 'off'.  The default is 'off'.
```

{{</ tab >}}
{{</ tabs>}}

### Make a Configuration Change

To make a configuration change:

1. Create a new revision ID with a POST:

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure -X POST https://127.0.0.1:8765/nvue_v1/revision
   {
      "2": {
      "state": "pending",
      "transition": {
        "issue": {},
        "progress": ""
      }
    }
   }
   ```

2. Record the revision ID. In the above example, the revision ID is `"2"`.

3. Make the change with a PATCH and link it to the revision ID:

   {{< tabs "MakeConfigChange">}}
{{< tab "Curl Command ">}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"99.99.99.99/32": {}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:876nvue_v1/interface/lo/ip/address?rev=2
{
  "99.99.99.99/32": {}
}
```

{{</ tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv set interface lo ip address 99.99.99.99/32
```

{{</ tab >}}
{{</ tabs>}}

4. Apply the changes with a PATCH to the revision changeset:

   {{< tabs "ApplyConfigChange">}}
{{< tab "Curl Command ">}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -H 'Content-Type:application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/revision/2
{
  "state": "apply",
  "transition": {
    "issue": {},
    "progress": ""
  }
}
```

{{</ tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config apply
```

{{</ tab >}}
{{</ tabs>}}

5. Review the status of the apply and the configuration:

   {{< tabs "ReviewConfigChange">}}
{{< tab "Curl Command ">}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -k -X GET https://127.0.0.1:8765/nvue_v1/revision/2
{
  "state": "applied",
  "transition": {
    "issue": {},
    "progress": ""
  }
}
```

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/interface/lo/ip/address
{
  "127.0.0.1/8": {},
  "99.99.99.99/32": {},
  "::1/128": {}
}
```
{{</ tab >}}
{{< tab "Python Code ">}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)
        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    payload = {
        "99.99.99.99/32": {}
    }
    apply_new_config("/interface/lo/ip/address",payload)
    time.sleep(DUMMY_SLEEP)
    nvue_get("/interface/lo/ip/address")
```

</div>

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv show interface lo ip address
   
-------------
99.99.99.99/32
127.0.0.1/8
::1/128
```

{{</ tab >}}
{{</ tabs>}}

### Troubleshoot Configuration Changes

When a configuration change fails, you see an error in the change request.

**Configuration Fails Because of a Dependency**

If you stage a configuration but it fails because of a dependency, the failure shows the reason. In the following example, the change fails because the BGP router ID is not set.

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/revision/6
{
  "state": "invalid",
  "transition": {
    "issue": {
      "0": {
        "code": "config_invalid",
        "data": {
          "location": "router.bgp.enable",
          "reason": "BGP requires router-id to be set globally or in the VRF.\n"
        },
        "message": "Config invalid at router.bgp.enable: BGP requires router-id to be set globally or in the VRF.\n",
        "severity": "error"
      }
    },
    "progress": "Invalid config"
  }
}
```

The staged configuration is missing `router-id`.

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/vrf/default/router/bgp?rev=6
{
  "autonomous-system": 65999,
  "enable": "on"
}
```

**Configuration Apply Fails with Warnings**

In some cases, such as the first push with NVUE or if you change a file manually instead of using NVUE, you see a warning prompt and the apply fails.

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure -X GET https://127.0.0.1:8765/nvue_v1/revision/6
{
  "6": {
    "state": "ays_fail",
    "transition": {
      "issue": {
        "0": {
          "code": "client_timeout",
          "data": {},
          "message": "Timeout while waiting for client response",
          "severity": "error"
        }
      },
      "progress": "Aborted apply after warnings"
    }
  }
```

To resolve this issue, observe the failures or errors, then inspect the configuration that you are trying to apply. After you resolve the errors, retry the API. If you prefer to overlook the errors and force an apply, add `"auto-prompt":{"ays": "ays_yes"}` to the configuration apply.

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"state":"apply","auto-prompt":{"ays": "ays_yes"}}' -H 'Content-Type:application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/revision/6
```

### Save a Configuration

To save an applied configuration change to the startup configuration file (`/etc/nvue.d/startup.yaml`) so that the changes persist after a reboot, use a PATCH to the applied revision with the `save` state.

{{< tabs "SaveConfig">}}
{{< tab "Curl Command ">}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -k -X PATCH -d '{"state": "save", "auto-prompt": {"ays": "ays_yes"}}' -H 'Content-Type: application/json'  https://127.0.0.1:8765/nvue_v1/revision/applied 
{ 
  "state": "save",
  "transition": {
    "issue": {},
    "progress": ""
  }
}
```

{{< /tab >}}
{{< tab "Python Code ">}}

<div class="scroll">

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def save_nvue_changeset():
    apply_payload = {"state": "save", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/applied"
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    save_nvue_changeset()
```

</div>

{{< /tab >}}
{{< tab "NVUE CLI ">}}

```
cumulus@switch:~$ nv config save
saved
```

{{< /tab >}}
{{< /tabs >}}

### Unset a Configuration Change

To unset a configuration change, use the `null` value to the key. For example, to delete `vlan100` from a switch, use the following syntax:

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"vlan100":null}' -H 'Content-Type: application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/interface/rev=4
```

When you unset a change, you must still use the `PATCH` action. The value indicates removal of the entry. The data is `{"vlan100":null}` with the PATCH action.

### Use the API for Active Monitoring

The example below fetches the counters for `interface swp1`.

{{< tabs "ActiveMonitoring" >}}
{{< tab "Curl Command" >}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -k -X GET https://127.0.0.1:8765/nvue_v1/interface/swp1/link/stats
{
  "carrier-transitions": 6,
  "in-bytes": 293771538,
  "in-drops": 0,
  "in-errors": 0,
  "in-pkts": 2321737,
  "out-bytes": 366068936,
  "out-drops": 0,
  "out-errors": 0,
  "out-pkts": 3536629
}
```

{{< /tab >}}
{{< tab "Python Code" >}}

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

if __name__ == "__main__":
    r = requests.get(url=nvue_end_point + "/interface/swp1/link/stats",
                     auth=auth,
                     verify=False)
    print("=======Interface swp1 Statistics=======")
    print(json.dumps(r.json(), indent=2))
```

{{< /tab >}}
{{< tab "NVUE CLI" >}}

```
cumulus@switch:~$ nv show interface swp1 link stats
                     operational  applied  pending  description
-------------------  -----------  -------  -------  ----------------------------------------------------------------------
carrier-transitions  6                              Number of times the interface state has transitioned between up and...
in-bytes             280.15 MB                      total number of bytes received on the interface
in-drops             0                              number of received packets dropped
in-errors            0                              number of received packets with errors
in-pkts              2321659                        total number of packets received on the interface
out-bytes            349.10 MB                      total number of bytes transmitted out of the interface
out-drops            0                              The number of outbound packets that were chosen to be discarded eve...
out-errors           0                              The number of outbound packets that could not be transmitted becaus...
out-pkts             3536508                        total number of packets transmitted out of the interface
```

{{< /tab >}}
{{< /tabs >}}

### Convert CLI Changes to Use the API

You can take a configuration change from the CLI and use the API to configure the same set of changes.

1. Make your configuration changes on the system with the NVUE CLI.

   ```
   cumulus@switch:~$ nv set system hostname switch01
   cumulus@switch:~$ nv set interface lo ip address 99.99.99.99/32
   cumulus@switch:~$ nv set interface eth0 ip address 192.168.200.6/24
   cumulus@switch:~$ nv set interface bond0 bond member swp1-4
   ```

2. View the changes as a JSON blob.

   ```
   cumulus@switch:~$ nv config diff -o json
   [
     {
       "set": {
         "interface": {
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
           "lo": {
             "ip": {
               "address": {
                 "99.99.99.99/32": {}
               }
             }
           }
         },
         "system": {
           "hostname": "switch01"
         }
       }
     }
   ]
   ```

3. Staple the JSON blob to a root patch request as the payload.

   <div class="scroll">

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{
         "interface": {
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
           "lo": {
             "ip": {
               "address": {
                 "99.99.99.99/32": {}
               }
             }
           }
         },
         "system": {
           "hostname": "switch01"
         }
       }' -k -X PATCH https://127.0.0.1:8765/nvue_v1/?rev=3

   {
     "bridge": {
       "domain": {
         "br_default": {
           "type": "vlan-aware",
           "vlan": {
             "10": {
               "vni": {
                 "10": {}
               }
             },
             "20": {
               "vni": {
                 "20": {}
               }
             },
             "30": {
               "vni": {
                 "30": {}
               }
             }
           }
         }
       }
     },
     "evpn": {
       "enable": "on"
     },
     "interface": {
       "bond1": {
         "bond": {
           "lacp-bypass": "on",
           "member": {
             "swp1": {}
           },
   ...
   ```

   </div>

4. Apply the changes with a PATCH to the revision changeset.

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' -H 'Content-Type:application/json' -k -d '{"state": "apply", "auto-prompt": {"ays": "ays_yes"}}' -X PATCH https://127.0.0.1:8765/nvue_v1/revision/3
   {
     "state": "apply",
     "transition": {
       "issue": {},
       "progress": ""
     }
   }
   ```

5. Review the status of the apply and the configuration:

   {{< tabs "CLItoAPIReviewConfigChange">}}
{{< tab "Curl Command ">}}

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' -k -X GET https://127.0.0.1:8765/nvue_v1/revision/3
   {
     "state": "applied",
     "transition": {
       "issue": {},
       "progress": ""
     }
   }
   ```

{{</ tab >}}
{{< tab "Python Code ">}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    payload = {
      "interface": {
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
        "lo": {
          "ip": {
            "address": {
              "99.99.99.99/32": {}
            }
          }
        }
      },
      "system": {
        "hostname": "switch01"
      }
    }
    apply_new_config("/",payload)
    time.sleep(DUMMY_SLEEP)
    nvue_get("/interface/bond0")
    nvue_get("/interface/lo")
    nvue_get("/system")

   ```

   </div>

{{</ tab >}}
{{</ tabs>}}

## API Examples

The following section provides practical API examples.

### Configure the System

To set the system hostname, pre-login or post-login message, and time zone on the switch, send a targeted API request to `/nvue_v1/system`.

{{< tabs "SystemConfig" >}}
{{< tab "Curl Command" >}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"system": {"hostname":"switch01","timezone":"America/Los_Angeles","message":{"pre-login":"Welcome to NVIDIA Cumulus Linux","post-login:"You have successfully logged in to switch01"}}}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/?rev=4
```

{{< /tab >}}
{{< tab "Python Code" >}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    payload = {
      "system": 
      {
        "hostname":"switch01",
        "timezone":"America/Los_Angeles",
        "message":
        {
          "pre-login":"Welcome to NVIDIA Cumulus Linux",
          "post-login:"You have successfully logged in to switch01"
        }
      }
    }
    apply_new_config("/",payload) # Root patch
    time.sleep(DUMMY_SLEEP)
    nvue_get("/system")
   ```

</div>

{{< /tab >}}
{{< tab "NVUE CLI" >}}

```
cumulus@switch:~$ nv set system hostname switch01
cumulus@switch:~$ nv set system timezone America/Los_Angeles
cumulus@switch:~$ nv set system message pre-login "Welcome to NVIDIA Cumulus Linux"
cumulus@switch:~$ nv set system message post-login "You have successfully logged into switch01"
```

{{< /tab >}}
{{< /tabs >}}

### Configure Services

To set up NTP, DNS, and SNMP on the switch, send a targeted API request to `/nvue_v1/service`.

{{< tabs "ServicesConfig" >}}
{{< tab "Curl Command" >}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"service": { "ntp": {"default":{"server:{"4.cumulusnetworks.pool.ntp.org":{"iburst":"on"}}}}, "dns": {"mgmt":{"server:{"192.168.1.100":{}}}}, "syslog": {"mgmt":{"server:{"192.168.1.120":{"port":8000}}}}}}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/?rev=5
```

{{< /tab >}}
{{< tab "Python Code" >}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    payload = {
      "service":
      {
        "ntp":
        {
          "default":
          {
            "server:
            {
              "4.cumulusnetworks.pool.ntp.org":
              {
                "iburst":"on"
              }
            }
          }
        },
        "dns":
        {
          "mgmt":
          {
            "server:
            {
              "192.168.1.100":{}
            }
          }
        },
        "syslog":
        {
          "mgmt":
          {
            "server:
            {
              "192.168.1.120":
              {
                "port":8000
              }
            }
          }
        }
      }
    }
    apply_new_config("/",payload) # Root patch
    time.sleep(DUMMY_SLEEP)
    nvue_get("/service/ntp")
    nvue_get("/service/dns")
    nvue_get("/service/syslog")
   ```

   </div>

{{< /tab >}}
{{< tab "NVUE CLI" >}}

```
cumulus@switch:~$ nv set service ntp default server 4.cumulusnetworks.pool.ntp.org iburst on
cumulus@switch:~$ nv set service dns mgmt server 192.168.1.100 
cumulus@switch:~$ nv set service syslog mgmt server 192.168.1.120 port 8000
```

{{< /tab >}}
{{< /tabs >}}

### Configure Users

The following example creates a new user, then deletes the user.

{{< tabs "UsersConfig" >}}
{{< tab "Curl Command" >}}

This example creates a new user called `test1`.

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"system": {"aaa": {"user": {"test1": {"hashed-password":"72b28582708d749c6c82f3b3f226041f1bd37090281641eaeba8d44bd915d0042d609a92759d9f6fb96475cb0601cf428cd22613df8a53a09461e0b426cf0a35","role": "nvue-monitor","enable": "on","full-name": "Test User"}}}}}' -k -X PATCH https://127.0.0.1:8765/nvue_v1/?rev=5
```

This example deletes the `test1` user.

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -k -X DELETE https://127.0.0.1:8765/nvue_v1/system/aaa/user/test1?rev=6
```

{{< /tab >}}
{{< tab "Python Code" >}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def delete_config(path):
    # Create an NVUE changeset
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Equivalent to JSON `null`
    payload = None

    # Stage the change
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                        auth=auth,
                        verify=False,
                        data=json.dumps(payload),
                        params=query_string,
                        headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the staged changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":

    # Need to create a hashed password - The supported password
    # hashes are documented here:
    # https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-55/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts/#hashed-passwords  # noqa
    # Here in this example, we use SHA-512
    import crypt
    hashed_password = crypt.crypt("hello$world#2023", salt=crypt.METHOD_SHA512)
    payload = {
        "system": {
            "aaa": {
                "user": {
                    "test1": {
                        "hashed-password": hashed_password,
                        "role": "nvue-monitor",
                        "enable": "on",
                        "full-name": "Test User",
                    }
                }
            }
        }
    }
    apply_new_config("/",payload) # Root patch
    time.sleep(DUMMY_SLEEP)
    nvue_get("/system/user/aaa")

    """Delete an existing user account using the AAA API."""
    delete_config("/system/aaa/user/test1")
    time.sleep(DUMMY_SLEEP)
    nvue_get("/system/user/aaa")
   ```

   </div>

{{< /tab >}}
{{< tab "NVUE CLI" >}}

This example creates a new user `test1`.

```
cumulus@switch:~$ nv set system aaa user test1
cumulus@switch:~$ nv set system aaa user test1 full-name "Test User" 
cumulus@switch:~$ nv set system aaa user test1 password "abcd@test"
cumulus@switch:~$ nv set system aaa user test1 role nvue-monitor
cumulus@switch:~$ nv set system aaa user test1 enable on
```

This example deletes the user `test1`.

```
cumulus@switch:~$ nv unset system aaa user test1
```

{{< /tab >}}
{{< /tabs >}}

### Configure an Interface

The following example configures an interface.

{{< tabs "InterfaceConfig" >}}
{{< tab "Curl Command" >}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"swp1": {"type":"swp","link":{"state":"up"}}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/interface?rev=6 
```

{{< /tab >}}
{{< tab "Python Code" >}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    payload = {
      "swp1":
      {
        "type":"swp",
        "link":
        {
          "state":"up"
          }
        }
      }
    apply_new_config("/interface",payload)
    time.sleep(DUMMY_SLEEP)
    nvue_get("/interface/swp1")
   ```

</div>

{{< /tab >}}
{{< tab "NVUE CLI" >}}

```
cumulus@switch:~$ nv set interface swp1
```

{{< /tab >}}
{{< /tabs >}}

### Configure a Bond

The following example configures a bond.

{{< tabs "BondConfig" >}}
{{< tab "Curl Command" >}}

<div class="scroll">

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"bond0": {"type":"bond","bond":{"member":{"swp1":{},"swp2":{},"swp3":{},"swp4":{}}}}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/interface?rev=7
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

</div>

{{< /tab >}}
{{< tab "Python Code" >}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    payload = {
      "bond0":
      {
        "type":"bond",
        "bond":
        {
          "member":
          {
            "swp1":{},
            "swp2":{},
            "swp3":{},
            "swp4":{}
          }
        }
      }
    }
    apply_new_config("/interface",payload)
    time.sleep(DUMMY_SLEEP)
    nvue_get("/interface/bond0")
```

</div>

{{< /tab >}}
{{< tab "NVUE CLI" >}}

```
cumulus@switch:~$ nv set interface bond0 bond member swp1-4
```

{{< /tab >}}
{{< /tabs >}}

### Configure a Bridge

The following example configures a bridge.

{{< tabs "BridgeConfig" >}}
{{< tab "Curl Command" >}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"swp1": {"bridge":{"domain":{"br_default":{}}},"swp2": {"bridge":{"domain":{"br_default":{}}}}}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/interface?rev=8
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"untagged":1,"vlan":{"10":{},"20":{}}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/bridge/domain/br_default?rev=8
```

{{< /tab >}}
{{< tab "Python Code" >}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    int_payload = {
      "swp1":
      {
        "bridge":
        {
          "domain":
          {
            "br_default":{}
          }
        },
        "swp2": 
        {
          "bridge":
          {
            "domain":
            {
              "br_default":{}
            }
          }
        }
      }
    }
    apply_new_config("/interface",int_payload)
    br_payload = {
      "untagged":1,
      "vlan":
      {
        "10":{},
        "20":{}
      }
    }
    apply_new_config("/bridge/domain/br_default",br_payload)
    time.sleep(DUMMY_SLEEP)
    nvue_get("/interface/swp1")
    nvue_get("/bridge/domain/br_default")
   ```
  
  </div>

{{< /tab >}}
{{< tab "NVUE CLI" >}}

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 10,20
cumulus@switch:~$ nv set bridge domain br_default untagged 1
```

{{< /tab >}}
{{< /tabs >}}

### Configure BGP

The following example configures BGP.

{{< tabs "BGPConfig" >}}
{{< tab "Curl Command" >}}

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"bgp": {"autonomous-system": 65101,"router-id":"10.10.10.1"}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/router?rev=9
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"bgp":{"neighbor":{"swp51":{"remote-as":"external"}},"address-family":{"ipv4-unicast":{"network":{"10.10.10.1/32":{}}}}}}' -H 'Content-Type: application/json' -k -X PATCH https://127.0.0.1:8765/nvue_v1/vrf/default/router?rev=9
```

{{< /tab >}}
{{< tab "Python Code" >}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

def apply_new_config(path,payload):
    # Create a new revision ID
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # Delete existing configuration
    query_string = {"rev": changeset}
    r = requests.delete(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Patch the new configuration
    
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + path,
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the changes to the new revision changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    rt_payload = {
      "bgp":
      {
        "autonomous-system": 65101,
        "router-id":"10.10.10.1"
      }
    }
    apply_new_config("/router",rt_payload)
    vrf_payload = {
      "bgp":
      {
        "neighbor":
        {
          "swp51":
          {
            "remote-as":"external"
          }
        },
        "address-family":
        {
          "ipv4-unicast":
          {
            "network":
            {
              "10.10.10.1/32":{}
            }
          }
        }
      }
    }
    apply_new_config("/vrf/default/router",vrf_payload)
    time.sleep(DUMMY_SLEEP)
    nvue_get("/router")
    nvue_get("/vrf/default/router")
```

</div>

{{< /tab >}}
{{< tab "NVUE CLI" >}}

```
cumulus@switch:~$ nv set router bgp autonomous-system 65101
cumulus@switch:~$ nv set router bgp router-id 10.10.10.1
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
```

{{< /tab >}}
{{< /tabs >}}

### Action Operations

The NVUE action operations are ephemeral operations that do not modify the state of the configuration; they reset counters for interfaces, BGP, QoS buffers and pools, and remove conflicts from protodown MLAG bonds.

{{< tabs "ActionOperations" >}}
{{< tab "Curl Command" >}}

```
cumulus@switch:~$ curl -H 'Content-Type:application/json' -u 'cumulus:cumulus' -d '{"@clear": {"state": "start", "parameters": {}}}' -k -X POST "https://127.0.0.1:8765/nvue_v1/interface/swp1/qos/counter" 
1
cumulus@switch:~$ curl -u 'cumulus:cumulus' -k -X GET "https://127.0.0.1:8765/nvue_v1/action/1" 
```

{{< /tab >}}
{{< tab "Python Code" >}}

<div class=scroll>

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="cumulus", password="password")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def nvue_action():
    r = requests.post(url=nvue_end_point + path,
                      auth=auth,
                      verify=False,
                      data=json.dumps(apply_payload),
                      headers=mime_header)
    print_request(r.request)
    print_response(r)
    return response

def nvue_get(path):
    r = requests.get(url=nvue_end_point + path,
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

if __name__ == "__main__":
    payload = {
      "@clear": 
      {
        "state": "start", 
        "parameters": {}
      }
    }
    action_id=nvue_action("/interface/swp1/qos/counter",payload)
    time.sleep(DUMMY_SLEEP)
    nvue_get(f"/action/{action_id}")
   
```

</div>

{{< /tab >}}
{{< tab "NVUE CLI" >}}

```
cumulus@switch:~$ nv action clear interface swp1 qos counter
```

{{< /tab >}}
{{< /tabs >}}

## Example Python Script

In the following python example, the `full_config_example()` method sets the system pre-login message, enables BGP globally, and changes a few other configuration settings in a single bulk operation. The API end-point goes to the root node `/nvue_v1`. The `bridge_config_example()` method performs a targeted API request to `/nvue_v1/bridge/domain/<domain-id>` to set the `vlan-vni-offset` attribute.

{{< expand "Example Python Script" >}}

```
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import json
import time

auth = HTTPBasicAuth(username="vagrant", password="vagrant")
nvue_end_point = "https://127.0.0.1:8765/nvue_v1"
mime_header = {"Content-Type": "application/json"}

DUMMY_SLEEP = 5  # In seconds
POLL_APPLIED = 1  # in seconds
RETRIES = 10

def print_request(r: requests.Request):
    print("=======Request=======")
    print("URL:", r.url)
    print("Headers:", r.headers)
    print("Body:", r.body)

def print_response(r: requests.Response):
    print("=======Response=======")
    print("Headers:", r.headers)
    print("Body:", json.dumps(r.json(), indent=2))

def sanity():
    # Basic retrieval to check connectivity
    r = requests.get(url=nvue_end_point + "/system",
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

def create_nvue_changest():
    r = requests.post(url=nvue_end_point + "/revision",
                      auth=auth,
                      verify=False)
    print_request(r.request)
    print_response(r)
    response = r.json()
    changeset = response.popitem()[0]
    return changeset

def apply_nvue_changeset(changeset):
    # apply_payload = {"state": "apply"}
    apply_payload = {"state": "apply", "auto-prompt": {"ays": "ays_yes"}}
    url = nvue_end_point + "/revision/" + requests.utils.quote(changeset,
                                                               safe="")
    r = requests.patch(url=url,
                       auth=auth,
                       verify=False,
                       data=json.dumps(apply_payload),
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

def full_config_example():
    # Create an NVUE changeset
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))

    # https://www.asciiart.eu/comics/batman
    pre_login_message = u"""
                   ,.ood888888888888boo.,
              .od888P^""            ""^Y888bo.
          .od8P''   ..oood88888888booo.    ``Y8bo.
       .odP'"  .ood8888888888888888888888boo.  "`Ybo.
     .d8'   od8'd888888888f`8888't888888888b`8bo   `Yb.
    d8'  od8^   8888888888[  `'  ]8888888888   ^8bo  `8b
  .8P  d88'     8888888888P      Y8888888888     `88b  Y8.
 d8' .d8'       `Y88888888'      `88888888P'       `8b. `8b
.8P .88P            """"            """"            Y88. Y8.
88  888                                              888  88
88  888                                              888  88
88  888.        ..                        ..        .888  88
`8b `88b,     d8888b.od8bo.      .od8bo.d8888b     ,d88' d8'
 Y8. `Y88.    8888888888888b    d8888888888888    .88P' .8P
  `8b  Y88b.  `88888888888888  88888888888888'  .d88P  d8'
    Y8.  ^Y88bod8888888888888..8888888888888bod88P^  .8P
     `Y8.   ^Y888888888888888LS888888888888888P^   .8P'
       `^Yb.,  `^^Y8888888888888888888888P^^'  ,.dP^'
          `^Y8b..   ``^^^Y88888888P^^^'    ..d8P^'
              `^Y888bo.,            ,.od888P^'
                   "`^^Y888888888888P^^'"
"""

    # https://www.asciiart.eu/comics/superman
    post_login_message = u'''
        _____________________________________________
      //:::::::::::::::::::::::::::::::::::::::::::::\\
    //:::_______:::::::::________::::::::::_____:::::::\\
  //:::_/   _-"":::_--"""        """--_::::\_  ):::::::::\\
 //:::/    /:::::_"                    "-_:::\/:::::|^\:::\\
//:::/   /~::::::I__                      \:::::::::|  \:::\\
\\:::\   (::::::::::""""---___________     "--------"  /::://
 \\:::\  |::::::::::::::::::::::::::::""""==____      /::://
  \\:::"\/::::::::::::::::::::::::::::::::::::::\   /~::://
    \\:::::::::::::::::::::::::::::::::::::::::::)/~::://
      \\::::\""""""------_____::::::::::::::::::::::://
        \\:::"\               """""-----_____:::::://
          \\:::"\    __----__                )::://
            \\:::"\/~::::::::~\_         __/~:://
              \\::::::::::::::::""----""":::://
                \\::::::::::::::::::::::::://
                  \\:::\^""--._.--""^/::://
                    \\::"\         /":://
                      \\::"\     /":://
                        \\::"\_/":://
                          \\::::://
                            \\_//
                              "
'''

    # Prepare payload which configures a few
    # different switch configurations
    payload = {
        "interface":{
            "eth0":{
                "description": "management port"
            }
        },
        "router":{
            "bgp":{
                "enable":"on"
            }
        },
        "system":{
            "message":{
                "pre-login": pre_login_message,
                "post-login": post_login_message
            },
            "timezone": "Europe/Paris",
            "config": {
               "snippet": {
                   "test-flexible-snippet": {
                       "file": "/tmp/blah",
                       "content": "NVIDIA rocks"
                   },
                   "frr.conf": "hello world"
               }
            }
        },
        "service": {
            "ntp": {
                "mgmt": {
                    "listen": "eth0"
                }
            }
        }
    }
    # Stage the change
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + "/",  # Root patch
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the staged changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def bridge_config_example(domain_id):
    # Create an NVUE changeset
    changeset = create_nvue_changest()
    print("Using NVUE Changeset: '{}'".format(changeset))
    payload = {
        "vlan-vni-offset": 1000
    }

    # Stage the change
    query_string = {"rev": changeset}
    r = requests.patch(url=nvue_end_point + f"/bridge/domain/{domain_id}",
                       auth=auth,
                       verify=False,
                       data=json.dumps(payload),
                       params=query_string,
                       headers=mime_header)
    print_request(r.request)
    print_response(r)

    # Apply the staged changeset
    apply_nvue_changeset(changeset)

    # Check if the changeset was applied
    is_config_applied(changeset)

def message_get():
    # Get the system pre-login/post-login
    # message that was configured.
    r = requests.get(url=nvue_end_point + "/system/message",
                     auth=auth,
                     verify=False)
    print_request(r.request)
    print_response(r)

def is_config_applied(changeset) -> bool:
    # Check if the configuration was indeed applied
    global RETRIES
    global POLL_APPLIED
    retries = RETRIES
    while retries > 0:
        r = requests.get(url=nvue_end_point + "/revision/" + requests.utils.quote(changeset, safe=""),
                         auth=auth,
                         verify=False)
        response = r.json()
        print(response)

        if response["state"] == "applied":
            return True
        retries -= 1
        time.sleep(POLL_APPLIED)

    return False

if __name__ == "__main__":
    sanity()
    time.sleep(DUMMY_SLEEP)
    full_config_example()
    time.sleep(DUMMY_SLEEP)
    bridge_config_example("br_default")
    time.sleep(DUMMY_SLEEP)
    message_get()
```

{{< /expand >}}

## Try the API

To try out the NVUE REST API, use the {{<exlink url="https://air.nvidia.com/marketplace?demo_id=aa77bb13-6a7d-431c-9203-640510778beb" text="NVUE API Lab">}} available on NVIDIA Air. The lab provides a basic example to help you get started. You can also try out the other examples in this document.

## Resources

For information about using the NVUE REST API, refer to the {{<mib_link url="cumulus-linux-56/api/index.html" text="NVUE API Swagger documentation.">}}
The full object model download is available {{<mib_link url="cumulus-linux-56/api/openapi.json" text="here.">}}

## Considerations

- Unlike the NVUE CLI, the NVUE API does not support configuring a plain text password for a user account; you must configure a hashed password for a user account with the NVUE API.
- If you need to make multiple updates on the switch, NVIDIA recommends you use a root patch, which can make configuration changes with fewer round trips to the switch. Running many specific NVUE PATCH APIs to set or unset objects requires many round trips to the switch to set up the HTTP connection, transfer payload and responses, manage network utilization, and so on.

## Related Information

- {{<exlink url="https://docs.nginx.com/" text="NGINX documentaion">}}
- {{<exlink url="https://help.ubuntu.com/lts/serverguide/certificates-and-security.html" text="Ubuntu Certificates and Security documentation">}}
- {{<exlink url="https://pypi.org/project/requests/" text="Python requests module">}}
