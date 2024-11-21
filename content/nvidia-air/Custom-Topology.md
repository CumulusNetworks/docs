---
title: Custom Topology
author: NVIDIA
weight: 40
product: NVIDIA Air
---
Network topologies describe which nodes a data center is comprised of, how they are configured and which other nodes they are connected to.

NVIDIA Air offers multiple means of creating custom topologies and new simulations.

## The Drag-and-Drop Topology Builder
One way to create fully custom simulations is with the built-in topology builder. It provides a drag-and-drop editor to design any custom network.

To get started, perform the following instructions:

1. Navigate to [https://air.nvidia.com/simulations](https://air.nvidia.com/simulations). 
2. Click the **Create Simulation** button.
3. Give your simulation a **Name**.
4. Select **Blank Canvas** as the **Type**.
5. Optionally, assign an Organization to the sim. Read more about them in [Organizations](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Organizations/). 
6. Optionally, add a **ZTP script** to the simulation. You can read more about them in [ZTP Scripts](#ztp-scripts).
   1. Toggle on the **Apply ZTP Template** button.
   2. Enter your ZTP script. A default script is prefilled to help you get started. 
7. Click **Create**.

{{<img src="/images/guides/nvidia-air/CreateSimulation.png" alt="" width="930px">}}

### ZTP Scripts
You can add an optional **ZTP script** to the simulation when creating a new one. The ZTP script will be copied directly as-is into the `oob-mgmt-server` of the simulation. Any node making a ZTP request on the OOB management network has access to this ZTP script through a DHCP server and web server running on the `oob-mgmt-server`.

A default script is prefilled to help you get started. It implements some common ZTP features on Cumulus Linux, such as changing the default password or downloading SSH keys. You can modify it to your needs.

```
#!/bin/bash
# Created by Topology-Converter v4.7.1
#    Template Revision: v4.7.1

function error() {
  echo -e "e[0;33mERROR: The Zero Touch Provisioning script failed while running the command $BASH_COMMAND at line $BASH_LINENO.e[0m" >&2
}
trap error ERR

SSH_URL="http://192.168.200.1/authorized_keys"
# Uncomment to setup SSH key authentication for Ansible
# mkdir -p /home/cumulus/.ssh
# wget -q -O /home/cumulus/.ssh/authorized_keys $SSH_URL

# Uncomment to unexpire and change the default cumulus user password
# passwd -x 99999 cumulus
# echo 'cumulus:Cumu1usLinux!' | chpasswd

# Uncomment to make user cumulus passwordless sudo
# echo "cumulus ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/10_cumulus

# Uncomment to enable all debian sources & netq apps3 repo
# sed -i 's/#deb/deb/g' /etc/apt/sources.list
# wget -q -O pubkey https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey
# apt-key add pubkey
# rm pubkey

# Uncomment to allow NTP to make large steps at service restart
# echo "tinker panic 0" >> /etc/ntp.conf
# systemctl enable ntp@mgmt

exit 0
#CUMULUS-AUTOPROVISIONING
```

### Manage Nodes
Drag and drop servers and switches from the **System Palette** on the right into the workspace.

You can choose your hardware model based on available NVIDIA Spectrum (SNXXXX) switches. This does not affect the simulation but acts as a macro to pre-populate the number of ports per switch model. You don’t need to use each port.

Click on a node to view its **Node Properties**.

- **Name**: Node hostname.
- **Operating System**: OS automatically installed onto the node. No need to boot into ONIE or install it yourself.
- **CPUs**: Number of CPUs. Default 1-2 GB depending on Spectrum switch selected.
- **Memory (GB)**: Amount of RAM. Default 2 GB.
- **Storage (GB)**: Amount of hard disk space. Default 10 GB.
- **Connectors**: Choose an available port to directly connect to any port on another node.
- Make sure to click the **Update Node** button when finished making changes.
- Delete a node with the **Delete Node** button.

There are also various **Advanced Options**, such as enabling **UEFI Secure Boot**.

{{<img src="/images/guides/nvidia-air/AddNode.png" alt="">}}

When you are done creating your topology, click **Workspace > Start Simulation** to start the sim. **You cannot add, remove or edit nodes once the sim is started for the first time.**

{{<img src="/images/guides/nvidia-air/WorkspaceStart.png" alt="" width="200px">}}

### OOB Management Network
On the **System Palette**, there is an option to toggle **Enable OOB**. Toggling this setting enables the out-of-band management network that connects all nodes with each other. It also adds an `oob-mgmt-switch` and `oob-mgmt-server` to your simulation. When you [enable SSH](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Quick-Start/#services)
in your sim, you will SSH into the `oob-mgmt-server`, making this node an ideal start point for configuration. Air handles the configuration automatically for you.

{{<img src="/images/guides/nvidia-air/EnableOOB.png" alt="" width="200px">}}

You can manually add more `oob-mgmt-switches` and `oob-mgmt-servers` to your simulation if you need when this toggle is **off**. But the **Enable OOB** toggle must be enabled to use the OOB network.

## Custom Topologies with DOT Files
Air supports creating custom topologies using DOT files. 

DOT files are the filetype used with the open-source graph visualization software Graphviz. They are simple, text-based files and allow for quick and easy customization. 

You can upload DOT files directly into Air to generate a topology. This allows you to easily share and create copies of a topology and save the topology somewhere in a reusable file. You can modify them in any text editor, like notepad or VS Code.

### DOT Syntax
DOT files use the `.dot` file extention. They define nodes, attributes and connections for generating a topology for a network.

Here is an example of a simple topology DOT file with 1 spine, 2 leaves and 2 servers connected to each leaf.
```
graph "Demo" {
  "spine01" [ function="spine" memory="4096" os="sonic-vs-202305" cpu="2" ]
  "leaf01" [ function="leaf" memory="4096" os="sonic-vs-202305" cpu="2" nic_model="e1000"]
  "leaf02" [ function="leaf" memory="4096" os="sonic-vs-202305" cpu="2" secureboot="true"]
  "server01" [ function="server" memory="2048" os="generic/ubuntu2404" cpu="2"]
  "server02" [ function="server" memory="2048" os="generic/ubuntu2204" cpu="3" storage="20"]
    "leaf01":"eth1" -- "server01":"eth1"
    "leaf02":"eth1" -- "server02":"eth1"
    "leaf01":"eth2" -- "spine01":"eth1"
    "spine01":"eth2" -- "leaf02":"eth2"
}
```
Below are some common use cases for customizing your DOT topology. Air is not limited to accepting only these options. Contact [NVIDIA Networking Support](https://www.nvidia.com/en-us/networking/support/) for more information.

#### Operating System
You can set the OS of the node with the `os` option: 
```
"server" [os="cumulus-vx-5.10.1"]
```

For a list of available operating systems, view the **Operating System** dropdown in the **Node Properties** when using the [drag-and-drop editor](#the-drag-and-drop-topology-builder). 

#### Disk Space
By default, nodes in Air have 10GB of hard disk space. You can give more with the `storage` option, in GB:

```
"server" [os="generic/ubuntu2404" storage="20"]
```

If the node does not recognize the increase in storage, you can perform the following commands in the node to extend the partition and resize the fileystem: 
```
sudo growpart /dev/vda 1
sudo resize2fs /dev/vda1
```

Verify the change was applied:

```
df -h | grep vda1
/dev/vda1        20G  2.1G   18G  11% /
```

#### CPU
You can customize the number of allocated CPUs with the `cpu` option:
```
"server" [os="generic/ubuntu2404" cpu="4"]
```

#### Creating Connections
You can create port connections by defining the node and its port with another.
```
"leaf01":"swp49" -- "leaf02":"swp49"
"leaf01":"swp50" -- "leaf02":"swp50"
```

#### Memory
You can customize the RAM with the `memory` option, in MB: 
```
"server" [os="generic/ubuntu2404"  memory="2048"]
```

### Examples
Labs in the [Demo Marketplace](https://air.nvidia.com/demos) are maintained with external GitLab repositories. Here you can find the `topology.dot` file used to build the lab to reference from. Many demonstrate how to use more options beyond what is listed above.

To access them, click on the **Documentation** button on any lab in the Demo Marketplace. It will lead you to the GitLab repo for the lab. You may have to explore the GitLab a bit to find the `topology.dot` file. 

### Uploading a DOT
To upload a DOT file into Air:
1. Navigate to [air.nvidia.com/simulations](https://air.nvidia.com/simulations). 
2. Click the **Create Simulation** button.
2.	Give your simulation a **Name**.
3.	Select **DOT** as the **Type**.
4.	Drag or select your DOT file to upload.
5. Optionally, assign an Organization to the sim. Read more about them in [Organizations](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Organizations/). 
6. Optionally, add a **ZTP script** to the simulation. You can read more about them in [ZTP Scripts](#ztp-scripts).
     1. Toggle on the **Apply ZTP Template** button.
     2. Enter your ZTP script. A default script is prefilled to help you get started.
7. Optionally, click **Advanced** and provide a **OOB-MGMT-SERVER CONFIG SCRIPT** that executes on the `oob-mgmt-server` when the simulation is started.
8. Click **Create**.

Air will build a custom topology based on the DOT file. 

{{<img src="/images/guides/nvidia-air/CreateADOT.png" alt="">}}

## Import a Topology via API
You can import JSON formatted topologies via API.

{{< tabs "TabID110 ">}}
{{< tab "Example 1">}}

The following topology defines two nodes (`node-1` and `node-2`) connected to each other via their respective `eth1` interfaces, and the Out-of-Band management network enabled by default. 

```
{
    "nodes": {
        "node-1": {
            "os": "generic/ubuntu2204"
        },
        "node-2": {
            "os": "generic/ubuntu2204"
        }
    },
    "links": [
        [{"node": "node-1", "interface": "eth1"}, {"node": "node-2", "interface": "eth1"}]
    ]
}
```

{{< /tab >}}
{{< tab "Example 2">}}

The following topology defines two nodes (`node-1` and `node-2`) connected to each other via their respective `eth1` interfaces, and the Out-of-Band management network disabled (`"oob": false`). The example showcases:
- Custom values for configurable node fields (`cpu`, `memory`, `storage`)
- Public-facing interface (with a custom `mac` address) to the outside world (`eth2` of `node-1`)
- Referencing `os` image by specific UUID (`node-2`)

```
{
    "oob": false,
    "nodes": {
        "node-1": {
            "os": "generic/ubuntu2204",
            "cpu": 2,
            "memory": 2048
        },
        "node-2": {
            "os": "defb3ffc-e29b-4d3a-a5fb-41ed1974f938",
            "memory": 2048,
            "storage": 25
        }
    },
    "links": [
        [{"node": "node-1", "interface": "eth1"}, {"node": "node-2", "interface": "eth1"}],
        [{"node": "node-1", "interface": "eth2", "mac": "02:00:00:00:00:07"}, "exit"]
    ]
}
```

{{< /tab >}}
{{< /tabs >}}

A more detailed schema for this format can be viewed by visiting the [API documentation](https://air.nvidia.com/api/#/v2/v2_simulations_import_create).

{{< expand "Import Instructions" >}}

In order to import a topology, the following API v2 SDK method can be used:

```
from air_sdk.v2 import AirApi

air = AirApi(
    authenticate=True,
    username='<username>',
    password='<password-or-token>',
)
simulation = air.simulations.create_from(
    title='<simulation-name>',
    format='JSON',
    content=<topology-content>,
    organization=<optional-organization>
)
```

{{%notice info%}}
Minimum required SDK version for this feature is `air-sdk>=2.14.0`
{{%/notice%}}

Topology content can be provided in multiple ways:

{{< tabs "TabID111 ">}}
{{< tab "Python Dictionary">}}

```
simulation = air.simulations.create_from(
    'my-simulation',
    'JSON',
    {
        'nodes': {
            'node-1': {
                'os': 'generic/ubuntu2204',
            },
            'node-2': {
                'os': 'generic/ubuntu2204',
            },
        },
        'links': [
            [{'node': 'node-1', 'interface': 'eth1'}, {'node': 'node-2', 'interface': 'eth1'}]
        ]
    },
)
```

{{< /tab >}}
{{< tab "JSON String">}}

```
simulation = air.simulations.create_from(
    'my-simulation',
    'JSON',
    '{"nodes": {"node-1": {"os": "generic/ubuntu2204"}, "node-2": {"os": "generic/ubuntu2204"}}, "links": [[{"node": "node-1", "interface": "eth1"}, {"node": "node-2", "interface": "eth1"}]]}'
)
```

{{< /tab >}}
{{< tab "File Path">}}

```
import pathlib
simulation = air.simulations.create_from(
    'my-simulation',
    'JSON',
    pathlib.Path('/path/to/topology.json')
)
```

{{< /tab >}}
{{< tab "File Descriptor">}}

```
import pathlib
with pathlib.Path('/path/to/topology.json').open('r') as topology_file:
    simulation = air.simulations.create_from(
        'my-simulation',
        'JSON',
        topology_file
    )
```

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

## Export a Topology via API
Existing simulations can be exported into a JSON representation via API. 

A more detailed schema for this format can be viewed by visiting the [API documentation](https://air.nvidia.com/api/#/v2/v2_simulations_export_retrieve).


{{< expand "Export Instructions" >}}

In order to export a simulation, the following API v2 SDK method can be used:

```
from air_sdk.v2 import AirApi

air = AirApi(
    authenticate=True,
    username='<username>',
    password='<password-or-token>',
)
topology = air.simulations.export(
    simulation='<simulation-instance-or-id>',
    format='JSON',
    image_ids=True,  # defaults to False
)
```

{{%notice info%}}
Minimum required SDK version for this feature is `air-sdk>=2.15.0`
{{%/notice%}}

{{< /expand >}}

## Create a Custom Topology from the Production Network

This section describes how to create a simulation based on an existing production deployment.

{{%notice info%}}
These scripts have only been validated in a Linux environment.
{{%/notice%}}

{{< /expand >}}

### Gather cl-support from the Production Network
Use [these playbooks](https://gitlab.com/cumulus-consulting/features/cl_support_ansible) to gather the `cl-support` script output. The `ReadMe` in the repository provides instructions on how to run the playbook to gather the `cl-support` output.

### Create topology.dot from the Production Network
After you obtain the `cl-support` output, you can create a `topology.dot` file with [this script](https://gitlab.com/cumulus-consulting/features/cl_support_lldp_parser)
. You can run the script using `python3`. Here is sample output:

```
$ python3 cl_support_lldp_parser.py
Extracting: /home/cumulus/cl_support_lldp_parser/cl_support_leaf01_20210721_164553.txz
Extracting: /home/cumulus/cl_support_lldp_parser/cl_support_spine02_20210721_164553.txz
Extracting: /home/cumulus/cl_support_lldp_parser/cl_support_leaf02_20210721_164553.txz
Extracting: /home/cumulus/cl_support_lldp_parser/cl_support_spine01_20210721_084129.txz
folder is: /home/cumulus/cl_support_lldp_parser/cl_support_leaf01_20210721_164553
leaf01
    leaf01:eth0 -- oob-mgmt-switch:swp2
    leaf01:swp31 -- spine01:swp1
    leaf01:swp32 -- spine02:swp1
folder is: /home/cumulus/cl_support_lldp_parser/cl_support_spine02_20210721_164553
spine02
    spine02:eth0 -- oob-mgmt-switch:swp6
    spine02:swp1 -- leaf01:swp32
    spine02:swp2 -- leaf02:swp32
folder is: /home/cumulus/cl_support_lldp_parser/cl_support_leaf02_20210721_164553
leaf02
    leaf02:eth0 -- oob-mgmt-switch:swp4
    leaf02:swp31 -- spine01:swp2
    leaf02:swp32 -- spine02:swp2
folder is: /home/cumulus/cl_support_lldp_parser/cl_support_spine01_20210721_084129
spine01
    spine01:eth0 -- oob-mgmt-switch:swp5
    spine01:swp1 -- leaf01:swp31
    spine01:swp2 -- leaf02:swp31
DOTFILE: cl_support_lldp_parser.dot
```

The command writes the output to `cl_support_lldp_parser.dot`. You need to manually edit this file to define the node versions and clean up any superfluous configurations:

```
$ cat cl_support_lldp_parser.dot
graph dc1 {
"leaf01" [function="leaf" ]
"oob-mgmt-switch" [function="leaf" ]
"spine01" [function="leaf" ]
"spine02" [function="leaf" ]
"leaf02" [function="leaf" ]
    "leaf01":"eth0" -- "oob-mgmt-switch":"swp2"
    "leaf01":"swp31" -- "spine01":"swp1"
    "leaf01":"swp32" -- "spine02":"swp1"
    "spine02":"eth0" -- "oob-mgmt-switch":"swp6"
    "spine02":"swp2" -- "leaf02":"swp32"
    "leaf02":"eth0" -- "oob-mgmt-switch":"swp4"
    "leaf02":"swp31" -- "spine01":"swp2"
    "spine01":"eth0" -- "oob-mgmt-switch":"swp5"
}
```
### Restore Configuration Files

After you create the simulation, you can restore the configuration files.

This [python script](https://gitlab.com/cumulus-consulting/features/cl_support_file_extractor)
pulls out all the relevant files and collates them into folders so you can use them to restore configuration from inside the simulation.

You can also use the [infrastructure as code](https://gitlab.com/cumulus-consulting/features/simple-iac)
Ansible playbook to restore configurations.
