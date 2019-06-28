---
title: Integrating with VMware NSX-V
author: Cumulus Networks
weight: 141
aliases:
 - /display/CL34/Integrating+with+VMware+NSX-V
 - /pages/viewpage.action?pageId=7112574
pageID: 7112574
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
Switches running Cumulus Linux can integrate with VMware NSX-V to act as
VTEP gateways. The VMware NSX-V controller provides consistent
provisioning across virtual and physical server infrastructures.

{{% imgOld 0 %}}

## <span>Getting Started</span>

Before you integrate VXLANs with NSX-V, make sure you have the following
components:

  - A switch (L2 gateway) with a Broadcom Tomahawk, Trident II+ or
    Trident II chipset, or a Mellanox Spectrum chipset running Cumulus
    Linux

  - OVSDB server (ovsdb-server), included in Cumulus Linux

  - VTEPd (ovs-vtepd), included in Cumulus Linux

Integrating a VXLAN with NSX-V involves:

  - Bootstrapping the NSX-V integration

  - Configuring the transport zone and segment ID

  - Configuring the logical layer

  - Verifying the VXLAN configuration

### <span>Caveats and Errata</span>

  - As mentioned in [Network
    Virtualization](/version/cumulus-linux-343/Network_Virtualization/),
    the switches with the source and destination VTEPs cannot reside on
    the same subnet; there must be at least one layer 3 hop between the
    VXLAN source and destination.

  - There is no support for [VXLAN
    routing](/version/cumulus-linux-343/Network_Virtualization/VXLAN_Routing)
    in the Tomahawk, Trident II+ and Trident II chips; use a loopback
    interface or external router.

  - The `ovsdb-server` cannot select the loopback interface as the
    source IP address, causing TOR registration to the controller to
    fail. To work around this issue, run:
    
        cumulus@switch:~$ net add bgp redistribute connected
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit

  - Do not use 0 or 16777215 as the VNI ID, as they are reserved values
    under Cumulus Linux.

  - For more information about NSX-V, see the VMware NSX User Guide,
    version 4.0.0 or later.

## <span>Bootstrapping the NSX-V Integration</span>

Before you start configuring the gateway service and logical switches
and ports that comprise the VXLAN, you need to complete some steps to
bootstrap the process. You need to do the bootstrapping just once,
before you begin the integration.

### <span>Enabling the openvswitch-vtep Package</span>

Before you start bootstrapping the integration, you need to enable then
start the `openvswitch-vtep` package, as it is disabled by default in
Cumulus Linux.

    cumulus@switch$ sudo systemctl enable openvswitch-vtep.service
    cumulus@switch$ sudo systemctl start openvswitch-vtep.service

### <span>Using the Bootstrapping Script</span>

A script is available so you can do the bootstrapping automatically. For
information, read `man vtep-bootstrap`.

    cumulus@switch:~$ vtep-bootstrap -h
    usage: vtep-bootstrap [-h] [--controller_ip CONTROLLER_IP]
                          [--controller_port CONTROLLER_PORT] [--no_encryption]
                          [--credentials-path CREDENTIALS_PATH]
                          [--pki-path PKI_PATH]
                          switch_name tunnel_ip management_ip
     
     
    positional arguments:
      switch_name         Switch name
      tunnel_ip           local VTEP IP address for tunnel termination (data
                          plane)
      management_ip       local management interface IP address for OVSDB
                          conection (control plane)
     
     
    optional arguments:
      -h, --help            show this help message and exit
      --controller_ip CONTROLLER_IP
      --controller_port CONTROLLER_PORT
      --no_encryption       clear text OVSDB connection
      --credentials-path CREDENTIALS_PATH
      --pki-path PKI_PATH

The output of the script is displayed here:

    cumulus@switch:~$ vtep-bootstrap --credentials-path /var/lib/openvswitch vtep7 --controller_ip 192.168.110.110 172.16.20.157 192.168.110.25
    Executed: 
        create certificate on a switch, to be used for authentication with controller
         ().
    Executed: 
        sign certificate
         (vtep7-req.pem     Wed May  3 01:15:24 UTC 2017
            fingerprint bcc876b7bc8d1d596d1e78d3bde9337d2550f92e).
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

In the above example, the following information was passed to the
`vtep-bootstrap` script:

  - `--credentials-path /var/lib/openvswitch`: Is the path to where the
    certificate and key pairs for authenticating with the NSX controller
    are stored.

  - `vtep7`: is the ID for the VTEP, the switch name.

  - `192.168.110.110`: Is the IP address of the NSX controller.

  - `172.16.20.157`: Is the datapath IP address of the VTEP.

  - `192.168.110.25`: Is the IP address of the management interface on
    the switch.

These IP addresses will be used throughout the rest of the examples
below.

### <span>Manually Bootstrapping the NSX-V Integration</span>

