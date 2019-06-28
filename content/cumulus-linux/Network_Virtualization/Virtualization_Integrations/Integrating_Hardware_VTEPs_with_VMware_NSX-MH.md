---
title: Integrating Hardware VTEPs with VMware NSX-MH
author: Cumulus Networks
weight: 393
aliases:
 - /display/DOCS/Integrating+Hardware+VTEPs+with+VMware+NSX-MH
 - /pages/viewpage.action?pageId=8362796
pageID: 8362796
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
Switches running Cumulus Linux can integrate with VMware NSX
Multi-Hypervisor (MH) to act as hardware VTEP gateways. The VMware
NSX-MH controller provides consistent provisioning across virtual and
physical server infrastructures.

{{% imgOld 0 %}}

Cumulus Linux also supports integration with VMware NSX in high
availability mode. Refer to [OVSDB Server High
Availability](/cumulus-linux/Network_Virtualization/Virtualization_Integrations/OVSDB_Server_High_Availability).

## <span>Getting Started</span>

Before you integrate VXLANs with NSX-MH, make sure you have a layer 2
gateway; a Broadcom Tomahawk, Trident II+, Trident II, Maverick, or
Mellanox Spectrum switch running Cumulus Linux. Cumulus Linux includes
OVSDB server (`ovsdb-server`) and VTEPd (`ovs-vtepd`), which support
[VLAN-aware
bridges](/cumulus-linux/Layer_2/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode).

To integrate a VXLAN with NSX-MH, you need to:

  - Configure the NSX-MH integration on the switch.

  - Configure the transport and logical layers from the NSX Manager.

  - Verify the VXLAN configuration.

{{%notice note%}}

Cumulus Linux supports security protocol version TLSv1.2 for SSL
connections between the OVSDB server and the NSX controller.

The OVSDB server cannot select the loopback interface as the source IP
address, causing top of rack registration to the controller to fail. To
work around this issue, run the `net add bgp redistribute connected`
command followed by the `net commit` command.

{{%/notice%}}

## <span>Configure the Switch for NSX-MH Integration</span>

Before you start configuring the gateway service, logical switches, and
ports that comprise the VXLAN, you need to enable and start the
`openvswitch-vtep` service, and configure the NSX integration on the
switch, either using the script or performing the manual configuration.

### <span>Start the openvswitch-vtep Service</span>

To enable and start the `openvswitch-vtep` service, run the following
command:

    cumulus@switch:~$ sudo systemctl enable openvswitch-vtep.service
    cumulus@switch:~$ sudo systemctl start openvswitch-vtep.service

<span style="color: #36424a;"> </span>

{{%notice note%}}

In previous versions of Cumulus Linux, you had to edit the
`/etc/default/openvswitch-vtep` file and then start the
<span style="color: #000000;"> `openvswitch-vtep` service </span> . Now,
you just have to enable and start the ` openvswitch-vtep  `
<span style="color: #000000;"> service </span> .

{{%/notice%}}

### <span>Configure the NSX-MH Integration Using the Configuration Script</span>

A script is available so you can configure the NSX-MH integration on the
switch automatically.

In a terminal session connected to the switch, run the `vtep-bootstrap`
command with these options:

  - `controller_ip` is the IP address of the NSX controller
    (192.168.100.17 in the example command below).

  - The ID for the VTEP (`vtep7` in the example command below).

  - The datapath IP address of the VTEP (`172.16.20.157` in the example
    command below). This is the VXLAN anycast IP address.

  - The IP address of the management interface on the switch
    (`192.168.100.157` in the example command below). This interface is
    used for control traffic.

