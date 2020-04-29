---
title: Quick Start
author: Cumulus Networks
weight: 20
product: Cumulus Networks Guides
version: "1.0"
draft: true
---
To take a *quick* look at a Cumulus Networks golden standard demo, use our simulation platform, Cumulus In the Cloud. The simulation platform has no system requirements or dependencies. Visit [Cumulus In the Cloud](https://cumulsunetworks.com/citc) to get a full blank slate Cumulus Linux reference topology; you can even one-click deploy any of the golden standard demos right from the UI.

{{%notice info%}}

Ensure that all system dependencies are satisfied first. See {{<link url="User-Guide#software-requirements" text="Software Requirements">}} for more information.

{{%/notice%}}

The memory requirements of a full cldemo2 topology are:

| Deployment    | Memory      |
| ------------- |-------------|
| With NetQ     | 23296MB     |
| Without NetQ  | 15104MB     |

## Start a Golden Standard Demo Topology

An Ubuntu 18.04LTS box with additional CPU and memory resources for installing NetQ is included in the out of band management network of the base Cumulus Linux reference topology. NetQ is not a required element for any of the golden standard demos to properly function. NetQ is used in the topology to power CI/CD testing and to preview and test the NetQ functionality. If you do not intent to use NetQ, we recommended you do not start it in simulation to save an additional 8GB of memory.

1. Select the demo topology that you want to use from the {{% exlink text="Golden Turtle Gitlab page" url="https://gitlab.com/cumulus-consulting/goldenturtle" %}}.

2. Perform a git clone for your selected Golden Turtle demo using the `--recurse-submodules` argument to also download the required base Cumulus Reference Simulation Topology:

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

3. Change to the directory created in the previous step. The directory name matches the name of the project from the git clone operation.

    ```
    user@host:~# cd dc_configs_vxlan_evpnsym/
    user@host:~/dc_configs_vxlan_evpnsym#
    ```

4. Run the `start-demo.sh` script. If you do not intent to use the NetQ telemetry server, use the`--no-netq` option to skip booting the server.

    During this step, Vagrant starts and provisions the base simulation. It might take about 15 or more minutes for this step to complete depending on the host machine and internet connection speed.

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

5. After the launch script succeeds, change to the `cldemo2/simulation` directory:

    ```
    user@host:~/dc_configs_vxlan_evpnsym# cd cldemo2/simulation/
    user@host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation#
    ```

6. Run the `vagrant ssh oob-mgmt-server` command to enter the simulation onto the oob-mgmt-server. This is your jump box to reach the other devices in the network.

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

7. Change to the automation directory:

    ```
    vagrant@oob-mgmt-server:~$ cd automation/
    vagrant@oob-mgmt-server:~/automation$
    ```

8. Run the ansible playbook to configure your selected demo:

    {{%notice note%}}

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

Check the `README.md` on your selected demo repo for more information about that specific topology, such as IP addresses and for a small guided tour of the specific technologies or architectures in the demo.

## Start the Blank Cumulus Reference Topology

Starting the reference topology by itself is not normally required unless you are looking to build configuration from scratch or intend to start from a completely blank slate network topology.

The Cumulus Linux Reference Topology is included as a submodule in all of the Cumulus Networks golden standard demos. This eliminates the need to clone the base reference topology project. For more information about submodules see the contributor’s guide. <!-- TODO: add link to contributor's guide -->

1. Clone the cldemo2 Cumulus Linux Reference topology:

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

2. Change to the `cldemo2` directory created by the previous step:

    ```
    user@host:~# cd cldemo2/
    user@host:~/cldemo2#
    ```  

3. Run the `start-blank-topology.sh` script to launch the simulation. Optionally, you can use the `--no-netq` argument to skip loading the 8GB 4 vCPU netq-ts box, if you do not intent to use it.

    ```
    user@host:~/cldemo2# ./start-blank-topology.sh --no-netq
    Starting OOB management devices
    Bringing machine 'oob-mgmt-switch' up with 'libvirt' provider...
    Bringing machine 'oob-mgmt-server' up with 'libvirt' provider...
    <output omitted for brevity>
    ```

    This step might take time depending on internet connection speed and host machine.

4. After the launch script succeeds, change to the simulation directory:

    ```
    user@host:~/cldemo2# cd simulation/
    user@host:~/cldemo2/simulation#
    ```

5. Use the `vagrant ssh` command to ssh into the oob-mgmt-server. This is the jump box to access the rest of the simulation.

Refer to the `README.md` for the Cumulus Linux Reference Topology Gitlab project and the developers guide for more information about how to start developing and building onto this blank slate topology.

## Destroy and End a Simulation

From the `simulation` folder, run the `vagrant destroy -f` command:

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

To destroy individual systems or VMs, specify the system or VM names in the `vagrant destroy` command:

```
user@host:~/cldemo2/simulation# vagrant destroy server08 -f
==> server08: Removing domain...
user@host:~/cldemo2/simulation#
```
