---
title: OVSDB Server High Availability
author: NVIDIA
weight: 700
toc: 4
---
{{%notice warning%}}
OVSDB server high availability is an [early access feature]({{<ref "/knowledge-base/Support/Support-Offerings/Early-Access-Features-Defined" >}}).
{{%/notice%}}

Cumulus Linux supports integration with VMware NSX in both *standalone mode* and *OVSDB server high availability mode* (where the data plane is running in active-active mode). For information about VMware NSX in standalone mode and for a description of the components that work together to integrate VMware NSX and Cumulus Linux, see {{<link url="Integrating-Hardware-VTEPs-with-VMware-NSX-V">}}.

{{%notice note%}}
Cumulus Linux supports OVSDB service node replication only.
{{%/notice%}}

With OVSDB server high availability mode, you use two peer Cumulus Linux switches in an MLAG configuration. Both the MLAG primary and MLAG secondary switch contain OVSDB server and VTEPd. The OVSDB servers synchronize their databases with each other and always maintain the replicated state unless failover occurs; for example, the peer link bond breaks, a switch fails, or the OVSDB server goes down. Both of the VTEPd components talk to the active OVSDB server to read the configuration and then push the configuration to the kernel. Only the active OVSDB server communicates with the NSX controller, unless failover occurs and then the standby OVSDB server takes over automatically. Although the Cumulus switches are configured as an MLAG pair, the NSX controller sees them as a single system (the NSX controller is not aware that multiple switches exist).

The following examples show OVSDB server high availability mode.

**Example 1:** The OVSDB server on the MLAG primary switch is active. The OVSDB server on the MLAG secondary switch is the hot standby. Only the active OVSDB server communicates with the NSX controller.

{{< img src = "/images/cumulus-linux/ovsdb-example.png" >}}

**Example 2:** If failover occurs, the OVSDB server on the MLAG
secondary switch becomes the active OVSDB server and communicates with
the NSX controller.

{{< img src = "/images/cumulus-linux/ovsdb-example2.png" >}}

When the OVSDB server on the MLAG primary switch starts responding again, it resynchronizes its database, becomes the active OVSDB server, and connects to the controller. At the same time, the OVSDB server on the MLAG secondary switch stops communicating with the NSX controller, synchronizes with the now active OVSDB server, and takes the standby role again.

{{%notice note%}}
When you upgrade Cumulus Linux, both the `/usr/share/openvswitch/scripts/ovs-ctl-vtep` file and the database file `conf.db` are overwritten. Be sure to back up both files before upgrading.
{{%/notice%}}

## Getting Started