If you don’t use the script, then you must:

  - Initialize the OVS database instance

  - Generate a certificate and key pair for authentication by NSX-V

  - Configure a switch as a VTEP gateway

These steps are described next.

### <span>Generating the Credentials Certificate</span>

First, in Cumulus Linux, you must generate a certificate that the NSX
controller uses for authentication.

1.  In a terminal session connected to the switch, run the following
    commands:
    
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

2.  In `/usr/share/openvswitch/scripts/ovs-ctl-vtep`, make sure the
    lines containing **private-key**, **certificate** and
    **bootstrap-ca-cert** point to the correct files;
    **bootstrap-ca-cert** is obtained dynamically the first time the
    switch talks to the controller:
    
        # Start ovsdb-server.
        set ovsdb-server "$DB_FILE"
        set "$@" -vANY:CONSOLE:EMER -vANY:SYSLOG:ERR -vANY:FILE:INFO
        set "$@" --remote=punix:"$DB_SOCK"
        set "$@" --remote=db:Global,managers
        set "$@" --remote=ptcp:6633:$LOCALIP
        set "$@" --private-key=/root/cumulus-privkey.pem
        set "$@" --certificate=/root/cumulus-cert.pem
        set "$@" --bootstrap-ca-cert=/root/controller.cacert
    
    If files have been moved or regenerated, restart the OVSDB server
    and `vtepd`:
    
        cumulus@switch:~$ sudo systemctl restart openvswitch-vtep.service

3.  Define the NSX Controller Cluster IP address in OVSDB. This causes
    the OVSDB server to start contacting the NSX controller:
    
        cumulus@switch:~$ sudo vtep-ctl set-manager ssl:192.168.100.17:6632

4.  Define the local IP address on the VTEP for VXLAN tunnel
    termination. First, find the physical switch name as recorded in
    OVSDB:
    
        cumulus@switch:~$ sudo vtep-ctl list-ps
        vtep7
    
    Then set the tunnel source IP address of the VTEP. This is the
    datapath address of the VTEP, which is typically an address on a
    loopback interface on the switch that is reachable from the
    underlying L3 network:
    
        cumulus@switch:~$ sudo vtep-ctl set Physical_Switch vtep7 tunnel_ips=172.16.20.157

Once you finish generating the certificate, keep the terminal session
active, as you need to paste the certificate into NSX Manager when you
configure the VTEP gateway.

### <span>Configuring the Switch as a VTEP Gateway</span>

After you create a certificate, connect to NSX Manager in a browser to
configure a Cumulus Linux switch as a hardware VTEP gateway. In this
example, the IP address of the NSX Manager is 192.168.110.23.

1.  In NSX Manager, add a new HW VTEP gateway. Click the **Network &
    Security** icon, **Service Definitions** category, then the
    **Hardware Devices** tab. Under **Hardware Devices**, click **+**.
    The Create Add Hardware Devices window appears.
    
    {{% imgOld 1 %}}

2.  In the **Name** field, give the HW VTEP gateway a name.

3.  Enable the BFD service to the service nodes. Select the **Enable
    BFD** check box.

4.  From the terminal session connected to the switch where you
    generated the certificate, copy the certificate and paste it into
    the **Certificate** text field. Copy only the bottom portion,
    including the `BEGIN CERTIFICATE` and `END CERTIFICATE` lines. For
    example, copy all the highlighted text in the terminal terminal and
    paste it into NSX Manager:
    
        cumulus@switch:~$ cd /var/lib/openvswitch
        cumulus@switch:/var/lib/openvswitch$ ls
        conf.db  pki  vtep7-cert.pem  vtep7-privkey.pem  vtep7-req.pem
        cumulus@switch:/var/lib/openvswitch$ cat vtep7-cert.pem
    
    {{% imgOld 2 %}}

5.  Click **OK** to save the gateway.  
    
    {{% imgOld 3 %}}

Once communication is established between the switch and the controller,
a `controller.cacert` file will be downloaded onto the switch.

Verify the controller and switch handshake is successful. In a terminal
connected to the switch, run this command:

    cumulus@switch:~$ sudo ovsdb-client dump -f list | grep -A 7 "Manager"
    Manager table
    _uuid               : 2693ea2e-306-4c23-ac03-934ala304077
    inactivity_probe    : []
    is_connected        : true
    max_backoff         : []
    other_config        : {}
    status              : {sec_since_connect="557", state=ACTIVE}
    target              : "ssl:192.168.110.110:6640"

## <span>Configuring the Transport Zone and Segment ID</span>

After you finish bootstrapping the NSX-V integration, you need to
configure the transport zone and segment ID.

1.  In the **Installation** category, click the **Logical Network
    Preparation** tab, then click the **Segment ID** tab.

