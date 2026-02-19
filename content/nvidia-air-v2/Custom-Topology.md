---
title: Custom Topology
author: NVIDIA
weight: 40
product: NVIDIA Air 2.0
---
## The Drag-and-Drop Topology Builder

One way to create custom simulations is with the built-in topology builder, which provides a drag-and-drop editor to design any custom network. To get started, navigate to [https://air-ngc.nvidia.com/simulations](https://air-ngc.nvidia.com/simulations).

1. Select **Create Simulation**.
2. Provide a name for your simulation.
3. Select **Blank Canvas** as the type.
4. (Optional) Add a [ZTP script](#ztp-scripts) to the simulation:
   1. Select **Apply ZTP Template**.
   2. Enter your ZTP script. A default script is prefilled to help get you started.
5. Click **Create**.

{{<img src="/images/guides/nvidia-air-v2/CreateSimulation.png" alt="" width="800px">}}

### ZTP Scripts

When you create a new simulation, Air gives you the option to add a zero-touch provisioning (ZTP) script. The ZTP script is copied to the simulation's `oob-mgmt-server`. Any node making a ZTP request on the out-of-band management network has access to this ZTP script through a DHCP server and web server running on the `oob-mgmt-server`.

{{%notice note%}}
You must have the out-of-band-network enabled to use ZTP scripts.
{{%/notice%}}

A default script is prefilled to help you get started. It implements common ZTP features on Cumulus Linux, such as changing the default password or downloading SSH keys. You can edit the default script directly in the UI.

{{< expand "Default ZTP script" >}}
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
{{< /expand >}}

### Manage Nodes

You can drag servers and switches from the **System Palette** to the workspace. Air provides access to hardware models based on available NVIDIA Spectrum switches. The model does not affect the simulation, but allows Air to pre-populate the number of ports based on the switch model. You do not need to use each port.

Select a node to view or edit its properties.
- **Name**: Node hostname.
- **Operating System**: Name of the OS installed on the node. The OS is installed automatically.
- **CPUs**: Number of CPUs. The default is 1 or 2 GB depending on the Spectrum switch.
- **Memory (GB)**: Amount of RAM (default is 2 GB).
- **Storage (GB)**: Amount of hard disk space (default is 10 GB).
- **Connectors**: Choose an available port to connect directly to any port on another node.

Make sure to select **Update Node** when you complete the changes. You can delete nodes by selecting **Delete Node**.

Air also provides advanced options, such as enabling UEFI secure boot.

{{<img src="/images/guides/nvidia-air-v2/AddNode.png" alt="">}}
<br>
<br>
After you create your topology, start the simulation. You cannot add, remove, or edit nodes after the simulation starts for the first time.

### Breakout Ports

For switch nodes, you can break out a port into multiple sub-ports to simulate multi-lane configurations. For example, breaking out `swp1` into four sub-ports creates `swp1s0`, `swp1s1`, `swp1s2`, and `swp1s3`.

To break out a port:

1. Select a switch node to open its properties panel.
2. In the **Connectors** section, click **Breakout Port**.
3. Select the ports you want to break out.
4. Choose the split type (number of sub-ports) and click **Confirm**.

{{<img src="/images/guides/nvidia-air-v2/BreakoutPorts.png" alt="Breakout Port dialog showing port selection and split type">}}

The available split options depend on the switch model. To revert a breakout, select **Delete Breakout** in the Breakout Port dialog.

{{%notice note%}}
Breakout ports can only be configured before the simulation starts for the first time. Only data plane interfaces on switch nodes support breakout — management and OOB interfaces do not.
{{%/notice%}}

### Outbound Links

Outbound links connect a node's interface directly to external networks, giving that interface internet access independently of the OOB management network. This is useful when you need a node to have a public-facing interface — for example, to simulate an edge router or a firewall with an external uplink.

To configure an outbound link:

1. Select a node to open its properties panel.
2. In the **Connectors** section, click the port you want to connect externally.
3. In the Connect dialog, toggle **Outbound link** on.

{{<img src="/images/guides/nvidia-air-v2/OutboundLink.png" alt="Connect dialog showing outbound link toggle">}}

Outbound interfaces appear in the **Services** tab, where you can create services (such as SSH or HTTP) that terminate on the outbound interface.

{{%notice note%}}
An outbound interface connects directly to the external network. It cannot also be connected to another node's interface.
{{%/notice%}}

### OOB Management Network

On the **System Palette**, there is an option to **Enable OOB**. This setting enables the out-of-band management network that connects all nodes to each other. It also adds an `oob-mgmt-switch` and `oob-mgmt-server` to your simulation. When you enable SSH, you connect to the `oob-mgmt-server`, making this node an ideal starting point for configurations. Air handles the configuration automatically for you.

{{<img src="/images/guides/nvidia-air-v2/EnableOOB.png" alt="System Palette showing OOB and NetQ toggles" width="400px">}}
<br>
<br>
You can add more `oob-mgmt-switches` and `oob-mgmt-servers` to your simulation manually even when **Enable OOB** is set to off. However, you must switch **Enable OOB** on to use the out-of-band network.

## Importing Custom Topologies with External Files
You can create custom topologies in Air by importing either JSON (recommended) or DOT files. These files define a network's nodes, attributes, and connections. You can modify the file with any text editor.

When you upload external topology files directly to Air, you can: 

- Share and create copies of a topology
- Save the topology in a reusable file
- Streamline automation
- Generate very large topologies

### JSON
The following JSON topology is an example of a simple topology with 1 spine, 2 leaf nodes, and 2 servers connected to each leaf. 

{{< expand "View Sample JSON Topology" >}}

```
{
    "format": "JSON",
    "title": "Demo",
    "ztp": null,
    "content": {
        "nodes": {
            "leaf01": {
                "cpu": 2,
                "memory": 4096,
                "storage": 10,
                "os": "sonic-vs-202305",
                "features": {
                    "uefi": false,
                    "tpm": false
                },
                "pxehost": false,
                "secureboot": false,
                "oob": false,
                "emulation_type": null,
                "network_pci": {},
                "management_mac": "00:00:00:00:00:00"
            },
            "leaf02": {
                "cpu": 2,
                "memory": 4096,
                "storage": 10,
                "os": "sonic-vs-202305",
                "features": {
                    "uefi": false,
                    "tpm": false
                },
                "pxehost": false,
                "secureboot": false,
                "oob": false,
                "emulation_type": null,
                "network_pci": {},
                "management_mac": "00:00:00:00:00:00"
            },
            "server01": {
                "cpu": 2,
                "memory": 2048,
                "storage": 10,
                "os": "generic/ubuntu2404",
                "features": {
                    "uefi": false,
                    "tpm": false
                },
                "pxehost": false,
                "secureboot": false,
                "oob": false,
                "emulation_type": null,
                "network_pci": {},
                "management_mac": "00:00:00:00:00:00"
            },
            "server02": {
                "cpu": 2,
                "memory": 2048,
                "storage": 10,
                "os": "generic/ubuntu2404",
                "features": {
                    "uefi": false,
                    "tpm": false
                },
                "pxehost": false,
                "secureboot": false,
                "oob": false,
                "emulation_type": null,
                "network_pci": {},
                "management_mac": "00:00:00:00:00:00"
            },
            "spine01": {
                "cpu": 2,
                "memory": 4096,
                "storage": 10,
                "os": "sonic-vs-202305",
                "features": {
                    "uefi": false,
                    "tpm": false
                },
                "pxehost": false,
                "secureboot": false,
                "oob": false,
                "emulation_type": null,
                "network_pci": {},
                "management_mac": "00:00:00:00:00:00"
            }
        },
        "links": [
            [
                {
                    "interface": "eth1",
                    "node": "leaf01"
                },
                {
                    "interface": "eth1",
                    "node": "server01"
                }
            ],
            [
                {
                    "interface": "eth2",
                    "node": "leaf01"
                },
                {
                    "interface": "eth1",
                    "node": "spine01"
                }
            ],
            [
                {
                    "interface": "eth1",
                    "node": "leaf02"
                },
                {
                    "interface": "eth1",
                    "node": "server02"
                }
            ],
            [
                {
                    "interface": "eth2",
                    "node": "leaf02"
                },
                {
                    "interface": "eth2",
                    "node": "spine01"
                }
            ]
        ]
    }
}
```
{{< /expand >}}

<br>

When you view the nodes within Air after starting the simulation, notice that the resources are allocated according to the file:

{{<img src="/images/guides/nvidia-air-v2/JSONNodesExample.png" alt="">}}
<br>
<br>
When you view the links within Air after starting the simulation, notice that the nodes are connected based on the file, and also connected to the out-of-band management network: 

{{<img src="/images/guides/nvidia-air-v2/JSONLinksExample.png" alt="">}}

{{%notice note%}}
If you omit the `oob` key in your JSON file, the **Enable OOB** will still be set to **on** after you've uploaded your file with default resources and will be automatically connected to each node.
{{%/notice%}}

#### Custom OOB Management Network Resources

You can specify an `oob-mgmt-switch` and `oob-mgmt-server` to customize allocated resources.

{{< expand "View Custom OOB Network Example" >}}

```
{
    "format": "JSON",
    "title": "Demo",
    "ztp": null,
    "content": {
        "nodes": {
           ...
        },
        "links": [
            ...
        ],
        "oob": {
            "nodes": {
                "oob-mgmt-server": {
                    "cpu": 3,
                    "memory": 3072,
                    "storage": 21
                    
                },
                "oob-mgmt-switch": {
                    "cpu": 2,
                    "memory": 4096,
                    "storage": 20
                }
            }
        }
    }
}
```
{{< /expand >}}
<br>
When viewing the nodes within Air after starting the simulation, notice that the resources are allocated based on the file: 

{{<img src="/images/guides/nvidia-air-v2/JSONOOBExample.png" alt="">}}

#### Custom NetQ Node
You can create and customize a NetQ instance for your simulation.

{{< expand "View Custom NetQ Node Example" >}}

```
{
    "format": "JSON",
    "title": "Demo",
    "ztp": null,
    "content": {
        "nodes": {
           ...
        },
        "links": [
            ...
        ],
        "oob": {
            ...
        },
         "netq": {
            "nodes": {
                "netq-ts": {
                    "cpu": 4,
                    "memory": 6144,
                    "storage": 64,
                    "os": "netq-ts-cloud-4.12.0"
                }
            }
        }
    }
}
```
{{< /expand >}}
<br>
When viewing the nodes within Air, notice that the resources are allocated based on the file. 

{{<img src="/images/guides/nvidia-air-v2/JSONNetQExample.png" alt="">}}

### DOT

You can also create custom topologies in Air using a DOT file, which is the file type used with the open-source graph visualization software, Graphviz. DOT files are simple, customizable, text-based files. DOT files use the `.dot` file extension.

{{%notice info%}}
NVIDIA strongly recommends using JSON over DOT files due to improved validation, scalability, and broader adoption levels. 
{{%/notice%}}

The following is an example of a simple topology with 1 spine, 2 leaf nodes, and 2 servers connected to each leaf.

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

The following sections provide examples for common DOT file customizations.

#### Operating System

You can set the operating system of the node with the `os` option:

```
"server" [os="cumulus-vx-5.10.1"]
```

#### Disk Space

By default, nodes in Air have 10 GB of hard disk space. You can increase the space (in GB) by using the `storage` option:

```
"server" [os="generic/ubuntu2404" storage="20"]
```

#### CPU

You can customize the number of allocated CPUs with the `cpu` option:

```
"server" [os="generic/ubuntu2404" cpu="4"]
```

#### Create Connections

You can create port connections by defining the node and its port with another node and port.

```
"leaf01":"swp49" -- "leaf02":"swp49"
"leaf01":"swp50" -- "leaf02":"swp50"
```

#### Memory

You can customize RAM (in MB) with the `memory` option:

```
"server" [os="generic/ubuntu2404"  memory="2048"]
```

### Examples

Labs in the [Demo Marketplace](https://air-ngc.nvidia.com/demos) are maintained with external GitLab repositories. Here you can find the `topology.dot` or `topology.json` file used to build the lab and use it as a reference. To access the files, select **Documentation** on any lab in the Demo Marketplace. It will direct you to the demo's GitLab repository, where you can download the file used for the demo topology.

You can also launch a copy of a lab in the Demo Marketplace and then export the JSON file.

### Import a Topology

To import and upload a DOT or JSON topology file to Air, navigate to [air-ngc.nvidia.com/simulations](https://air-ngc.nvidia.com/simulations).

1. Click **Create Simulation**.
2. Provide a name for the simulation.
3. Select your desired filetype.
4. Upload the file to the UI.
5. (Optional) Add a [ZTP script](#ztp-scripts). Alternately, you can apply a ZTP script within the file.
     1. Select **Apply ZTP Template**.
     2. Enter your ZTP script. A default script is prefilled to help you get started.
6. (Optional) Click **Advanced** and provide an out-of-band management server configuration script that executes on the `oob-mgmt-server` when the simulation starts.
7. Click **Create**.

{{<img src="/images/guides/nvidia-air-v2/ImportJSON.png" alt="" >}}
<br>
<br>
Air redirects you to the [topology builder](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Custom-Topology/#the-drag-and-drop-topology-builder) with your custom topology created. You can continue to make adjustments as necessary.

### Export a Topology
You can export the topology for any existing simulation as a JSON file. From the **Topology** tab, click the **Export** icon in the toolbar to download the topology file. 

### Storage Limits

If you increase the storage of a node higher than its default, and Air does not recognize the increased storage, run the following commands **on the affected node** (not the `oob-mgmt-server`) to extend the partition and resize the file system:

```
sudo growpart /dev/vda 1
sudo resize2fs /dev/vda1
```

Verify the change:

```
df -h | grep vda1
/dev/vda1        20G  2.1G   18G  11% /
```

## Import a Topology with the API

You can import JSON formatted topologies through the API.

{{< tabs "TabID110 ">}}
{{< tab "Example 1">}}

The following topology defines two nodes (`node-1` and `node-2`) connected to each other through `eth1` interfaces. The out-of-band management network is enabled by default.

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

The following topology defines two nodes (`node-1` and `node-2`) connected to each other through `eth1` interfaces. The out-of-band management network is disabled (`"oob": false`). The example includes:
- Custom values for configurable node fields (`cpu`, `memory`, `storage`)
- An outbound link (`eth2` of `node-1`) that connects directly to external networks. In the links array, use the string `"outbound"` as the second element instead of a node reference.
- A reference to the `os` image by specific UUID (`node-2`)

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
        [{"node": "node-1", "interface": "eth2", "mac": "02:00:00:00:00:07"}, "outbound"]
    ]
}
```

{{%notice note%}}
The string `"exit"` is also accepted as an alias for `"outbound"` in the links array.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

For additional schemas, refer to the [API documentation](https://air-ngc.nvidia.com/api/#/Simulations/api_v3_simulations_import_create).

## Export a Topology through the API

You can export existing simulations into a JSON representation using the API. Refer to the [API documentation](https://air-ngc.nvidia.com/api/#/Simulations/api_v3_simulations_export_retrieve) for additional schema details.
