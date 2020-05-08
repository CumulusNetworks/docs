---
title: User Guide
author: Cumulus Networks
weight: 30
product: Cumulus Networks Guides
version: "1.0"
draft: true
---
This section discusses how you can run a Cumulus Production Ready automation, unchanged and unmodified on your own system in your enterprise. You can test, learn, and experience Cumulus Linux driven by best practice Ansible automation, and test drive our officially supported golden standard configurations and architectures by running the production ready automation as-is and unmodified.

For more details about how to customize, reuse and adapt these examples of simulation, automation or CI/CD for your own purposes, refer to the {{<link url="Integration-Guide" text="Integration Guide">}}.

## System Requirements

For a robust simulation environment and CI/CD with gitlab, a dedicated, always-on, enterprise class server is recommended. Using the NetQ server in individual development environments is not normally required and is normally only needed for CI testing where the gitlab-runner is installed and registered to your CI/CD enabled project.

### Hardware Requirements

- A Minimum of 16GB RAM (without NetQ) - 32GB Ram recommended
- A Minimum 256GB disk - more than 1TB disk recommended
- SSD recommended (NetQ requirement)
- Internet connectivity for package installs during simulation start up
- A minimum of eight CPU Cores
- 15104MB of memory *without* NetQ or 23296MB of memory *with* NetQ

### Software Requirements

- Operating systems:
    - Cumulus Linux 3.7.11 or later
    - Cumulus NetQ 2.4 or later (optional)
    - Ubuntu 16.04 or 18.04 (Cumulus Networks has *not* tested other Linux distributions, such as CentOS or RHEL)
- Software packages:
    - Vagrant 2.2.4 or later
    - Libvirt
    - Qemu
    - Git
- Vagrant plugins:
    - Vagrant-libvirt
    - Vagrant-scp

Refer to the {{<link title="Example Install Scripts" text="Example Install Scripts">}} for an example bash script that installs these package dependencies to be able to support Cumulus VX simulation with Vagrant and libvirt.

## Manually Start A Golden Standard Topology

The {{<link url="Quick-Start" text="Quick Start section">}} provides the easiest way to start a Production Ready automation demo after preparing the system using the bash script provided. However, if you want more control over which nodes start and in which order, you can launch the simulation manually. This method saves CPU and memory resources.