2.  Click **Edit** and add the segment IDs (VNIDs) to be used. Here VNIs
    5000-5999 are configured.
    
    {{% imgOld 4 %}}
    
    {{% imgOld 5 %}}

3.  Click **OK** to save and provision the segment IDs.

4.  Click the **Transport Zones** tab, choose the name of the transport
    zone.  
    
    {{% imgOld 6 %}}

5.  Select **Unicast** to choose the NSX-V Controller Cluster to handle
    the VXLAN control plane.  
    
    {{% imgOld 7 %}}

6.  Click **OK** to save the new transport zone.

Next, you will configure the logical layer on NSX-V.

## <span>Configuring the Logical Layer</span>

To complete the integration with NSX-V, you need to configure the
logical layer, which requires defining a logical switch (the VXLAN
instance) and all the logical ports needed.

### <span>Defining Logical Switches</span>

To define the logical switch, do the following:

1.  In NSX Manager, select the **Logical Switches** category. Click
    **+** to add a logical switch instance.  
    
    {{% imgOld 8 %}}

2.  In the **Name** field, enter a name for the logical switch.

3.  In the **Transport Zone** field, add the transport zone that you
    created earlier.

4.  In the **Replication Mode** field, select **Unicast** for
    replication by the service node. Then check the **Enable IP
    Discovery** check box.

5.  Click **OK**.  
    
    {{% imgOld 9 %}}

### <span>Configuring the Replication Cluster</span>

1.  Select the **Service Definitions** category, then click the
    **Hardware Devices** tab. Next to the **Replication Cluster** field,
    click **Edit**.
    
    {{% imgOld 10 %}}

2.  Hypervisors connected to the NSX controller for replication appear
    in the **Available Objects** list. Select the required service
    nodes, then click the green arrow to move them to the **Selected
    Objects** list.
    
    {{% imgOld 11 %}}

3.  Click **OK** to save the replication node configuration.

### <span>Defining Logical Switch Ports</span>

As the final step, define the logical switch ports. A VLAN-to-VNI
binding can be defined for each switch port associated with a particular
logical switch.

To define the logical switch ports, do the following:

1.  In NSX Manager, add a new logical switch port. Click the **Logical
    Switches** category. Under **Actions**, click **Manage Hardware
    Bindings**. The Manage Hardware Binding wizard appears.
    
    {{% imgOld 12 %}}

2.  Click **+** to add a logical port to the logical switch.  
    
    {{% imgOld 13 %}}

3.  Select the logical switch that you created earlier (5000).

4.  Select the switch port and the corresponding VLAN binding for
    logical switch 5000. This creates the logical switch port and also
    maps VLAN 16 of switch port swp2 to VNI 5000.

5.  Click **OK** to save the logical switch port. Connectivity is
    established. Repeat this procedure for each logical switch port you
    want to define.  
    
    {{% imgOld 14 %}}

## <span>Verifying the VXLAN Configuration</span>

Once configured, you can verify the VXLAN configuration using either or
both of these Cumulus Linux commands in a terminal connected to the
switch:

    cumulus@switch:/var/lib/openvswitch$ ip -d link show vxln5000
    65: vxln5000: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9152 qdisc noqueue master br-vxln5000 state UNKNOWN mode DEFAULT group default 
        link/ether da:d1:23:44:c4:5e brd ff:ff:ff:ff:ff:ff promiscuity 1 
        vxlan id 5000 local 172.16.20.157 srcport 0 0 dstport 4789 ageing 300 
        bridge_slave state forwarding priority 8 cost 100 hairpin off guard off root_block off fastleave off learning on flood on port_id 0x8006 port_no 0x6 designated_port 32774 designated_cost 0 designated_bridge 8000.16:28:56:cc:97:e5 designated_root 8000.16:28:56:cc:97:e5 hold_timer    0.00 message_age_timer    0.00 forward_delay_timer    0.00 topology_change_ack 0 config_pending 0 proxy_arp off proxy_arp_wifi off mcast_router 1 mcast_fast_leave off mcast_flood on neigh_suppress off addrgenmode eui64 

    cumulus@switch:/var/lib/openvswitch$ bridge fdb show
    b6:fb:be:89:99:65 dev vxln5000 master br-vxln5000 permanent
    00:50:56:b5:3f:d2 dev vxln5000 master br-vxln5000 static
    00:00:00:00:00:00 dev vxln5000 dst 172.16.1.11 self permanent
    00:50:56:b5:3f:d2 dev vxln5000 dst 172.16.1.11 self static
    36:cc:7a:bc:b9:e1 dev vxln0 master br-vxln0 permanent
    00:23:20:00:00:01 dev dummy0 master br-vxln0 permanent
    00:23:20:00:00:01 dev dummy 5000 master br-vxln5000 permanent
    7c:fe:90:0b:c5:7e dev swp2.16 master br-vxln5000 permanent
