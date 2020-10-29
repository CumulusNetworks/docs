---
title: NVIDIA Cumulus Networking Soulution Guide for NSX-T Deplyoment with Apstra AOS
author: NVIDIA Networking
product: NVIDIA Networking Guides
---

## Executive Summary

BLA BLA BLA

## This Solution Guide is Based on the Following Reference Design

### Topology Diagram

{{<figure src="/images/guides/apstra-nsx/ref.topo.png" caption="Ref Solution">}}

### Physical Devices 

In reference topology we used the following hardware:
- 2 x Nvidia Spectrum SN2410 (48x25G+8x100G)
- 2 x Nvidia Spectrum SN2010 (18x25G+4x100G)
- 4 x Nvidia Spectrum SN2700 (32x100G)
- 4 x ESXi Hypervisors (2x25G NIC)
- 1 x Bare Metal Server (2x100G NIC)

### Software

In reference topology we used the following software versions:
- Cumulus Linux 3.7.12
- VMware vCenter 7.0
- VMware NSX-T 2.5
- Apstra AOS 3.3.0
- Ubuntu 18.4 (bare-metal server)

### Racks

The reference topology we used is built of three racks:
- **Rack 1** – Two SN2410 in MLAG + 2 ESXi Hypervisors connected in Active/Active (LACP) bonding (2x25G)
- **Rack 2** – Two SN2010 in MLAG + 2 ESXi Hypervisors connected in Active/Active (LACP) bonding (2x25G)
- **Rack 3** – Two SN2700 in MLAG + Bare-Metal server connected in Active/Active (LACP) bonding (2x100G)
  
All interconnect is done with 2xSN2700 spine switches.

### Physical Connectivity 

The connectivity based on initial LLDP information. After Apstra AOS configuration (or PRA), some of the LLDP information may differ.

