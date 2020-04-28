---
title: Cumulus Production Ready Automation
author: Cumulus Networks
product: Cumulus Networks Guides
version: "1.0"
draft: true
---
## Overview

Cumulus production ready automation provides several examples of a fully operationalized automated data center. This includes:

* A standard reference topology for all examples
* A full Vagrant/libvirt simulation of the reference topology
* Best practice Ansible automation and infrastructure as code (IaC)
* Working examples of continuous integration/continuous deployment (CI/CD) using Gitlab
* CI/CD testing powered by NetQ Cloud
* A variety of golden standard EVPN-VXLAN architecture reference configurations

This production ready automation package is meant to be both a learning resource and serve as a starting template for anyone looking to implement these features, technologies and operational workflows in their own Cumulus Linux Network environments.

Network devices and hosts in simulation that are the core architecture of this example are simulated in a pre-constructed network topology referred to as the Cumulus Linux Reference Topology or cldemo2 in shorthand. This simulation environment is based on Vagrant and libvirt/kvm. It provides the foundational physical infrastructure and bootstrap configuration, to be able to support and demonstrate Cumulus Linux features and technologies. Additional technical details are discussed in the {{%link title="#Cumulus Linux Reference Topology" text="Cumulus Linux Reference Topology" %}} section of this guide.

{{%notice tip%}}
This is the second Cumulus Linux demo environment, creating the name `cldemo2`
{{%/notice%}}

Examples of Cumulus best practice Ansible automation and infrastructure as code (IaC) are also provided in this package. A completely stock Ansible core installation is used without any vendor specific or 3rd party plugins. Examples of Ansible best practices using roles, highly granular templates, and structured variables represent how your network configurations can be stored as a highly scalable version of infrastructure as code. It is that base code that gets rendered by the automation engine to produce the final configurations that exist on the network devices. 

As network operations become more programmatic and automated, and in combination with a robust simulation platform, CI/CD and devops style workflows are supplanting legacy workflows. Configuration changes can be automatically tested in a simulated environment to allow for more rapid and robust change management workflows. Cumulus production ready automation provides an example CI/CD pipeline implemented on Gitlab with the CI network testing and validation powered by {{% exlink text="Cumulus NetQ" url="https://docs.cumulusnetworks.com/cumulus-netq/" %}}.

These golden standard demos and the underlying base reference topology are officially hosted on gitlab in the Golden Turtle folder of Cumulus Consulting’s Gitlab group: https://gitlab.com/cumulus-consulting/goldenturtle

{{<notice tip>}}
The name "Golden Turtle" comes from the idea of a "golden reference" and the Cumulus Networks mascot the rocket turtle. Golden reference + rocket turtle = Golden Turtle.
{{</notice>}}
### Officially Supported Golden Standard Demos
Cumulus Networks currently provides three officially supported demo solutions to overlay and provision the Cumulus reference topology. All of these demos are EVPN-VXLAN environments that each perform tenant routing in a different style
* [EVPN Layer 2 Only](https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnl2only) - An EVPN-VXLAN environment with only layer 2 extension.
* [EVPN Centralized Routing](https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpncent) - A EVPN-VXLAN environment with layer 2 extension between tenants with inter-tenant routing on a centralized (fw) device.
* [EVPN Symmetric Mode](https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym) - An EVPN-VXLAN environment with layer 2 extension, layer 3 VXLAN routing and VRFs for multi-tenancy
More detailed information such as IP addressing and specifics of the included features can be found on the README.md page of each demo:

https://gitlab.com/cumulus-consulting/goldenturtle

### The Cumulus Linux Reference topology

The Cumulus Linux reference topology provides a common and consistent preconfigured spine and leaf base network topology. This serves as the basis for all supported Cumulus demos and golden standards. This reference topology is intended to be a blank slate with a minimal configuration to prepare the simulation to receive additional deployment and provisioning that demonstrates a feature or represents a fully operational production network.

When the reference topology simulation environment is started, all interfaces (except for the out of band management network) are unconfigured and administratively down. The golden standard configurations and demos provide interface and routing protocol configurations that are applied to this simulation topology.

Please see the Contributors Guide for more information on how to build a package like this or contribute your own demo or environment for the base cumulus reference topology.

The Cumulus Linux reference topology provides a complete 2-tier spine and leaf topology. It also includes a complete out of band management. Devices include:

* 4x Cumulus Linux 3.7 spines
* 2x Cumulus Linux 3.7 leafs
* 8x Ubuntu 18.04 servers
* 2x Cumulus Linux 3.7 border leafs
* 2x Cumulus Linux 3.7 "fw" devices providing a placeholder for ‘policy’ devices
* 1x Ubuntu 18.04 out of band management server (oob-mgmt-server)
* 1x Cumulus Linux 3.7 out of band management switch (oob-mgmt-switch)
* 1x Cumulus NetQ Cloud virtual appliance (netq-ts)


{{<img src="/images/guides/cldemo2-diagram.png" >}}



The Cumulus Linux reference topology is included with every officially supported Cumulus Linux demo. More details about that relationship are discussed in the Contributors Guide. Those looking to see the full example of cumulus production ready automation should visit and use one of the {{<link text="EVPN VXLAN golden standard demos" title="#Officially Supported Golden Standard Demos" >}}. 

