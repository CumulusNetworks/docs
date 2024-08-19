---
title: NVUE API
author: NVIDIA
weight: 125
toc: 3
---
In addition to the CLI, NVUE supports a REST API. Instead of accessing Cumulus Linux using SSH, you can interact with the switch using an HTTP client, such as cURL or a web browser.

## Access the NVUE API

To access the NVUE API, run these commands on the switch:

```
cumulus@switch:~$ sudo ln -s /etc/nginx/sites-{available,enabled}/nvue.conf
cumulus@switch:~$ sudo sed -i 's/listen localhost:8765 ssl;/listen \[::\]:8765 ipv6only=off ssl;/g' /etc/nginx/sites-available/nvue.conf
cumulus@switch:~$ sudo systemctl restart nginx
```

## Access the NVUE API from a Front Panel Port

To access the NVUE REST API from a front panel port (swp) on the switch:

1. Ensure that the `nvue.conf` file is present in the `/etc/nginx/sites-enabled` directory.

   Either copy the packaged template file `nvue.conf` from the `/etc/nginx/sites-available` directory to the `/etc/nginx/sites-enabled` directory or create a symbolic link.

2. Edit the `nvue.conf` file and add the `listen` directive with the IPv4 or IPv6 address of the swp interface you want to use.

   The default `nvue.conf` file includes a single `listen localhost:8765 ssl;` entry. Add an entry for each swp interface with its IP address. Make sure to use an accessible HTTP (TCP) port (subject to any ACL/firewall rules). For information on the NGINX `listen` directive, see {{<exlink url="http://nginx.org/en/docs/http/ngx_http_core_module.html#listen" text="the NGINX documentation" >}}.

3. Restart the `nginx` service:

   ```
   cumulus@switch:~$ sudo systemctl reload-or-restart nginx
   ```

{{%notice note%}}
- The swp interfaces must be part of the default VRF on the Cumulus Linux switch or virtual appliance.
- To access the REST API from the switch running `curl` locally, invoke the REST API client from the default VRF from the Cumulus Linux shell by prefixing the command with `ip vrf exec default curl`.
- To access the NVUE REST API from a client on a peer Cumulus Linux switch or virtual appliance, or any other off-the-shelf Linux server or virtual machine, make sure the switch or appliance has the correct IP routing configuration so that the REST API HTTP packets arrive on the correct target interface and VRF.
{{%/notice%}}

## Transport Layer Security
<!-- vale off -->
Cumulus Linux contains a self-signed certificate and private key used server-side in this application so that it works out of the box; however, NVIDIA recommends you use your own certificates and keys. Certificates must be in PEM format.
<!-- vale on -->
For step by step documentation on generating self-signed certificates and keys, and installing them on the switch, refer to the {{<exlink url="https://help.ubuntu.com/lts/serverguide/certificates-and-security.html" text="Ubuntu Certificates and Security documentation">}}.

After installing the certificates and keys, edit the `/etc/nginx/sites-available/nvue.conf` file to set the `ssl_certificate` and the `ssl_certificate_key` values to your keys, then restart NGINX with the `sudo systemctl restart nginx` command.

## Run cURL Commands

You can run the cURL commands from the command line. Use the username and password for the switch. For example:

```
cumulus@switch:~$ curl  -u 'cumulus:CumulusLinux!' --insecure https://127.0.0.1:8765/nvue_v1/interface
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

### Set a Configuration Change

To make a configuration change with the NVUE API:

1. Create a new revision ID using a POST:

   ```
   cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' --insecure -X POST https://127.0.0.1:8765/nvue_v1/revision
   {
     "4": {
       "state": "pending",
       "transition": {
         "issue": {},
         "progress": ""
       }
     }
   }

   ```

   {{%notice note%}}

To allow the `cumulus` user access to the NVUE API, you must change the default password for the `cumulus` user.
{{%/notice%}}

2. Record the revision ID. In the above example, the revision ID is `"4"`

3. Make the change using a PATCH and link it to the revision ID:

   ```
   cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' -d '{"99.99.99.99/32": {}}' -H 'Content-Type: application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/interface/lo/ip/address?rev=4
   {
     "99.99.99.99/32": {}
   }
   ```

4. Apply the changes using a PATCH to the revision changeset.

   ```
   cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' -d '{"state":"apply"}' -H 'Content-Type:application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/revision/4
   {
     "state": "apply",
     "transition": {
       "issue": {},
       "progress": ""
     }
   }
   ```

5. Review the status of the apply and the configuration:

   ```
   cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' --insecure https://127.0.0.1:8765/nvue_v1/revision/4
   {
     "state": "applied",
     "transition": {
       "issue": {},
       "progress": ""
     }
   }
   ```

   ```
   cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' --insecure https://127.0.0.1:8765/nvue_v1/interface/lo/ip/address
   {
     "127.0.0.1/8": {},
     "99.99.99.99/32": {},
     "::1/128": {}
   }
   ```

6. To collect the applied configuration:

   ```
   cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' --insecure -X GET "https://127.0.0.1:8765/nvue_v1/?rev=applied&filled=false"
   ```

### Save an Applied Configuration

To save an applied configuration change to the startup configuration (`/etc/nvue.d/startup.yaml`) so that the changes persist after a reboot, use a PATCH to the applied revision with the `save` state. For example:

```
cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' --insecure -X PATCH -d '{"state": "save", "auto-prompt": {"ays": "ays_yes"}}' -H 'Content-Type: application/json'  https://127.0.0.1:8765/nvue_v1/revision/applied
```

### Unset a Configuration Change

To unset a change, use the `null` value to the key. For example, to delete `vlan100` from a switch, use the following syntax:

```
cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' -d '{"vlan100":null}' -H 'Content-Type: application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/interface/rev=4
```

When you unset a change, you must still use the `PATCH` action. The value indicates removal of the entry. The data is `{"vlan100":null}` with the PATCH action.

### Patch Operations

To change configuration settings with the REST API, you can either perform:
- A root patch, where you run the NVUE PATCH API on the root node of the schema so that a single PATCH operation can change one, some, or the entire configuration in a single payload. The payload of the PATCH method must be aware of the entire NVUE object model schema because you make the configuration changes relative to the root node `/nvue_v1`. 
- A targeted configuration patch, where you run a specific NVUE REST API, targeted at a particular OpenAPI end-point URI, to make a configuration change. Based on the NVUE schema definition, you need to direct the PATCH REST API request at a particular endpoint (for example, `/nvue_v1/vrf/{vrf-id}/router/bgp`) and provide the payload that conforms to the schema. With a targeted configuration patch, you can control individual resources.

You typically perform a *root patch* to push all configurations to the switch in bulk. For example, if you use a centralized configuration engine (such as an SDN controller or a network management system) to push the entire switch configuration every time you need to make a change, regardless of how small or large the change. A root patch can also make configuration changes with fewer round trips to the switch; running many specific NVUE PATCH APIs to set or unset objects requires many round trips to the switch to set up the HTTP connection, transfer payload and responses, manage network utilization, and so on.

In the following python example, the `full_config_example()` method sets the system pre-login message, enables BGP globally, and a changes a few other configuration settings in a single bulk operation. The API end-point goes to the root node `/nvue_v1`. The `bridge_config_example()` method performs a targeted API request to `/nvue_v1/bridge/domain/{domain-id}` to set the `vlan-vni-offset` attribute.

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

## Troubleshoot Configuration Changes

When a configuration change fails, you see an error in the change request.

### Configuration Fails Because of a Dependency

If you stage a configuration but it fails because of a dependency, the failure shows the reason. In the following example, the change fails because the BGP router ID is not set:

```
cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' --insecure https://127.0.0.1:8765/nvue_v1/revision/4
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

The staged configuration is missing `router-id`:

```
cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' --insecure https://127.0.0.1:8765/nvue_v1/vrf/default/router/bgp?rev=4
{
  "autonomous-system": 65999,
  "enable": "on"
}
```

### Configuration Apply Fails with Warnings

In some cases, such as the first push with NVUE or if you change a file manually instead of using NVUE, you see a warning prompt and the apply fails:

```
cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' --insecure -X GET https://127.0.0.1:8765/nvue_v1/revision/4
{
  "4": {
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

To resolve this issue, observe the failures or errors, and inspect the configuration that you are trying to apply. After you resolve the errors, retry the API. If you prefer to overlook the errors and force an apply, add `"auto-prompt":{"ays": "ays_yes"}` to the configuration apply.

```
cumulus@switch:~$ curl -u 'cumulus:CumulusLinux!' -d '{"state":"apply","auto-prompt":{"ays": "ays_yes"}}' -H 'Content-Type:application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/revision/4
```

## NVUE REST API Documentation

For information about using the NVUE REST API, refer to the {{<mib_link url="cumulus-linux-54/api/index.html" text="NVUE API documentation.">}}

## Considerations

Unlike the NVUE CLI, the NVUE API does not support configuring a plain text password for a user account; you must configure a hashed password for a user account with the NVUE API.

## Related Information

- {{<exlink url="https://docs.nginx.com/" text="NGINX documentation">}}
- {{<exlink url="https://help.ubuntu.com/lts/serverguide/certificates-and-security.html" text="Ubuntu Certificates and Security documentation">}}
