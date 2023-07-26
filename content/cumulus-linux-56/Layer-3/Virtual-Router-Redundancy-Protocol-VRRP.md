---
title: Virtual Router Redundancy Protocol - VRRP
author: NVIDIA
weight: 963
toc: 3
---
<span style="background-color:#F5F5DC">[VRRP](## "Virtual Router Redundancy Protocol")</span> allows two or more network devices in an active standby configuration to share a single virtual default gateway. The VRRP router that forwards packets at any given time is the master. If this VRRP router fails, another VRRP standby router automatically takes over as master. The master sends VRRP advertisements to other VRRP routers in the same virtual router group, which include the priority and state of the master. VRRP router priority determines the role that each virtual router plays and who becomes the new master if the master fails.

Use VRRP when you have multiple distinct devices that connect to a layer 2 segment through multiple logical connections (not through a single bond). VRRP elects a single active forwarder that *owns* the virtual MAC address while it is active. This prevents the forwarding database of the layer 2 domain from continuously updating in response to MAC flaps because the switch receives frames sourced from the virtual MAC address from discrete logical connections.

All virtual routers use 00:00:5E:00:01:XX for IPv4 gateways or 00:00:5E:00:02:XX for IPv6 gateways as their MAC address. The last byte of the address is the Virtual Router IDentifier (VRID), which is different for each virtual router in the network. Only one physical router uses this MAC address at a time. The router replies with this address when it receives ARP requests or neighbor solicitation packets for the IP addresses of the virtual router.

{{%notice note%}}
- Cumulus Linux supports both VRRPv2 and VRRPv3. The default protocol version is VRRPv3.
- You can configure a maximum of 255 virtual routers on a switch.
- You cannot use VRRP with <span style="background-color:#F5F5DC">[MLAG](## "Multi-chassis Link Aggregation")</span>.
- To configure VRRP on an <span style="background-color:#F5F5DC">[SVI](## "Switched Virtual Interface")</span> or {{<link url="Traditional-Bridge-Mode" text="traditional mode bridge">}}, you need to edit the `etc/network/interfaces` and `/etc/frr/frr.conf` files.
- You can use VRRP with layer 3 interfaces and subinterfaces that are part of a <span style="background-color:#F5F5DC">[VRF](## "Virtual Routing and Forwarding")</span>.
- You cannot use VRRP in an <span style="background-color:#F5F5DC">[EVPN](## "Ethernet Virtual Private Network")</span> configuration; use MLAG and VRR instead.
You cannot configure both VRR and VRRP on the same switch.
{{%/notice%}}

{{<exlink url="https://tools.ietf.org/html/rfc5798#section-4.1" text="RFC 5798">}} describes VRRP in detail.

The following example illustrates a basic VRRP configuration.

{{< img src = "/images/cumulus-linux/vrrp-example.png" >}}

### Configure VRRP

To configure VRRP, specify the following information on each switch:

- **A virtual router ID (VRID) that identifies the group of VRRP routers**. You must specify the same ID across all virtual routers in the group.
- **One or more virtual IP addresses for the virtual router group**. These IP addresses do not directly connect to a specific interface. The switch redirects inbound packets to a virtual IP address to a physical network interface.

You can also set these optional parameters:

| Optional Parameter | Default Value | Description|
| -----------| -------------| ------------- |
| `priority` | 100 | The priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master. |
| `advertisement interval` | 1000 milliseconds | The advertisement interval is the interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950.|
| `preempt` | enabled | Preempt mode lets the router take over as master for a virtual router group if it has a higher priority than the current master. Preempt mode is on by default. To disable preempt mode, edit the `/etc/frr/frr.conf` file to add the line `no vrrp <VRID> preempt` to the interface stanza, then restart the FRR service.|
| `version` | 3 | The VRRP protocol version. You can specify a value of either 2 or 3.|

The following example commands configure two switches (spine01 and spine02) that form one virtual router group (VRID 44) with IPv4 address 10.0.0.1/24 and IPv6 address 2001:0db8::1/64. *spine01* is the master; it has a priority of 254. *spine02* is the backup VRRP router.

{{%notice note%}}
The parent interface must use a primary address as the source address on VRRP advertisement packets.
{{%/notice%}}

{{< tabs "TabID448 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID504 ">}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface swp1 ip address 10.0.0.2/24
cumulus@spine01:~$ nv set interface swp1 ip address 2001:0db8::2/64
cumulus@spine01:~$ nv set interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
cumulus@spine01:~$ nv set interface swp1 ip vrrp virtual-router 44 address 2001:0db8::1
cumulus@spine01:~$ nv set interface swp1 ip vrrp virtual-router 44 priority 254
cumulus@spine01:~$ nv set interface swp1 ip vrrp virtual-router 44 advertisement-interval 5000
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ nv set interface swp1 ip address 10.0.0.3/24
cumulus@spine02:~$ nv set interface swp1 ip address 2001:0db8::3/64
cumulus@spine02:~$ nv set interface swp1 ip vrrp virtual-router 44 address 10.0.0.1/24
cumulus@spine02:~$ nv set interface swp1 ip vrrp virtual-router 44 address 2001:0db8::1/64
cumulus@spine02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

{{< tabs "TabID557 ">}}
{{< tab "spine01 ">}}

1. Edit the `/etc/network/interface` file to assign an IP address to the parent interface; for example:

   ```
   cumulus@spine01:~$ sudo vi /etc/network/interfaces
   ...
   auto swp1
   iface swp1
       address 10.0.0.2/24
       address 2001:0db8::2/64
   ```

2. Enable the `vrrpd` daemon, then start the FRR service. See {{<link title="FRRouting">}}.

3. From the vtysh shell, configure VRRP.

    ```
    cumulus@spine01:~$ sudo vtysh
    ...
    spine01# configure terminal
    spine01(config)# interface swp1
    spine01(config-if)# vrrp 44 ip 10.0.0.1
    spine01(config-if)# vrrp 44 ipv6 2001:0db8::1
    spine01(config-if)# vrrp 44 priority 254
    spine01(config-if)# vrrp 44 advertisement-interval 5000
    spine01(config-if)# end
    spine01# write memory
    spine01# exit
    ```

{{< /tab >}}
{{< tab "spine02 ">}}

1. Edit the `/etc/network/interface` file to assign an IP address to the parent interface; for example:

   ```
   cumulus@spine02:~$ sudo vi /etc/network/interfaces
   ...
   auto swp1
   iface swp1
       address 10.0.0.3/24
       address 2001:0db8::3/64
   ```

2. Enable the `vrrpd` daemon, then start the FRR service. See {{<link title="FRRouting">}}.

3. From the vtysh shell, configure VRRP.

   ```
   cumulus@spine02:~$ sudo vtysh
   ...
   spine02# configure terminal
   spine02(config)# interface swp1
   spine02(config-if)# vrrp 44 ip 10.0.0.1
   spine02(config-if)# vrrp 44 ipv6 2001:0db8::1
   spine02(config-if)# end
   spine02# write memory
   spine02# exit
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

The vtysh commands save the configuration in the `/etc/network/interfaces` file and the `/etc/frr/frr.conf` file. For example:

```
cumulus@spine01:~$ sudo cat /etc/network/interfaces
...
auto swp1
iface swp1
    address 10.0.0.2/24
    address 2001:0db8::2/64
    vrrp 44 10.0.0.1/24 2001:0db8::1/64
...
```

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
interface swp1
vrrp 44
vrrp 44 advertisement-interval 5000
vrrp 44 priority 254
vrrp 44 ip 10.0.0.1
vrrp 44 ipv6 2001:0db8::1
...
```

### Show VRRP Configuration

To show global VRRP configuration, run the NVUE `nv show router vrrp` command:

```
cumulus@switch:~$ nv show router vrrp
                        applied
----------------------  -------
enable                  on     
advertisement-interval  1000   
preempt                 on     
priority                100    
```

The vtysh `show vrrp` command shows VRRP configuration and operational data:

```
...
switch# show vrrp
 Virtual Router ID                       44                          
 Protocol Version                        3                           
 Autoconfigured                          No                          
 Shutdown                                No                          
 Interface                               swp1                        
 VRRP interface (v4)                     vrrp4-3-44                  
 VRRP interface (v6)                     vrrp6-3-44                  
 Primary IP (v4)                         10.0.0.2                    
 Primary IP (v6)                         fe80::14a8:c009:2597:9854   
 Virtual MAC (v4)                        00:00:5e:00:01:2c           
 Virtual MAC (v6)                        00:00:5e:00:02:2c           
 Status (v4)                             Master                      
 Status (v6)                             Master                      
 Priority                                254                         
 Effective Priority (v4)                 254                         
 Effective Priority (v6)                 254                         
 Preempt Mode                            Yes                         
 Accept Mode                             Yes                         
 Advertisement Interval                  5000 ms                     
 Master Advertisement Interval (v4) Rx   5000 ms (stale)             
 Master Advertisement Interval (v6) Rx   5000 ms (stale)             
 Advertisements Tx (v4)                  4                           
 Advertisements Tx (v6)                  3                           
 Advertisements Rx (v4)                  0                           
 Advertisements Rx (v6)                  0                           
 Gratuitous ARP Tx (v4)                  1                           
 Neigh. Adverts Tx (v6)                  1                           
 State transitions (v4)                  2                           
 State transitions (v6)                  2                           
 Skew Time (v4)                          30 ms                       
 Skew Time (v6)                          30 ms                       
 Master Down Interval (v4)               15030 ms                    
 Master Down Interval (v6)               15030 ms                    
 IPv4 Addresses                          1                           
 ..................................      10.0.0.1                    
 IPv6 Addresses                          1                           
 ..................................      2001:db8::1
```

To show configuration and operational information about all configured VRRP virtual routers, run the NVUE `nv show interface <interface-id> ip vrrp virtual-router` command or the vtysh `show vrrp` command.

Add `-o json` at the end of the NVUE command to see the output in a more readable format:

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router -o json
{
  "44": {
    "accept-mode": "on",
    "address-family": {
      "ipv4": {
        "counters": {
          "adv-rx": 0,
          "adv-tx": 4663,
          "garp-tx": 1,
          "state-transitions": 2
        },
        "down-interval": 15030,
        "master-adv-interval": 5000,
        "primary-addr": "10.0.0.2",
        "priority": 254,
        "skew-time": 30,
        "status": "Master",
        "virtual-addresses": {
          "10.0.0.1": {}
        },
        "vmac": "00:00:5e:00:01:2c",
        "vrrp-interface": "vrrp4-3-44"
      },
      "ipv6": {
        "counters": {
          "adv-rx": 0,
          "adv-tx": 4662,
          "neigh-adv-tx": 1,
          "state-transitions": 2
        },
        "down-interval": 15030,
        "master-adv-interval": 5000,
        "primary-addr": "fe80::42cc:fd5c:fb48:76a8",
        "priority": 254,
        "skew-time": 30,
        "status": "Master",
        "virtual-addresses": {
          "2001:db8::1": {}
        },
        "vmac": "00:00:5e:00:02:2c",
        "vrrp-interface": "vrrp6-3-44"
      }
    },
    "advertisement-interval": 5000,
    "auto-config": "off",
    "interface": "swp1",
    "is-shutdown": "off",
    "preempt": "on",
    "priority": 254,
    "version": 3
  }
}
```

To show configuration information about a specific VRRP virtual router, run the NVUE `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id>` command or the vtysh `show vrrp <virtual-router-id>` command:

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router 44
                        operational  applied
----------------------  -----------  ------------
advertisement-interval  5000         5000
preempt                 on           auto
priority                254          254
version                 3            3
[address]                            10.0.0.1
[address]                            2001:0db8::1
accept-mode             on
auto-config             off
interface               swp1
is-shutdown             off
[address-family]        ipv4
[address-family]        ipv6
```

The vtysh `show vrrp <virtual-router-id>` command shows operational information in addition to configuration information:

```
...
switch# show vrrp  44

 Virtual Router ID                       44                          
 Protocol Version                        3                           
 Autoconfigured                          No                          
 Shutdown                                No                          
 Interface                               swp1                        
 VRRP interface (v4)                     vrrp4-3-44                  
 VRRP interface (v6)                     vrrp6-3-44                  
 Primary IP (v4)                         10.0.0.2                    
 Primary IP (v6)                         fe80::42cc:fd5c:fb48:76a8   
 Virtual MAC (v4)                        00:00:5e:00:01:2c           
 Virtual MAC (v6)                        00:00:5e:00:02:2c           
 Status (v4)                             Master                      
 Status (v6)                             Master                      
 Priority                                254                         
 Effective Priority (v4)                 254                         
 Effective Priority (v6)                 254                         
 Preempt Mode                            Yes                         
 Accept Mode                             Yes                         
 Advertisement Interval                  5000 ms                     
 Master Advertisement Interval (v4) Rx   5000 ms (stale)             
 Master Advertisement Interval (v6) Rx   5000 ms (stale)             
 Advertisements Tx (v4)                  4710                        
 Advertisements Tx (v6)                  4709                        
 Advertisements Rx (v4)                  0                           
 Advertisements Rx (v6)                  0                           
 Gratuitous ARP Tx (v4)                  1                           
 Neigh. Adverts Tx (v6)                  1                           
 State transitions (v4)                  2                           
 State transitions (v6)                  2                           
 Skew Time (v4)                          30 ms                       
 Skew Time (v6)                          30 ms                       
 Master Down Interval (v4)               15030 ms                    
 Master Down Interval (v6)               15030 ms                    
 IPv4 Addresses                          1                           
 ..................................      10.0.0.1                    
 IPv6 Addresses                          1                           
 ..................................      2001:db8::1 
 ```
