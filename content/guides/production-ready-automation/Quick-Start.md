---
title: Quick Start
weight: 41
---

This quick start provides a quick and easy way to run your own Vagrant, libvirt, and KVM server, with procedures on how to:

- Start a golden standard demo topology using a bash script
- Start the blank NVIDIA reference topology if you are looking to build configuration from scratch
- Destroy and end a simulation

To run a full reference topology *without* NetQ, you need 15104MB of memory. If you intend to run NetQ, you need 23296MB of memory. For complete system requirements, refer to {{<link text="Run the Production Ready Automation" title="Run Production Ready Automation" >}}.

{{%notice tip%}}

To take a *quick* look at an NVIDIA golden standard demo, use the NVIDIA simulation platform, Cumulus in the Cloud. The simulation platform has no system requirements or dependencies. Visit {{<exlink url="https://www.nvidia.com/en-us/networking/network-simulation/" text="Cumulus in the Cloud">}} to get a full blank slate reference topology. You can deploy any of the golden standard demos right from the UI with one click.

{{%/notice%}}

## Start a Golden Standard Demo Topology

The following procedure describes the easiest way to start a Production Ready automation demo using a bash script provided in the package. The bash script performs the following steps automatically:

- Checks if the NVIDIA reference topology submodule is present and attempts to download the reference topology if it is not present.
- Runs the `vagrant up` command for the out-of-band management network devices.
- Runs a series of `vagrant up` commands to bring up the rest of the network simulation.
- Runs the `vagrant scp` command to copy the network automation into the simulation.

To control which nodes start and in which order, and to save CPU and memory resources, you can run the simulation manually. Refer to {{<link text="Run the Production Ready Automation" title="Run Production Ready Automation" >}}.

To start a golden standard demo topology using a bash script:

1. From the {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle" text="Golden Turtle GitLab page">}}, select the demo topology that you want to use.

2. Run the `git clone` command for your selected Golden Turtle demo using the `--recurse-submodules` argument to also download the required base reference topology:

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

4. Run the `start-demo.sh` script. If you do not intent to use NetQ, add the `--no-netq` option.

    {{%notice note%}}

The out-of-band management network of the base NVIDIA reference topology includes an Ubuntu 18.04LTS system with additional CPU and memory resources for installing NetQ. NetQ is *not* a required element for any of the golden standard demos to function but is in the topology to provide power CI/CD testing, and to preview and test the NetQ functionality. If you do not intent to use NetQ, NVIDIA recommends that you do not start it in simulation to save an additional 8GB of memory.

{{%/notice%}}

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

     During this step, Vagrant starts and provisions the base simulation. It might take 15 or more minutes for this step to complete depending on the host machine and internet connection speed.

5. After the launch script succeeds, change to the `cldemo2/simulation` directory:

    ```
    user@host:~/dc_configs_vxlan_evpnsym# cd cldemo2/simulation/
    user@host:~/dc_configs_vxlan_evpnsym/cldemo2/simulation#
    ```

6. Run the `vagrant ssh oob-mgmt-server` command to enter the simulation onto the oob-mgmt-server. This is your jump system to reach the other devices in the network.

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

8. Run the Ansible playbook to configure your selected demo:

    {{%notice note%}}

You use the `-i` flag to specify the location of the Ansible inventory. This is a requirement, unless you move the inventory into a {{<exlink url="https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html" text="standard Ansible location">}}.

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

Check the `README.md` file on the selected demo repository for more information about the topology, such as IP addresses, and for a small guided tour of the specific technologies or architectures in the demo.

## Start a Blank Reference Topology

Every NVIDIA golden standard demo includes the NVIDIA reference topology as a submodule, which eliminates the need to clone the base reference topology project. <!-- For more information about submodules see the contributor’s guide. TODO: add link to contributor's guide -->

You can start the reference topology by itself if you want to build configuration from scratch or intend to start from a completely blank slate network topology.

1. Clone the NVIDIA reference topology (`cldemo2`):

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

3. Run the `start-blank-topology.sh` script to launch the simulation. If you do not intent to use NetQ, add the `--no-netq` option.

    ```
    user@host:~/cldemo2# ./start-blank-topology.sh --no-netq
    Starting OOB management devices
    Bringing machine 'oob-mgmt-switch' up with 'libvirt' provider...
    Bringing machine 'oob-mgmt-server' up with 'libvirt' provider...
    <output omitted for brevity>
    ```

    This step might take time depending on the host machine and internet connection speed.

4. After the launch script succeeds, change to the simulation directory:

    ```
    user@host:~/cldemo2# cd simulation/
    user@host:~/cldemo2/simulation#
    ```

5. Use the `vagrant ssh` command to SSH into the oob-mgmt-server. This is the jump system to access the rest of the simulation.

For more information about how to start developing and building onto this blank slate topology, refer to the `README.md` file for the NVIDIA reference topology GitLab project and the developer's guide.

## Destroy and End a Simulation

To destroy *all* the systems in the simulation, run the `vagrant destroy -f` command from the `simulation` folder:

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

To destroy an individual system, specify the system name in the `vagrant destroy` command:

```
user@host:~/cldemo2/simulation# vagrant destroy server08 -f
==> server08: Removing domain...
user@host:~/cldemo2/simulation#
```
