---
title: Integrating Hardware VTEPs with VMware NSX-V
author: NVIDIA
weight: 680
toc: 4
---
Switches running Cumulus Linux can integrate with VMware NSX-V to act as hardware VTEP gateways. The VMware NSX-V controller provides consistent provisioning across virtual and physical server infrastructures.

{{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv.png" >}}

Cumulus Linux also supports integration with VMware NSX in high availability mode. Refer to {{<link url="OVSDB-Server-High-Availability">}}.

## Get Started

Before you integrate VXLANs with NSX-V, make sure you have a layer 2 gateway. Cumulus Linux includes OVSDB server (`ovsdb-server`) and VTEPd (`ovs-vtepd`), which support {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridges">}}.

To integrate a VXLAN with NSX-V, you need to:

- Configure the NSX-V integration on the switch.
- Configure the transport and logical layers from the NSX Manager.
- Verify VXLAN configuration.

{{%notice note%}}
Cumulus Linux supports security protocol version TLSv1.2 for SSL connections between the OVSDB server and the NSX controller.

The OVSDB server cannot select the loopback interface as the source IP address, causing top of rack registration to the controller to fail. To work around this issue, run the NVUE `nv set vrf default router bgp address-family ipv4-unicast route-redistribute connected` command.
{{%/notice%}}
<!-- vale off -->
## Configure the Switch for NSX-V Integration
<!-- vale on -->
Before you start configuring the gateway service, and logical switches and ports that comprise the VXLAN, you need to enable and start the `openvswitch-vtep` service, and configure the NSX integration on the switch, either using the script or performing the manual configuration.
<!-- vale off -->
### Start the openvswitch-vtep Service
<!-- vale on -->
To enable and start the `openvswitch-vtep` service, run the following command:

```
cumulus@switch:~$ sudo systemctl enable openvswitch-vtep.service
cumulus@switch:~$ sudo systemctl start openvswitch-vtep.service
```
<!-- vale off -->
### Configure the NSX-V Integration with the Configuration Script
<!-- vale on -->
A script is available so you can configure the NSX-V integration on the switch automatically.

In a terminal session connected to the switch, run the `vtep-bootstrap` command with these options:

- `controller_ip` is the IP address of the NSX controller (192.168.100.17 in the example command below).
- The ID for the VTEP (`vtep7` in the example command below).
- The datapath IP address of the VTEP (`172.16.20.157` in the example command below). This is the VXLAN anycast IP address.
- The IP address of the management interface on the switch (`192.168.100.157` in the example command below). This interface is used for control traffic.

```
cumulus@switch:~$ vtep-bootstrap vtep7 --controller_ip 192.168.100.17 172.16.20.157 192.168.100.157
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

Run the following commands in the order shown to complete the configuration process:

```
cumulus@switch:~$ sudo systemctl restart openvswitch-vtep.service
cumulus@switch:~$ sudo ifreload -a
cumulus@switch:~$ sudo systemctl restart networking.service
```
<!-- vale off -->
### Configure the NSX-V Integration Manually
<!-- vale on -->
{{%notice note%}}
You can configure the NSX-V integration manually for standalone mode only; manual configuration for OVSDB server high availability is not supported.
{{%/notice%}}

If you do not want to use the configuration script to configure the NSX-V integration on the switch automatically, you can configure the integration manually, which requires you to perform the following steps:

- Generate a certificate and key pair for authentication by NSX-V.
- Configure a switch as a VTEP gateway.

#### Generate the Credentials Certificate

In Cumulus Linux, generate a certificate that the NSX controller uses for authentication.

1. In a terminal session connected to the switch, run the following commands:

    ```
    cumulus@switch:~$ sudo ovs-pki init
    Creating controllerca...
    Creating switchca...
    cumulus@switch:~$ sudo ovs-pki req+sign cumulus

    cumulus-req.pem Wed Oct 23 05:32:49 UTC 2013
            fingerprint b587c9fe36f09fb371750ab50c430485d33a174a

    cumulus@switch:~$ ls -l
    total 12
    -rw-r--r-- 1 root root 4028 Oct 23 05:32 cumulus-cert.pem
    -rw------- 1 root root 1679 Oct 23 05:32 cumulus-privkey.pem
    -rw-r--r-- 1 root root 3585 Oct 23 05:32 cumulus-req.pem
    ```

2. In the `/usr/share/openvswitch/scripts/ovs-ctl-vtep` file, make sure the lines containing **private-key**, **certificate**, and **bootstrap-ca-cert** point to the correct files; **bootstrap-ca-cert** is obtained dynamically the first time the switch talks to the controller:

    ```
    # Start ovsdb-server.
    set ovsdb-server "$DB_FILE"
    set "$@" -vANY:CONSOLE:EMER -vANY:SYSLOG:ERR -vANY:FILE:INFO
    set "$@" --remote=punix:"$DB_SOCK"
    set "$@" --remote=db:Global,managers
    set "$@" --remote=ptcp:6633:$LOCALIP
    set "$@" --private-key=/root/cumulus-privkey.pem
    set "$@" --certificate=/root/cumulus-cert.pem
    set "$@" --bootstrap-ca-cert=/root/controller.cacert
    set "$@ " --ssl-protocols=TLSv1,TLSv1.1,TLSv1.2
    ```

    If files have been moved or regenerated, restart the OVSDB server and VTEPd:

    ```
    cumulus@switch:~$ sudo systemctl restart openvswitch-vtep.service
    ```

3. Define the NSX Controller Cluster IP address in OVSDB. This causes the OVSDB server to start contacting the NSX controller:

    ```
    cumulus@switch:~$ sudo vtep-ctl set-manager ssl:192.168.100.17:6632
    ```

4. Define the local IP address on the VTEP for VXLAN tunnel termination. First, find the physical switch name as recorded in OVSDB:

    ```
    cumulus@switch:~$ sudo vtep-ctl list-ps
    vtep7
    ```

    Then set the tunnel source IP address of the VTEP. This is the datapath address of the VTEP, which is typically an address on a loopback interface on the switch that is reachable from the underlying layer 3 network:

    ```
    cumulus@switch:~$ sudo vtep-ctl set Physical_Switch vtep7 tunnel_ips=172.16.20.157
    ```

After you generate the certificate, keep the terminal session active; you need to paste the certificate into NSX Manager when you configure the VTEP gateway.
<!-- vale off -->
#### Enable ovs-vtepd to Use the VLAN-aware Bridge
<!-- vale on -->
By default, in stand-alone mode, the ovs-vtep daemon creates traditional bridges for each VXLAN VTEP. To use the VLAN-aware bridge with the VTEPs, edit the `/usr/share/openvswitch/scripts/ovs-ctl-vtep` file and uncomment the `--enable-vlan-aware-mode` line:

```
# Start ovs-vtepd
set ovs-vtepd unix:"$DB_SOCK "
set "$@ " -vconsole:emer -vsyslog:err -vfile:info
#set "$@ " --enable-vlan-aware-mode
```

Then restart the OVSDB server and VTEPd:

```
cumulus@switch:~$ sudo systemctl restart openvswitch-vtep.service
```
<!-- vale off -->
## Provision VMware NSX-V
<!-- vale on -->
### Configure the Switch as a VTEP Gateway

After you create a certificate, connect to NSX Manager in a browser to configure a Cumulus Linux switch as a hardware VTEP gateway. In this example, the IP address of the NSX Manager is 192.168.110.23.

1. In NSX Manager, add a new HW VTEP gateway. Click the **Network & Security** icon, **Service Definitions** category, then the **Hardware Devices** tab. Under **Hardware Devices**, click **+**. The Create Add Hardware Devices window opens.

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-hw-devs.png" >}}

2. In the **Name** field, provide a name for the HW VTEP gateway.
3. Enable the BFD service to the service nodes. Select the **Enable BFD** checkbox.
4. From the terminal session connected to the switch where you generated the certificate, copy the certificate and paste it into the **Certificate** text field. Copy only the bottom portion, including the `BEGIN CERTIFICATE` and `END CERTIFICATE` lines. For example, copy all the highlighted text in the terminal and paste it into NSX Manager:

    ```
    cumulus@switch:~$ cd /var/lib/openvswitch
    cumulus@switch:/var/lib/openvswitch$ ls
    conf.db  pki  vtep7-cert.pem  vtep7-privkey.pem  vtep7-req.pem
    cumulus@switch:/var/lib/openvswitch$ cat vtep7-cert.pem
    ```

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-add-hw-vtep.png" >}}

5. Click **OK** to save the gateway.  

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-mgr-svc.png" >}}

After communication is established between the switch and the controller, a `controller.cacert` file is downloaded onto the switch.

Verify that the controller and switch handshake is successful. In a terminal connected to the switch, run this command:

```
cumulus@switch:~$ sudo ovsdb-client dump -f list | grep -A 7 "Manager"
Manager table
_uuid               : 2693ea2e-306-4c23-ac03-934ala304077
inactivity_probe    : []
is_connected        : true
max_backoff         : []
other_config        : {}
status              : {sec_since_connect="557", state=ACTIVE}
target              : "ssl:192.168.110.110:6640"
```

## Configure the Transport and Logical Layers

### Configure the Transport Layer

After you finish configuring NSX-V integration on the switch, configure the transport zone and segment ID.

1. In NSX Manager, click the **Logical Network Preparation** tab in the **Installation** category, then click the **Segment ID** tab.

2. Click **Edit** and add the segment IDs (VNIDs) to be used. Here VNIs 5000-5999 are configured.

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-segment-id-tab.png" >}}

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-segment-id-edit.png" >}}

3. Click **OK** to save and provision the segment IDs.
4. Click the **Transport Zones** tab, choose the name of the transport zone.  

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-transport-zone.png" >}}

5. Select **Unicast** to choose the NSX-V Controller Cluster to handle the VXLAN control plane.  

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-transport-zone-new.png" >}}

6. Click **OK** to save the new transport zone.

### Configure the Logical Layer

To complete the integration with NSX-V, you need to configure the logical layer, which requires defining a logical switch (the VXLAN instance) and all the logical ports needed.

To define the logical switch:

1. In NSX Manager, select the **Logical Switches** category. Click **+** to add a logical switch instance.  

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-logical-switch-new.png" >}}

2. In the **Name** field, enter a name for the logical switch.
3. In the **Transport Zone** field, add the transport zone that you created earlier.
4. In the **Replication Mode** field, select **Unicast** for replication by the service node. Then check the **Enable IP Discovery** checkbox.
5. Click **OK**.  

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-logical-switch.png" >}}

To configure the Replication Cluster:

1. Select the **Service Definitions** category, then click the **Hardware Devices** tab. Next to the **Replication Cluster** field, click **Edit**.

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-replication-cluster.png" >}}

2. Hypervisors connected to the NSX controller for replication appear in the **Available Objects** list. Select the required service nodes, then click the green arrow to move them to the **Selected Objects** list.

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-replication-cluster-save.png" >}}

3. Click **OK** to save the replication node configuration.

### Define Logical Switch Ports

To define the logical switch ports (you can define a VLAN-to-VNI binding for each switch port associated with a particular logical switch):

1. In NSX Manager, add a new logical switch port. Click the **Logical Switches** category. Under **Actions**, click **Manage Hardware Bindings**. The Manage Hardware Binding wizard appears.

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-hw-bindings.png" >}}

2. Click **+** to add a logical port to the logical switch.  

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-hw-bindings-new.png" >}}

3. Select the logical switch that you created earlier (5000).

4. Select the switch port and the corresponding VLAN binding for logical switch 5000. This creates the logical switch port and also maps VLAN 16 of switch port swp2 to VNI 5000.

5. Click **OK** to save the logical switch port. Connectivity is established. Repeat this procedure for each logical switch port you want to define.  

    {{< img src = "/images/cumulus-linux/virtualization-integrations-nsxv-hw-bindings-save.png" >}}

## Verify the VXLAN Configuration

After configuration is complete, you can verify the VXLAN configuration using either or both of these Cumulus Linux commands in a terminal connected to the switch:

```
cumulus@switch:/var/lib/openvswitch$ ip -d link show vxln5000
65: vxln5000: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9152 qdisc noqueue master br-vxln5000 state UNKNOWN mode DEFAULT group default 
    link/ether da:d1:23:44:c4:5e brd ff:ff:ff:ff:ff:ff promiscuity 1 
    vxlan id 5000 local 172.16.20.157 srcport 0 0 dstport 4789 ageing 300 
    bridge_slave state forwarding priority 8 cost 100 hairpin off guard off root_block off fastleave off learning on flood on port_id 0x8006 port_no 0x6 designated_port 32774 designated_cost 0 designated_bridge 8000.16:28:56:cc:97:e5 designated_root 8000.16:28:56:cc:97:e5 hold_timer    0.00 message_age_timer    0.00 forward_delay_timer    0.00 topology_change_ack 0 config_pending 0 proxy_arp off proxy_arp_wifi off mcast_router 1 mcast_fast_leave off mcast_flood on neigh_suppress off addrgenmode eui64 
```

```
cumulus@switch:/var/lib/openvswitch$ bridge fdb show
b6:fb:be:89:99:65 dev vxln5000 master br-vxln5000 permanent
00:50:56:b5:3f:d2 dev vxln5000 master br-vxln5000 static
00:00:00:00:00:00 dev vxln5000 dst 172.16.1.11 self permanent
00:50:56:b5:3f:d2 dev vxln5000 dst 172.16.1.11 self static
36:cc:7a:bc:b9:e1 dev vxln0 master br-vxln0 permanent
00:23:20:00:00:01 dev dummy0 master br-vxln0 permanent
00:23:20:00:00:01 dev dummy 5000 master br-vxln5000 permanent
7c:fe:90:0b:c5:7e dev swp2.16 master br-vxln5000 permanent
```

To check that the active OVSDB server is connected to the NSX controller, run the `ovsdb-client dump Manager` command:

```
cumulus@switch:~$ sudo ovsdb-client dump Manager
Manager table
_uuid                                inactivity_probe is_connected max_backoff other_config status                                 target
------------------------------------ ---------------- ------------ ----------- ------------ -------------------------------------- -------------------
e700ad21-8fd8-4f09-96dc-fa7cc6e498d8 30000            true         []          {}           {sec_since_connect="68 ", state=ACTIVE} "ssl:54.0.0.2:6632"
```
