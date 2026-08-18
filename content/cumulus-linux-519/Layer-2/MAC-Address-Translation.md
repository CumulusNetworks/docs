---
title: MAC Address Translation
author: NVIDIA
weight: 525
toc: 3
---
MAC address translation enables you to translate the source MAC address for packets on egress and the destination MAC address for packets on ingress. MAC address translation is equivalent to {{<link url="Network-Address-Translation-NAT/#static-nat" text="static NAT">}} but operates at layer 2 on Ethernet frames.

## Configure MAC Address Translation

To configure MAC address translation:
- Enable MAC address translation. 
- Create a rule that matches a source or destination MAC address and translate the MAC address to a public MAC address.
- Apply the rule that matches a source MAC address to an outbound interface. Apply the rule that matches a destination MAC address to an inbound interface.

{{%notice note%}}
Cumulus Linux only supports one MAC address in a translation rule.
{{%/notice%}}

{{< tabs "TabID112 ">}}
{{< tab "NVUE Commands ">}}

The following example matches Ethernet packets with source MAC address 01:12:34:32:11:01 and translates the MAC address to 99:de:fc:32:11:01 on egress on swp5.

```
cumulus@switch:~$ nv set acl MACL1 type mac
cumulus@switch:~$ nv set acl MACL1 rule 1 match mac source-mac b8:ce:f6:3c:62:06  
cumulus@switch:~$ nv set acl MACL1 rule 1 action source-nat translate-mac 99:de:fc:32:11:01 
cumulus@switch:~$ nv config apply

cumulus@switch:~$ nv set interface swp5 acl MACL1 outbound  
cumulus@switch:~$ nv config apply   
```

The following example matches Ethernet packets with destination MAC address 01:12:34:32:11:01 and translates the MAC address to 99:de:fc:32:11:01 on ingress on swp5.

```
cumulus@switch:~$ nv set acl MACL2 type mac
cumulus@switch:~$ nv set acl MACL2 rule 1 match mac dest-mac 01:12:34:32:11:01 
cumulus@switch:~$ nv set acl MACL2 rule 1 action dest-nat translate-mac 99:de:fc:32:11:01
cumulus@switch:~$ nv config apply

cumulus@switch:~$ nv set interface swp5 acl MACL2 inbound  
cumulus@switch:~$ nv config apply   
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To create rules, use `cl-acltool`.

To add rules using `cl-acltool`, either edit an existing file in the `/etc/cumulus/acl/policy.d` directory and add rules under `[ebtables]` or create a new file in the `/etc/cumulus/acl/policy.d` directory and add rules under an `[ebtables]` section. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/60_mac.rules
[ebtables]

 #Add rule
```

**Example Rules**

The following example matches Ethernet packets with source MAC address 01:12:34:32:11:01 and translates the MAC address to 99:de:fc:32:11:01 on egress on swp5.

```
[ebtables]

-t nat -A POSTROUTING -s 01:12:34:32:11:01 -j snat --to-source 99:de:fc:32:11:01 –o swp5   
```

The following example matches Ethernet packets with destination MAC address 01:12:34:32:11:01 coming in on swp5 and translates the MAC address to 99:de:fc:32:11:01 on ingress on swp5.

```
[ebtables]

-t nat -A PREROUTING -d 01:12:34:32:11:01 -j dnat --to-dst 99:de:fc:32:11:01 –i swp5  
```

{{< /tab >}}
{{< /tabs >}}

## Show MAC Address Translation Configuration and Statistics

To show the current MAC address translation configuration:

```
cumulus@switch:~$ nv show acl
       type  Summary
-----  ----  -------
MACL1  mac   rule: 1
MACL2  mac   rule: 1
```

To show information about a specific MAC address translation rule, run the `nv show acl <name> --applied -o=json` command:

```
cumulus@switch:~$ nv show acl MACL1 --applied -o=json
{
  "rule": {
    "1": {
      "action": {
        "source-nat": {
          "translate-ip": {},
          "translate-mac": "99:de:fc:32:11:01",
          "translate-port": {}
        }
      },
      "match": {
        "mac": {
          "dest-mac-mask": "ff:ff:ff:ff:ff:ff",
          "source-mac": "b8:ce:f6:3c:62:06",
          "source-mac-mask": "ff:ff:ff:ff:ff:ff"
        }
      }
    }
  },
  "type": "mac"
}
```

To show statistics for MAC address translation, such as the number of packets that match the rules and the number of bytes in the matched packets, run the NVUE `nv show interface acl-statistics` command or the Linux `cl-acltool -L eb` command:

```
cumulus@switch:~$ nv show interface acl-statistics
Interface  ACL Name   Rule ID   In Packets  In Bytes  Out Packets  Out Bytes
---------  ---------  -------   ----------  --------  -----------  ---------
swp2       macl_snat  10                              14            1.13 KB
```

```
cumulus@switch:~$ sudo cl-acltool -L eb
-s ec:d:9a:84:8b:82 -o swp2 --comment rule_id:10 -j snat --to-src 0:0:0:0:0:2 --snat-target ACCEPT, pcnt = 14 -- bcnt = 1162
```

In the above example Linux command output:
- `pcnt` shows how many packets matched this rule (14 packets).
- `bcnt` shows the total number of bytes in the matched packets (1162 bytes).