To manually start a demo topology, such as {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym" text="EVPN Symmetric Mode">}}, ensure that you also fetch and pull down the included Cumulus Linux base Reference Topology. You can do this in one of two ways:

- Use the `--recurse-submodule` option with the initial `git clone`. This option also fetches the submodule files in the same step as the clone. We use this option in the procedure below.
- Perform a normal git clone, then fetch the submodule files separately with the `git submodule init` and `git submodule update` options. For more information about git submodules, see {{<exlink url="https://git-scm.com/book/en/v2/Git-Tools-Submodules" text="this guide">}}.

When the cldemo2 submodule files are properly downloaded, the cldemo2 folder will contain a subfolder named `simulation`. This `simulation` folder contains the Vagrantfile. Using `vagrant` commands like `vagrant ssh oob-mgmt-server` are only valid when issued from the same directory as the simulation’s Vagrantfile.

Download a golden standard automation demo such as EVPN Symmetric Mode. Use the `--recurse-submodule` option to make sure git also fetches the base Cumulus Linux Reference Topology simulation files.

```
user@host:~# git clone --recurse-submodules https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym.git
Cloning into 'dc_configs_vxlan_evpnsym'...
remote: Enumerating objects: 535, done.
remote: Counting objects: 100% (535/535), done.
remote: Compressing objects: 100% (300/300), done.
remote: Total 535 (delta 198), reused 465 (delta 133), pack-reused 0
Receiving objects: 100% (535/535), 66.78 KiB | 1.45 MiB/s, done.
Resolving deltas: 100% (198/198), done.
Submodule 'cldemo2' (https://gitlab.com/cumulus-consulting/goldenturtle/cldemo2.git) registered for path 'cldemo2'
Cloning into '/root/dc_configs_vxlan_evpnsym/cldemo2'...
remote: Enumerating objects: 215, done.
remote: Counting objects: 100% (215/215), done.
remote: Compressing objects: 100% (119/119), done.
remote: Total 852 (delta 139), reused 156 (delta 96), pack-reused 637
Receiving objects: 100% (852/852), 7.64 MiB | 8.21 MiB/s, done.
Resolving deltas: 100% (549/549), done.
Submodule path 'cldemo2': checked out '214c8a66e3fef8f6d5d2b1e13ca3942e4cfd120f'
```

Change into the folder created by the previous step, and into the `cldemo2/simulation` subfolder. This is the directory where the Vagrantfile is present and where vagrant commands are valid for this simulation

```
user@host:~# cd dc_configs_vxlan_evpnsym/cldemo2/simulation/
user@host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation# 
```

Perform a `vagrant up` for the out of band management devices. Omit the netq-ts if you do not intend on using it to save CPU and Memory resource consumption.

{{%notice info%}}

You must bring up the OOB Server and OOB Switch first. The OOB Server acts as the management network DHCP server. If the OOB Server and Switch are not online first, the management interfaces of the other network devices will be temporarily unreachable.

{{%/notice%}}

```
user@host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation# vagrant up oob-mgmt-server oob-mgmt-switch netq-ts
Bringing machine 'oob-mgmt-server' up with 'libvirt' provider...
Bringing machine 'oob-mgmt-switch' up with 'libvirt' provider...
Bringing machine 'netq-ts' up with 'libvirt' provider...
==> oob-mgmt-server: Checking if box 'generic/ubuntu1804' version '2.0.6' is up to date...
==> oob-mgmt-switch: Checking if box 'CumulusCommunity/cumulus-vx' version '3.7.11' is up to date...
==> netq-ts: Checking if box 'generic/ubuntu1804' version '2.0.6' is up to date...
<output omitted for brevity>
```

Perform a `vagrant up` to bring up the other network devices in any manner you wish. It is possible to bring up all of the rest of the nodes in the simulation with simply issuing a `vagrant up` with no devices specified. Vagrant for libvirt tries to start devices in parallel (start all at the same time). Occasionally, launching an entire Reference Topology Simulation in parallel can cause errors to occur that may result in a partial or incomplete bringup. It is recommended to break up the simulation bring up into smaller more manageable groups, to still be able to realize the speed benefits of parallelism and reduce the chances of errors during bringup.

In this example below, the bringup is split into 4 separate stages. Each stage separated by `&&` will be executed alone. The example below combines those serialized stages in one line. 

{{%notice tip%}}

The `&&` operator in Linux will only execute the next command if the previous command was successful. This will stop the bringup of the simulation if an error occurs.

{{%/notice%}}

```
user@host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation# vagrant up /leaf/ /spine/ && vagrant up server01 server02 server03 server04 && vagrant up server05 server06 server07 server08 && vagrant up border01 border02 fw1 fw2
```

Enter the simulation via the oob-mgmt-server by performing a `vagrant ssh oob-mgmt-server`

```
user@host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation# vagrant ssh oob-mgmt-server
                                                 _
      _______   x x x                           | |
 ._  <_______~ x X x   ___ _   _ _ __ ___  _   _| |_   _ ___
(' \  ,' || `,        / __| | | | '_ ` _ \| | | | | | | / __|
 `._:^   ||   :>     | (__| |_| | | | | | | |_| | | |_| \__ \
     ^T~~~~~~T'       \___|\__,_|_| |_| |_|\__,_|_|\__,_|___/
     ~"     ~"


############################################################################
#
#         Out Of Band Management Server (oob-mgmt-server)
#
############################################################################
vagrant@oob-mgmt-server:~$
```

Perform another `git clone` from your target golden standard demo project (refer to step 1) once inside the simulation to fetch the automation files. Alternatively, `vagrant scp` can be used to copy the automation files into the simulation.

```
vagrant@oob-mgmt-server:~$ git clone https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym
Cloning into 'dc_configs_vxlan_evpnsym'...
warning: redirecting to https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym.git/
remote: Enumerating objects: 560, done.
remote: Counting objects: 100% (560/560), done.
remote: Compressing objects: 100% (310/310), done.
remote: Total 560 (delta 214), reused 490 (delta 148), pack-reused 0
Receiving objects: 100% (560/560), 70.27 KiB | 3.90 MiB/s, done.
Resolving deltas: 100% (214/214), done.
vagrant@oob-mgmt-server:~$
```

Change into the project folder and into the automation subfolder

```
vagrant@oob-mgmt-server:~$ cd dc_configs_vxlan_evpnsym/automation/
vagrant@oob-mgmt-server:~/dc_configs_vxlan_evpnsym/automation$
```

Run the deploy.yml playbook and specify the inventory path with the `-i` option

```
vagrant@oob-mgmt-server:~/dc_configs_vxlan_evpnsym/automation$ ansible-playbook playbooks/deploy.yml -i inventories/pod1 --diff

PLAY [spine leaf border] ****************************************************************


TASK [Gathering Facts] ****************************************************************
Sunday 12 April 2020  23:35:25 +0000 (0:00:00.073)       0:00:00.073 ********** 
ok: [spine03]
ok: [spine04]
ok: [spine02]
ok: [spine01]
ok: [leaf01]
ok: [leaf02]
ok: [leaf03]
ok: [leaf04]
ok: [border02]
ok: [border01]
<output omitted for brevity>
```

You now have a deployed and operational golden standard Cumulus architecture. For more details about the specific network topology, it’s IP addressing and how to interact with the features in demonstration, visit the demo project page for the `README.md`.

## Automatically Launch Production Ready Automation on Cumulus in the Cloud

This method is the easiest way to experience the final product of the Cumulus golden standard EVPN VXLAN demo configurations. This method is best suited to fast track all of the simulation setup and provisioning and get to testing any of the official golden standard EVPN VXLAN demo configurations.

If you are interested in taking a closer look at the processes of automation, deployment and see the actual examples of the infrastructure as code, you’ll want to manually clone the demo project and manually run the automation playbook to render the config as code into the network devices. This automated process clones your selected demo repo and runs the Ansible deployment playbook for you with a few easy and convenient clicks from the Cumulus In the Cloud UI.

1. Go to http://cumulusnetworks.com/citc to request a demo or to reach your existing simulation.
2. After you reach your simulation console, choose a demo from the drop down menu on the left panel

    {{<img src="/images/guides/citc-interface-demo.png" >}}

3. Click the “Run Now" button
4. Follow the instructions on the `Guided Tour` panel to test and experience the unique aspects of your selected demo.

## Manually Launch Automation Demo Topology From Cumulus In the Cloud

[Cumulus in the Cloud](https://www.cumulusnetworks.com/citc) provides the fastest way to enjoy the experience of provisioning a full datacenter using best practice Ansible automation and see a working example of infrastructure as code. By removing the complexity of the simulation hardware and software dependencies, users can be in the driver’s seat of a fully provisioned data center to test the automation experience and any of the demo solution architectures in minutes. Cumulus in the cloud also includes a free temporary NetQ Cloud account to showcase NetQ’s features with live data from your simulation.

1. Start from the `oob-mgmt-server` on your cumulus in the cloud simulation. Use an SSH client to connect for the best experience. Find the SSH client connection information from the “Services" window in the UI.

    {{<img src="/images/guides/citc-interface-services.png" >}}

2. Perform a `git clone` from your target golden standard demo project. 

    ```
    vagrant@oob-mgmt-server:~$ git clone https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym
    Cloning into 'dc_configs_vxlan_evpnsym'...
    warning: redirecting to https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym.git/
    remote: Enumerating objects: 560, done.
    remote: Counting objects: 100% (560/560), done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 560 (delta 214), reused 490 (delta 148), pack-reused 0
    Receiving objects: 100% (560/560), 70.27 KiB | 3.90 MiB/s, done.
    Resolving deltas: 100% (214/214), done.
    vagrant@oob-mgmt-server:~$
    ```

3. Change into the project folder and into the automation subfolder

    ```
    vagrant@oob-mgmt-server:~$ cd dc_configs_vxlan_evpnsym/automation/
    vagrant@oob-mgmt-server:~/dc_configs_vxlan_evpnsym/automation$ 
    ```

4. Run the deploy.yml playbook. Include the `-i` option as specified below.

    ```
    vagrant@oob-mgmt-server:~/dc_configs_vxlan_evpnsym/automation$ ansible-playbook playbooks/deploy.yml -i inventories/pod1 --diff

    PLAY [spine leaf border] ****************************************************************

    TASK [Gathering Facts] ****************************************************************
    Sunday 12 April 2020  23:35:25 +0000 (0:00:00.073)       0:00:00.073 ********** 
    ok: [spine03]
    ok: [spine04]
    ok: [spine02]
    ok: [spine01]
    ok: [leaf01]
    ok: [leaf02]
    ok: [leaf03]
    ok: [leaf04]
    ok: [border02]
    ok: [border01]
    <output omitted for brevity>
    ```

At this stage you now have a deployed and operational golden standard Cumulus architecture. Visit the demo project page for the `README.md` for more details about the specific network topology, it’s IP addressing and how to interact with the features in demonstration.

## Install and Configure the NetQ Cloud Server

The Cumulus Linux reference topology includes an Ubuntu 18.04 server with additional CPU, memory and disk resources added to support a NetQ Cloud Server installation. Vagrant provisions this box with all of the required software package dependencies to be able to skip immediately to the bootstrap and install steps of the NetQ server setup documented [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-Platform/Prepare-Existing-NetQ-Appliance/) starting at the section “Download the bootstrap and NetQ installation tarballs."

To use the included NetQ Cloud server, you must have a few prerequisites satisfied:

- An active NetQ Cloud account with netq.cumulusnetworks.com
- An additional site/premises setup and provisioned that is dedicated for virtualization use. This amounts to a unique NetQ configuration key for your simulation environment. Do not mix a simulation topology with an existing site or use an existing and in-use NetQ premises config-key.
- The NetQ bootstrap tarball downloaded from cumulusnetworks.com
- The NetQ OPTA install tarball downloaded from cumulusnetworks.com

{{%notice info%}}

The `NetQ bootstrap` and `NetQ OPTA install` tarballs are two unique files.

{{%/notice%}}

### Stage the NetQ Installation Tarballs

The NetQ application and version is driven by the version of the bootstrap and install files that are used to install the NetQ application on the provided Ubuntu server. The installation procedure uses the NetQ agent that is preinstalled on the netq-ts box. You must stage the NetQ bootstrap and install tarball files that are downloaded from cumulusnetworks.com for the NetQ installation procedure.

You can stage the installation tarballs in either one of two locations relative to the netq-ts box:

1. On the local filesystem of the netq-ts itself. The bootstrap and installation tarballs must be copied onto the netq-ts box after the simulation has been started from `vagrant up`. This is typically accomplished using SCP or `vagrant scp`

2. On a remote HTTP server reachable by the netq-ts. The bootstrap and installation tarballs are placed onto an HTTP server and an HTTP url is provided during the bootstrap and installation procedures.

    You must decide whether to stage the installation tarball files directly onto the server for installation, or host them on a remote http server that the netq-ts can reach.

    The installation tarball files when they are downloaded from cumulusnetworks.com are named:

    - `netq-bootstrap-X.Y.Z.tgz` (bootstrap tarball)
    - `NetQ-X.Y.Z-opta.tgz` (install tarball)

    {{%notice info%}}

The `netq-bootstrap` and `netq-opta` image X.Y.Z version numbers must match.

{{%/notice%}}

### Stage from the Local Filesystem

Specific steps on how to login to cumulusnetworks.com and download the NetQ files can be found [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-Platform/Prepare-Existing-NetQ-Appliance/) starting at the section “Download the bootstrap and NetQ installation tarballs." Specific steps on how to copy the tarballs onto the simulation host are out of scope of this tutorial and the choice of the reader. Normally SCP is used to securely copy the files onto the Linux based simulation host.

In this procedure, we will copy the installation tarball files to the directory `/mnt/installables` although any directory that has sufficient read permissions will be suitable for staging these files. Repeat the following steps for each file:

1. Download the two required installation files from cumulusnetworks.com.
    - Bootstrap
    - Appliance (Cloud)

2. Move/copy the files onto the simulation host. SCP is most commonly used to push files onto the Linux based simulation host.

3. Use `vagrant scp` to copy the file from the simulation host into the simulation on the netq-ts. The `vagrant scp` plugin uses `vagrant ssh`, and therefore will be subject to the permissions of the user account `vagrant`. Copy files into the netq-ts into a path that the user `vagrant` has permissions, such as `/home/cumulus/`

4. Ensure that you issue the `vagrant scp` command from inside the `simulation` folder, colocated to the `Vagrantfile` for the simulation.

    ```
    user@simulation-host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation# vagrant scp /path/to/local/file/netq-boostrap-X.Y.Z.tgz netq-ts:/home/cumulus

    user@simulation-host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation# vagrant scp /path/to/local/file/NetQ-X.Y.Z-opta.tgz netq-ts:/home/cumulus
    ```

5. Vagrant ssh into the netq-ts and move the files to the `/mnt/installables` directory
    ```
    user@host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation# vagrant ssh netq-ts
    vagrant@netq-ts:~$
    vagrant@netq-ts:~$ sudo mv /home/cumulus/netq-boostrap-X.Y.Z.tgz /mnt/installables/
    vagrant@netq-ts:~$ sudo mv /home/cumulus/NetQ-X.Y.Z.tgz /mnt/installables/
    ```

### Stage from a Remote HTTP Server

Specific steps on how to login to cumulusnetworks.com and download the NetQ files can be found [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-Platform/Prepare-Existing-NetQ-Appliance/) starting at the section “Download the bootstrap and NetQ installation tarballs." Specific steps on how to copy the tarballs onto a remote HTTP server will vary depending on the specific http server software. This is an example procedure to setup an http server with Apache on a Debian or Ubuntu based Linux machine.

1. Download the two required installation files from cumulusnetworks.com.
    - Bootstrap
    - Appliance (Cloud)
2. Install apache2.
3. Confirm services are running.
4. Copy tarball files to the `/var/www/html` directory with permissions.
5. Derive http staging URLs for the next steps.

### Install the NetQ Application

This step sets up the NetQ Cloud server. This process installs the NetQ Cloud server application to be able to receive and aggregate agent data and securely transport it to the cloud associated with your account.

- You must have the bootstrap and install tarball files staged in either the local filesystem on the netq-ts or a remote http server accessible from the netq-ts. See the {{<link text="previous section" title="#Staging the NetQ installation tarballs on the netq-ts" >}} for instructions.
- Your NetQ config-key associated with the NetQ site/premises this simulation will occupy. This is received from Cumulus Networks via email as part of NetQ Cloud onboarding

More complete and detailed information about installing NetQ can be found in the NetQ documentation [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-Platform/Install-Cloud/). To complete the NetQ Cloud Server installation in the Cumulus demo topology, complete the following steps:

1. Perform the NetQ server bootstrap using the bootstrap tarball. Use `eth0` as the interface identifier as specified below. This step takes a few minutes

    ```
    vagrant@netq-ts:~$  netq bootstrap master interface eth0 tarball <URL-path>/netq-bootstrap-X.Y.Z.tgz
    2020-12-20 01:13:27.207201: master-node-installer: Extracting tarball <URL-path>/netq-bootstrap-X.Y.Z.tgz
    2019-12-20 01:14:44.157670: master-node-installer: Checking package requirements
    2019-12-20 01:15:10.402228: master-node-installer: Using eth0 IP X.X.X.X
    2019-12-20 01:15:10.812041: master-node-installer: Initializing kubernetes cluster
    -----------------------------------------
    Successfully bootstrapped the master node
    ```

    {{%notice note%}}

`<URL-path>` is either a local filesystem absolute path, or an HTTP server URL starting with `http://`

{{%/notice%}}

2. After the bootstrap step completes, perform the NetQ Application install with the `-opta.tgz` bundle and by using your config-key for your NetQ Cloud premises.

    ```
    vagrant@netq-ts:~$ netq install opta standalone full interface eth0 bundle <URL-path>/NetQ-X.Y.Z-opta.tgz config-key <your-config-key>
    2019-12-20  06:28:35.368116: master-node-installer: Installing in standalone mode
    2019-12-20  06:32:57.106586: master-node-installer: Installing infra components
    2019-12-20  06:34:06.365374: master-node-installer: Installing NetQ apps
    2019-12-20  06:40:31.810887: master-node-installer: Activating
    --------------------------------------
    Successfully installed the master node
    ```

{{%notice info%}}

`<URL-path>` is either a local filesystem absolute path, or an HTTP server URL starting with `http://`

{{%/notice%}}

### (Optional) Configure the NetQ CLI Agents

In most normal NetQ installation workflows, it would be required to configure and install the NetQ agent on all of the network devices and Linux hosts. The NetQ agent installation and configuration to point to NetQ server’s preconfigured static IP address, have already been completed as part of the Cumulus Linux Reference Topology provisioning from Vagrant. This step requires user credentials and cannot be preprovisioned with the Cumulus Reference Topology.

The NetQ CLI is a separate daemon that’s configured independently from the NetQ agent data collection and telemetry streaming daemon. To fully complete the NetQ installation in your demo environment, the CLI must also be configured and installed on all devices where you want to run netq CLI commands. In most deployments, this is also configured with every agent to be able to enjoy having all NetQ data from any device in the network.

**Prerequisites**

You must have a set of authorization keys generated for a NetQ user. For more information on this procedure, see the NetQ documentation [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-CLI/Install-NetQ-CLI-on-CL/#configure-netq-cli-using-the-cli) (Section “Configuring the CLI for Cloud Deployments"). This creates two keys:

  - Access-key
  - Secret-key

To install the CLI:

1. From devices in simulation that do not use mgmt VRF (Ubuntu Hosts and the NetQ server itself), issue the following command:

    ```
    vagrant@netq-ts:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <access-key> secret-key <secret-key> premise <netq-premise-name> port 443
    ```

    From devices in simulation that do use mgmt VRF (Cumulus Linux nodes: Leaf, Spine, Border, FW)

    ```
    cumulus@netq-ts:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <access-key> secret-key <secret-key> premise <netq-premise-name> vrf mgmt port 443
    ```

2. Restart the netq cli daemon

    `vagrant@netq-ts:~$  netq config restart cli`

3. Test a NetQ CLI command

    `vagrant@netq-ts:~$  netq show agents`

To deploy these NetQ CLI configuration commands to several devices at the same time, use ansible ad-hoc commands from the oob-mgmt-server. An example of how to configure the NetQ CLI on all of the Cumulus Linux nodes that use mgmt vrf is below:

```
vagrant@oob-mgmt-server:~$ ansible spine:leaf:exit -a 'netq config add cli server api.netq.cumulusnetworks.com access-key <access-key> secret-key <secret-key> premise <netq-premise-name> vrf mgmt port 443'
vagrant@oob-mgmt-server:~$ ansible spine:leaf:exit -a 'netq config restart cli'
```

For Ubuntu hosts use:

```
vagrant@oob-mgmt-server:~$ ansible host -a 'netq config add cli server api.netq.cumulusnetworks.com access-key <access-key> secret-key <secret-key> premise <netq-premise-name> vrf mgmt port 443'
vagrant@oob-mgmt-server:~$ ansible host -a 'netq config restart cli'
```

## Clean Up Stuck or Orphaned Simulations

Occasionally errors occur when you use Vagrant or when you delete files from a project that is in use.

To clean up stuck or orphaned libvirt simultations:

1. Use the `virsh list --all` command to inspect the system and see all running libvirt simulations. Find your libvirt *domains* that you want to clean up. Simulations often have a common prefix from the same simulation that is normally the parent folder.

2. Use `virsh` to perform three operations on each virtual machine (libvirt domain) that you want to clean up.
    1. `virsh destroy <name>`
    2. `virsh undefine <name>`
    3. `virsh vol-delete --pool default <name>.img`

Run the script below to clean up all simulations that match a common pattern from `virsh list`.

{{%notice info%}}

Use this script with caution on servers with other simulations and in shared environments as it does not prompt for confirmation and might delete systems you match accidentally!

{{%/notice%}}

```
#for vm in $(virsh list --all | grep <match-pattern> | awk -F ' ' '{print$2}'); do virsh destroy $vm; virsh undefine $vm; virsh vol-delete --pool default $vm.img; done
```