<!-- end list -->

    cumulus@switch:~$ vtep-bootstrap --controller_ip 192.168.100.17 vtep7 172.16.20.157 192.168.100.157
    Executed: 
        create certificate on a switch, to be used for authentication with controller
         ().
    Executed: 
        sign certificate
         (vtep-req.pem  Tue Sep 11 21:11:27 UTC 2018
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

Run the following commands in the order shown to complete the
configuration process:

    cumulus@switch:~$ sudo systemctl restart openvswitch-vtep.service
    cumulus@switch:~$ sudo ifreload -a
    cumulus@switch:~$ sudo systemctl restart networking.service

### <span>Configure the NSX-MH Integration Manually</span>

{{%notice note%}}

You can configure the NSX-V integration manually for standalone mode
only; manual configuration for OVSDB server high availability is not
supported.

{{%/notice%}}

If you do *not* want to use the configuration script to configure the
NSX-MH integration on the switch automatically, you can configure the
integration manually, which requires you to perform the following steps:

  - Generate a certificate and key pair for authentication by NSX.

  - Configure the switch as a VTEP gateway.

#### <span>Generate the Credentials Certificate</span>

In Cumulus Linux, generate a certificate that the NSX controller uses
for authentication.

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

2.  In the `/usr/share/openvswitch/scripts/ovs-ctl-vtep` file, make sure
    the lines containing **private-key**, **certificate**, and
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
    and VTEPd:
    
        cumulus@switch:~$ sudo systemctl restart openvswitch-vtep.service

3.  Define the NSX controller cluster IP address in OVSDB. This causes
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
    underlying layer 3 network:
    
        cumulus@switch:~$ sudo vtep-ctl set Physical_Switch vtep7 tunnel_ips=172.16.20.157

After you generate the certificate, keep the terminal session active;
you need to paste the certificate into NSX Manager when you configure
the VTEP gateway.

#### <span>Enable ovs-vtepd to Use the VLAN-aware Bridge</span>

By default, in stand-alone mode, the ovs-vtep daemon creates traditional
bridges for each VXLAN VTEP. To use the VLAN-aware bridge with the
VTEPs, edit the `/usr/share/openvswitch/scripts/ovs-ctl-vtep` file and
uncomment the `--enable-vlan-aware-mode` line:

    # Start ovs-vtepd
    set ovs-vtepd unix:“$DB_SOCK”
    set “$@” -vconsole:emer -vsyslog:err -vfile:info
    #set “$@” --enable-vlan-aware-mode

Then restart the OVSDB server and VTEPd:

    cumulus@switch:~$ sudo systemctl restart openvswitch-vtep.service

## <span>Provision VMware NSX-V</span>

### <span>Configure the Switch as a VTEP Gateway</span>

After you create a certificate, connect to NSX Manager in a browser to
configure a Cumulus Linux switch as a VTEP gateway. In this example, the
IP address of the NSX Manager is 192.168.100.12.

1.  In NSX Manager, add a new gateway. Click the **Network Components**
    tab, then the **Transport Layer** category. Under **Transport
    Node**, click **Add**, then select **Manually Enter All Fields**.
    The Create Gateway wizard opens.
    
    {{% imgOld 1 %}}

2.  In the Create Gateway dialog, select *Gateway* for the **Transport
    Node Type**, then click **Next**.

3.  In the **Display Name** field, provide a name for the gateway, then
    click **Next**.

4.  Enable the VTEP service. Select the **VTEP Enabled** checkbox, then
    click **Next**.

5.  From the terminal session connected to the switch where you
    generated the certificate, copy the certificate and paste it into
    the **Security Certificate** text field. Copy only the bottom
    portion, including the `BEGIN CERTIFICATE` and `END CERTIFICATE`
    lines. For example, copy all the highlighted text in the terminal:
    
    {{% imgOld 2 %}}
    
    Paste it into NSX Manager, then click **Next**:
    
    {{% imgOld 3 %}}

6.  In the Connectors dialog, click **Add Connector** to add a transport
    connector. This defines the tunnel endpoint that terminates the
    VXLAN tunnel and connects NSX to the physical gateway. You must
    choose a tunnel **Transport Type** of *VXLAN*. Choose an existing
    transport zone for the connector or click **Create** to create a new
    transport zone.

7.  Define the IP address of the connector (the underlay IP address on
    the switch for tunnel termination).

8.  Click **OK** to save the connector, then click **Save** to save the
    gateway.

After communication is established between the switch and the
controller, a `controller.cacert` file downloads onto the switch.

Verify that the controller and switch handshake is successful. In a
terminal connected to the switch, run this command:

    cumulus@switch:~$ sudo ovsdb-client dump -f list | grep -A 7 "Manager"
    Manager table
    _uuid               : 505f32af-9acb-4182-a315-022e405aa479
    inactivity_probe    : 30000
    is_connected        : true
    max_backoff         : []
    other_config        : {}
    status              : {sec_since_connect="18223", sec_since_disconnect="18225", state=ACTIVE}
    target              : "ssl:192.168.100.17:6632"

## <span id="src-8362796_IntegratingHardwareVTEPswithVMwareNSX-MH-config-transport-logical" class="confluence-anchor-link"></span><span>Configure the Transport and Logical Layers</span>

### <span>Configure the Transport Layer</span>

After you finish configuring the NSX-MH integration on the switch,
configure the transport layer. For each host-facing switch port to be
associated with a VXLAN instance, define a **Gateway Service** for the
port.

1.  In NSX Manager, add a new gateway service. Click the **Network
    Components** tab, then the **Services** category. Under **Gateway
    Service**, click **Add**. The Create Gateway Service wizard opens.

2.  In the Create Gateway Service dialog, select *VTEP L2 Gateway
    Service* as the **Gateway Service Type**.
    
    {{% imgOld 4 %}}

3.  Provide a **Display Name** for the service to represent the VTEP in
    NSX.

4.  Click **Add Gateway** to associate the service with the gateway you
    created earlier.

5.  In the **Transport Node** field, choose the name of the gateway you
    created earlier.

6.  In the **Port ID** field, choose the physical port on the gateway
    (for example, swp10) that will connect to a logical layer 2 segment
    and carry data traffic.

7.  Click **OK** to save this gateway in the service, then click
    **Save** to save the gateway service.

The gateway service shows up as type *VTEP L2* in NSX.

{{% imgOld 5 %}}

Next, configure the logical layer on NSX.

### <span>Configure the Logical Layer</span>

To complete the integration with NSX, you need to configure the logical
layer, which requires defining a logical switch (the VXLAN instance) and
all the logical ports needed.

<span style="color: #36424a;"> To define the logical switch: </span>

1.  In NSX Manager, add a new logical switch. Click the **Network
    Components** tab, then the **Logical Layer** category. Under
    **Logical Switch**, click **Add**. The Create Logical Switch wizard
    opens.

2.  In the **Display Name** field, enter a name for the logical switch,
    then click **Next**.
    
    {{% imgOld 6 %}}

3.  Under **Replication Mode**, select **Service Nodes**, then click
    **Next**.

4.  Specify the transport zone bindings for the logical switch. Click
    **Add Binding**. The Create Transport Zone Binding dialog opens.
    
    {{% imgOld 7 %}}

5.  In the **Transport Type** list, select *VXLAN*, then click **OK** to
    add the binding to the logical switch.
    
    {{% imgOld 8 %}}

6.  In the **VNI** field, assign the switch a VNI ID, then click **OK**.
    
    {{%notice note%}}
    
    Do not use 0 or 16777215 as the VNI ID; these are reserved values
    under Cumulus Linux.
    
    {{%/notice%}}

7.  Click **Save** to save the logical switch configuration.  
    
    {{% imgOld 9 %}}

### <span>Define Logical Switch Ports</span>

Logical switch ports can be virtual machine VIF interfaces from a
registered OVS or a VTEP gateway service instance on this switch, as
defined above in the Configuring the Transport Layer. You can define a
VLAN binding for each VTEP gateway service associated with the
particular logical switch.

To define the logical switch ports:

1.  In NSX Manager, add a new logical switch port. Click the **Network
    Components** tab, then the **Logical Layer** category. Under
    **Logical Switch Port**, click **Add**. The Create Logical Switch
    Port wizard opens.
    
    {{% imgOld 10 %}}

2.  In the **Logical Switch UUID** list, select the logical switch you
    created above, then click **Create**.
    
    {{% imgOld 11 %}}

3.  In the **Display Name** field, provide a name for the port that
    indicates it is the port that connects the gateway, then click
    **Next**.

4.  In the **Attachment Type** list, select *VTEP L2 Gateway*.

5.  In the **VTEP L2 Gateway Service UUID** list, choose the name of the
    gateway service you created earlier.

6.  In the **VLAN** list, you can choose a VLAN if you want to connect
    only traffic on a specific VLAN of the physical network. Leave it
    blank to handle all traffic.

7.  Click **Save** to save the logical switch port. Connectivity is
    established. Repeat this procedure for each logical switch port you
    want to define.
    
    {{% imgOld 12 %}}

## <span id="src-8362796_IntegratingHardwareVTEPswithVMwareNSX-MH-MH-verify-vxlan-config" class="confluence-anchor-link"></span><span>Verify the VXLAN Configuration</span>

After configuration is complete, verify the VXLAN configuration in a
terminal connected to the switch using these Cumulus Linux commands:

    cumulus@switch1:~$ sudo ip –d link show vxln100
    71: vxln100: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-vxln100 state UNKNOWN mode DEFAULT
        link/ether d2:ca:78:bb:7c:9b brd ff:ff:ff:ff:ff:ff
        vxlan id 100 local 172.16.20.157 port 32768 61000 nolearning ageing 1800 svcnode 172.16.21.125

or

    cumulus@switch1:~$ sudo bridge fdb show
    52:54:00:ae:2a:e0 dev vxln100 dst 172.16.21.150 self permanent
    d2:ca:78:bb:7c:9b dev vxln100 permanent
    90:e2:ba:3f:ce:34 dev swp2s1.100
    90:e2:ba:3f:ce:35 dev swp2s0.100
    44:38:39:00:48:0e dev swp2s1.100 permanent
    44:38:39:00:48:0d dev swp2s0.100 permanent

Use the `ovsdb-client dump` <span style="color: #333333;"> command to
troubleshoot issues on the switch. This command verifies that the
controller and switch handshake is successful (and works only for VXLANs
integrated with NSX): </span>

    cumulus@switch:~$ sudo ovsdb-client dump -f list | grep -A 7 "Manager"
    Manager table
    _uuid               : 505f32af-9acb-4182-a315-022e405aa479
    inactivity_probe    : 30000
    is_connected        : true
    max_backoff         : []
    other_config        : {}
    status              : {sec_since_connect="18223", sec_since_disconnect="18225", state=ACTIVE}
    target              : "ssl:192.168.100.17:6632"
