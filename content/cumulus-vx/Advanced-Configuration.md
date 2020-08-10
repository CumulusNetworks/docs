---
title: Advanced Configuration
author: Cumulus Networks
weight: 46
---
This section describes advanced procedures that you can follow to get more out of Cumulus VX.

- Test the Cumulus Linux upgrade process in your virtual environment by installing a Cumulus VX binary image with ONIE.
- Run the conversion script on your switches so that you can take the self-paced labs in the {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand/" text="Virtual Test Drive">}}.
- Run the topology converter to convert a topology file into a Vagrantfile so you can create a topology of your choice.

## Install an ONIE Virtual Machine

Cumulus VX images include the GRUB boot loader and Open Network Install Environment (ONIE) preinstalled. You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

After booting the VM, reboot into ONIE Rescue mode using one of two methods:

- Select ONIE Rescue mode on next reboot and reboot the VM with the `sudo onie-select -rf && sudo reboot` command.
- Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

To install Cumulus VX, run the `onie-nos-install <URL to cumulus-linux-vx-amd64.bin>` command.

## Run the Conversion Script

The self-paced labs in the {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand/" text="Virtual Test Drive">}} use the following topology:

IMAGE

To run the labs, you need to first run a script to update the port configuration.

## Run the Topology Converter

To create a topolgy of your choice, you can use the topology converter to convert a `topology.dot` (DOT-specified network graph) file to a Vagrantfile. The `topology.dot` file describes the network topology link-by-link.

{{%notice note%}}

The topology converter is supported for Virtualbox and Libvirt Vagrant.

{{%/notice%}}

The topology converter:

- Remaps interfaces on VX switches and hosts to match the interfaces used in the provided topology file
- Removes extra Ruby-based logic from the Vagrantfile to provide simple human-readable output
- Generates a Vagrantfile that contains servers and switches and anything else that can be found in a Vagrant Box image
- Does not require Vagrant, Virtualbox, or libvirt to be installed to create the Vagrantfile

### Install the Topology Converter

Follow the steps below to install the topology converter.

{{< tabs "TabID01 ">}}

{{< tab "Ubuntu">}}

```
local@host:~$ sudo apt install python3-pip
local@host:~$ sudo pip3 install --upgrade pip
local@host:~$ sudo pip3 install setuptools
local@host:~$ sudo pip3 install pydotplus
local@host:~$ sudo pip3 install jinja2
local@host:~$ sudo pip3 install ipaddress
```

{{< /tab >}}

{{< tab "MacOS ">}}

```
local@host:~$ brew install python3
local@host:~$ sudo pip install --upgrade pip
local@host:~$ sudo pip install setuptools
local@host:~$ sudo pip install pydotplus
local@host:~$ sudo pip install jinja2
local@host:~$ sudo pip install ipaddress
```

{{< /tab >}}

{{< /tabs >}}

### Convert a Topology

1. Create a `topology.dot` file or use a file provided by Cumulus Networks {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/-/tree/master/documentation#example-topologies" text="here">}}. The following example `toplology.dot` file contains leaf1, which is connected on swp40 and swp50 to leaf2, and server1, which is connected via eth1 to swp1 on leaf1 and eth2 to swp1 on leaf1:

   ```
   graph dc1 {
    "leaf1" [function="leaf" os="CumulusCommunity/cumulus-vx" memory="768" config="./helper_scripts/extra_switch_config.sh"]
    "leaf2" [function="leaf" os="CumulusCommunity/cumulus-vx" memory="768" config="./helper_scripts/extra_switch_config.sh"]
    "server1" [function="host" os="boxcutter/ubuntu1404" memory="512" config="./helper_scripts/extra_server_config.sh"]
      "leaf1":"swp40" -- "leaf2":"swp40"
      "leaf1":"swp50" -- "leaf2":"swp50"
      "server1":"eth1" -- "leaf1":"swp1"
      "server1":"eth2" -- "leaf2":"swp1"
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

The topology converter reads the provided topology file line by line, and learns information about each node and each link in the topology. This information is stored in a variables datastructure. A `jinja2` template `Vagrantfile.j2` (stored in the `/templates` directory) is used to create a Vagrantfile based on the variables datastructure.
