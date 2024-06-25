---
title: Advanced Configuration
author: NVIDIA
weight: 46
product: Cumulus VX
version: '5.x'
---
This section describes advanced procedures that help you get more out of Cumulus VX; for example, you can:

- Test the Cumulus Linux upgrade process in your virtual environment by installing a Cumulus VX binary image with ONIE.
- Convert the two leaf and one spine topology so that you can follow the {{<exlink url="https://www.nvidia.com/en-us/networking/linux-on-demand/" text="Cumulus Linux on demand">}} lab tutorials.
- Run the topology converter script to convert a topology file into a Vagrantfile so you can simulate a custom network topology that includes servers and custom interface names and connections.

## Install an ONIE Virtual Machine

Cumulus VX images include the GRUB boot loader and Open Network Install Environment (ONIE). You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

After booting the VM, reboot into ONIE Rescue mode using one of two methods:

- Select ONIE Rescue mode on next reboot and reboot the VM with the `sudo onie-select -rf && sudo reboot` command.
- Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

To install Cumulus VX, run the `onie-nos-install <URL to cumulus-linux-vx-amd64.bin>` command.

## Convert the Topology for Cumulus Linux on Demand

NVIDIA offers {{<exlink url="https://www.nvidia.com/en-us/networking/linux-on-demand/" text="Cumulus Linux on-demand">}} to help you get familiar with Cumulus Linux. This introductory lab tutorial includes various self-paced labs that let you practice configuring Cumulus Linux and use features such as NCLU, FRR, and BGP unnumbered.

The Cumulus Linux on-demand labs use the following topology:

{{< img src="/images/cumulus-vx/testdrive-topology.png" width="400" >}}

To be able to follow the labs, you need to convert the two leaf and one spine topology used in this documentation to the topology used in the labs.