{{< tabs "TABID01 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt-vrf:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost                RemotePort
---------  -----  -------  ------------------------  -----------------
eth0       1G     Mgmt     lab-hrm-flr0-10-60-0-109  25
swp25      25G    Default  sl01w02esx201.vwd.clx     1c:34:da:67:8c:6c
swp27      25G    Default  sl01w02esx202.vwd.clx     1c:34:da:67:8c:64
swp51      100G   Default  spine01                   swp1
swp52      100G   Default  spine01                   swp2
swp53      100G   Default  spine02                   swp1
swp54      100G   Default  spine02                   swp2
swp55      100G   Default  leaf02                    swp55
swp56      100G   Default  leaf02                    swp56
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt-vrf:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost                RemotePort
---------  -----  -------  ------------------------  -----------------
eth0       1G     Mgmt     lab-hrm-flr0-10-60-0-109  26
swp25      25G    Default  sl01w02esx201.vwd.clx     1c:34:da:67:8d:1c
swp27      25G    Default  sl01w02esx202.vwd.clx     1c:34:da:67:8d:10
swp51      100G   Default  spine01                   swp3
swp52      100G   Default  spine01                   swp4
swp53      100G   Default  spine02                   swp3
swp54      100G   Default  spine02                   swp4
swp55      100G   Default  leaf01                    swp55
swp56      100G   Default  leaf01                    swp56
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt-vrf:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost                RemotePort
---------  -----  -------  ------------------------  -----------------
eth0       100M   Mgmt     lab-hrm-flr0-10-60-0-109  21
swp1       25G    Default  sl01w01esx11.vwd.clx      98:03:9b:13:f2:58
swp3       25G    Default  sl01w01esx12.vwd.clx      98:03:9b:13:f3:d8
swp19      100G   Default  spine01                   swp31
swp20      100G   Default  spine02                   swp31
swp21      100G   Default  leaf04                    swp21
swp22      100G   Default  leaf04                    swp22
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt-vrf:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost                RemotePort
---------  -----  -------  ------------------------  -----------------
eth0       100M   Mgmt     lab-hrm-flr0-10-60-0-109  22
swp1       25G    Default  sl01w01esx11.vwd.clx      98:03:9b:13:f2:c0
swp3       25G    Default  sl01w01esx12.vwd.clx      98:03:9b:13:f2:64
swp19      100G   Default  spine01                   swp32
swp20      100G   Default  spine02                   swp32
swp21      100G   Default  leaf03                    swp21
swp22      100G   Default  leaf03                    swp22
```
{{< /tab >}}
{{< tab "leaf05 ">}}
```
cumulus@leaf05:mgmt-vrf:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost                RemotePort
---------  -----  -------  ------------------------  ----------
eth0       1G     Mgmt     lab-hrm-flr0-10-60-0-109  36
**swp1       100G   Default  bare_metal.vwd.clx        ens2p1**
swp27      100G   Default  spine01                   swp9
swp28      100G   Default  spine01                   swp10
swp29      100G   Default  spine02                   swp9
swp30      100G   Default  spine02                   swp10
swp31      100G   Default  leaf06                    swp31
swp32      100G   Default  leaf06                    swp32
```
{{< /tab >}}
{{< tab "leaf06 ">}}
```
cumulus@leaf06:mgmt-vrf:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost                RemotePort
---------  -----  -------  ------------------------  ----------
eth0       1G     Mgmt     lab-hrm-flr0-10-60-0-109  34
swp1       100G   Default  bare_metal.vwd.clx        ens2p2
swp27      100G   Default  spine01                   swp11
swp28      100G   Default  spine01                   swp12
swp29      100G   Default  spine02                   swp11
swp30      100G   Default  spine02                   swp12
swp31      100G   Default  leaf05                    swp31
swp32      100G   Default  leaf05                    swp32
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
cumulus@spine01:mgmt-vrf:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost                RemotePort
---------  -----  -------  ------------------------  ----------
eth0       1G     Mgmt     lab-hrm-flr0-10-60-0-109  24
swp1       100G   Default  leaf01                    swp51
swp2       100G   Default  leaf01                    swp52
swp3       100G   Default  leaf02                    swp51
swp4       100G   Default  leaf02                    swp52
swp9       100G   Default  leaf05                    swp27
swp10      100G   Default  leaf05                    swp28
swp11      100G   Default  leaf06                    swp27
swp12      100G   Default  leaf06                    swp28
swp31      100G   Default  leaf03                    swp19
swp32      100G   Default  leaf04                    swp19
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
cumulus@spine02:mgmt-vrf:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost                RemotePort
---------  -----  -------  ------------------------  ----------
eth0       1G     Mgmt     lab-hrm-flr0-10-60-0-109  23
swp1       100G   Default  leaf01                    swp53
swp2       100G   Default  leaf01                    swp54
swp3       100G   Default  leaf02                    swp53
swp4       100G   Default  leaf02                    swp54
swp9       100G   Default  leaf05                    swp29
swp10      100G   Default  leaf05                    swp30
swp11      100G   Default  leaf06                    swp29
swp12      100G   Default  leaf06                    swp30
swp31      100G   Default  leaf03                    swp20
swp32      100G   Default  leaf04                    swp20
```
{{< /tab >}}
{{< /tabs >}}

# Netowrk Configuration Automation using Apstra AOS

## Topology Preperations

### Step 1 - Create Logical Devices

Networks can be designed in AOS before considering hardware vendors by using logical devices (abstractions of physical devices) to specify common device form factors such as number, speeds, and roles of each port in one or more rack units (panels).<br />In our case, we are using custom logical devices that were designed to perfectly match our custom reference topology, but you can find a lot of predefined logical devices that can suit your needs.

Go to **Logical Devices** tab in the **Design** category
{{<figure src="/images/guides/apstra-nsx/1-Logical_devices.JPG">}}
Press on the **Create Logical Device** button
{{<figure src="/images/guides/apstra-nsx/1.1-create_logical_devic.JPG">}}
In the opened window, fill the following parameters:
- Logical Device name
- Create device's panel ports count
- Define ports speeds and destiny (which devices types they can be connected to) 

Below is an example of Logical Device matching to Nvidia Mellanox MSN2010 switch with 18x25Gbps + 4x100Gbps ports.<br /> 
The first panel consists of 18 ports SFP25 (25Gbps) and destined to connect to the L2/L3 server or an external router (won’t be used in this reference topology).
{{<figure src="/images/guides/apstra-nsx/1.2-create logical device panel1.JPG">}}
The second panel consists of 4 QSFP28 ports (100Gbps) and destined to connect to the Peer switch for MLAG, spine switches, and external router (again, it’s optional).
{{<figure src="/images/guides/apstra-nsx/1.2-create logical device panel2.JPG">}}
After all panel ports set, review them, and press **Create** to create the Logical device.
{{<figure src="/images/guides/apstra-nsx/1.3-create logical device.JPG">}}
Repeat those actions to create the needed Logical Devices for the reference topology.<br />Once done, you can check out your custom devices by searching for them in the Logical Devices list (or for any other predefined logical device)
{{<figure src="/images/guides/apstra-nsx/1.5-create the models as you need.JPG">}}

{{%notice note%}}In our reference topology, for each of our servers, we created custom Logical Devices: 
- ESXi with 2x25Gbps ports 
- Bare-metal server with 2x100Gbps ports 
{{<figure src="/images/guides/apstra-nsx/1.6-custom servers logical devices for this solution.JPG">}}{{%/notice%}}

### Step 2 - Create Interfaces Maps

Interface maps consist of interfaces used for achieving the intended network configuration rendering. They map interfaces between logical devices and physical hardware devices (represented with device profiles) while adhering to vendor specifications. Nvidia Mellanox switches profiles for MSN2010, MSN2100, MSN2410, and MSN2700 are predefined in AOS, so no need to create them. 
If your environment consists of newer NVIDIA switche models (e.g., SN3xxx or SN4xxx series ), create them in **Devices/Device Profiles** by following AOS UM.

Go to **Interfaces Maps** tab in the **Design** category
{{<figure src="/images/guides/apstra-nsx/2-interface map.JPG">}}
Press on **Create Interfaces Map** button
{{<figure src="/images/guides/apstra-nsx/2.1-create interface map.JPG">}}
In the opened window, fill Interface Map’s **Name** and select the needed **Logical Device** and **Profile**. We created custom Logical Devices in the previous step, the profiles for them are predefined in Apstra AOS. As mentioned, custom Device Profiles can be created in **Devices/Device Profiles**.<br />
Press on **Select Interfaces** near each of the port types and select the amounts. Once done, press **Create** to create and map the interfaces to the logical devices
{{<figure src="/images/guides/apstra-nsx/2.2-fill interface map info and select ports.JPG">}}
Here are all our created reference topology interfaces maps
{{<figure src="/images/guides/apstra-nsx/2.3-after all needed interafces maps created.JPG">}}

### Step 3 - Create Rack Types

Rack Types are standard build patterns that define the type and number of leaf switch network devices and servers for a rack build. There are predefined rack types in AOS, and you can also create, clone, edit, and delete them.<br />
For our reference topology, we will create a new Rack Types to match each of our custom racks designs.

Go to the **Rack Types** tab in the **Design** category
{{<figure src="/images/guides/apstra-nsx/3-rack type.jpg">}}
Press on the **Create Rack Type** button
{{<figure src="/images/guides/apstra-nsx/3.1-create rack type.JPG">}}
In the opened window, fill Rack Type’s name and connectivity type (L2/L3).
{{%notice note%}} In our reference topology, we are using L2 MLAG connections on the TOR switches, so we selected L2 connectivity type.{{%/notice %}}
{{<figure src="/images/guides/apstra-nsx/3.2-rack creation1.JPG">}}

In the **Leaf** tab, fill the following parameters: 
- Name
- Logical Device
- Number of Uplink ports and their speeds
- Redundancy Protocol (MLAG) and its parameters: 
    - Peer-Link (ISL) ports and speed
    - ISL Port-Channel number
{{<figure src="/images/guides/apstra-nsx/3.2-rack creation2.JPG">}}

Go to the **Server** tab to connect the server to the leaf switches and fill the following parameters:
- Name
- Amount
- Port-Channel ID (in our case it will be MLAG Port-Channel)
- Logical device (we created custom logical devices for our ESXi and bare-metal server earlier)
{{<figure src="/images/guides/apstra-nsx/3.2-rack creation3-server.JPG">}}

Add links to the server by pressing **Add link** button. 
In the opened section, set the following parameters:
- Link’s name 
- Switch (in our case, we have only one leaf pair) 
- Dual-Homed attachment type
- Active LACP LAG mode
- Physical link count per switch
- Links speed (this automatically taken from the logical device of the server)
{{<figure src="/images/guides/apstra-nsx/3.2-rack creation3-server-links.JPG">}}

Following the same steps, add the second ESXi hypervisor link (with MLAG Port 2) to the rack

Once done, preview the created Rack Type and press **Create** to create it
{{<figure src="/images/guides/apstra-nsx/3.2-rack creation-topology preview and create.JPG">}}
We repeated the same steps to create 3 custom Rack Types for our reference topology.
{{%notice note%}} For the bare-metal server, we used the appropriate logical device we created earlier. {{%/notice %}}
{{<figure src="/images/guides/apstra-nsx/3.3-created 3 types for our topo, on BM, use BM server logical device.JPG">}}

### Step 4 - Create Templates

Tere are two Template types in Apstra AOS:
- **Rack-based** templates - Used to build 3-stage Clos networks by defining the rack connectivity from the server to the Top-of-Rack and Spine switches. Each can be different in terms of its connection type L2/L3. 
- **POD-based** templates - Used to build 5-stage Clos networks, essentially combining multiple rack-based templates into one by connecting them with a Super-Spine switches layer.

In our reference topology, we are using a single POD of 3 different racks. So we created three different Rack-based templates. 

Go to the **Templates** tab in the **Design** category 
{{<figure src="/images/guides/apstra-nsx/5-templates.JPG">}}
Press on the **Create Template** button
{{<figure src="/images/guides/apstra-nsx/5.1-create template.JPG">}}
In the opened window, fill the Template details:
- Name
- Type (as mentioned before, we are using Rack-based templates in our reference topology) 
- Policies:
    - Unique BGP ASN allocation
    - Default Routing Policy
    - MP-BGP EVPN overlay 
    - IPv4 P2P Leaf-Spine links
{{<figure src="/images/guides/apstra-nsx/5.2-create template1.JPG">}}
{{%notice note%}}Overlay encapsulation in NSX-T deployments is done by it and uses Geneve protocol. In our case, there is a bare-metal rack as well, so VXLAN encapsulation will be used to connect the virtualized and the physical environments.<br />More details about the different types of NSX-T deployments will be covered later on in this guide.{{%/notice %}}
Select previously created rack types, and the Spine Logical Device (are using 2 Spines in our reference topology)
{{<figure src="/images/guides/apstra-nsx/5.3-create template structure.JPG">}}
Preview the topology of the Template and press **Create**
{{<figure src="/images/guides/apstra-nsx/5.4-create template preview_new.png">}}
You can search for the our newly created template by by querying it from the templates list
{{<figure src="/images/guides/apstra-nsx/5.5-search for template.JPG">}}

### Step 5 - Create Device Agents

Devices connected to AOS are managed with Device Agents using Push and Pull methods. AOS provides an integrated Agent installer that automates installation and verification of AOS Agents on network devices.

There are two agent types:
- **Onbox** - Installed on the device itself 
- **Offbox** - Is running on the AOS server-side and communicates with the device through its API 
{{%notice note%}}AOS doesn't support Offbox agent for Cumulus Linux, so for our reference topology we will install Onbox agent on our switches.{{%/notice %}}

Go to **Agents** tab in the **Devices** category
{{<figure src="/images/guides/apstra-nsx/4_5.0-agants.JPG">}}
Press on **Create Onbox Agetn(s)** button
{{<figure src="/images/guides/apstra-nsx/4_5.0-agants create.JPG">}}
Fill the following parameters:
- IP addresses of the switches (range can be used) 
- Devices' credentials 
- Leave the rest of the parameters with their default valuse 
Once done, press **Create**
{{<figure src="/images/guides/apstra-nsx/4_5-create agent.JPG">}}
Wait until agents finish installing on the switches
{{<figure src="/images/guides/apstra-nsx/4_5-create agent progress.JPG">}}
Once all agents are installed successfully, **Job State** should show **SUCCESS** on all switches.<br />At this point, the device information will appear (system ID and hostname)
{{<figure src="/images/guides/apstra-nsx/4_5-agent installed.JPG">}}
After the agents are installed on the switches, we need to acknowledge the devices in AOS. <br />
Go to the **Managed Devices** tab under **Devices** category
{{<figure src="/images/guides/apstra-nsx/4_6-managed devices.JPG">}}
Select all devices and press on the **V** icon to acknowledge the devices
{{<figure src="/images/guides/apstra-nsx/4_6-ack devices.JPG">}}
{{%notice note%}}If not all device profiles automatically set, check the needed device, press on the **Pencil** icon, and set **Profile** and **Admin State** to **NORMAL**.<br />
Now, the device will be acknowledged automatically.{{<figure src="/images/guides/apstra-nsx/4_6-ack devices full.png">}}{{%/notice %}}

## Network Intent Preperations

### Step 1 - Create Blueprint

After we assembled all the raw materials from the abstractions, reference design, and inventory elements (logical devices, interfaces maps, rack types, profiles, and templates), the next step is to create a Blueprint for our network.<br /> 
Blueprint pulls everything into your best-practice, validated solution. The blueprint will push the configuration into the infrastructure and monitor for state changes and anything else that can affect our intent compliance.

Go to the **Blueprints** category
{{<figure src="/images/guides/apstra-nsx/6-blueprints.JPG">}}
Press on **Create Blueprint** button
{{<figure src="/images/guides/apstra-nsx/6.1-create blueprint.JPG">}}
In the opened window, set the Blueprint’s **Name** and select the topology **Template**.<br /> 
Once selected, the intent preview will be available
{{<figure src="/images/guides/apstra-nsx/6.2-create blueprint1.JPG">}}
Preview Blueprint’s toplogy and parameters, press **Create** to create it
{{<figure src="/images/guides/apstra-nsx/5.4-create template preview_new.png">}}
{{<figure src="/images/guides/apstra-nsx/6.2-create blueprint3.JPG">}}
Wait till the Blueprint finishes creating, and it will be available in the Blueprints Dashboard
{{<figure src="/images/guides/apstra-nsx/6.3-blueprint dashboard.JPG">}}

### Step 2 - Configure the Blueprint

To configure the network intent, we need to configure the Blueprints parameters. Click on the blueprint’s name to enter it.

The first page is the Blueprint’s Dashboard, which is currently empty as we have no intent configured yet.<br />
Once all Staged configuration is set and committed into the environment, this dashboard will show the network intent, it’s status and changes in real-time.
{{<figure src="/images/guides/apstra-nsx/7-blueprint status.JPG">}}

To start configuring the network intent, go to the **Staged** tab. In this tab, we have to configure our network’s **Physical** and **Virtual** parameters.
{{<figure src="/images/guides/apstra-nsx/7.1-staged.JPG">}}

#### Physical Intent Configuration

Go to **Physical** configuration and start with assigninig **Resource Pools** for the following parameters:
- Spines’ BGP ASN allocation
- Leafs’ BGP ASN allocation 
- Spines’ Loopback IP addresses  
- Leafs’ Loopback IP addresses
- Leaf-Spine P2P LInks IP addresses

To set the above parameters, press on the **Red status indicator** near each of them (one-by-one), and edit them by pressing the **Pencil** icon
{{<figure src="/images/guides/apstra-nsx/7.2-config1.JPG">}}
Select the desired resource pools, and press on the **Save** button 
{{<figure src="/images/guides/apstra-nsx/7.2-config2.JPG">}}
{{%notice note%}}It is possible to create custom **Resource Pools** for any of the above parameters (Leaf/Spine BGP ASN, Leaf/Spine Loopbacks, P2P IPs, and VNIs).<br />
To create them, go to **Resources** category and select the needed tab. 
{{<figure src="/images/guides/apstra-nsx/4-resource pools (optional).JPG">}}
In this guide, we are using AOS predefined pools so that custom resource pools creation steps won’t be covered. For more information, check out the AOS UM.{{%/notice %}}
After all the resources selected, all status indicators should appear **Green**
{{<figure src="/images/guides/apstra-nsx/7.2-config3.JPG">}}
Set the devices’ **Interfaces Maps** by clicking on the **Device Profiles** icon (2nd one).<br />
Click on each of the Devices’ **Red status indicator**, and press on the **Pencil** icon to select **Device Profile**
{{<figure src="/images/guides/apstra-nsx/7.2-config4.JPG">}}
Select the appropriate **Interface Map** for each switch (can be done for all by select all checkbox).<br />
The **Device Profile** will be automatically set since it was assigned to the **Interfaces Map** earlier in the configuration. Once all set, press **Update Assignment**
{{<figure src="/images/guides/apstra-nsx/7.2-profiles assignemt.png">}}
After all interfaces maps are set, all switches satatus indicators should be **Green**
{{<figure src="/images/guides/apstra-nsx/7.2-config5.JPG">}}
{{%notice note%}}As we are not managing server configuration, we can leave their interface maps unselected. It's optional.{{%/notice %}}
Assign **System IDs** to the switches. Go to the **Devices** tab by pressing on the middle icon, click on the **Yellow status indicator**, and press on the **Pencil** icon to edit
{{<figure src="/images/guides/apstra-nsx/8-system ids.JPG">}}
In the opened window, assign **System ID** for each of the devices. They should be avalible for each one based on the information from the Agents we installed on them earlier. The **Deployment Mode** will be automatically set to **Deploy**. Once all selected, press on the **Update Assignments**
{{<figure src="/images/guides/apstra-nsx/8.1-set system ids.JPG">}}
All **System IDs** should be set for all the switches<be />
(Server system IDs are not available as no agents were installed on them. Again, this is optional)
{{<figure src="/images/guides/apstra-nsx/8.2-system ids complete.png">}}
{{%notice info%}}Before moving on to the **Virtual** environment configuration, we need to ensure that our **Physical Connectivity** (physical cabling) is aligned with our intent. When a blueprint is created, the interface connectivity will be automatically assumed and done by it.<br />
But, not always the cabling is being done after the intent configured in AOS. If this is the case and the cabling already exists, it's possible to update the blueprint default cabling assumption in a few ways.<br />
Go to **Links** under the **Physical** configuration in **Staged** tab
{{<figure src="/images/guides/apstra-nsx/9-lldp.JPG">}}
In this output, all the environment links will be displayed according to the AOS assumption.<br />
To change the cabling to your own, use the buttons above the table
{{<figure src="/images/guides/apstra-nsx/9.1-lldp buttons.png">}}
Using these buttons allows us to upload a custom cabling schema, export or edit the AOS assumed cabling, change links speeds, or refresh the cabling according to the LLDP from the managed switches.<br /> 
In our case, we are using different cabling schema (as presented in the reference topology diagram). So we will update AOS default schema using LLDP information from our switches.<br />
Press on the **Refresh** icon to gather LLDP information from the switches, and once done, press **Update Cabling Map from LLDP**
{{<figure src="/images/guides/apstra-nsx/9-lldp1.JPG">}}
Review the gathered LLDP information in the opened window, update if needed, and press **Update**
{{<figure src="/images/guides/apstra-nsx/9.2-lldp update.png">}}
Now, the LLDP information (environment cabling) is matching the **Staged** AOS configuration
{{<figure src="/images/guides/apstra-nsx/9-lldp match.png">}}
{{%notice note%}}You can clear the LLDP data, and return on these steps if there was a cabling change afterward.{{%/notice %}}
{{%/notice %}}

With that, our reference topology physical intent is done (almost...).

#### Virtual Intent Configuration

Prior to moving on to the fabric virtual configuration, which will include **Virtual Networks** (VLANs and L2VNIs) and **Security Zones** (VRFs and L3VNIs). Let's jump a bit forward and complete our MLAG peer-links configuration.<br />
Go to the **Virtual** configuration in **Staged** tab
{{<figure src="/images/guides/apstra-nsx/10-virtual_tab.png">}}
Click on the **Red status indicator** of **SVI Subnets-MLAG domain**, press ont the **Pencil** icon, select the desired IP addresses pool, and press **Save** button.<br />
We chose the same resource pool as for the Leaf-Spine P2P links
{{<figure src="/images/guides/apstra-nsx/11-mlag_svi.png">}}
Once saved, the indicator should become **Green**
{{<figure src="/images/guides/apstra-nsx/11-mlag_svi_indicator.png">}}

Now, when our **Physical** intent is complete with the MLAG configuration as well, we can move on to the **Virtual** intent configuration.<br />
ESX Hypervisors use a few traffic types traversing over our L3 network - Storage, vMotion, Mgmt., and Tunnel(TEP). Our reference topology, as VMware's best practice, will consider each rack as a different cluster. Thus, each rack will have different subnet for each underlying VLAN, but, with the same VLAN ID to simplify things. It doesn't mean that we will use all those VLANs for our checks, but in a full deployment, they must persist.<br />
The other requiemrnt is to have IP reachability between all ESX hypervisors underlying networks (VLAN subnets). For that, all these VLANs' subnets will be advertised via BGP from the ToR switches. The Virtual Machines (VMs) routing will be done by the NSX-T T1 Distributed Router (T1 DR) inisde the ESX and T0 router (on EDGE node) to advertise them into the physical enviorment.
{{%notice note%}}NSX-T 3.0 provides another option to have virtualized to physycal enviormtns connectivity by using NSX-T Agent on BM servers.<br /> 
Our reference guide won't cover NSX-T Agent use-cases and concentrate on an environment where users do not desire the agent, or it can't be installed on the BM server (e.g., old BM server). In our case, we will use NSX-T T0 Router for VXLAN overlay tunnels to stretch the L2 networks between the virtualized and the physical environments. The L2 networks on the virtual environment are stretched using Geneve encapsulated tunnels (over TEP VLAN) on the ESX hypervisors and sent as regular IP traffic over the L3 fabric.{{%/notice %}}

First let's understand the Packet Flows in our reference enviorment to be ready for our **Virtual** intent configuration.
{{%notice info%}}
### Packet Flow using NSX-T 2.5 
{{<figure src="/images/guides/apstra-nsx/nsx2.5.JPG">}}
**VM-VM Traffic**<br /> 
Traffic inside the virtualized environment encapsulated into Geneve tunnels. The encapsulation/decapsulation is handled by the TEP devices (Tunnel End Point), which is the ESX Hypervisors. In case, routing between differnt VM subnets, NSX-T T1 DR router can be used (VM subnets GW).

**VM-Bare-Metal Traffic**<br /> 
Traffic from the virtualized environment to the outside world (physical environment) must traverse via the NSX-EDGE T0 router. 
1.	VM traffic arrives Geneve encapsulated to the NSX-EDGE (T0 router)
2.	The T0 router decapsulates the Geneve header and sends the traffic as Regular IP traffic towards the ToR switch, which acts as VXLAN HW-VTEP 
3.	Local ToR VTEP encapsulates the traffic into the VXLAN tunnel and sends it to the remote VTEP (BM ToR). The VXLAN Tunnel is established between the local ToR and the remote ToR switches
4.	The BM VTEP decapsulates the VXLAN header and sends the traffic as regular to the BM server<br />
<br />

### Packet Flow using NSX-T 3.0 (Wihouth NSX-T Agent)
{{<figure src="/images/guides/apstra-nsx/nsx3.0.JPG">}}
**VM-VM Traffic**<br /> 
Same as with NSX-T 2.5, traffic inside the virtualized environment encapsulated into Geneve tunnels. The encapsulation/decapsulation is handled by the TEP devices (Tunnel End Point), which is the ESX Hypervisors. In case, routing between differnt VM subnets, NSX-T T1 DR router can be used (VM subnets GW).

**VM-Bare-Metal**<br />
As with NSX-T 2.5, traffic from the virtualized environment to the outside world (physical environment) must traverse via the NSX-EDGE T0 router. 
1.	The traffic arrives Geneve encapsulated from the VM to the NSX-EDGE (T0 router) 
2.	The T0 router decapsulates the Geneve header and encapsulates it again but into a VXLAN tunnel, then sends the traffic as VXLAN traffic towards the remote ToR switch (BM rack), which acts as VXLAN HW-VTEP 
3.	The local ToR switch only sends regular IP traffic and isn’t aware of the VXLAN header. The VXLAN tunnel is established between the NSX-EDGE and the remote HW-VTEP ToR
4.	The BM VTEP decapsulates the VXLAN header and sends the traffic as regular to the BM server.<br />
{{%/notice %}}

Now, when we understand the packet flow for each of the NSX-T versions, we can continue with our **Virtual** intent configuration.<br />
Create **Virtual Network** (VLANs) as required by VMware for each ESX host:
- Mgmt.
- Storage
- vMotion
- Tunnel (TEP)

{{%notice note%}}There is a predefined Default security zone associated with any new Blueprint. When using NSX-T 2.5, all SVIs configured for **Virtual Networks** in this zone are in the “default” VRF. This is the same VRF used for the “underlay” or fabric network routing between network devices. With NSX-T 3.0, AOS will allow VLAN to non-default VRF assignemt {{<figure src="/images/guides/apstra-nsx/13-default security zone.png">}}{{%/notice %}}

Go to the **Virtual Networks** configuration in **Virtual** tab
{{<figure src="/images/guides/apstra-nsx/10-virtual_tab_new.JPG">}}
Press on the **Create Virtual Networks** button
{{<figure src="/images/guides/apstra-nsx/12-create vritual network.png">}}
In the oppened window, set the following settings:
- Vritual Netowrk (VN) Type
- VN Name 
- Security Zone (we keep it simple and define the same VN name as the Security zone name)
- VNI (L2 VNI)
- Mark the VLAN ID createtion on all leafs and set the VLAN ID for this VN (L2VNI). This creates the VLAN-to-VNI mapping on the ToR switches. 
- Enalbe IPv4 Connectivity, and leave the **IPv4 Subnet** and the **Virtual Gateway IPv4** blank, we will set the addressing using the resource pools

{{%notice note%}}As mentined, we consider in each rack as a different ESX cluster, so regardless the use of the same VLAN ID, each rack has to be configured with a diffrent subnet per VLAN on the corresponding ToR pair {{%/notice %}}

{{<figure src="/images/guides/apstra-nsx/12-create vlan storage.JPG">}}
Set whether the **Default Endpoint Types** will be **VLAN Tagged** or **Untagged**. We are using **VLAN Tagged** ports connected to the ESXi hypervisors and the Bare-metal server
{{<figure src="/images/guides/apstra-nsx/12-create vlan storage tagged.JPG">}}
Assign these settings to two of the three leafs (rack 1 and 2) and press **Create**. This action will create these VLANs on the switches.<br /> 
In our use-case, only the ToR switches of those racks will use VLAN and BGP configuration (middle rack will use also VXLAN, but for the EDGE(T0)-to-BM traffic)  
{{<figure src="/images/guides/apstra-nsx/12-create vlan storage assign.JPG">}}
Once created, we can see that "Tunnel" VLAN (VLAN ID 30) was created on both racks
{{<figure src="/images/guides/apstra-nsx/12-create vlan storage show.JPG">}}
Repeat the same actions for the rest of the VLANs. But, don't assign the VLANs to the MLAG ports
{{<figure src="/images/guides/apstra-nsx/12-unassigned.JPG">}}
{{%notice note%}}AOS and NSX-T integration, helps to indicate and fix any VLAN missmatch between the blueprint and the actual NSX-T configuration. In our example, we created 4 VLANs per each ESX transport node. But, we won't use them all in practice besides VLAN30 as our Geneve tunnels (TEP). Rest of the VLANs are created for the sake of VMware requirments example and that's the reason we aren't assignning them to all MLAG ports. By that, we can eliminate irrelevant errors in AOS validations.{{%/notice %}} 
Once All created, you will see the table with all
{{<figure src="/images/guides/apstra-nsx/12-create vlan storage all.JPG">}}
Now, we need to assign the SVI IP addresses for the created VLANs. These addresses will be the Gateways for our ESX Hypervisors, and will BGP will advertise them to the underlay fabric.<br />
Click on the **Red Status Indicator** of the **SVI Subnets - Virtual Networks**, press the **Pencil** icon, select the predefined pool and press **Save** 
{{<figure src="/images/guides/apstra-nsx/12-vlan svi assign.JPG">}}
Once saved, the indicator will become **Green** 
{{<figure src="/images/guides/apstra-nsx/12-vlan svi assign green.JPG">}}
The IP addresses should now be assigned to all VLANs.<br />
In our reference we chose AOS to automatically set the following underlying IP addresses scheme (can be changed or set manually):
- **VLAN 2** - Mgmt:<br />
    Rack 01 - 172.16.0.0/24<br /> 
    Rack 02 - 172.16.1.0/24
- **VLAN 10** - Storage:<br />
    Rack 01 - 172.16.6.0/24<br /> 
    Rack 02 - 172.16.7.0/24
- **VLAN 20** - vMotion:<br />
    Rack 01 - 172.16.2.0/24<br /> 
    Rack 02 - 172.16.3.0/24
- **VLAN 30** - Tunnel(TEP):<br />
    Rack 01 - 172.16.4.0/24<br /> 
    Rack 02 - 172.16.5.0/24

Rack 03 is our BM rack, so no need to assign ESX underlaying VLANs on it.
{{<figure src="/images/guides/apstra-nsx/12-vlan svi assign all.JPG">}}

VMs in the same subnet will communicate in L2 between the ESX hosts over Geneve tunnels, the routing between the VM subnets, will be handeled by NSX-T T1 distributed routers. In case VMs will have to send traffic to the bare-metal server, T0 router will route them out to the outside world by using BGP. In our solution guide, we don't cover the steps of creating NSX-T elemets.<br />
For NSX-T T0 router to work with the TOR switches, we have to create a new Security zone (VRF) and another 3 vritual networks (VLANs). One VN will be for an additional TEP (Tunnel) VLAN for the EDGE node to communucate with rest of the transport nodes. The two ohter VLANs (VNs) for the EDGE uplink ports which will be used as external links and BGP will be established on them as well. Both the uplink VNs will be placed into the new created security zone. But, before we create those, we need to create a logical External Router for the NSX-T T0 inside AOS. <br /> 
To do so, go to the **External Routers** configuration inside the **External Systems** category 
{{<figure src="/images/guides/apstra-nsx/14-external routers.png">}}
There are couple of example external routers present in AOS, but we will use our own NSX-T T0 router. Press on the **Create External Router** button
{{<figure src="/images/guides/apstra-nsx/14-external routers create.png">}}
In the oppened window, set NSX-T T0 router **Name**, **IPv4 Loopback Address**, BGP **ASN**, and press **Create** to add it
{{<figure src="/images/guides/apstra-nsx/14-external routers create details.JPG">}}
Once created, it will appear in the external router's inventory
{{<figure src="/images/guides/apstra-nsx/14-external routers inventory.JPG">}}
Now, when the external router for NSX-T T0 is ready, lets return to the **Staged** configuration inside the **Blueprints**.<br />
Import the new external router into the blueprint by going into **Catalog** tab
{{<figure src="/images/guides/apstra-nsx/14-external routers import.JPG">}}
Press on the **Import External Router** button
{{<figure src="/images/guides/apstra-nsx/14-external routers button.jpg">}}
Select the created **External Router** and press **Import Exteral Router**
{{<figure src="/images/guides/apstra-nsx/14-external router import.JPG">}}
The NSX-T T0 router is now imported into the Blueprint
{{<figure src="/images/guides/apstra-nsx/14-external router imported.JPG">}}
To connect the ToR switches with the T0 external router, go to the **Physical** tab. In the **Selected Rack** and the **Selected Node** drop-boxes, select the needed rack and one of the ToR switches indide it
{{<figure src="/images/guides/apstra-nsx/15-external router links rack select.JPG">}}
At the top of the selected ToR switch connectivity, press on **Add links** to connect the NSX-T T0 router 
{{<figure src="/images/guides/apstra-nsx/15-external router links rack add links.JPG">}}
From the drop-down menu, select **Add external router links**
{{<figure src="/images/guides/apstra-nsx/15-external router links add.JPG">}}
In the oppened window, select the desired ports (one per ToR switch) which will be connected to the ESX node with the NSX EDGE T0 router on.<br /> 
Once the port selected, click on its name with the appropriate speed (in our case we use 25 Gbps, default) and press on the **Add Link** green button. Repeat the same action for the second switch. 
{{<figure src="/images/guides/apstra-nsx/15-external router links and types.JPG">}}
{{%notice note%}}Current AOS implementation restricts usage of additional links between the ESX node and the ToR switches for EDGE usage. It's impossible to apply the existing Trunk ports between the ESX node and the ToR switches as external router ports.{{%/notice %}}
When both links added, select the **External Router** from the drop-down menu, and set the **Connectivity Type** to **L2**. Once done, press **Add**
{{%notice note%}}As EDGE VM doesn't support active-active deployment, we can't use A/A bond connection, so we select only **L2**. Later, we will create two different VLANs for the uplinks - one per T0 router uplink.{{%/notice %}}
Once added, we can see the new port on the switch connectivity diagram
{{<figure src="/images/guides/apstra-nsx/15-external router links added.JPG">}}
Now, we need to create the new secutiry zone (VRF) for the T0 router uplinks. This VRF will be used to communucate with the outside world (bare-metal rack).<br />
Go to the **Security Zones** in the **Virtual** tab 
{{<figure src="/images/guides/apstra-nsx/13-security zones.JPG">}}
Press on the **Create Security Zone** button
{{<figure src="/images/guides/apstra-nsx/13-create security zone.png">}}
In the oppened window, set new VRF's **Name**, **VLAN ID**, and **VNI**
{{<figure src="/images/guides/apstra-nsx/13-create security zone1.JPG">}} 
Uncheck the **Spine Leaf Links** and **Loopbacks** under the **Export Policy**, and export a default route press **Create** 
{{<figure src="/images/guides/apstra-nsx/13-create security zone11.JPG">}}
Once created, **Route Target** will be automatically set
{{<figure src="/images/guides/apstra-nsx/13-create security zone2.JPG">}}
Now, set the **Leaf Loopback IPs** for the created **RED** VRF. Press on the **Red Status Indicator** near the VRF name, press on the **Pencil** icon, select the **Private-10.0.0.0/8** pool (as we did with loopbacks settings for the physical intent), and press **Save** button
{{<figure src="/images/guides/apstra-nsx/13-loopback ips.JPG">}}
All indicators will be **Green** once done (EVPN L3 VNIs are already Green as we set them during VRF creation).<br />
To add the External Routers' uplinks we've just created, press on the Security Zone's name to edit its parameters. Under **External Connectivity Points**, press on the **Add Connectivity Point** button
{{<figure src="/images/guides/apstra-nsx/13-security zone params.JPG">}}
In the openned window, set Connectivity Point's parameters:
- **Connectivity Type** - L2 (as we set to the external router links we added earlier)
- **Routing Protocol** - BGP
- **Peering Type** - Interface
- **VLAN ID**
- **IPv4 Subnet**
- **Links** - Select one of the swtiches links we created and press **Add Link**
{{<figure src="/images/guides/apstra-nsx/13-security zone external routing.JPG">}}
Once the links added, fill the **Resources** for it (IP addressing) and press **Add** 
{{<figure src="/images/guides/apstra-nsx/13-security zone external routing part2.JPG">}}
This will automatically create the Virtual Network (VLAN) and its SVI on the selected switch (link). BGP session between will establish based on these parameters and the ASN of the swtiches and the NSX-T T0 external router.<br /> 
Repeaat the same for the 2nd uplink to the other ToR (but in different VLAN).<br />
Once both links set into the VRF, they will appear under the **External Connectivity Points**
{{<figure src="/images/guides/apstra-nsx/13-security zone connectivity points.JPG">}}
Lets validate that the VNs were created for our external router uplinks. Go to **VIrtual Networks** under **Virtual** tab and two new virtual networks should appear with **External** type in our custom security zone with the IP allocation we set
{{<figure src="/images/guides/apstra-nsx/13-security zone VN auto create.JPG">}}

To enable NSX-T Edge communicate with other TEP devices (ESX transport nodes), we have to create additional TEP VLAN that will serve for Edge's tunnel encapsulation. This action is identical as we did bofere for each of the ESX nodes (VLAN30).<br />
Create new Virual Network by pressing **Create Virtual Networks** button
{{<figure src="/images/guides/apstra-nsx/12-create vritual network.png">}}
In the openned window, select VN parameters:
- **Type** - VLAN
- **Name**
- **Default VLAN ID**
- **IPv4 Connectivity** - Enabled and IPv4 subnet and GW set
- **Default Endpoint Types** - Set the needed MLAG port to be tagged with the new VLAN. 
{{<figure src="/images/guides/apstra-nsx/12-create vlan edge tep.JPG">}}
Assign the VLAN to the relevat Rack and press **Create**
{{<figure src="/images/guides/apstra-nsx/12-create vlan edge tep assign.JPG">}}
Now, new VN for Edge TEP will appear in the table
{{<figure src="/images/guides/apstra-nsx/12-create vlan edge tep done.JPG">}}

## Apstra AOS and NSX-T Integraion

AOS and NSX-T integration helps deploying the necessary fabric VLANs needed for deploying virtualized enviorment in the Data Center or for providing connectivity between the overlay and the underlay networks. This feature makes sure the fabric is ready in terms of LAG, MTU and VLAN configuration as per NSX-T Transport Nodes requirements. Also, AOS provides visibility into the virtualized envioemrnt by enabling to see the VMs, VM ports, and physical gateway ports. AOS helps identify if an issue exists on the fabric or on the virtual infrastructure and eliminates manual config validation tasks between the NSX-T Nodes side and the ToR switches.
{{%notice info%}}AOS NSX-T Edge integration supports only Bare Metal Edge deployments. As our reference guide uses NSX-T Edge on a VM, no Edge integraion will be shown{{%/notice %}}
Connect VMware NSX-T to the AOS (add more text here...)
Go to the **Virtual Infra Managers** tab in the **External Systems** category
{{<figure src="/images/guides/apstra-nsx/20-virtual infra.png">}}
Press on the **Create Virtual Infra Manager** button
{{<figure src="/images/guides/apstra-nsx/20-add virtual infra.png">}}
Select the **Virtual Infra Type**, **Address**, **Credentials**, and press **Create**
{{<figure src="/images/guides/apstra-nsx/20-add nsx-t.JPG">}}
{{%notice note%}}It is optional to also connect the vCneter to AOS, this allows a complete visibility into the virtualized enviorment{{%/notice %}}
Once NSX-T connected to AOS, it's tate should be **CONNECTED**
{{<figure src="/images/guides/apstra-nsx/20-connected nsx-t.JPG">}}

To add NSX-T virtual manager into virtual network intent, go back to the Blueprint, into the **Virtual Infra** tab in the **Virtual** configuration 
{{<figure src="/images/guides/apstra-nsx/21-virtual infra blueprint.JPG">}}
Press on the **Add Virtual Infa** button
{{<figure src="/images/guides/apstra-nsx/20-add virtual infra button.png">}}
In the oppened window, select the NSX-T from the **Virtual Infra Manger** drop-down, set **VN type** as VLAN, and press **Create**
{{<figure src="/images/guides/apstra-nsx/21-virtual infra add to blueprint.JPG">}}
Once added, it will appear in the virtual infrastucture managers list
{{<figure src="/images/guides/apstra-nsx/21-virtual infra added to BP.JPG">}}

Now, let's create VXLAN interfaces per our VM networks (VLAN100 and VLAN200)



















Once all set, commit the changes by pressing **Commit** button in **Uncommited tab**
{{<figure src="/images/guides/apstra-nsx/100-commit.JPG">}}



## NSX side validation

On the NSX T0 router we will have 2 BGP neighbors
```
nsxedge2(tier0_sr)> get bgp neighbor summary
BFD States: NC - Not configured, AC - Activating,DC - Disconnected
            AD - Admin down, DW - Down, IN - Init,UP - Up
BGP summary information for VRF default for address-family: ipv4Unicast
Router ID: 172.16.10.6  Local AS: 65000

Neighbor                            AS          State Up/DownTime  BFD InMsgs  OutMsgs InPfx  OutPfx
172.16.9.3                          64517       Estab 1d04h27m     NC  107640  107646  7      8
172.16.10.2                         64516       Estab 1d04h26m     NC  107609  107610  7      8
```
