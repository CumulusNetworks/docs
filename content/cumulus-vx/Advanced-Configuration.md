---
title: Advanced Configuration
author: Cumulus Networks
weight: 46
---
This section describes advanced procedures that help you get more out of Cumulus VX:

- Test the Cumulus Linux upgrade process in your virtual environment by installing a Cumulus VX binary image with ONIE.
- Convert the two leaf and one spine topology so that you can follow the {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand/" text="Cumulus Linux on demand">}} lab tutorials.
- Run the topology converter script to convert a topology file into a Vagrantfile so you can simulate a custom network topology.

## Install an ONIE Virtual Machine

Cumulus VX images include the GRUB boot loader and Open Network Install Environment (ONIE) preinstalled. You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

After booting the VM, reboot into ONIE Rescue mode using one of two methods:

- Select ONIE Rescue mode on next reboot and reboot the VM with the `sudo onie-select -rf && sudo reboot` command.
- Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

To install Cumulus VX, run the `onie-nos-install <URL to cumulus-linux-vx-amd64.bin>` command.

## Convert the Topology for Cumulus Linux on Demand

Cumulus Networks offers {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand/" text="Cumulus Linux on demand">}} to help you get familiar with Cumulus Linux. This introductory lab tutorial includes various self-paced labs that let you practice configuring Cumulus Linux and use features such as NCLU, FRR, and BGP unnumbered.

The Cumulus Linux on demand labs use the following topology:

{{< img src="/images/cumulus-vx/testdrive-topology.png" width="400" >}}

To be able to follow the labs, you need to convert the two leaf and one spine topology we use in this documentation to the topology used in the labs.

{{%notice tip%}}

As an alternative to using Cumulus VX with the Cumulus Linux on demand labs, you can use {{<exlink url="https://cumulusnetworks.com/products/cumulus-in-the-cloud/" text="Cumulus in the Cloud">}}, which is a free, personal, virtual data center network that provides a low-effort way to see Cumulus Networks technology in action. Your virtual data center consists of two racks with two dual-homed servers connected with a leaf-spine network.

{{%/notice%}}

To convert the topology, change the ports on leaf01 and leaf02 (spine01 does not require any port changes) and create the server01 and server 02 virtual servers.

### Change the Ports

1. On both **leaf01** and **leaf02**, obtain the MAC address for swp1, swp2, and swp3:

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

2. On both **leaf01** and **leaf02**, change the ports associated with the MAC address obtained for swp1, swp2, and swp3 from the previous step; for example:

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

3. Bring up swp49, swp50, and swp51:

   ```
   cumulus@leaf01:mgmt:~$ net add interface swp49,swp50,swp51
   cumulus@leaf01:mgmt:~$ net commit
   ```

### Create server01 and server02

In your hypervisor environment, create two virtual servers; server01 and server02.

   - On server01, connect eth1 to swp1 on leaf01 and eth02 to swp1 on leaf02.

   - On server02, connect eth1 to swp2 on leaf01 and eth02 to swp2 on leaf02.

Refer to the your hypervisor documentation for detailed instructions on creating virtual servers and network connections.

After you change the ports and create server01 and server02, you are ready to go to {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand" text="Cumulus Linux on demand">}} and follow the lab tutorials.

## Run the Topology Converter

The topology Converter can help you to simulate a custom network topology directly on your laptop or on a dedicated server. The topology can be extremely complete; you can simulate hosts as well as network equipment.

The topology converter translates a graphviz topology file (`.dot` file), which describes the network topology link-by-link, into a Vagrantfile, which fully represents the topology. Vagrantfiles are used with Vagrant to interconnect VMs. You can then simulate the topology with either Virtualbox and Vagrant or with KVM-QEMU and Vagrant.

The topology converter:

- Remaps interfaces on VX switches and hosts to match the interfaces used in the provided topology file.
- Removes extra Ruby-based logic from the Vagrantfile to provide simple human-readable output.
- Generates a Vagrantfile that contains servers and switches and anything else that can be found in a Vagrant Box image.

### Install the Topology Converter

Follow the steps below to install the required tools, and download the topology converter script and required files.

This procedure assumes you are on a system running Linux and have a vagrant box image available.

1. Install the tools required to run the topology converter:

   ```
   local@host:~$ sudo apt install python3-pip
   local@host:~$ sudo pip3 install --upgrade pip
   local@host:~$ sudo pip3 install setuptools
   local@host:~$ sudo pip3 install pydotplus
   local@host:~$ sudo pip3 install jinja2
   local@host:~$ sudo pip3 install ipaddress
   ```

2. Download the topology converter source code from {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/" text="gitlab">}}.

   The topology converter script (`topology_converter.py`) and required files download to the `topology_converter` folder, which also includes a subfolder for documentation and a subfolder for example topologies.

### Convert a Topology

1. In the `topology_converter` folder (which includes `topology_converter.py`), create a `topology.dot` file.

   The following example `toplology.dot` file represents the topology used in the Cumulus Linux on demand labs; leaf01, leaf02, spine01, server01, and server02. With the following topology, you can follow the lab tutorials with {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand" text="Cumulus Linux on demand">}}.

   ```
   graph dc1 {
   "spine01" [function="spine" os="CumulusCommunity/cumulus-vx" memory="768" config="./helper_scripts/extra_switch_config.sh"]
   "leaf01" [function="leaf" os="CumulusCommunity/cumulus-vx" memory="768" config="./helper_scripts/extra_switch_config.sh"]
   "leaf02" [function="leaf" os="CumulusCommunity/cumulus-vx" memory="768" config="./helper_scripts/extra_switch_config.sh"]
   "server01" [function="host" os="ubuntu/xenial64" memory="512" config="./helper_scripts/extra_server_config.sh"]
   "server02" [function="host" os="ubuntu/xenial64" memory="512" config="./helper_scripts/extra_server_config.sh"]
      "spine01":"swp1" -- "leaf01":"swp51"
      "spine01":"swp2" -- "leaf02":"swp51"
      "leaf01":"swp40" -- "leaf02":"swp40"
      "leaf01":"swp50" -- "leaf02":"swp50"
      "server01":"eth1" -- "leaf01":"swp1"
      "server01":"eth2" -- "leaf02":"swp1"
      "server02":"eth1" -- "leaf01":"swp2"
      "server02":"eth2" -- "leaf02":"swp2"
   }

   ```

3. Run the following command to convert the `topology.dot` file to a Vagrantfile:

   ```
   local@host:$ python3 ./topology_converter.py ./topology.dot
   ```

   With Libvirt, run the following command:

   ```
   local@host:$ python3 ./topology_converter.py ./topology.dot -p libvirt
   ```

4. Start the simulation with the `vagrant up` command. With Livirt, start the simulation with the `vagrant up --provider=libvirt` command.

The topology converter reads the provided topology file line by line, and learns information about each node and each link in the topology. This information is stored in a variables datastructure. A `jinja2` template (`/templates/Vagrantfile.j2`) is used to create a Vagrantfile based on the variables datastructure.

To explore the topology converter further, read the documentation and take a look at the selection of example topologies included with the source code you downloaded.

If you encounter any issues, you can file them directly in the {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/" text="gitlab topology converter project">}}. You can also go to {{<exlink url="cumulusnetworks.slack.com" text="Cumulus Networks community slack">}} to discuss issues or ask questions about using the topology converter.
