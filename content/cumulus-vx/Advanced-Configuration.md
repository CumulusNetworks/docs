---
title: Advanced Configuration
author: Cumulus Networks
weight: 46
---
This section describes advanced procedures that help you get more out of Cumulus VX:

- Test the Cumulus Linux upgrade process in your virtual environment by installing a Cumulus VX binary image with ONIE.
- Convert the two leaf and one spine topology so that you can take the {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand/" text="Virtual Test Drive">}} labs.
- Run the topology converter script to convert a topology file into a Vagrantfile so you can simulate a custom network topology.

## Install an ONIE Virtual Machine

Cumulus VX images include the GRUB boot loader and Open Network Install Environment (ONIE) preinstalled. You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

After booting the VM, reboot into ONIE Rescue mode using one of two methods:

- Select ONIE Rescue mode on next reboot and reboot the VM with the `sudo onie-select -rf && sudo reboot` command.
- Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

To install Cumulus VX, run the `onie-nos-install <URL to cumulus-linux-vx-amd64.bin>` command.

## Convert the Topology for the Virtual Test Drive Labs

Cumulus Networks offers the {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand/" text="Virtual Test Drive">}} to help you get familiar with Cumulus Linux. The test drive includes various self-paced labs that let you practice configuring Cumulus Linux and use features such as BGP.

The Virtual Test Drive labs use the following topology:

{{< img src="/images/cumulus-vx/testdrive-topology.png" width="400" >}}

To be able to follow the labs, you need to convert the two leaf, one spine topology we use in this documentation to the topology used in the labs.

{{%notice tip%}}

As an alternative to using Cumulus VX with Virtual Test Drive labs, you can use {{<exlink url="https://cumulusnetworks.com/products/cumulus-in-the-cloud/" text="Cumulus in the Cloud">}}, which is a free, personal, virtual data center network that provides a low-effort way to see Cumulus Networks technology in action. Your virtual data center consists of two racks with two dual-homed servers connected with a leaf-spine network.

{{%/notice%}}

To convert the topology, change the ports on leaf01 and leaf02 (spine01 does not require any port changes) and create the server01 and server 02 VMs.

### Change the Ports

1. On both **leaf01** and **leaf02**, obtain the MAC address for swp1, swp2, and swp3. Run the following commands:

   ```
   cumulus@leaf01:mgmt:~$ ip link show swp1
   OUTPUT

   cumulus@leaf01:mgmt:~$ ip link show swp2
   OUTPUT

   cumulus@leaf01:mgmt:~$ ip link show swp3
   OUTPUT
   ```

2. On both **leaf01** and **leaf02**, change the ports associated with the MAC addresses you obtained in the previous step:

   Run this command to change swp1 to swp51. Replace `<mac-address>` with the MAC address you obtained for swp1 above:

   ```
   cumulus@leaf01:mgmt:~$ echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="<mac-address>", NAME="swp51", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   ```

   Run this comand to change swp2 to swp49. Replace `<mac-address>` with the MAC address you obtained for swp2 above:

   ```
   cumulus@leaf01:mgmt:~$ echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="<mac-address>", NAME="swp49", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   ```

   Run this comand to change swp3 to swp50. Replace `<mac-address>` with the MAC address you obtained for swp3 above:

   ```
   cumulus@leaf01:mgmt:~$ echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="<mac-address>", NAME="swp50", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   ```

### Create the server01 and server02 VMs

Create two VMS, server01 and server02.

   - On server01, connect eth1 to swp1 on leaf01 and eth02 to swp1 on leaf02.

   - On server02, connect eth1 to swp2 on leaf01 and eth02 to swp2 on leaf02.

Refer to the your hypervisor documentation for detailed instructions on creating server VMs and network connections.

## Run the Topology Converter

The topology Converter can help you to simulate a custom network topology directly on your laptop or on a dedicated server. The topology can be extremely complete so that you can simulate hosts as well as network equipment.

The topology converter translates a graphviz topology file (`.dot` file), which describes the network topology link-by-link, into a Vagrantfile, which fully represents the topology. Vagrantfiles are used with Vagrant to interconnect VMs. You can then simulate the topology in either Virtualbox or with KVM-QEMU and Libvirt.

The topology converter:

- Remaps interfaces on VX switches and hosts to match the interfaces used in the provided topology file.
- Removes extra Ruby-based logic from the Vagrantfile to provide simple human-readable output.
- Generates a Vagrantfile that contains servers and switches and anything else that can be found in a Vagrant Box image.

{{%notice note%}}

To run the topology converter script and create the Vagrantfile, you do not need to have Vagrant, Virtualbox, or libvirt installed.

{{%/notice%}}

### Install the Topology Converter

Follow the steps below to install the required tools, and download the topology converter script and necessary files.

This procedure assumes you are on a system running Linux and have a vagrant box image available.

1. Install the tools required to run the topology converter script:

   ```
   local@host:~$ sudo apt install python3-pip
   local@host:~$ sudo pip3 install --upgrade pip
   local@host:~$ sudo pip3 install setuptools
   local@host:~$ sudo pip3 install pydotplus
   local@host:~$ sudo pip3 install jinja2
   local@host:~$ sudo pip3 install ipaddress
   ```

2. Download the following files from {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/" text="gitlab">}}:

   - The `topology_converter.py` file
   - The `templates/Vagrantfile.j2` template file
   - The `helper_scripts/extra_switch_config.sh` file and the `helper_scripts/extra_server_config.sh` file

3. Create a directory from which to run the topology converter. Add the files you dowloaded in the previous step.

   The `Vagrantfile.j2` file must be in the `templates` subdirectory. The `extra_switch_config.sh` file must be in the `helper_scripts` subdirectory. For example:

   ```
   local@host:~$ mkdir topology_converter
   local@host:~$ cd topology_converter
   local@host:topology_converter$ cp /Users/abc/Downloads/topology_converter.py topology_converter.py
   local@host:topology_converter$ mkdir templates helper_scripts
   local@host:topology_converter$ cp /Users/abc/Downloads/templates_Vagrantfile.j2 templates/Vagrantfile.j2
   local@host:topology_converter$ cp /Users/abc/Downloads/helper_scripts_extra_switch_config.sh helper_scripts/extra_switch_config.sh
   local@host:topology_converter$ cp /Users/abc/Downloads/helper_scripts_extra_server_config.sh helper_scripts/extra_server_config.sh
   ```

### Convert a Topology

1. Create a `topology.dot` file or use a file provided by Cumulus Networks {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/-/tree/master/documentation#example-topologies" text="here">}}. The following example `toplology.dot` file represents the topology used in the self-paced labs of the Virtual Test Drive, which includes leaf01, leaf02, spine01, server01, and server02.

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

2. Place the `topology.dot` file in the same directory as `topology_converter.py` (or any subdirectory in the directory that contains `topology_converter.py`).

3. Run the following command to convert the `topology.dot` file to a Vagrantfile:

   {{< tabs "TabID02 ">}}

{{< tab "Ubuntu">}}

```
local@host:~$ python3 ./topology_converter.py ./topology.dot
```

{{< /tab >}}

{{< tab "Libvirt ">}}

```
local@host:~$ python3 ./topology_converter.py ./topology.dot -p libvirt
```

{{< /tab >}}

{{< /tabs >}}

4. Start the simulation with the `vagrant up` command. If you are using Livirt, start the simulation with the `vagrant up --provider=libvirt` command.

The topology converter reads the provided topology file line by line, and learns information about each node and each link in the topology. This information is stored in a variables datastructure. A `jinja2` template (`/templates/Vagrantfile.j2`) is used to create a Vagrantfile based on the variables datastructure.

To see a selection of example topologies and view complete documentation on the topology converter, go to {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/" text="gitlab">}}.
