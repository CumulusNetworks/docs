---
title: NVUE API
author: NVIDIA
weight: 125
toc: 3
---
This section provides information about using the NVUE API.

## Access the API

To access the NVUE API, run these commands on the switch:

```
cumulus@switch:~$ sudo ln -s /etc/nginx/sites-{available,enabled}/nvue.conf
cumulus@switch:~$ sudo sed -i 's/listen localhost:8765 ssl;/listen \[::\]:8765 ipv6only=off ssl;/g' /etc/nginx/sites-available/nvue.conf
cumulus@switch:~$ sudo systemctl restart nginx
```

## Access the NVUE REST API from a Front Panel Port

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

Cumulus Linux contains a self-signed certificate and private key used server-side in this application so that it works out of the box; however, NVIDIA recommends you use your own certificates and keys. Certificates must be in PEM format.

For step by step documentation on generating self-signed certificates and keys, and installing them on the switch, refer to the {{<exlink url="https://help.ubuntu.com/lts/serverguide/certificates-and-security.html" text="Ubuntu Certificates and Security documentation">}}.

After installing the certificates and keys, edit the `/etc/nginx/sites-available/nvue.conf` file to set the `ssl_certificate` and the `ssl_certificate_key` values to your keys, then restart NGINX with the `sudo systemctl restart nginx` command.

## Run cURL Commands

You can run the cURL commands from the command line. Use the username and password for the switch. For example:

```
cumulus@switch:~$ curl  -u 'cumulus:CumulusLinux!' --insecure https://127.0.0.1:8765/cue_v1/interface
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

## Set a Configuration Change

To make a configuration change with the NVUE API:

1. Create a new revision ID using a POST:

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure -X POST https://127.0.0.1:8765/nvue_v1/revision
   {
     "changeset/cumulus/2021-11-02_16.09.18_5Z1K": {
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

2. Record the revision ID. In the above example, the revision ID is `"changeset/cumulus/2021-11-02_16.09.18_5Z1K"`

3. Make the change using a PATCH and link it to the revision ID:

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"99.99.99.99/32": {}}' -H 'Content-Type: application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/interface/lo/ip/address?rev=changeset/cumulus/2021-11-02_16.09.18_5Z1K
   {
     "99.99.99.99/32": {}
   }
   ```

4. Apply the changes using a PATCH to the revision changeset. You must use the full key value for the revision and replace `/`​ with `%2F`​ in the list:

   ```
   cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"state":"apply"}' -H 'Content-Type:application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/revision/changeset%2Fcumulus%2F2021-11-02_16.09.18_5Z1K
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
   cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/revision/changeset%2Fcumulus%2F2021-11-02_16.09.18_5Z1K
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

## Unset a Configuration Change

To unset a change, use the `null` value to the key. For example, to delete `vlan100` from a switch, use the following syntax:

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"vlan100":null}' -H 'Content-Type: application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/interface?rev=changeset/cumulus/2021-11-29_11.46.23_6C7T
```

When you unset a change, you must still use the `PATCH` action. The value indicates removal of the entry. The data is `{"vlan100":null}` with the PATCH action.

## Troubleshoot Configuration Changes

When a configuration change fails, you see an error in the change request.

### Configuration Fails Because of a Dependency

If you stage a configuration but it fails because of a dependency, the failure shows the reason. In the following example, the change fails because the BGP router ID is not set:

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/revision/changeset%2Fcumulus%2F2021-11-02_13.57.25_5Z1H
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
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure https://127.0.0.1:8765/nvue_v1/vrf/default/router/bgp?rev=changeset%2Fcumulus%2F2021-11-02_13.57.25_5Z1H
{
  "autonomous-system": 65999,
  "enable": "on"
}
```

### Configuration Apply Fails with Warnings

In some cases, such as the first push with NVUE or if you change a file manually instead of using NVUE, you see a warning prompt and the apply fails:

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' --insecure -X GET https://127.0.0.1:8765/nvue_v1/revision/changeset%2Fcumulus%2F2021-11-02_16.09.18_5Z1K
{
  "changeset/cumulus/2021-11-02_16.09.18_5Z1K": {
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

To resolve this issue, include `"auto-prompt":{"ays": "ays_yes"}` to the configuration apply:

```
cumulus@switch:~$ curl -u 'cumulus:cumulus' -d '{"state":"apply","auto-prompt":{"ays": "ays_yes"}}' -H 'Content-Type:application/json' --insecure -X PATCH https://127.0.0.1:8765/nvue_v1/revision/changeset%2Fcumulus%2F2021-11-02_16.09.18_5Z1K
```

## NVUE REST API Documentation

For information about using the NVUE REST API, refer to the {{<mib_link url="cumulus-linux-51/api/index.html" text="NVUE API documentation.">}}

## Related Information

- {{<exlink url="https://docs.nginx.com/" text="NGINX documentation">}}
- {{<exlink url="https://help.ubuntu.com/lts/serverguide/certificates-and-security.html" text="Ubuntu Certificates and Security documentation">}}
