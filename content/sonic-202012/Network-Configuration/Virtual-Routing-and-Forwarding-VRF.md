---
title: Virtual Routing and Forwarding - VRF
author: Cumulus Networks
weight: 430
product: SONiC
version: 202012
siteSlug: sonic
---


This command is used to bind an interface to a VRF. By default, all layer 3 interfaces are placed in the default VRF.

Configure VRFs in the VRF table in `/etc/sonic/config_db.json`.

{{<tabs "VRF">}}

{{<tab "SONiC CLI">}}

admin@leaf01:~$ sudo config interface fec Ethernet4 fc

{{</tab>}}

{{<tab "config_db.json">}}

Configure the VRF in the PORT table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        "lanes": "29,30,31,32",  - hardware lanes associated with this port
        "fec": "fc",             - Forward Error Correction mode
        "mtu": "9100",           - Port MTU
        "alias": "Ethernet4",   - Port alias
        "admin_status": "up",    - Admin status
        "speed": "100000",       - port speed (in Mbit/s)
        "pfc_asym": "on",         - Flag shows if asymmetric PFC feature is enabled on this port
    },

    ...

}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y



## Management VRFs
