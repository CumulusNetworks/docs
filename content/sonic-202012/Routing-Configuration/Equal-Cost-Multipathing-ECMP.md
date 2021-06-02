---
title: Equal Cost Multipathing - ECMP
author: NVIDIA
weight: 530
product: SONiC
version: 202012
siteSlug: sonic
---

*Fine-grained ECMP* (equal cost multipathing) provides a mechanism to configure a consistent and layered hashing.

With regular ECMP, any change to a container's contents results in a rehashing of all the flows, with most of them changing the resulting next hop. Fine-grained ECMP exposes a large fixed size ECMP table to the application, which takes full management, assigning a portion of the hash bins to each of the next hops.

## Configure ECMP

Currently there is no CLI available to configure ECMP; you can only configure it directly in the `config_db.json` file, in the FG_NHG, FG_NHG_MEMBER and FG_NHG_PREFIX tables.

You configure the following fields in the FG_NHG table:

- `bucket_size`: The total hash bucket size desired. The recommended value is the lowest common multiple of *1..{maximum # of next hops}*.
- `match_mode`: The filtering method used to identify when to use fine-grained or regular route handling:
  - `nexthop-based`: Looks to the next hop IP address to filter routes and uses fine-grained ECMP when the next hop IP address matches the FG_NHG_MEMBER IP address.
  - `route-based`: Looks to the prefix to filter routes, and uses fine-grained ECMP when the route prefix matches the FG_NHG_PREFIX prefix.

You configure the following fields in the FG_NHG_MEMBER table:

- `bank`: An index that specifies a bank or group where the redistribution occurs.
- `link`: A link associated with the `next-hop-ip`. If configured, it enables next hop withdrawal or addition when the link's operational state changes.
- `FG_NHG`: Reference the FG_NHG table and provide the next hop group name.

You configure the following field in the FG_NHG_PREFIX table:

- `FG_NHG`: Reference the FG_NHG table and provide the next hop group name.

### Configure Next Hop-based Mode

Following is an example configuration using next hop-based mode:

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json
{ 
    "FG_NHG": { 
        "2-VM-Sets": { 
            "bucket_size": 12, 
            "match_mode": "nexthop-based" 
        } 
    }, 

    "FG_NHG_MEMBER": { 
        "1.1.1.1": { 
            "FG_NHG": "2-VM-Sets", 
            "bank": 0, 
            "link": "Ethernet4" 
        }, 
        "1.1.1.2": { 
            "FG_NHG": "2-VM-Sets", 
            "bank": 0, 
            "link": "Ethernet8" 
        }, 
        "1.1.1.3": { 
            "FG_NHG": "2-VM-Sets", 
            "bank": 1, 
            "link": "Ethernet12" 
        }, 
        "1.1.1.4": { 
            "FG_NHG": "2-VM-Sets", 
            "bank": 1, 
            "link": "Ethernet16" 
        } 
    }
}
admin@switch:~$ sudo config save -y
```

### Configure Route-based Mode

Following is an example configuration using route-based mode:

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json
{
    "FG_NHG": {
        "2-VM-Sets": {
            "bucket_size": 12,
            "match_mode": "route-based"
        }
    },
    "FG_NHG_PREFIX": {
        "10.10.10.10/32": {
            "FG_NHG": "2-VM-Sets"
        }
    },
    "FG_NHG_MEMBER": {
        "1.1.1.1": {
            "FG_NHG": "2-VM-Sets",
            "bank": 0,
            "link": "Ethernet4"
        },
        "1.1.1.2": {
            "FG_NHG": "2-VM-Sets",
            "bank": 0,
            "link": "Ethernet8"
        },
        "1.1.1.3": {
            "FG_NHG": "2-VM-Sets",
            "bank": 1,
            "link": "Ethernet12"
        },
        "1.1.1.4": {
            "FG_NHG": "2-VM-Sets",
            "bank": 1,
            "link": "Ethernet16"
        }
    }
}
admin@switch:~$ sudo config save -y
```

## Show the ECMP Configuration

To display fine-grained ECMP information in a hash view, run:

```
admin@switch:~$ show fgnhg hash-view

+-----------------+--------------------+----------------+ 
| FG_NHG_PREFIX   | Next Hop           | Hash buckets   | 
+=================+====================+================+ 
| 100.50.25.12/32 | 200.200.200.4      | 0              | 
|                 |                    | 1              | 
|                 |                    | 2              | 
|                 |                    | 3              | 
|                 |                    | 4              | 
|                 |                    | 5              | 
|                 |                    | 6              | 
|                 |                    | 7              | 
|                 |                    | 8              | 
|                 |                    | 9              |
|                 |                    | 10             | 
|                 |                    | 11             | 
|                 |                    | 12             | 
|                 |                    | 13             | 
|                 |                    | 14             | 
|                 |                    | 15             | 
+-----------------+--------------------+----------------+ 
```

To display fine-grained ECMP active next hops, run:

```
admin@sonic:~$ show fgnhg active-hops
+-----------------+--------------------+
| FG_NHG_PREFIX   | Active Next Hops   |
+=================+====================+
| 100.50.25.12/32 | 200.200.200.4      |
|                 | 200.200.200.5      |
+-----------------+--------------------+
| fc:5::/128      | 200:200:200:200::4 |
|                 | 200:200:200:200::5 |
+-----------------+--------------------+
```

## Policy-based Hashing  

*Policy-based hashing* (PBH) extends Fine Grained ECMP. It provides a custom hashing for specific types of packets based on an inner 5 tuple, such as SRC/DST port, SRC/DST IPv4/IPv6 or IP protocol. It uses {{<link url="Access-Control-Lists-ACLs" text="ACL rules">}} to calculate and set the ECMP hash.

After you enable it, PBH is automatically configured on all existing ports and port channels in the system.

Only static hashes are currently supported. For additional values, please contact your NVIDIA Mellanox support.

PBH is disabled by default. To enable it, add the following key/value in the SAI XML for the relevant SKU you wish to use:

    <pbhash_gre><value></pbhash_gre>

Example:

```
admin@switch:~$ sudo vi /usr/share/sonic/device/x86_64-mlnx_msn3800-r0/ACS-MSN3800/sai_3800.xml

<?xml version="1.0"?> 
<root> 
    <platform_info type="3800"> 
        <!-- Device MAC address  --> 
        <device-mac-address>00:02:03:04:05:00</device-mac-address> 
        <!-- Enable PBH static --> 
        <pbhash_gre>100</pbhash_gre> 
...
```

{{%notice info%}}

PBH is supported only on NVIDIA Spectrum 2 and Spectrum 3 ASICs. It is not available on NVIDIA Spectrum 1 switches and switches from other vendors.

{{%/notice%}}