Before you configure OVSDB server high availability, make sure you have **two switches running Cumulus Linux in an MLAG configuration**. Cumulus Linux includes OVSDB server (`ovsdb-server`) and VTEPd (`ovs-vtepd`), which support {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridges">}}.

The following example configuration in the `/etc/network/interfaces` file shows the *minimum* MLAG configuration required (the MLAG peerlink configuration and the dual-connected bonds on the peer switches). The dual-connected bonds are identified in the NSX controller by their `clag-id` (single-connected bonds or ports are identified by their usual interface names prepended with the name of the particular switch to which they belong). When you create the Gateway Service for the dual-connected bonds (described in {{<link url="#configure-the-transport-and-logical-layers" text="Configuring the Transport and Logical Layers">}}, below), make sure to select the `clag-id` named interfaces instead of the underlying individual physical ports. All the logical network configurations are provisioned by the NSX controller.

```
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    mtu  9202
    alias Local Node/s leaf01 and Ports swp5 swp6 <==> Remote  Node/s leaf02 and Ports swp5 swp6

auto peerlink-3.4094
iface peerlink-3.4094
    address 10.0.0.24/32
    address 169.254.0.9/29
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.10
    clagd-args --vm --debug 0x0
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.25

auto hostbond4
iface hostbond4
    bond-slaves swp7
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    mtu  9152
    alias Local Node/s leaf01 and Ports swp7 <==> Remote  Node/s hostd-01 and Ports swp1
    clag-id 1

auto hostbond5
iface hostbond5
    bond-slaves swp8
    bond-mode 802.3ad
    bond-min-links 1
    bond-lacp-rate 1
    mtu  9152
    alias Local Node/s leaf01 and Ports swp8 <==> Remote  Node/s hostd-02 and Ports swp1
    clag-id 2
```

To configure OVSDB server high availability, you need to:

- Determine on which switch you want to run the active OVSDB server (the MLAG primary switch or the MLAG secondary switch).
- Configure the NSX integration on both switches.
- Configure the Transport and Logical Layers from the NSX Manager.
- Verify the VXLAN Configuration.

{{%notice note%}}
The OVSDB server cannot select the loopback interface as the source IP address, causing top of rack registration to the controller to fail. To work around this issue, run the NVUE `nv set vrf default router bgp address-family ipv4-unicast route-redistribute connected` command.
{{%/notice%}}

## Configure the NSX Integration on the Switch

Before you start configuring the gateway service, the logical switches, and ports that comprise the VXLAN, you need to enable and start the `openvswitch-vtep` service, then run the configuration script **on both the MLAG primary and MLAG secondary switches**. Follow these steps:

Enable and start the `openvswitch-vtep` service:

```
cumulus@switch:~$ sudo systemctl enable openvswitch-vtep.service
cumulus@switch:~$ sudo systemctl start openvswitch-vtep.service
```

Run the configuration script provided with Cumulus Linux:

1. On the switch where you want to run the active OVSDB server, run the `vtep-bootstrap` command with these options:

    - `db_ha active` specifies that the OVSDB server on this switch is the *active* server.
    - `db_ha_vip` is any unused IP address in the subnet used by the peerlink control subinterface (4094 is typically used). This creates a /32 route that can be reached from either MLAG switch (`169.254.0.11:9998` in the example below).
    - `db_ha_repl_sv` specifies the IP address of the **active** OVSDB server (`169.254.0.9:9999` in the example command below). The standby OVSDB server uses this IP address to synchronize the database.
    - `controller_port` is the port used to communicate with the NSX controller.
    - `controller_ip` is the IP address of the NSX controller (192.168.100.17 in the example command below).
    - The ID for the VTEP (`vtep7` in the example command below).
    - The datapath IP address of the VTEP (`172.16.20.157` in the example command below). This is the VXLAN anycast IP address.
    - The IP address of the management interface on the switch (`192.168.100.157` in the example command below). This interface is used for control traffic.

      ```
      cumulus@switch:~$ vtep-bootstrap  --db_ha active  --db_ha_vip 169.254.0.11:9998  --db_ha_repl_sv 169.254.0.9:9999 --controller_ip 192.168.100.17 vtep7 172.16.20.157 192.168.100.157
      Executed:
                create certificate on a switch, to be used for authentication with controller
                  ().
      Executed:
                sign certificate
                  (vtep7-req.pem   Tue Sep 11 21:11:27 UTC 2018
                    fingerprint a4cda030fe5e458c0d7ba44e22f52650f01bcd75).
      Executed:
                define physical switch
                 ().
      Executed:
                define NSX controller IP address in OVSDB
                  ().
      Executed:
                define local tunnel IP address on the switch
                  ().
      Executed:
                define management IP address on the switch
                  ().
      Executed:
                restart a service
                 ().
      ```

2. On the switch where you want to run the standby OVSDB server, run `vtep-bootstrap` command with the same options as above but replace `db_ha active` with `db_ha standby`:

    ```
    cumulus@switch:~$ vtep-bootstrap  --db_ha standby  --db_ha_vip 169.254.0.11:9998  --db_ha_repl_sv 169.254.0.9:9999 --controller_ip 192.168.100.17 vtep7 172.16.20.157 192.168.100.157
    Executed:
            create certificate on a switch, to be used for authentication with controller
              ().
    Executed:
            sign certificate
              (vtep7-req.pem   Tue Sep 11 21:11:27 UTC 2018
                fingerprint a4cda030fe5e458c0d7ba44e22f52650f01bcd75).
    Executed:
            define physical switch
              ().
    Executed:
            define NSX controller IP address in OVSDB
              ().
    Executed:
            define local tunnel IP address on the switch
              ().
    Executed:
            define management IP address on the switch
              ().
    Executed:
            restart a service
              ().
    ```

3. From the switch running the active OVSDB server, copy the certificate files (`hostname-cert.pem` and `hostname-privkey.pem`) to the same location on the switch with the standby OVSDB server.

    {{%notice note%}}
The certificate and key pairs for authenticating with the NSX controller are generated automatically when you run the configuration script and are stored in the `/home/cumulus` directory. The same certificate must be used for both switches.
    {{%/notice%}}

4. On the switch running the *active* OVSDB server and then the switch running the *standby* OVSDB server, run the following commands in the order shown to complete the configuration process:

    ```
    cumulus@switch:~$ sudo systemctl restart openvswitch-vtep.service
    cumulus@switch:~$ sudo ifreload -a
    cumulus@switch:~$ sudo systemctl restart networking.service
    ```

    For information about the configuration script, read `man vtep-bootstrap` or run the command `vtep-bootstrap --help`.

## Configure the Transport and Logical Layers

After you finish configuring the NSX integration on both the MLAG primary and MLAG secondary switch, you need to configure the transport and logical layers from the NSX Manager. Refer to {{<link url="Integrating-Hardware-VTEPs-with-VMware-NSX-V">}}.

## Troubleshooting

After you configure OVSDB server high availability, you can check that configuration is successful.

To check the sync status on the *active* OVSDB server, run the following command:

```
cumulus@switch:~$ sudo ovs-appctl -t /var/run/openvswitch/ovsdb-server.`pidof ovsdb-server`.ctl ovsdb-server/sync-status
state: active
```

To check the sync status on the *standby* OVSDB server, run the following command:

```
cumulus@switch:~$ sudo ovs-appctl -t /var/run/openvswitch/ovsdb-server.`pidof ovsdb-server`.ctl ovsdb-server/sync-status
state: backup
replicating: tcp:169.254.0.9:9999
database: hardware_vtep
```

To check that the active OVSDB server is connected to the NSX controller, run the `ovsdb-client dump Manager` command:

```
cumulus@switch:~$ sudo ovsdb-client dump Manager
Manager table
_uuid                                inactivity_probe is_connected max_backoff other_config status                                 target
------------------------------------ ---------------- ------------ ----------- ------------ -------------------------------------- -------------------
e700ad21-8fd8-4f09-96dc-fa7cc6e498d8 30000            true         []          {}           {sec_since_connect="68 ", state=ACTIVE} "ssl:54.0.0.2:6632"
```

To make sure the MLAG configuration is correct, run the `clagctl` command:

```
cumulus@switch:~$ sudo clagctl
```

The following example command output shows that MLAG *is* configured correctly on the active OVSDB server:

```
cumulus@switch:~$ sudo clagctl
The peer is alive
  Our Priority, ID, and Role: 4096 00:02:00:00:00:46 primary
  Peer Priority, ID, and Role: 8192 00:02:00:00:00:4e secondary
  Peer Interface and IP: peerlink-3.4094 169.254.0.10
  VxLAN Anycast IP: 36.0.0.1
  Backup IP: 27.0.0.22 (active)
  System MAC: 44:38:39:ff:ff:01
CLAG Interfaces
Our Interface Peer Interface CLAG Id Conflicts Proto-Down Reason
---------------- ---------------- ------- -------------------- -----------------
  vxln14567102 vxln14567102 - - -
  vxln14567103 vxln14567103 - - -
```

The following example command output shows that MLAG is *not* configured correctly on the active OVSDB server or that the peer is down:

```
cumulus@switch:~$ sudo clagctl
The peer is not alive
  Our Priority, ID, and Role: 4096 00:02:00:00:00:46 primary
  Peer Interface and IP: peerlink-3.4094 169.254.0.10
  VxLAN Anycast IP: 36.0.0.1
  Backup IP: 27.0.0.22 (inactive)
  System MAC: 44:38:39:ff:ff:01
CLAG Interfaces
Our Interface Peer Interface CLAG Id Conflicts Proto-Down Reason
---------------- ---------------- ------- -------------------- -----------------
  vxln14567102 - - - -
  vxln14567103 - - - -
```

To make sure that the BFD sessions are up and running, run the `ptmctl -b` command:

```
cumulus@switch:~$ sudo ptmctl -b

--------------------------------------------------------
port   peer      state  local     type       diag  vrf
--------------------------------------------------------
vxln0  54.0.0.4  Up     36.0.0.1  singlehop  N/A   N/A
vxln0  54.0.0.3  Up     36.0.0.1  singlehop  N/A   N/A
```

{{%notice note%}}
When `switchd` and networking services are restarted, the BFD sessions might be interrupted. If you notice that the sessions are down, restart the `openvswitch-vtep`.service.
{{%/notice%}}

If you encounter interface or VXLAN bridge configuration issues after adding the hardware bindings, run the `ifreload -a` command to reload all network interfaces.

```
cumulus@switch:~$ sudo ifreload -a
```

If you still encounter issues with high availability after you restart `openvswitch-vtep.service`, run `ifreload -a`, and restart `networking.service`, reboot the switch running the *standby* OVSDB server.

```
cumulus@switch:~$ sudo reboot
```
