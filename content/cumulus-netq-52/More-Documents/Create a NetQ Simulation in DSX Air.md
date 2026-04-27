---
title: Create a NetQ Simulation in DSX Air
author: NVIDIA
weight: 1120
toc: 3
---

{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air-v2/" text="NVIDIA DSX Air">}} is a cloud-hosted, data center simulation platform that behaves like a real-world production environment. Follow the steps in this guide to create a NetQ simulation using DSX Air.

## Prerequisites

To access DSX Air, you need an NGC account and organization. Refer to the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air-v2/Account-Setup" text="NVIDIA DSX Air user guide">}} for more information.

## Create a Switch Topology in Air

1. Navigate to https://dsx-air.nvidia.com/simulations  
1. Click **New Simulation**, enter a name, select **Blank Canvas**, then click **Create**.  
1. A blank canvas appears with a "System Palette" containing switches and servers. Drag and drop switches onto the canvas. Do not use the switch named `oob-mgmt-switch`.  
1. Build your topology by placing switches on the canvas. Click on any switch to configure links between switches.
1. Rename switches (e.g., `SN2100-1`, `SN2201-1`) by clicking each switch.  
1. After you're finished configuring switches and links, enable OOB (out-of-band network) by selecting the toggle under your username.
1. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> **Export Simulation** to download the topology as a JSON file.  


## Add the NetQ Server to the JSON File

1. Open the downloaded JSON file in a text editor.  
2. Add the following block at the end of the `Nodes` array, then save the file:

```
"netq-master": {
  "memory": 65536,
  "cpu": 16,
  "storage": 500,
  "os": "netq-5.2.0",
  "cpu_mode": "host-passthrough"
}
```
3. If a newer NetQ image is available, update the `os` value accordingly.


## Create the Simulation Using the Updated JSON

1. Click **New Simulation** and enter a name.  
2. Select **JSON** as the simulation type and upload the JSON file you created in the previous section.  
3. Enable **Apply ZTP Template**. Delete the contents and replace them with `ZTPScript.sh`. The ZTP script sets the OOB management server IP address to `192.168.200.1` and updates the default switch password from `cumulus` to `netq_123`:
{{<expand "ZTPScript.sh">}}
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
mkdir -p /home/cumulus/.ssh
wget -O /home/cumulus/.ssh/authorized_keys $SSH_URL

# Uncomment to unexpire and change the default cumulus user password
passwd -x 99999 cumulus
echo 'cumulus:netq_123' | chpasswd

# Uncomment to make user cumulus passwordless sudo
echo "cumulus ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/10_cumulus

# Uncomment to enable all debian sources & netq apps3 repo
sed -i 's/#deb/deb/g' /etc/apt/sources.list
wget -O pubkey https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey
apt-key add pubkey
rm pubkey

# Uncomment to allow NTP to make large steps at service restart
echo "tinker panic 0" >> /etc/ntp.conf
systemctl enable ntp@mgmt

exit 0
#CUMULUS-AUTOPROVISIONING
```
{{</expand>}}

4. Click **Create**. After the simulation is loaded, select the play button to start the simulation.

5. It can take up to a minute to load the simulation. After the simulation is loaded, refresh the page to view it. You can drag the nodes using your mouse to reposition them.

After the ZTP script runs on all switches and NetQ fully boots, configure the NetQ agents and load the UI, as described in the next section.

## Configure NetQ Agents and Expose the NetQ UI

### Verify NetQ Services

1. Select the `netq-master` node to open the node's terminal.  
2. Log in and update credentials when prompted:
   - Username: `nvidia`  
   - Password: `nvidia`  

3. Verify all NetQ pods are running:

```
kubectl get pods -A
```

### Configure Switch Agents

1. Click each switch node and log in using the password configured by the ZTP script, `netq_123`.

2. Run the following command on each switch to point the NetQ agent to the `netq-master` server:

```
netq config add agent server netq-master port 31980 vrf mgmt && netq config restart agent
```

### Configure OOB Management Server and Create NetQ UI Service

1. Click the `OOB-mgmt-server` node and change the default credentials:
   - Username: `ubuntu`  
   - Password: `nvidia`  

2. Run the following command on the OOB management server to configure port forwarding:

```
IP=$(getent hosts netq-master | awk '{print $1}') && sudo iptables -t nat -A PREROUTING -p tcp -m tcp --dport 444 -j DNAT --to-destination $IP:443
```

4. Create a service to expose the NetQ UI:
   - Navigate to the **Services** tab  
   - Click **New Service**  
   - Provide the following values:
     - Name: `netq-ui`  
     - Interface: `oob-mgmt-server:eth0`  
     - Service Type: `HTTPS`  
     - Service Port: `444`  

5. Refresh the page to see the new service.  

## Access the NetQ UI

1. Open a browser and navigate to `https://<external-host>:<external-port>/`. The external host and port values are located on the *Services* page.  

3. Log in using the default credentials:
   - Username: `admin`  
   - Password: `admin`  