## Quick Start
If you’re trying to take a quick look at a Cumulus Networks golden standard demo, the easiest way to get started is by using our simulation platform, [Cumulus In the Cloud](https://cumulsunetworks.com/citc). By using our platform, there are no system requirements or dependencies. Simply visit https://cumulsunetworks.com/citc to get a full blank slate Cumulus Linux reference topology and you can even one-click deploy any of the golden standard demos right from the UI. 

{{<notice info>}}
Ensure that all system dependencies are satisfied first. See {{<link title="#System Software Requirements and Dependencies" text="this section" >}} for more information. 
{{</notice>}}

The memory requirements of a full cldemo2 topology are:

| Deployment    | Memory        |
| ------------- |:-------------:|
| With NetQ   	  | 23296MB    	|
|  Without NetQ |  15104MB 	|

### Starting a Golden Standard Demo Topology
An Ubuntu 18.04LTS box with additional CPU and memory resources for installing NetQ is included in the out of band management network of the base Cumulus Linux reference topology. NetQ is not a required element for any of the golden standard demos to properly function. NetQ is used in the topology to power CI/CD testing and to preview and test NetQ’s functionality. If NetQ is not intended to be used for the purpose of starting this simulation, then it is generally recommended to not start it in simulation to save an additional 8GB of memory.


1. Select the demo topology that you want to start with from the Golden Turtle Gitlab page: https://gitlab.com/cumulus-consulting/goldenturtle 
2. Perform a git clone for your selected Golden Turtle demo using the `--recurse-submodules` argument to also download the required base Cumulus Reference Simulation Topology
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
3. Change to the directory created from the previous step. The directory name will match the name of the project from the git clone operation.
```
user@host:~# cd dc_configs_vxlan_evpnsym/
user@host:~/dc_configs_vxlan_evpnsym# 
```
4. Run the script named `start-demo.sh` and pass in the`--no-netq` option to skip booting the NetQ telemetry server box if it will not be used. During this step, Vagrant will be starting and provisioning the base simulation. It may take 10-15 or more minutes for this step to complete depending on the host machine and internet connection speed.
```
user@host:~/dc_configs_vxlan_evpnsym# ./start-demo.sh --no-netq
Starting OOB management devices
Bringing machine 'oob-mgmt-server' up with 'libvirt' provider...
Bringing machine 'oob-mgmt-switch' up with 'libvirt' provider...
==> oob-mgmt-server: Checking if box 'generic/ubuntu1804' version '2.0.6' is up to date...
==> oob-mgmt-switch: Checking if box 'CumulusCommunity/cumulus-vx' version '3.7.11' is up to date...
==> oob-mgmt-server: Creating image (snapshot of base box volume).
==> oob-mgmt-switch: Creating image (snapshot of base box volume).
==> oob-mgmt-server: Creating domain with the following settings...
<output omitted for brevity>
```
4. After the launch script succeeds, cd into the directory `cldemo2/simulation`
```
user@host:~/dc_configs_vxlan_evpnsym# cd cldemo2/simulation/
user@host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation# 
```
5. Use the command `vagrant ssh oob-mgmt-server` to enter the simulation onto the oob-mgmt-server device. This is your jump box to reach the other devices in the network.
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

7. Change to the automation directory

vagrant@oob-mgmt-server:~$ cd automation/
vagrant@oob-mgmt-server:~/automation$ 
```
8. Run the ansible playbook to configure your selected demo
{{%notice info%}}
The `-i` flag is used to specify the location of the Ansible inventory. This is required, unless the inventory is moved into a [standard Ansible location](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html).
{{%/notice%}}
```
vagrant@oob-mgmt-server:~/automation$ ansible-playbook playbooks/deploy.yml -i inventories/pod1 --diff

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

Next, check the `README.md` on your selected demo repo for more information about that specific topology such as IP addresses and for a small guided tour of the specific technologies or architectures in demo.

### Starting the Blank Cumulus Reference Topology

Starting the reference topology by itself is not normally required unless you are looking to build configuration from scratch or otherwise intend on starting from a completely blank slate network topology. 

If you are planning on running or testing one of the golden standard automation demos, the Cumulus Linux Reference Topology is included as a submodule in all of the Cumulus Networks golden standard demos. This eliminates the need to clone the base reference topology project. For more information about submodules see the contributor’s guide. <!-- TODO: add link to contributor's guide --> 

1. Clone the cldemo2 Cumulus Linux Reference topology
```
user@host:~# git clone https://gitlab.com/cumulus-consulting/goldenturtle/cldemo2.git
Cloning into 'cldemo2'...
remote: Enumerating objects: 215, done.        
remote: Counting objects: 100% (215/215), done.        
remote: Compressing objects: 100% (119/119), done.        
remote: Total 852 (delta 139), reused 156 (delta 96), pack-reused 637        
Receiving objects: 100% (852/852), 7.64 MiB | 8.21 MiB/s, done.
Resolving deltas: 100% (549/549), done.
```
2. Change into the `cldemo2` directory created by the previous step

```
user@host:~# cd cldemo2/
user@host:~/cldemo2# 
```  
3. Run the start-blank-topology.sh script to launch the simulation.  Optionally use the `--no-netq` argument to skip loading the 8GB 4 vCPU netq-ts box if it will not be used.
```
user@host:~/cldemo2# ./start-blank-topology.sh --no-netq
Starting OOB management devices
Bringing machine 'oob-mgmt-switch' up with 'libvirt' provider...
Bringing machine 'oob-mgmt-server' up with 'libvirt' provider...
<output omitted for brevity>
```
This step may take time depending on internet connection speed and host machine

4. After the launch script succeeds Change into the simulation directory
```
user@host:~/cldemo2# cd simulation/
user@host:~/cldemo2/simulation# 
```
5. Use the `vagrant ssh` command to ssh into the oob-mgmt-server. This is the bastion host or jump box to access the rest of the simulation.

Refer to the `README.md` on the choosen Cumulus Linux Reference Topology Gitlab project and the developers guide for more information about how to get started developing and building onto this blank slate topology.

### Destroying and Ending a Simulation

From inside of the folder `simulation`, issue the command `vagrant destroy -f`
```
user@host:~/cldemo2/simulation# vagrant destroy -f
==> server08: Removing domain...
==> server07: Removing domain...
==> server06: Removing domain...
==> server05: Removing domain...
==> server04: Removing domain...
==> server03: Removing domain...
==> server02: Removing domain...
==> server01: Removing domain...
==> netq-ts: Removing domain...
==> leaf04: Removing domain...
==> leaf03: Removing domain...
==> leaf02: Removing domain...
==> leaf01: Removing domain...
==> fw2: Removing domain...
==> fw1: Removing domain...
==> spine04: Removing domain...
==> spine03: Removing domain...
==> spine02: Removing domain...
==> spine01: Removing domain...
==> border02: Removing domain...
==> border01: Removing domain...
==> oob-mgmt-switch: Removing domain...
==> oob-mgmt-server: Removing domain...
user@host:~/cldemo2/simulation# 
```

Individual machines or VMs can be destroyed by specifying the name(s) in the vagrant destroy command.
```
user@host:~/cldemo2/simulation# vagrant destroy server08 -f
==> server08: Removing domain...
user@host:~/cldemo2/simulation# 
```

## Users Guide
In this section, we’ll cover how to run Cumulus Production Ready automation, unchanged and unmodified on your own system in your enterprise. You can test, learn, and experience using Cumulus Linux driven by best practice Ansible automation and test drive our officially supported golden standard configurations and architectures by running the production ready automation as-is and unmodified.

For more details about how to customize, reuse and adapt these examples of simulation, automation or CI/CD for your own purposes, refer to the {{% link title="#Integration Guide" text="Integration Guide" %}} section

### System Hardware Requirements
* Min 16GB RAM (Without NetQ) | Recommended 32GB Ram
* Min 256GB Disk | Recommended >1TB Disk
* SSD Recommended (NetQ Requirement)
* Internet connectivity for package installs during simulation bringup
* Minimum of 8x CPU Cores

{{%notice tip%}}
Tight on resources? See the manual start section for more information about how to start a subset of this simulation. Or try it on our hardware for free with [Cumulus in the Cloud](http://cumulusnetworks.com/citc)
{{%/notice%}}

The memory requirements of a full cldemo2 topology are:

| Deployment    | Memory        |
| ------------- |:-------------:|
| With NetQ   	  | 23296MB    	|
|  Without NetQ |  15104MB 	|

### System Software Requirements and Dependencies
**Operating Systems**
* Cumulus Linux 3.7.11 or later
* Cumulus NetQ 2.4 or later (optional) 
* Ubuntu 16.04 or 18.04

{{< notice note>}}
Other Linux distributions, like CentOS or RHEL, may be supported, but have not been tested.
{{< /notice >}}

**Software Packages**
* Vagrant 2.2.4 or later
* Libvirt
* Qemu
* Git

**Vagrant plugins**
* Vagrant-libvirt
* Vagrant-scp

Refer to {{%link title="#Appendix A" %}} for an example bash script that installs these package dependencies to be able to support Cumulus VX simulation with Vagrant/libvirt.

### Manually Starting A Golden Standard Topology
The easiest method to get a Production Ready automation demo started, after preparing the system, is in the {{< link title="#Quick Start" text="Quick Start" >}} section of this guide. The quick start uses a bash script to automatically perform the following steps:

* Checks if the Cumulus Linux Reference Topology submodule is present. If not, it attempts to download it
* Performs a vagrant up for the oob-mgmt-network devices
* Performs a series of vagrant up commands to bring up the rest of the network simulation
* Copies the network automation into the simulation using `vagrant scp`

Manually launching a simulation can give you more control over which nodes start, and which order they start in. This can be useful for several reasons, the most useful of which is to simply save CPU and memory resources.

To manually start a demo topology such as [EVPN Symmetric Mode](https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym), you must ensure that you also fetch and pull down the included Cumulus Linux base Reference Topology. This can be done in one of two ways:

* Use the `--recurse-submodule` option with the initial `git clone`. This will have git also fetch the submodule files in the same step as the clone. This is the option you will see in the procedure below.
* Perform a normal git clone, then manually fetch the submodule files separately with ‘git submodule init’ and ‘git submodule update’. See this guide https://git-scm.com/book/en/v2/Git-Tools-Submodules for more information about git submodules.

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

{{<notice info>}}
You must bring up the OOB Server and OOB Switch first. The OOB Server acts as the management network DHCP server. If the OOB Server and Switch are not online first, the management interfaces of the other network devices will be temporarily unreachable.
{{</notice>}}
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

At this stage you now have a deployed and operational golden standard Cumulus architecture. Visit the demo project page for the `README.md` for more details about the specific network topology, it’s IP addressing and how to interact with the features in demonstration. 
### Automatically Launching the Production Ready Automation on Cumulus in the Cloud

This method is the easiest way to experience the final product of the Cumulus golden standard EVPN VXLAN demo configurations. This method is best suited to fast track all of the simulation setup and provisioning and get to testing any of the official golden standard EVPN VXLAN demo configurations.

If you are interested in taking a closer look at the processes of automation, deployment and see the actual examples of the infrastructure as code, you’ll want to manually clone the demo project and manually run the automation playbook to render the config as code into the network devices. This automated process clones your selected demo repo and runs the Ansible deployment playbook for you with a few easy and convenient clicks from the Cumulus In the Cloud UI.

1. Go to http://cumulusnetworks.com/citc to request a demo or to reach your existing simulation.
2. Once you reach your simulation console, choose a demo from the drop down menu on the left panel
{{<img src="/images/guides/citc-interface-demo.png" >}}


3. Click the “Run Now" button
4. Follow the instructions on the `Guided Tour` panel to test and experience the unique aspects of your selected demo.
### Manually Launching an Automation Demo Topology From Cumulus In the Cloud
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

### Installing and Configuring the NetQ Cloud Server

The Cumulus Linux reference topology includes an Ubuntu 18.04 server with additional CPU, memory and disk resources added to support a NetQ Cloud Server installation. Vagrant provisions this box with all of the required software package dependencies to be able to skip immediately to the bootstrap and install steps of the NetQ server setup documented [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-Platform/Prepare-Existing-NetQ-Appliance/) starting at the section “Download the bootstrap and NetQ installation tarballs."

In order to use the included NetQ Cloud server, you must have a few prerequisites satisfied:
* An active NetQ Cloud account with netq.cumulusnetworks.com
* An additional site/premises setup and provisioned that is dedicated for virtualization use. This amounts to a unique NetQ configuration key for your simulation environment. Do not mix a simulation topology with an existing site or use an existing and in-use NetQ premises config-key.
* The NetQ bootstrap tarball downloaded from cumulusnetworks.com
* The NetQ OPTA install tarball downloaded from cumulusnetworks.com



{{%notice info%}}
The `NetQ bootstrap` and `NetQ OPTA install` tarballs are two unique files. 
{{%/notice%}}

#### Staging the NetQ installation tarballs on the netq-ts
The NetQ application and version is driven by the version of the bootstrap and install files that are used to install the NetQ application on the provided Ubuntu server. The installation procedure uses the NetQ agent that is preinstalled on the netq-ts box. Users must stage the NetQ bootstrap and install tarball files that are downloaded from cumulusnetworks.com for the NetQ installation procedure.

Users may stage the installation tarballs in either one of two locations relative to the netq-ts box:
 
1. On the local filesystem of the netq-ts itself. The bootstrap and installation tarballs must be copied onto the netq-ts box after the simulation has been started from `vagrant up`. This is typically accomplished using SCP or `vagrant scp`
2. On a remote HTTP server reachable by the netq-ts. The bootstrap and installation tarballs are placed onto an HTTP server and an HTTP url is provided during the bootstrap and installation procedures.

You must decide whether to stage the installation tarball files directly onto the server for installation, or host them on a remote http server that the netq-ts can reach.

The installation tarball files when they are downloaded from cumulusnetworks.com are named:
1. `netq-bootstrap-X.Y.Z.tgz` (bootstrap tarball) 
2. `NetQ-X.Y.Z-opta.tgz` (install tarball)

{{%notice info%}}
The `netq-bootstrap` and `netq-opta` image X.Y.Z version numbers must match.
{{%/notice%}}

#### Staging from the Local Filesystem
Specific steps on how to login to cumulusnetworks.com and download the NetQ files can be found [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-Platform/Prepare-Existing-NetQ-Appliance/) starting at the section “Download the bootstrap and NetQ installation tarballs." Specific steps on how to copy the tarballs onto the simulation host are out of scope of this tutorial and the choice of the reader. Normally SCP is used to securely copy the files onto the Linux based simulation host.

In this procedure, we will copy the installation tarball files to the directory `/mnt/installables` although any directory that has sufficient read permissions will be suitable for staging these files. Repeat the following steps for each file:

1. Download the two required installation files from cumulusnetworks.com.
    1. Bootstrap
    2. Appliance (Cloud)
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
#### Staging from a Remote HTTP Server 
Specific steps on how to login to cumulusnetworks.com and download the NetQ files can be found [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-Platform/Prepare-Existing-NetQ-Appliance/) starting at the section “Download the bootstrap and NetQ installation tarballs." Specific steps on how to copy the tarballs onto a remote HTTP server will vary depending on the specific http server software. This is an example procedure to setup an http server with Apache on a Debian or Ubuntu based Linux machine.

1. Download the two required installation files from cumulusnetworks.com.
    1. Bootstrap
    2. Appliance (Cloud)
2. Install apache2
3. Confirm services are running
4. Copy tarball files to the `/var/www/html` directory with permissions
5. Derive http staging URLs for the next steps

#### Installing the NetQ Application
This step sets up the NetQ Cloud server. This process installs the NetQ Cloud server application to be able to receive and aggregate agent data and securely transport it to the cloud associated with your account.

##### Prerequisites
* You must have the bootstrap and install tarball files staged in either the local filesystem on the netq-ts or a remote http server accessible from the netq-ts. See the {{<link text="previous section" title="#Staging the NetQ installation tarballs on the netq-ts" >}} for instructions.
* Your NetQ config-key associated with the NetQ site/premises this simulation will occupy. This is received from Cumulus Networks via email as part of NetQ Cloud onboarding

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

{{%notice info%}}
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

#### (Optional) Configuring the NetQ CLI agents in the topology.
In most normal NetQ installation workflows, it would be required to configure and install the NetQ agent on all of the network devices and Linux hosts. The NetQ agent installation and configuration to point to NetQ server’s preconfigured static IP address, have already been completed as part of the Cumulus Linux Reference Topology provisioning from Vagrant. This step requires user credentials and cannot be preprovisioned with the Cumulus Reference Topology. 

The NetQ CLI is a separate daemon that’s configured independently from the NetQ agent data collection and telemetry streaming daemon. To fully complete the NetQ installation in your demo environment, the CLI must also be configured and installed on all devices where you want to run netq CLI commands. In most deployments, this is also configured with every agent to be able to enjoy having all NetQ data from any device in the network.

##### Prerequisites
* You must have a set of authorization keys generated for a NetQ user. For more information on this procedure, see the NetQ documentation [here](https://docs.cumulusnetworks.com/cumulus-netq-24/Cumulus-NetQ-Deployment-Guide/Install-NetQ/Install-NetQ-CLI/Install-NetQ-CLI-on-CL/#configure-netq-cli-using-the-cli) (Section “Configuring the CLI for Cloud Deployments"). This creates two keys:
  * Access-key
  * Secret-key

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

Test a NetQ CLI command

`vagrant@netq-ts:~$  netq show agents`

To deploy these NetQ CLI configuration commands to several devices at the same time, use ansible ad-hoc commands from the oob-mgmt-server. An example of how to configure the NetQ CLI on all of the Cumulus Linux nodes that use mgmt vrf is below:
```
vagrant@oob-mgmt-server:~$ ansible spine:leaf:exit -a ‘netq config add cli server api.netq.cumulusnetworks.com access-key <access-key> secret-key <secret-key> premise <netq-premise-name> vrf mgmt port 443’
vagrant@oob-mgmt-server:~$ ansible spine:leaf:exit -a ‘netq config restart cli’

#Ubuntu hosts

vagrant@oob-mgmt-server:~$ ansible host -a ‘netq config add cli server api.netq.cumulusnetworks.com access-key <access-key> secret-key <secret-key> premise <netq-premise-name> vrf mgmt port 443’
vagrant@oob-mgmt-server:~$ ansible host -a ‘netq config restart cli’
```

## Integration Guide
### Overview
This portion of the Production Ready Automation documentation provides guidance on how to customize and adapt the main individual pieces of the Cumulus Production Ready Automation to suit your own needs and work for your own environment.

There are three main features of Cumulus Production Ready Automation that depend on each other to provide the fully operationalized automated data center.

* Base simulation
* Automation providing infrastructure as code (IaC)
* Continuous Integration / Continuous Deployment (CI/CD)

This guide will be broken into sections that will provide guidance on how to customize the three main features above.

Building a simulation that represents your production network is the first step in taking advantage of next generation NetDevOps style operational workflows. Ideally all network changes are tested in simulation or in a staging environment before they reach production. Cumulus VX is an extremely lightweight and high fidelity simulation platform. With a small memory footprint and all of the software components being exactly the same as Cumulus Linux running on hardware, a highly scalable and robust simulation environment can be constructed that matches the production environment, 1:1. From interface labels all the way down to even MAC addresses.

{{% notice note %}}
For more about why Cumulus Networks made the choices they did for Production Ready Automation read the [blog post](https://cumulusnetworks.com/blog/production-ready-automation/) that describes our motivations and technical reasoning. 
{{% /notice %}}
#### Infrastructure as Code
IaC or (Infrastructure as code) is an abstract concept that simply amounts to storing your network configurations or a coded version of your network configuration normally in a source code repository. The choice of your automation engine or automation tools drives and influences the ways you can turn your network configurations into more highly scalable and repeatable chunks of “code" that get rendered by the automation tools during deployment.

Cumulus Production Ready Automation uses Ansible as it’s automation engine. Due to this choice, our version of infrastructure as code are the Ansible best practices that includes the use of roles, Jinja2 templates, and structured variable files.

As part of the Production Ready Automation complete Ansible configurations include: 
* playbooks
* roles
* templates 
* variables 
* inventory

#### Continuous Integration and Continuous Delivery
CI/CD is an abbreviation for Continuous Integration and Continuous Deployment. These terms are normally used together, but are actually distinct and separate stages. It is possible to perform just CI, without CD, for example, but one wouldn’t normally implement CD without CI.

The CI step, or “Continuous Integration" is based on the idea that changes should be able to happen frequently and at any time of day. But before changes can be “integrated" or accepted and be considered for deployment into production, the whole network, with those changes, must be able to pass a set of testing to ensure that the change does not cause an unintended consequence or is an otherwise bad change.

Once testing passes and the change is integrated from the CI stage, the CD stage or “continual deployment" stage is optionally also carried out automatically. For the network, this could mean that changes that pass automated testing from CI, could then be automatically deployed to the production environment. Automated CD is still uncommon for network operations.

{{<notice info>}}
Cumulus Networks strongly recommends that all customers deploy a CI strategy. We recommend against a CD strategy for most customers. Using CD can lead to network changes during critical business hours with unintended consequences. Only organizations with proper testing and operations in place should consider CD.
{{</notice>}}
### Getting Started
#### System Hardware Requirements
For a robust simulation environment and CI/CD with gitlab, a dedicated, always-on, enterprise class server is recommended. Using the NetQ server in individual development environments is not normally required and is normally only needed for CI testing where the gitlab-runner is installed and registered to your CI/CD enabled project.

#### Hardware Requirements
* Memory requirements will vary and can be controlled, but to estimate the needs for your simulation, use the values below:
    * Each Cumulus Linux Node = 768MB
    * Each Ubuntu 18.04 host = 512MB 
    * Oob-mgmt-server = 1024MB
    * Oob-mgmt-switch = 768MB
    * Netq-ts = 8192MB
* Disk requirements will vary. Vagrant/libvirt uses thin disk images but a good reference point is
    * 256GB Disk with >64GB free memory
    * Recommended >1TB Disk
    * SSD Recommended (NetQ Requirement)
* High Speed Broadband/Wideband Internet Connection for package installs during simulation bringup
* Min 8x x86_64 CPU Cores

#### System Software Requirements and Dependencies
**Operating Systems**
* Cumulus Linux 3.7.11 or later
* Cumulus NetQ 2.4 or later (optional) 
* Ubuntu 16.04 or 18.04

{{< notice note>}}
Other Linux distributions, like CentOS or RHEL, may be supported, but have not been tested.
{{< /notice >}}

**Software Packages**
* Vagrant 2.2.4 or later
* Libvirt
* Qemu
* Git

**Vagrant plugins**
* Vagrant-libvirt
* Vagrant-scp


See Appendix A & B for sample bash scripts to install the software package and environment dependencies.
#### CI/CD Requirements and Dependencies
* Account with gitlab.com or you own internal gitlab instance 
* A dedicated simulation environment for the gitlab-runner to start and test simulations
* Gitlab-runner package installed on the simulation host machine
    * Setup a gitlab-runner user & environment on the system
* A project on your gitlab instance that is setup with simulation, automation & IAC
* NetQ Cloud Account with a premises/site dedicated for simulation

#### The Anatomy of a Cumulus Linux Golden Standard Demo Project
There are three main features of Cumulus Production Ready Automation that depend on each other to provide the fully operationalized automated data center.

* Base simulation
* Automation and IaC
* CI/CD - Continuous Integration / Continuous Deployment

In a Cumulus official golden standard demo repo, the important files and folders map to the three main features above in the following way:
```
dc_configs_vxlan_evpnsym/
├── automation
├── cldemo2
│   ├── ci-common
│   ├── documentation
│   ├── LICENSE
│   ├── README.md
│   ├── simulation
│   └── tests
├── .git
├── .gitignore
├── .gitlab-ci.yml
├── LICENSE
├── README.md
├── start-demo.sh
└── tests
```
#### File/Folder descriptions
`Automation` - This is the folder tree that contains all of the required files to support the Ansible automation and IaC. 

`cldemo2/ci-common` - This is the folder that contains the common scripts used for CI/CD in all of the officially supported colden standard demo project. Generally, all of the scripts that are called by the gitlab-ci.yml file exist here that perform the work in the CI pipeline

`│   ├── simulation` - This is the folder tree that contains all of the files required to support the base Cumulus Linux Reference Topology simulation.This is where the topology_converter, Vagrantfile, and all of the associated provisioning scripts for the base reference simulation topology live.

`├── .git` This directory contains the git project data and configuration. This is technically part of the configuration as code, but should really never need to be manually modified or customized. Git commands look for this directory to perform their work on the files of the project. If you are creating your own custom project, this folder can and probably should be deleted (or you can fork the project in gitlab).

`├── .gitignore` - This file informs git which files to ignore and not track as part of the project. This normally includes the .vagrant folder inside of the simulation folder and other dynamic run-time files that are not useful or intended to be part of the source code of the project.

{{%notice info%}}
Not including the `.vagrant` folder in your `.gitignore` can lead to an unnecessarily large git repository. 
{{%/notice%}}

`├── .gitlab-ci.yml` - This file defines the CI pipeline stages and jobs for Gitlab CI. This is a form of a configuration file. The example provided in the Cumulus Linux Golden Standard projects is a starting point and reference for how to model your own CI pipeline. Refer to the gitlab ci documentation for more information
`└── tests` - This folder contains the CI test scripts for the project. These scripts are copied into the simulation and run from inside of the simulation. Each project and demo may have a unique set of tests, and thus scripts for this stage of CI are broken out from the rest of the common CI scripts and remain unique to the project.

These demo simulations are a good basis for how to organize your own project. In our unique use case we are providing a common base topology for reuse across many different possible different solution architectures. For this reason, we are using a git submodule to include that base reference topology with the automation repo so everything can be packaged together.

For real world deployments, the use of a git submodule is unlikely to be necessary or useful. It makes more sense, in cases without the use of a submodule, have the `simulation` folder and the `ci-common` folder be under the root of the project instead of inside a subfolder as they are in the golden standard demos. This additional cldemo2 folder is imposed by the submodule feature. 

{{<notice info>}}
If you elect to make this suggested change, it has an impact and requires changes to the hard-coded relative paths in the .gitlab-ci.yml file and the ci-common scripts to not include the cldemo2 subfolder.
{{</notice>}}

Customizing a simulation
Building a custom simulation is the foundation of transforming and automating your network and operations. A custom Vagrant/libvirt topology using Cumulus VX, is automatically generated by using the topology_converter tool.

Topology_converter is relied on to handle the complexity of building, generating and maintaining the Vagrantfile. Topology_converter produces a Vagrantfile and brings with it all of the associated bootstrap provisioning scripts to be able to provide the experience of performing a simple "vagrant up" and having a connected network simulation ready to receive further network configuration.

Since a Vagrantfile is difficult to build, modify and maintain by hand, there is really no other feasible way to manage a custom simulation other than by using and relying on the topology_converter utility. 

{{<notice info>}}
It is not recommended to manually edit and maintain a raw Vagranfile. Always use topology_converter workflows to make changes to the Vagrantfile
{{</notice>}}

Refer to the topology_converter gitlab project and documentation for detailed information about the topology_converter utility, all of its options, and detailed instructions on how to build a .dot file. These are the high level steps required to create a custom Cumulus VX topology:

1. Consider how to handle out of band management. The easiest option is to use the [“Automated Network Management" feature](https://gitlab.com/cumulus-consulting/tools/topology_converter/-/tree/master/documentation/auto_mgmt_network). Alternatively, the out of band management network can be manually created in the topology.dot file to more accurately represent your production network.
2. Create a `topology.dot` file. The name of the file does not have to be topology.dot, but the contents must be in the graphviz format and syntax. Use the cldemo2.dot file in the Cumulus Linux Reference Topology project as a reference or template to define your own set of network nodes, attributes and links.
3. Put all of the topology_converter project files and your custom topology.dot file in a ‘simulation’ folder of your project. Perform a git clone to obtain all of the topology_converter project files. Copying the topology_converter files from the ‘simulation’ directory of The Cumulus Linux Reference Topology (cldemo2) is possible, but has a number of extr
4. Create the Vagrantfile from your topology definition. Ensure the `-p libvirt` option is specified. If the “automated Network Management" feature is used, the -c option in topology_converter is required.

`python3 ./topology_converter.py ./topology.dot -c -p libvirt`

### Customizing Automation and IaC

Cumulus Networks has provided a scalable and extensible framework for how to store or encode a data center network configuration and deploy it using Ansible automation. IaC or infrastructure as code is the concept of thinking about your network configuration as a form of source code just like in the software development world.

Modifying these aspects of the Cumulus Production Ready Automation commands a deep understanding of the underlying technologies which are beyond the scope of this guide. Namely Ansible and Ansible roles, jinja2 template engine and the basics of structuring and representing data using yaml. Cumulus Professional services is available to assist you through a process of customizing and operationalizing this Production Ready Automation custom for your unique requirements. Contact your sales representative for more details.

In a software context, code is “built" to produce “binaries" or executable code specific for the OS and CPU architecture that will run it. A compiler is used to render high level human readable code into a format that’s understood by the machine. In a network context, the final build product needs to be the flat configuration files running on the network devices that they understand. The automation engine used to deploy to the network usually drives what the base IaC code will look like. For Cumulus Production Ready Automation using Ansible, the config as code examples are a combination of jinja2 templates and structured variable files in the automation folders. During deployment with Ansible, the templates are populated with values from the structured variable files. The process of generating the final configuration from the templates and variables is sometimes referred to as “rendering" the configuration. In continuing the analogy to software development, “rendering" the configuration during Ansible deployment is similar to the process of compiling and linking source code into an executable file.

There are a nearly infinite number of ways to implement network configuration or infrastructure as code. Flat configuration files are a form code, so the most primitive version of IaC could be simply storing copies of device configuration files. This primitive example can even have deployment be automated; simply push flat configuration files using your automation tools, from the central repository to the devices. That would be one way to implement automation and IaC, but without realizing many of the scale and efficiency benefits of the solutions. In this example, configuration files are still modified individually, per device. 

Customizing the Ansible automation to create or modify roles and modify the playbooks requires proficiencies using Ansible that are out of scope of this guide. The core concept in use to provide the granular control of the inventory is based on Ansible roles. Please see Ansible’s documentation on using roles [here](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html).
### Customizing and Setting up CI/CD
#### Introduction to Network CI/CD on Gitlab
CI/CD is the next logical step after successfully implementing your version of IaC and thinking about applying the concept of automatically producing builds of your network code for automated testing and verification.

Cumulus Production Ready Automation uses Gitlab for CI/CD. References for Gitlab CI can be found [here](https://docs.gitlab.com/ee/ci/README.html). **Caution**: Most CI/CD Guides and references are contextualized for classic software development CI workflows. Our use case of CI/CD for the network is building network simulations as the product of the code is a corner case.

{{<notice tip>}}
Most cloud based CI tools are run inside containers and do not support running Cumulus Vx. {{</notice>}}

{{<notice tip>}}
Cumulus Production Ready Automation with Vagrant/libvirt only supports a single gitlab runner per Gitlab project.
{{</notice>}}

A CI Pipeline is made up of stages that are executed in series or connected in a Pipeline. (One at a time in order until completion). A CI Stage consists of one or more jobs that can be executed in parallel. Jobs are individual CI tasks that you design and configure to either pass or fail. CI jobs are executed by a piece of software called a gitlab-runner. 
#### Gitlab-runner Overview
The gitlab-runner is an agent that you install on the server that is your dedicated simulation-host that will run the simulations and testing for CI/CD for your project. The gitlab-runner installs like any other software package and uses a unique registration token to connect and register to your gitlab project for your IaC.

After being registered to the project, it periodically polls outbound to gitlab.com CI as a service to see if there are any jobs in queue that it needs to run. If it finds a job, it executes it according to the `gitlab-ci.yml` file.

The gitlab-runner uses the `shell` executor type. We have a unique set of dependencies for building network simulations and heavy system requirements such that we require a dedicated runner for our project. The shell executor can be thought of as if a user were executing commands on the server from a bash shell. Due to this, native bash scripts are used to drive the CI jobs. See the gitlab-ci 
#### Branching Strategy
Gitlab CI pipelines are dynamically built and then executed when code is pushed to the remote repository (normally gitlab.com). Different versions of code can exist on different branches as changes move upstream toward `master` and CI pipelines can be controlled independently and uniquely for each branch in a project. This ability to customize pipelines per branch are what allow for different automated workflows as changes are merged into upstream branches. An introduction to the gitlab flow best practices are [here](https://docs.gitlab.com/ee/topics/gitlab_flow.html) although be cautioned that a network and IaC operational workflow is a still a novel use case of most CI/CD implementations.

**Cumulus suggests the following branching strategy and as a simple starting point:**
* `master` branch - represents what is currently deployed on the network. The pipeline that runs against this branch could deploy to your live network. This is the CD (continuous delivery or continuous deployment) 
* `dev` or Development or Staging Branch - represents changes that get deployed to the staging or development network and thoroughly tested. Referred to as `dev` branch moving forward.
* Private/working Branches - Branches that originate from the dev branch. These branches are where operators perform their work. A branch usually represents a change or set of changes for a common purpose. For example, a branch to track changes for each change request ticket maps nicely onto existing change control workflows. These branches are merged back into the `dev` branch after the work is completed.

**Example Workflow Guidelines:**
* All operators must have access to a development environment where they can stand up their own private versions of the network simulation to perform their work and local unit testing.
* (optional) Operators can develop test scripts for their CI testing phase to confirm/check their specific changes.
* All operators start work (clone) from the `dev` branch 
* All operators perform all of their own work in their private/working branch.
* After operators have complete their changes, their working branch is merged into the `dev` branch
* After merge to `dev`, the CI pipeline runs to build, deploy and test the network based on the current code in the `dev` branch (now with the changes from the merge)
* Only after the CI pipeline succeeds and all testing passes, should dev be allowed to be merged into the `master` branch.
* The code from the `master` branch is deployed to the live network.


The last step is currently expected to be performed manually in the Cumulus Networks Production Ready Automation examples. Automating the deployment to the live network from the `master` branch CI pipeline is the full realization of a completely automated CI/CD enabled network operations workflow. In a fully automated workflow, only the CI pipeline makes deployments to the live network when there is a merge to `master`. The merges to `master` are also automatic as a result of robust automated testing and a pass result from testing against the `dev` branch.

As a matter of practice, it is uncommon to need to fully automate deployments to the live production network. This is the “CD" “continuous delivery" component of the CI/CD paradigm. Most network operators still prefer to queue up changes in a batch and deploy to the live network manually from the `master` branch on a periodic schedule. 


##### Installing and registering the gitlab-runner to your project

Installing and registering the gitlab-runner to the project is a relatively simple task. It is important to remember that all jobs will run on the server and in the environment as the `gitlab-runner` user. Therefore, perform at least some manual testing and initial development for CI on your gitlab-runner server under that user as there are occasionally some thing such as vagrant plugins that differ per user.

See Appendix B for a basic shell script to cover the baseline dependencies. This is only tested on Ubuntu 16.04 and Ubuntu 18.04.
Procedure
1. Install the gitlab-runner software. The official instructions can be found here
2. Create the gitlab-runner user and setup the user environment
    * Starting as root, add the gitlab-runner user to the `libvirtd` group
`adduser gitlab-runner libvirtd`
    * Change to gitlab-runner user
`sudo su - gitlab-runner`
    * Append `/usr/sbin` to the $PATH variable and put it in `.bashrc`
`echo 'PATH=/usr/sbin:$PATH' >> ./.bashrc`
    * Install the vagrant plugins that are needed when the gitlab-runner user runs CI jobs
`vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp`
3. Locate the gitlab-runner registration token for your project. This can be found on your project on gitlab.com. On the left panel, browse through Settings -> CI/CD. Then expand the “Runners" Section. Scroll down to the section “Set up a specific Runner manually" The registration token is in step 3. It will look something like this: `zLZLhVDkfJPq7eWXV6rw`
4. Perform the gitlab-runner registration. 

Gitlab runner registration parameters:

| Gitlab Parameter    | Setting        |
| ------------- |:-------------:|
| Gitlab-ci coordinator URL       | https://gitlab.com     |
| Gitlab-ci token |  From Step #3 above  |
| Gitlab-ci description for this runner | Any informative description of this server |
| Gitlab-ci tags | None. Leave Blank. Press Return | 
| Executor | shell | 

```
user@hosti:~# gitlab-runner register
Runtime platform                                    arch=amd64 os=linux pid=143019 revision=4c96e5ad version=12.9.0
Running in system-mode.                            
                                                   
Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com/):
https://gitlab.com
Please enter the gitlab-ci token for this runner:
<Registration-token-from-step#3>
Please enter the gitlab-ci description for this runner:
[host]: <any-description-here>
Please enter the gitlab-ci tags for this runner (comma separated):
<Leave this blank! Just press enter here for NO TAGS>
Registering runner... succeeded                     runner=qfzmHDDk
Please enter the executor: docker+machine, parallels, virtualbox, docker-ssh, shell, ssh, docker-ssh+machine, kubernetes, custom, docker:
shell
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded! 
```
1. Start the gitlab-runner runner
```
user@host:~# gitlab-runner start
Runtime platform                                    arch=amd64 os=linux pid=145596 revision=4c96e5ad version=12.9.0
user@host:~# 
```
2. Confirm the runner status on gitlab.com

On your project on gitlab.com, on the left panel, browse through Settings -> CI/CD. Then expand the “Runners" Section. Scroll down to the section “Runners activated for this project". Check to make sure the runner that was just registered is present in this list with a green “ready" indicator.
#### Gitlab CI Variables
Gitlab CI provides a number of built in environment variables for use in CI scripts. A list of all of the available variables provided by gitlab can be found [here](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)

The included ci-common and test scripts rely on the following built in variables:
```
$CI_COMMIT_SHORT_SHA
$CI_COMMIT_BRANCH
$CI_PROJECT_NAME
```
Gitlab also provides a way for a user to define custom environment variables for the runner for that project. Access to view, change, or add variables require that you have developer or maintainer privileges on the project and can access the project's settings.

Since NetQ installation requires unique configuration and access keys, these are stored as masked (and can optionally be configured to be used/valid only on protected branches) variables with the Gitlab project. Then these variables are called during the NetQ provisioning CI job to allow for programmatic provisioning of NetQ in the automated CI pipeline. 

It is generally considered best practice to configure a dedicated/dummy CI and CLI user in NetQ cloud User Management. This allows the generated access-key and secret-key from this account to be more easily disposable in the event they need to be revoked or changed. See the NetQ documentation for more information about setting up netQ users and generating auth keys to store with your CI/CD enabled gitlab project.
Variables required to support the provided CI scripts
Configure the following variables in the Settings -> CI/CD -> Variables area in Gitlab on your project if you wish to use the reference ci-common and test scripts unmodified:

| Variable Name            | Description                                                                                                                                                                                                                          | Example Value                                                    |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| CONCURRENCY\_ID          | An integer value to help the simulation\-host be able to support concurrent simulations for concurrent projects\. This is requires if your gitlab runner supports multiple projects that may run simulations concurrently\.          | 1                                                                |
| NETQ\_ACCESS\_KEY        | A valid access\-key generated from the NetQ cloud user Management page\.                                                                                                                                                             | bf5802fd59456d7be723d85f99c303b5c943c536f75b86e1da8fb94a48a18dfa |
| NETQ\_BOOTSTRAP\_TARBALL | The URL to the NetQ bootstrap tarball on the netq\-ts\. See the staging the NetQ installation tarballs for more information\. This variable must be entered/stored in gitlab as base64 encoded due to the / characters in the path\. | L21udC9pbnN0YWxsYWJsZXMvbmV0cS1ib290c3RyYXAtMi40LjEudGd6         |
| NETQ\_CONFIG\_KEY        | The config\-key for your your dedicated premises for CI and simulation from Cumulus NetQ Cloud Onboarding process email\.                                                                                                            | CXx0Dh1zY3XucHJXZDMubmV0cx5jdX11bHVzbmV0d29Ya3MuYd9tGLsD         |
| NETQ\_OPTA\_TARBALL      | The URL of the NetQ OPTA install tarball\. See the staging the NetQ installation tarballs section for more information\. This variable must be entered/stored in gitlab as base64 encoded to due to the / characters in the path\.   | L21udC9pbnN0YWxsYWJsZXMvTmV0US0yLjQuMS1vcHRhLnRneg==             |
| NETQ\_PREMISE\_NAME      | The string of your premises name for this dedicated CI/CD simulation environment                                                                                                                                                     | netq\-demo\-dc\-6                                                |
| NETQ\_SECRET\_KEY        | The valid secret\-key for the associated access\-key that is also provided\. Only available once at generation in NetQ Cloud User Management                                                                                         | hxXoSwlcJqKVyu7V/FT7eHpSKrz4jKIr15OMX9Z9MTI=                     |


#### Customizing the CI Pipeline
Gitlab CI uses a configuration file contained in the project files to define the pipeline. A pipeline is made of up a series of sequential stages. A stage is made up of one or more jobs that may run in parallel. The .gitlab-ci.yml file defines the stages, jobs, what occurs in each job and also the order in which the stages are executed.

CI/CD for a network as code departs slightly from a traditional software code workflow. For our use case, first we must build and provision a simulation network that represents production. Building a simulation from scratch is the current paradigm that we use for our golden standard configurations. After creating a fresh simulation, we can then deploy our IaC to that contains our changes. Then, with those changes, we perform a testing phase to ensure that the network is functional for our needs. If all of that provisioning, deploying, and testing is successful, we can be confident that the same process, on production equipment, will share that same success.

{{<notice info>}}
It would also be possible to build a CI/CD pipeline for a simulation environment in an “always-on" mode; where the staging/development simulation is not destroyed after each pipeline run. This creates additional challenges such as rollback integrity after failed runs such as, “How do we ensure the pipeline properly undoes what it attempted, and failed to do?"
{{</notice>}}
##### Example Gitlab CI Stages
###### lint
In the lint stage, basic yaml syntax checking is performed. This stage helps catch basic syntax and format errors that would cause failures in later stages and ensures good formatting.
###### prep simulation environment
This stage prepares the environment for the rest of the pipeline stages. Special dependencies for the CI pipeline jobs in later stages should be checked for and optionally installed or remediated in this stage.
###### oob-mgmt bringup
This stage is responsible for bringing up the devices that makeup the out of band management network. This comprises of the `oob-mgmt-server`, `oob-mgmt-switch`, and the `netq-ts`. This stage also copies the `automation` folder and `tests` folder from the demo project into the oob-mgmt-server and netq-ts. The `automation` folder contains the ansible playbooks, roles and inventory that will configure the network. The `tests` folder contains the testing scripts that are used in the later `test simulation` stage
###### network bringup
The network bringup stage consists of two jobs. These jobs are not related to each other and can run in parallel (if the gitlab-runner is configured with enough workers) to help speedup pipeline runs.

The first job is the `network bringup` job. This job’s purpose is to simply use vagrant to build out the rest of the simulation network beyond simply the out of band management network.

The other job that runs in this stage is the NetQ provisioning job. This job is simple in its steps, but takes the longest amount of time. This stage installed NetQ cloud from its two component tarball files. Bringing the out of band management network up first, allows us to immediately move into provisioning the NetQ Cloud server while the rest of the network is also being created and built.
###### provision simulation
This stage is responsible for running ansible playbooks on the oob-mgmt-server that provision the network with the changes that have been made to the branch.
###### test simulation
This stage also has two jobs that run in parallel. Testing is performed using NetQ and then additional network testing can be performed from the oob-mgmt-server. Each testing runs as it’s own job and thus both may run at the same time, in parallel.
###### cleanup simulation
In this final stage, the NetQ Cloud premises is cleaned up for the next simulation and the simulation itself is destroyed.
##### General Procedure - Customize CI Pipeline
With Gitlab CI, the .gitlab-ci.yml file describes the CI Pipeline, its jobs and what each job does. This section focuses on reusing a .gitlab-ci.yml file from Cumulus Production Ready Automation for your own use.

The included example .gitlab-ci.yml files have been created and defined specifically to separate out the complex logic of each job from the pipeline and job definition itself. As you will see in the provided .gitlab-ci.yml examples, each job has a single `script:` line. Each single `script:` line is simply a call to another shell script. This makes the .gitlab-ci.yml file neater, cleaner, and easier to start from.

As a starting point, use a .gitlab-ci.yml file from one of the golden standard demo topologies such as EVPN Symmetric mode as the starting point for your .gitlab-ci.yml file. The .gitlab-ci.yml file from the Cumulus Linux Reference Topology cldemo2 does not contain a provision stage where we call an ansible playbook to deploy a network configuration.

In our examples on Gitlab, we make use of [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to package the the base CI/CD scripts and the Cumulus Reference Topology itself (the Vagrantfile). This is only due to the need for reuse, but for production networks, this can all be packaged together in the same project. We do not normally recommend using a submodule unless there will be shared code across multiple projects. 

When git submodules are not in use for the project, the `variables:` key in a job can be removed. It is only required when the project is using a submodule.
In the following example, we would be able to remove `variables:` and it’s children.
```
prep:
  stage: prep simulation environment
  variables:
    GIT_SUBMODULE_STRATEGY: recursive
  script:
    - bash ./cldemo2/ci-common/prep.sh
  only:
    - /^dev.*$/
```

This yaml output can be modified to be
```
prep:
  stage: prep simulation environment
  script:
    - bash ./cldemo2/ci-common/prep.sh
  only:
    - /^dev.*$/
```

{{<notice info>}}
Remove these two lines for each job when working from our .gitlab-ci.yml examples if you are not using any submodules in your project.
{{</notice>}}

Lastly, for each job that is defined in the .gitlab-ci.yml file, check the `script:` lines to ensure that the path is correct to each shell script. Note that, in our published Production Ready Automation examples, the paths to the shell scripts, are inside of the cldemo2 submodule.

#### Overview for Adding/Enabling CI/CD to your existing Gitlab project

There are many ways to structure the code for CI/CD in your project that may be simpler for your use case. If you intend on using the provided example’s model of calling discrete and modular bash scripts for each job, a high level overview of implementing and enabling CI for your project is as follows:

1. Plan a permanent dedicated gitlab-runner simulation-host machine. Review system requirements and package dependencies.
2. Install the gitlab-runner and package dependencies (see {{<link text="Appendix B" title="#Appendix B" >}})
3. {{<link text="Register gitlab runner to the project" title="#Installing and registering the gitlab-runner to your project" >}}. Pause the gitlab-runner on the project until the rest of the supporting CI/CD scripts are in place. Disable shared and public runners for the project.
4. Evaluate the example CI pipeline design & stages. Use .gitlab-ci.yml file as an example.
5. Place your .gitlab-ci.yml file in the root of your project
6. Determine the CI scripts that are required for each job from your .gitlab-ci.yml file.
7. Create a folder to contain the CI scripts for your CI jobs. This is the `ci-common` scripts directory in the `cldemo2` project
8. Populate your project’s CI scripts folder with the scripts called by the .gitlab-ci.yml file jobs (in the script: block).
9. Resume your gitlab runner on the project and start testing your CI pipeline by making commits and pushing to your project.

## Appendix A 
### Package dependency install script without Gitlab CI/CD
```
#!/bin/bash
#
#Debian/Ubuntu setup script
#run with/as sudo/root
#
apt-get update -y
apt-get install -qy libvirt-bin libvirt-dev qemu-utils qemu git
addgroup libvirtd
usermod -a -G libvirtd <users-that-will-run-simulations>
wget https://releases.hashicorp.com/vagrant/2.2.7/vagrant_2.2.7_x86_64.deb
dpkg -i vagrant_2.2.7_x86_64.deb
vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp
```
## Appendix B
### Package dependency install script including Gitlab runner for CI/CD
```
#!/bin/bash
#
#Debian/Ubuntu setup script
#run with/as sudo/root
#
apt-get update -y
apt-get install -qy libvirt-bin libvirt-dev qemu-utils qemu git
addgroup libvirtd
usermod -a -G libvirtd <users-that-will-run-simulations>
wget https://releases.hashicorp.com/vagrant/2.2.7/vagrant_2.2.7_x86_64.deb
dpkg -i vagrant_2.2.7_x86_64.deb
vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp
# setup gitlab-runner
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
apt-get install gitlab-runner
sudo su - gitlab-runner
echo 'PATH=/usr/sbin:$PATH' >> ./.bashrc
adduser gitlab-runner libvirtd 
vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp
```
## Appendix C
### Cleaning up Stuck/Orphaned Libvirt Simulations from Vagrant

Occasionally errors may occur while using Vagrant or an in use project’s files may get deleted forgetting that the simulation may have still been running. In instances where either simulations are orphaned without the ability to use Vagrant to clean them up, it may be necessary to use virsh to destroy and clean them up. 

1. Use virsh list --all to inspect the system and see all running libvirt simulations. Find your libvirt ‘domains’ that you wish to clean-up. Simulations often have a common prefix from the same simulation that is normally the parent folder. For unmodified Cumulus Networks demos, the 
2. Use virsh to perform three operations on each virtual machine (libvirt domain) that you wish to cleanup.
    1. virsh destroy <name>
    2. virsh undefine <name>
    3. virsh vol-delete --pool default <name>.img
Use the script below to clean up all simulations that match a common pattern from `virsh list`. * Please use this with caution on servers with other simulations and in shared environments as it does not ask for confirmation and may delete machines you match accidentally! *
```
#for vm in $(virsh list --all | grep <match-pattern> | awk -F ' ' '{print$2}'); do virsh destroy $vm; virsh undefine $vm; virsh vol-delete --pool default $vm.img; done
```
