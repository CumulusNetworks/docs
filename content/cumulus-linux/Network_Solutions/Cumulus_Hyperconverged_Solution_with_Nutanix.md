---
title: Cumulus Hyperconverged Solution with Nutanix
author: Cumulus Networks
weight: 261
aliases:
 - /display/DOCS/Cumulus+Hyperconverged+Solution+with+Nutanix
 - /pages/viewpage.action?pageId=9012165
pageID: 9012165
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
The Cumulus Hyperconverged Solution (HCS) in Cumulus Linux supports
automated integration with the Nutanix Prism Management solution and the
Nutanix AHV hypervisor. Cumulus HCS automatically configures ports
attached to Nutanix nodes, provisions networking and manages VLANs with
Nutanix Prism and Nutanix AHV.

In addition, you can augment the deployment with:

  - [Cumulus on a
    Stick](https://cumulusnetworks.com/cumulus-on-a-stick/) for [zero
    touch
    provisioning](/cumulus-linux/Installation_Management/Zero_Touch_Provisioning_-_ZTP)
    Nutanix and Cumulus HCS without any user interaction or additional
    equipment.

  - [Cumulus NetQ](#src-9012165) for network telemetry and unprecedented
    real-time and historic visibility into dynamic changes in both the
    network and virtual machines.

  - Out-of-band management and IPMI access using [Cumulus
    RMP](https://docs.cumulusnetworks.com/display/RMP/Cumulus+RMP) or a
    generic Cumulus Linux switch, enabling the full provisioning of a
    zero-touch data and management network, eliminating any network
    deployment delays when standing up a Nutanix cluster.

Cumulus HCS has two major components:

  - **Nutanix LLDP Switch Agent**. When enabled, the agent listens for
    directly connected Nutanix servers via LLDP and enables MLAG bonding
    on the relevant ports.

  - **Nutanix Webhook VLAN Provisioner**. Cumulus Linux switches
    register with the Nutanix CVM and wait to receive Nutanix webhooks.
    When a new VM is deployed on a server in the cluster, the CVM sends
    a message to the Cumulus Linux switch with the physical server name
    and relevant VLANs. The switch then dynamically provisions the
    configuration on the ports of the specific physical server.  
      
    Cumulus HCS periodically polls Nutanix Prism for information about
    VMs in the cluster. When a new VM is discovered, the service
    automatically identifies the physical Nutanix server hosting the VM
    and discovers any VLANs required for the VM. The service then
    automatically adds these VLANs to the default [VLAN-aware
    bridge](/cumulus-linux/Layer_2/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode),
    the MLAG peer link and the automatically created bond to the Nutanix
    node. When a VM is powered off, removed or moved, and the associated
    VLAN has no other VMs, the VLAN is automatically removed from the
    bridge, peer link and dynamic bond.

## <span>Prerequisites</span>

  - 2 [Cumulus Networks-compatible
    switches](https://cumulusnetworks.com/hcl) running Cumulus Linux
    3.7.3 or later

  - Nutanix AOS 5.5.8 or later

  - Nutanix AHV 20170830.185 or later

  - LLDP enabled on Nutanix (which is the default in 5.5.8 and later)

  - IP connectivity between the Cumulus Linux switches and the Nutanix
    controller VMs (CVMs)

  - [MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG)
    enabled on the Cumulus Linux switches

Cumulus HCS runs on any platform. However, this chapter assumes a
typical Nutanix deployment with the following configuration:

  - Leaf switches with 48 x 10G or 25G ports

  - Four or more 40G or 100G uplinks

  - Nutanix servers are attached to any of the 10G or 25G ports

  - MLAG peer link is on the first two uplink ports: swp49 and swp50

  - Connections to other infrastructure are on ports swp51 and above

  - The eth0 management interface is configured for [management
    VRF](/cumulus-linux/Layer_3/Management_VRF) via DHCP

  - For automatic configuration, the gateway IP addresses for all VMs,
    including the CVM, do not exist on the Cumulus Linux switches.

The example configuration utilizes the following topology. All
configuration focuses on the leaf01 and leaf02 switches. Configurations
for spine01 and spine02 are not included.

{{% imgOld 0 %}}

## <span>Configure Cumulus HCS and Nutanix</span>

<span style="color: #000000;"> The method you choose for configuring
Cumulus HCS and Nutanix depends upon whether or not you already have
Cumulus Linux installed on your switches, which are named
<span style="color: #000000;"> *leaf01* and *leaf02* </span> in the
example configuration above. </span>

  - <span style="color: #000000;"> If you have bare-metal switches
    without Cumulus Linux installed, follow the steps below for
    configuring a bare-metal switch with ZTP. </span>

  - <span style="color: #000000;"> If Cumulus Linux is already installed
    on your switches, follow the steps below for manually configuring an
    existing Cumulus Linux switch. </span>

### <span>Configure the Service with ZTP</span>

<span style="color: #000000;"> The following steps describe how to
<span style="color: #000000;"> use zero touch provisioning </span> to
install Cumulus Linux and fully configure Cumulus HCS and Nutanix on
your network. </span>

<span style="color: #000000;"> To do this, you need a [Cumulus on a
Stick](https://cumulusnetworks.com/cumulus-on-a-stick/) disk image and a
USB stick with at least 1GB of storage. </span>

1.  <span style="color: #000000;"> Insert the USB stick into your
    computer and copy the Cumulus on a Stick files onto it. </span>

2.  <span style="color: #000000;"> <span style="color: #000000;"> On the
    USB stick, open the `ztp_config.txt` file in a text editor and set
    your Nutanix username and password and the server IP address, then
    save and close the file.  
    </span> </span>
    
        # Fill in the parameters below to allow for ZTP to 
        # automatically configure the switch for Nutanix
        #
        # The username for the Nutanix API. Likely the username you use to login to Prism. (Required)
        NUTANIX_USERNAME=admin
        # The password for the user. (Required)
        NUTANIX_PASSWORD=nutanix/4u
        # The IP address of a Nutanix CVM or the CVM anycast/cluster IP. (Required)
        NUTANIX_IP=10.1.1.123
        # IP address and subnet mask of this switch in the CVM subnet. Used to communicate to the Prism API.
        SWITCH_CVM_IP=10.1.1.254/24
        # If you do not want to use DHCP on the switch eth0, define the static switch IP and mask below. (Optional)
        #SWITCH_MANAGEMENT_IP=10.0.0.11/24
        # If you define a static IP, what is the gateway the switch should use for management traffic? (Optional)
        #SWITCH_DEFAULT_GATEWAY=10.1.1.1
        # If you have Layer 2 connections to existing infrastructure, define them here. Separate the interfaces with a comma. (Optional)
        UPLINKS=swp51,swp52
        # It is assumed that ports swp49 and swp50 will be used for the inter-switch link. If you have other ports, define them here. (Optional)
        #PEERLINK=swp49,swp50

3.  <span style="color: #000000;"> Place the USB stick into the Cumulus
    Linux switch (leaf01) and power on the switch. Cumulus Linux is
    automatically installed, including the license and a baseline
    configuration. The switch reboots multiple times during this
    process. Depending on your specific hardware platform, this process
    can take up to 20 minutes. After the installation completes, the
    LEDs corresponding to the ports connected to the Nutanix nodes
    illuminate in green. </span>

4.  <span style="color: #000000;"> When the installation completes,
    remove the USB stick and repeat this procedure on the other Cumulus
    Linux switch (leaf02). </span>

### <span>Configure the Service Manually</span>

If Cumulus Linux is already installed on your switches, follow the steps
below to configure Cumulus Linux, Nutanix and Cumulus HCS.

1.  Configure MLAG on both the leaf01 and leaf02 nodes. The `sys-mac` is
    a MAC address from the Cumulus Networks reserved MAC address space
    and must be the same on both MLAG peers. If you are deploying more
    than one pair of switches with MLAG, the `sys-mac` must be unique
    for each pair of MLAG-configured switches.
    
        cumulus@leaf01:~$ net add interface swp49,swp50 mtu 9216
        cumulus@leaf01:~$ net add clag peer sys-mac 44:38:39:FF:40:00 interface swp49,swp50 primary
        cumulus@leaf01:~$ net commit
    
        cumulus@leaf02:~$ net add interface swp49,swp50 mtu 9216
        cumulus@leaf02:~$ net add clag peer sys-mac 44:38:39:FF:40:00 interface swp49,swp50 secondary
        cumulus@leaf02:~$ net commit

2.  Configure the default layer 2 bridge. Add a unique IP address to
    each leaf in the same subnet as the CVM.
    
        cumulus@leaf01:~$ net add bridge bridge ports peerlink
        cumulus@leaf01:~$ net add bridge bridge pvid 1
        cumulus@leaf01:~$ net add vlan 1 ip address 10.1.1.201/24
        cumulus@leaf01:~$ net commit
    
        cumulus@leaf02:~$ net add bridge bridge ports peerlink
        cumulus@leaf02:~$ net add bridge bridge pvid 1
        cumulus@leaf02:~$ net add vlan 1 ip address 10.1.1.202/24
        cumulus@leaf02:~$ net commit
    
    {{%notice note%}}
    
    In both configurations the `pvid` value of *1* indicates the native
    VLAN ID. If you don't know the value for the native VLAN ID, use
    *1*.
    
    {{%/notice%}}

3.  Edit the `/etc/default/cumulus-hyperconverged` file and set the
    Nutanix username, password and server IP address. Do this on both
    switches (leaf01 and leaf02). Cumulus Linux uses the settings in
    this file to authenticate and communicate with the Nutanix cluster.
    
        cumulus@leaf02:~$ sudo nano /etc/default/cumulus-hyperconverged
         
        ### /etc/default/cumulus-hyperconverged config file
        # username for Prism (required)
        USERNAME=admin
        # password for Prism (required)
        PASSWORD=nutanixpassword
        # CVM address used by the service (required)
        SERVER=10.1.1.11
        # Hook server address (optional)
        #HOOK_SERVER=10.0.0.0
        # Hook port (optional)
        #HOOK_PORT=9440
        # Socket timeout (optional)
        #SOCKET_TIMEOUT=10.0.0.0
        # single/multi rack configuration (optional)
        VXLAN_CONFIG=False
        # loglevel: verbose/debug (optional)
        LOGLEVEL=verbose
        # periodic sync timeout (optional)
        #PERIODIC_SYNC_TIMEOUT=60
    
    {{%notice tip%}}
    
    These settings are defined
    [below](#src-9012165_CumulusHyperconvergedSolutionwithNutanix-chs_settings).
    
    {{%/notice%}}
    
    {{%notice note%}}
    
    The server IP address may be a specific Nutanix CVM address or the
    virtual cluster IP address.
    
    {{%/notice%}}

4.  Enable and start Cumulus HCS on leaf01 and leaf02.
    
        cumulus@leaf01:~$ sudo systemctl enable cumulus-hyperconverged
        cumulus@leaf01:~$ sudo systemctl start cumulus-hyperconverged
    
        cumulus@leaf02:~$ sudo systemctl enable cumulus-hyperconverged
        cumulus@leaf02:~$ sudo systemctl start cumulus-hyperconverged

5.  Verify that the service is running on leaf01 and leaf02.
    
        cumulus@leaf01:~$ sudo systemctl status cumulus-hyperconverged
        ● cumulus-hyperconverged.service - Cumulus Linux Hyperconverged Daemon
           Loaded: loaded (/lib/systemd/system/cumulus-hyperconverged.service; enabled)
           Active: active (running) since Mon 2019-01-07 03:36:26 UTC; 56min ago
         Main PID: 4206 (cumulus-hyperco)
           CGroup: /system.slice/cumulus-hyperconverged.service
                   ├─4206 /usr/bin/python /usr/bin/cumulus-hyperconverged
                   └─6300 /usr/sbin/lldpcli -f json watch
    
        cumulus@leaf02:~$ sudo systemctl status cumulus-hyperconverged
        ● cumulus-hyperconverged.service - Cumulus Linux Hyperconverged Daemon
           Loaded: loaded (/lib/systemd/system/cumulus-hyperconverged.service; enabled)
           Active: active (running) since Mon 2019-01-07 03:36:26 UTC; 56min ago
         Main PID: 4207 (cumulus-hyperco)
           CGroup: /system.slice/cumulus-hyperconverged.service
                   ├─4207 /usr/bin/python /usr/bin/cumulus-hyperconverged
                   └─4300 /usr/sbin/lldpcli -f json watch
    
    {{%notice tip%}}
    
    <span style="color: #000000;"> If the service fails to start, you
    may find more information in the service's log file. View the log
    with `sudo journalctl -u cumulus-hyperconverged`. </span>
    
    {{%/notice%}}

6.  Enable the server-facing ports to accept inbound LLDP frames and
    configure jumbo MTU on both leaf01 and leaf02.
    
        cumulus@leaf01:~$ net add interface swp1-48 mtu 9216
        cumulus@leaf01:~$ net commit
    
        cumulus@leaf02:~$ net add interface swp1-48 mtu 9216
        cumulus@leaf02:~$ net commit

At this point, the service is fully configured. It may take up to 60
seconds for LLDP frames to be received to trigger Cumulus HCS.

### <span>Cumulus HCS Configuration Settings</span>

<span style="color: #000000;"> Some of the settings you can configure
include: </span>

  - <span style="color: #000000;"> HOOK\_SERVER: the source IP the
    switch uses when communicating with the Nutanix API. By default, it
    follows the routing table. </span>

  - <span style="color: #000000;"> HOOK\_PORT: the port on which the
    Nutanix CVM is running. The default is *9440*. </span>

  - <span style="color: #000000;"> SOCKET\_TIMEOUT: the amount of time
    to wait for a timeout when attempting to communicate with the
    Nutanix API. The default is *10* seconds. </span>

  - <span style="color: #000000;"> VXLAN\_CONFIG: when set to *TRUE*,
    Cumulus HCS automatically provisions VXLAN VNIs as well as VLANs.
    </span>

  - <span style="color: #000000;"> LOGLEVEL: describes the logging
    level. *Verbose* and *Debug* are acceptable values. Verbose provides
    information about bond and VLAN creation while Debug helps in
    troubleshooting by providing more information </span>
    <span style="color: #000000;"> from sources like LLDP and the
    Nutanix webhook. </span>

  - <span style="color: #000000;"> PERIODIC\_SYNC\_TIMEOUT: how long
    before Cumulus HCS times out dynamic configurations without
    contacting the Nutanix API. The default is *60* seconds. </span>

## <span>Configure Uplinks</span>

<span style="color: #000000;"> How you configure uplinks depends upon
whether you configured Cumulus HCS with ZTP or manually. </span>

<span style="color: #000000;"> If you used ZTP, you can edit the ZTP
settings file to define the uplink ports and the VLANs assigned to those
uplinks. </span>

<span style="color: #000000;"> If you manually configured the service,
you need to enable the uplinks and define the associated VLANs, as shown
below. You need to configure both leaf01 and leaf02. </span>

    cumulus@leaf01:~$ net add interface swp51-52 mtu 9216
    cumulus@leaf01:~$ net add interface swp51-52 bridge vids 1-2999,4000-4094
    cumulus@leaf01:~$ net add interface swp51-52 bridge pvid 1
    cumulus@leaf01:~$ net commit

    cumulus@leaf02:~$ net add interface swp51-52 mtu 9216
    cumulus@leaf02:~$ net add interface swp51-52 bridge vids 1-2999,4000-4094
    cumulus@leaf02:~$ net add interface swp51-52 bridge pvid 1
    cumulus@leaf02:~$ net commit

{{%notice tip%}}

In this example, all VLANs are allowed on the uplink ports. Configuring
any set of VLANs is allowed. Be aware that [VLANs 3000-3999 are
reserved](VLAN-aware_Bridge_Mode.html#src-8362673_VLAN-awareBridgeMode-vlan_range)
on Cumulus Linux. This example assumes the untagged or native VLAN is
VLAN ID (`pvid`) *1*. Change the VLAN ID as needed.

{{%/notice%}}

## <span>Add Local Default Gateways</span>

<span style="color: #000000;"> You can add one or more local default
gateways on both switches to provide a redundant solution, as shown
below. It does not matter whether you configured Cumulus HCS with ZTP or
manually. ZTP does not add any gateway configuration. </span>

<span style="color: #000000;"> To provide redundant gateways for the
dual-attached Nutanix servers, Cumulus Linux relies on </span>
<span style="color: #000000;"> [Virtual Router
Redundancy](/cumulus-linux/Layer_2/Virtual_Router_Redundancy_-_VRR_and_VRRP)
(VRR). VRR enables hosts to communicate with any redundant router
without reconfiguration, running dynamic routing protocols, or running
router redundancy protocols. This means that redundant routers will
respond to [Address Resolution
Protocol](/cumulus-linux/Layer_3/Address_Resolution_Protocol_-_ARP)
(ARP) requests from hosts. Routers are configured to respond in an
identical manner, but if one fails, the other redundant routers will
continue to respond, leaving the hosts with the impression that nothing
has changed. </span>

    cumulus@leaf01:~$ net add vlan 1 ip address 10.1.1.11/24
    cumulus@leaf01:~$ net add vlan 1 ip address-virtual 00:00:5e:00:01:01 10.1.1.1/24
    cumulus@leaf01:~$ net commit

    cumulus@leaf02:~$ net add vlan 1 ip address 10.1.1.12/24
    cumulus@leaf02:~$ net add vlan 1 ip address-virtual 00:00:5e:00:01:01 10.1.1.1/24
    cumulus@leaf02:~$ net commit

<span style="color: #000000;"> The first configuration line defines the
IP address assigned to each switch, which is required and must be
unique. On leaf01, this IP address is *10.1.1.11/24*; on leaf02, it is
*10.1.1.12/24*. </span>

<span style="color: #000000;"> The second line defines the virtual IP
address that is used as the default gateway address for any hosts in
this VLAN. On both leaf01 and leaf02 this IP address is *10.1.1.1/24*.
The address-virtual MAC address is assigned from a reserved pool of
Cumulus Networks MAC addresses. The address must start with
00:00:05:00:01: and end with any hex value between 00 and ff. Both
leaf01 and leaf02 must have the same MAC address. Outside of this switch
pair, this MAC address must be unique and only be assigned to a single
switch pair in your network. </span>

## <span>Out-of-band Solutions</span>

<span style="color: #000000;"> You can configure out-of-band management
in one of two ways: </span>

  - <span style="color: #000000;"> Using [Cumulus
    RMP](https://docs.cumulusnetworks.com/display/RMP/Cumulus+RMP),
    which is the recommended way. </span>

  - <span style="color: #000000;"> Running Cumulus Linux on a
    [supported 1G non-Cumulus RMP
    switch](https://cumulusnetworks.com/products/hardware-compatibility-list/?Speed=1G).
    </span>

### <span>Cumulus RMP</span>

<span style="color: #000000;"> Cumulus RMP is a ready-to-deploy solution
that enables out-of-band management for web-scale networks. With Cumulus
RMP, you can directly manage and support Nutanix systems in the rack
without relying on the rest of the network. </span>

<span style="color: #000000;"> To deploy Nutanix with Cumulus RMP,
connect the Nutanix 1G IPMI, 1G Shared IPMI and 1G ports to the Cumulus
RMP switch. No additional configuration is required. </span>

<span style="color: #000000;"> Cumulus RMP does not support MLAG or
active/active connections across Cumulus RMP switches. Connections
across more than one Cumulus RMP switch rely on traditional [spanning
tree
protocol](/cumulus-linux/Layer_2/Spanning_Tree_and_Rapid_Spanning_Tree)
for redundancy. </span>

### <span>Other Cumulus Linux 1G Switches</span>

<span style="color: #000000;"> If you want to use a non-Cumulus RMP 1G
switch that supports Cumulus Linux for out-of-band management, you must
manually install the Cumulus Linux software and license and set up the
baseline configuration. The default [Cumulus on a Stick
image](https://cumulusnetworks.com/cumulus-on-a-stick/) has this
information. </span>

<span style="color: #000000;"> Once you install the software, you can
use the following command to configure all ports for a single, untagged
management VLAN, including any uplinks. </span>
<span style="color: #000000;"> </span>

    cumulus@oob-switch:~$ net add interface swp1-52 bridge access 1

You can assign a management IP address to this same untagged bridge
interface. Use an appropriate IP address for your infrastructure.

    cumulus@oob-switch:~$ net add vlan 1 ip address 192.0.2.1/24

Apply the configuration:

    cumulus@oob-switch:~$ net commit

{{%notice note%}}

In both configurations the value of *1* indicates the native or untagged
VLAN ID. If you want to use a different VLAN ID, just replace the *1* in
both commands with the desired VLAN ID.

{{%/notice%}}

## <span>Troubleshoot Cumulus HCS</span>

<span style="color: #000000;"> Some ways you can troubleshoot Cumulus
HCS include: </span>

  - <span style="color: #000000;"> Checking that bonds are being
    dynamically created. </span>

  - <span style="color: #000000;"> Ensuring LLDP messages are being
    received. </span>

  - <span style="color: #000000;"> Verifying the Cumulus HCS
    configuration. </span>

### <span>Verify Dynamic Bonds Are Being Created</span>

<span style="color: #000000;"> Use the `net show interface bonds`
command to verify that bonds are being dynamically created. The
following example shows that three bonds, *bond\_swp1*, *_bond\_swp2_*
and *__bond\_swp3__* are created automatically, which means that Cumulus
HCS is operating correctly. The name of every dynamically created bond
begins with *_bond\__* and ends with the interface name. </span>

    cumulus@leaf01:~$ net show interface bonds
        Name       Speed   MTU  Mode     Summary
    --  ---------  -----  ----  -------  ----------------------------------
    UP  bond_swp1  1G     1500  802.3ad  Bond Members: swp1(UP)
    UP  bond_swp2  1G     1500  802.3ad  Bond Members: swp2(UP)
    UP  bond_swp3  1G     1500  802.3ad  Bond Members: swp3(UP)
    UP  peerlink   2G     1500  802.3ad  Bond Members: swp49(UP), swp50(UP)

### <span>Verify LLDP Messages Are Being Received</span>

If bonds are not being created, then
[LLDP](/cumulus-linux/Layer_2/Link_Layer_Discovery_Protocol/) messages
may not be getting through. You can check for this possibility using the
`net show lldp` command:

    cumulus@leaf01:~$ net show lldp
    LocalPort  Speed  Mode           RemoteHost       RemotePort
    ---------  -----  -------------  ---------------  ----------
    swp1       1G     BondMember     NTNX-e08c61ec-A  ens3
    swp2       1G     BondMember     NTNX-d618a06d-A  ens3
    swp3       1G     BondMember     NTNX-4e6eac27-A  ens3
    swp49      1G     BondMember     leaf02           swp49
    swp50      1G     BondMember     leaf02           swp50
    swp52      1G     NotConfigured  spine01          swp1
    swp52      1G     NotConfigured  spine02          swp1

### <span>View Detailed Nutanix LLDP Information</span>

<span style="color: #000000;"> Cumulus HCS replies on the LLDP
`SysDescr` field to identify a Nutanix host. Run the </span> `net show
lldp <swp>` <span style="color: #000000;"> command to view the complete
LLDP details of the Nutanix node and verify the `SysDescr` field.
</span>

    cumulus@leaf01:~$ net show lldp swp1
    -------------------------------------------------------------------------------
    LLDP neighbors:
    -------------------------------------------------------------------------------
    Interface:    swp1, via: LLDP, RID: 37, Time: 0 day, 01:42:23
      Chassis:
        ChassisID:    mac 2c:c2:60:50:f6:8a
        SysName:      NTNX-e08c61ec-A
        SysDescr:     CentOS Linux 7 (Core) Linux 4.4.77-1.el7.nutanix.20180425.199.x86_64 #1 SMP Thu Apr 26 01:01:53 UTC 2018 x86_64
        MgmtIP:       10.1.1.10
        MgmtIP:       fe80::2ec2:60ff:fe50:f68a
        Capability:   Bridge, on
        Capability:   Router, off
        Capability:   Wlan, off
        Capability:   Station, off
      Port:
        PortID:       mac 2c:c2:60:50:f6:8a
        PortDescr:    ens3
        TTL:          120
        PMD autoneg:  supported: yes, enabled: yes
          Adv:          10Base-T, HD: yes, FD: yes
          Adv:          100Base-TX, HD: yes, FD: yes
          Adv:          1000Base-T, HD: no, FD: yes
          MAU oper type: 1000BaseTFD - Four-pair Category 5 UTP, full duplex mode
    -------------------------------------------------------------------------------

## <span>Caveats</span>

  - Reloading Cumulus HCS causes the bond interfaces to rebuild. For the
    stability of the Nutanix cluster, do not reload the service on both
    leaf switches simultaneously.

## <span>More Information</span>

  - [Hyperconverged infrastructure
    site](https://cumulusnetworks.com/networking-solutions/converged-infrastructure/)
    on the Cumulus Networks website

<span style="color: #000000;">  
</span>