{{%notice tip%}}
As an alternative to using Cumulus VX with the Cumulus Linux on demand labs, you can use {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/air/" text="NVIDIA AIR">}}, which is a free, personal, virtual data center network that provides a low-effort way to see NVIDIA technology in action. Your virtual data center consists of two racks with two dual-homed servers connected with a leaf-spine network.
{{%/notice%}}

To convert the topology, you need to:

- Change the ports on leaf01 and leaf02 (spine01 does not require any port changes)
- Create the server01 and server 02 virtual servers

For VirtualBox and Vagrant or KVM-QEMU and Vagrant, you can run the topology converter to convert the topology. See {{<link url="#run-the-topology-converter" text="Run the Topology Converter">}} section below.

### Change the Ports

Follow these steps on both **leaf01** and **leaf02**:

1. Obtain the MAC address for swp1, swp2, and swp3:

   {{< tabs "TabID45 ">}}

{{< tab "swp1 ">}}

```
cumulus@leaf01:mgmt:~$ ip link show swp1
3: swp1: <BROADCAST,MULTICAST,UP,LOWER,LOWER_UP> mtu 9216 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
   link/ether 08:00:27:8c:cf:41 brd ff:ff:ff:ff:ff:ff:ff
```

{{< /tab >}}

{{< tab "swp2 ">}}

```
cumulus@leaf01:mgmt:~$ ip link show swp2
4: swp2: <BROADCAST,MULTICAST,UP,LOWER,LOWER_UP> mtu 9216 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
   link/ether 08:00:27:2a:5b:4e brd ff:ff:ff:ff:ff:ff:ff
```

{{< /tab >}}

{{< tab "swp3 ">}}

```
cumulus@leaf01:mgmt:~$ ip link show swp3
5: swp3: <BROADCAST,MULTICAST,UP,LOWER,LOWER_UP> mtu 9216 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
   link/ether 08:00:27:91:9a:48 brd ff:ff:ff:ff:ff:ff:ff
```

{{< /tab >}}

{{< /tabs >}}

2. As root, change the ports associated with the MAC address obtained for swp1, swp2, and swp3 from the previous step; for example:

   {{< tabs "TabID65 ">}}

{{< tab "Change swp1 to swp51 ">}}

```
root@leaf01:mgmt:~$ echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="08:00:27:8c:cf:41", NAME="swp51", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
```

{{< /tab >}}

{{< tab "Change swp2 to swp49 ">}}

```
root@leaf01:mgmt:~$ echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="08:00:27:2a:5b:4e", NAME="swp49", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
```

{{< /tab >}}

{{< tab "Change swp3 to swp50 ">}}

```
root@leaf01:mgmt:~$ echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="08:00:27:91:9a:48", NAME="swp50", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
 ```

{{< /tab >}}

{{< /tabs >}}

   {{%notice note%}}
Cumulus VX supports the use of Linux {{<exlink text="udev rules" url="https://wiki.debian.org/udev">}} to rename interfaces to match any desired topologies.
{{%/notice%}}

3. As root, run the following command to disable default remapping on Cumulus VX, then reboot the switch.

   ```
   root@leaf01:mgmt:~$ mv /etc/hw_init.d/S10rename_eth_swp.sh /etc/S10rename_eth_swp.sh.backup
   root@leaf01:mgmt:~$ reboot
   ```

4. Log in to the switch, then bring up swp49, swp50, and swp51:

   ```
   cumulus@leaf01:mgmt:~$ net add interface swp49,swp50,swp51
   cumulus@leaf01:mgmt:~$ net commit
   ```

### Create server01 and server02

In your hypervisor environment, create two Ubuntu virtual servers; server01 and server02.

- On server01, connect eth1 to swp1 on leaf01 and eth02 to swp1 on leaf02.
- On server02, connect eth1 to swp2 on leaf01 and eth02 to swp2 on leaf02.

Refer to your hypervisor documentation for detailed instructions on creating virtual servers and network connections.

After you change the ports and create server01 and server02, you are ready to go to {{<exlink url="https://www.nvidia.com/en-us/networking/linux-on-demand/" text="Cumulus Linux on-demand">}} and follow the lab tutorials.

## Run the Topology Converter

The topology converter can help you to simulate a custom network topology directly on your laptop or on a dedicated server. The topology can be extremely complete; you can simulate hosts as well as network equipment.

The topology converter translates a Graphviz topology file (`.dot` file), which describes the network topology link-by-link, into a Vagrantfile, which fully represents the topology. Vagrant uses Vagrantfiles to define VM settings and connections. You can then simulate the topology with either VirtualBox and Vagrant or with KVM-QEMU and Vagrant.

The topology converter:

- Remaps interfaces on VX switches and hosts to match the interfaces used in the provided topology file.
- Removes extra Ruby-based logic from the Vagrantfile to provide simple human-readable output.
- Generates a Vagrantfile that contains servers and switches and anything else found in a Vagrant <!-- vale off -->Box<!-- vale on --> image.

### Install the Topology Converter

Follow the steps below to install the required tools, and download the topology converter script and required files.

This procedure assumes you are on a system running Linux and have a Vagrant <!-- vale off -->Box<!-- vale on --> image available.

1. Install the tools required to run the topology converter:

   ```
   local@host:~$ sudo apt install python3-pip
   local@host:~$ sudo pip3 install --upgrade pip
   local@host:~$ sudo pip3 install setuptools
   local@host:~$ sudo pip3 install pydotplus
   local@host:~$ sudo pip3 install jinja2
   local@host:~$ sudo pip3 install ipaddress
   ```

2. Download the topology converter source code from {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/" text="GitLab">}}.

   The topology converter script (`topology_converter.py`) and required files download to the `topology_converter` folder, which also includes a subfolder for documentation and a subfolder for example topologies.

### Convert a Topology

1. In the `topology_converter` folder (which includes `topology_converter.py`), create a `topology.dot` file.

   The following example `toplology.dot` file represents the topology used in the Cumulus Linux on demand labs; leaf01, leaf02, spine01, server01, and server02. With the following topology, you can follow the lab tutorials with {{<exlink url="https://www.nvidia.com/en-us/networking/linux-on-demand/" text="Cumulus Linux on demand">}}.

   ```
   graph dc1 {
   "spine01" [function="spine" os="CumulusCommunity/cumulus-vx" memory="768" config="./helper_scripts/extra_switch_config.sh"]
   "leaf01" [function="leaf" os="CumulusCommunity/cumulus-vx" memory="768" config="./helper_scripts/extra_switch_config.sh"]
   "leaf02" [function="leaf" os="CumulusCommunity/cumulus-vx" memory="768" config="./helper_scripts/extra_switch_config.sh"]
   "server01" [function="host" os="ubuntu/xenial64" memory="512" config="./helper_scripts/extra_server_config.sh"]
   "server02" [function="host" os="ubuntu/xenial64" memory="512" config="./helper_scripts/extra_server_config.sh"]
      "spine01":"swp1" -- "leaf01":"swp51"
      "spine01":"swp2" -- "leaf02":"swp51"
      "leaf01":"swp49" -- "leaf02":"swp49"
      "leaf01":"swp50" -- "leaf02":"swp50"
      "server01":"eth1" -- "leaf01":"swp1"
      "server01":"eth2" -- "leaf02":"swp1"
      "server02":"eth1" -- "leaf01":"swp2"
      "server02":"eth2" -- "leaf02":"swp2"
   }

   ```

2. Run the following command to convert the `topology.dot` file to a Vagrantfile:

   ```
   local@host:$ python3 ./topology_converter.py ./topology.dot
   ```

   With Libvirt, run the following command:

   ```
   local@host:$ python3 ./topology_converter.py ./topology.dot -p libvirt
   ```

   The topology converter reads the provided topology file line by line, and learns information about each node and each link in the topology. It stores this information in a `variables` data structure. You use a `jinja2` template (`/templates/Vagrantfile.j2`) to create a Vagrantfile based on the `variables` data structure.

3. Start the simulation with the `vagrant up` command. With Livirt, start the simulation with the `vagrant up --provider=libvirt` command.

4. Log in to each switch, then bring up the interfaces.

To explore the topology converter further, read the documentation and take a look at the selection of example topologies included with the source code you downloaded.

If you encounter any issues, you can file them directly in the {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/" text="GitLab topology converter project">}}.
