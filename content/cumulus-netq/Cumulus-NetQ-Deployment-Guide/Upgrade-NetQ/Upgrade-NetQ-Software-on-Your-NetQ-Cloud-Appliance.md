---
title: Upgrade NetQ Software on Your NetQ Cloud Appliance
author: Cumulus Networks
weight: 127
aliases:
 - /display/NETQ/Upgrade+the+NetQ+Appliance
 - /pages/viewpage.action?pageId=12321037
pageID: 12321037
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
This document describes the steps required to upgrade the NetQ Software (versions 2.1.0 through 2.2.1) installed and running on your NetQ Cloud Appliance to NetQ version 2.2.2.

{{%notice info%}}

Cumulus Networks recommends only upgrading NetQ during a network
maintenance window.

{{%/notice%}}

{{%notice note%}}

Events generated during the upgrade process will not be available in the
database. Once the upgrade process is complete, the NetQ Agents resynchronize with
the current state of the Host or Cumulus Linux switch with the NetQ or NetQ Cloud
Appliance.

{{%/notice%}}

## Prerequisites

Before you begin the upgrade process, please note the following:

  - Cumulus recommends upgrading your NetQ Agents to obtain the latest
    features and bug fixes, but it is not required.
  - The NetQ installer pod `netq-installer` should be up in either the
    *Containercreating* or *Running* state. The `netq-installer` pod
    state could also be *ContainerCreating*, in which case the host is
    initializing with the SSH keys.

{{%notice info%}}

Cumulus Networks recommends you install the NetQ or NetQ Cloud Appliance as part of an out-of-band management network to ensure it can monitor in-band network
issues without being affected itself.

{{%/notice%}}

## Perform an In-place Upgrade of Cumulus NetQ

An in-place upgrade is recommended for upgrades from Cumulus NetQ 2.2.1. If you are upgrading from NetQ 2.2.0 or earlier, a [disk image upgrade](#perform-a-disk-image-upgrade-of-Cumulus-NetQ) is recommended.

### In-place Upgrade Workflow
Upgrading NetQ involves backing up your data, downloading and installing the new version of NetQ software, restoring your NetQ data, and upgrading and configuring the NetQ Agents.

{{< figure src="/images/netq/upgrade-wkflow-in-place-cloud-nqcldappl-222.png"  width="500" >}}

### Install and Configure the CLI

The first step in upgrading NetQ software on your NetQ Cloud Appliance is to install and configure the CLI. This enables use of the new upgrade command.

1. Verify or edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.  

   ```
   cumulus@switch:~$ sudo nano /etc/apt/sources.list
   ...
   deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.2
   ...
   ```

2. Update the local `apt` repository, then install the NetQ apps  package on the switch.

   ```
   cumulus@switch:~$ sudo apt-get update
   cumulus@switch:~$ sudo apt-get install netq-apps
   ```

### Download and Install NetQ Software

1. Use the new CLI upgrade command to download and install the software in a single step.

```
cumulus@netq-appliance:~$ netq upgrade opta tarball download 2.2.2
2019-08-29 21:25:58.343212: opta-installer: Upgrading OPTA
2019-08-29 21:26:17.549618: opta-installer: Extracting tarball /mnt/installables/NetQ-2.2.2-opta.tgz
2019-08-29 21:26:38.427990: opta-installer: Checking for configkey
2019-08-29 21:26:38.991100: opta-installer: Upgrading netq-installer pod
2019-08-29 21:30:45.981703: opta-installer: Upgrading netq-opta pod
2019-08-29 21:35:47.161308: opta-installer: Validating upgrade
------------------------------
Successfully upgraded the opta
```

2. Confirm the upgrade was successful.

```
cumulus@netq-appliance:~$ cat /etc/app-release
APPLIANCE_VERSION=2.2.2
APPLIANCE_MANIFEST_HASH=a7f3cda
APPLIANCE_NAME="NetQ Cloud Appliance"

cumulus@netq-appliance:~$ dpkg -l | egrep "netq-agent|netq-apps"
ii  netq-agent                        2.2.2-cl3u20~156694d619.810054e      amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
ii  netq-apps                         2.2.2-cl3u20~156694d619.810054e      amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux
```

{{%notice info%}}

If you have changed the IP Address or hostname of your appliance, you need to
re-register this address with the Kubernetes containers before you can
continue.

1.  Reset all Kubernetes administrative settings. Run the command twice
    to make sure all directories and files have been reset.  
    ```
    cumulus@switch:~$ sudo kubeadm reset -f  
    cumulus@switch:~$ sudo kubeadm reset -f
    ```

2.  Remove the Kubernetes configuration.  
    ```
    cumulus@switch:~$ sudo rm /home/cumulus/.kube/config
    ```

3.  Reset the NetQ Platform install daemon.  
    ```
    cumulus@switch:~$ sudo systemctl reset-failed
    ```

4.  Reset the Kubernetes service.  
    ```
    cumulus@switch:~$ sudo systemctl restart cts-kubectl-config
    ```  
    **Note**: Allow 15 minutes for the prompt to return.

{{%/notice%}}

### Verify the Operation of NetQ

1. Run the `netq show opta-health` command to verify all applications are
    operating properly. Please allow 10-15 minutes for all applications to come up and report their status.

     ```
     cumulus@<netq-appliance>:~$ netq show opta-health
     OPTA is healthy
     ```         

     {{%notice note%}}

If the results do not indicate the server is healthy after 30 minutes, open a [support ticket](https://cumulusnetworks.com/support/file-a-ticket/) and attach the output of the `opta-support` command.

      {{%/notice%}}

3.  Verify that NTP is configured and running. NTP operation is critical
    to proper operation of NetQ. Refer to [Setting Date and Time](/cumulus-linux/System-Configuration/Setting-Date-and-Time/) in the *Cumulus Linux User Guide* for details and instructions.

4.  Continue the NetQ installation by loading the NetQ Agent on each switch or host you want to monitor. Refer to [Upgrade the NetQ Agents and CLI on Your Switches and Hosts](#upgrade-the-netq-agents-and-cli-on-your-switches-and-hosts) for instructions.

## Perform a Disk Image Upgrade of Cumulus NetQ

A disk image upgrade is recommended for upgrades from Cumulus NetQ 2.2.0 or earlier. An [in-place upgrade](#perform-an-in-place-upgrade-of-Cumulus-NetQ) is recommended for upgrades from NetQ 2.2.1.

### Disk Image Upgrade Workflow
Upgrading NetQ involves backing up your data, downloading and installing the new version of NetQ software, restoring your NetQ data, and upgrading and configuring the NetQ Agents.

{{< figure src="/images/netq/upgrade-wkflow-disk-img-cloud-nqcldappl-222.png" width="700" >}}

### Backup Your NetQ Data

If you want to retain the data you have already collected with an earlier version of Cumulus NetQ, you need to backup that data as follows:

Run the provided backup script to create a backup file in `/opt/<backup-directory>` being sure to replace the `backup-directory` option with the name of the directory you want to use for the backup file.
 ```
 cumulus@<netq-appliance>:~$ ./backuprestore.sh --backup --localdir /opt/<backup-directory>
 ```
The file is named `netq_master_snapshot_<timestamp>.tar.gz`. For more detail about the script and the back up process, refer to [Backup NetQ](../../Backup-and-Restore-NetQ/Backup-NetQ).

### Download the NetQ Software Image

The next step is to obtain the new image.

1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.

2.  Click *2.2* from the **Version** list box, and then select
  *2.2.2* from the submenu.

3.  From the **Hypervisor/Platform** list box, select *Appliance (Cloud)*.

      {{< figure src="/images/netq/NetQ-22-Download-Options-222.png" width="500" >}}

4.  Click **Download**.

      {{< figure src="/images/netq/netq-22-nqappl-dwnld-222.png" width="200" >}}

### Install the Image Using ONIE

ONIE is an open source project (equivalent to PXE on servers) that enables the installation of network operating systems (NOS) on a bare metal switch. Use the `onie-install -a -i <image-location>` command to install the image from the web or local file.

- This example installs the image from a web server, then reboots the appliance.

```
cumulus@netq-platform:~$ sudo onie-install -a -i http://10.0.1.251/cumulus-netq-server-2.2.2-ts-amd64.bin && sudo reboot
```

- This example installs the image from a local file, then reboots the appliance.

```
cumulus@netq-platform:~$ sudo onie-install -a -i /home/<local-directory>/<path>/cumulus-netq-server-2.2.2-ts-amd64.bin && sudo reboot
```

Verify the release has been updated successfully.

```
cumulus@netq-platform:~$ cat /etc/app-release
APPLIANCE_VERSION=2.2.2
APPLIANCE_MANIFEST_HASH=a7f3cda
APPLIANCE_NAME="NetQ Cloud Appliance"

cumulus@netq-platform:~$ dpkg -l | egrep "netq-agent|netq-apps"
ii  netq-agent                        2.2.2-cl3u20~1566b48619.810054e      amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
ii  netq-apps                         2.2.2-cl3u20~1566b48619.810054e      amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux
```

### Restore Your NetQ Data

Restore the configuration files to the new release. Run the restore script being sure to replace the `backup-directory` option with the name of the directory where the backup file resides.

 ```
 cumulus@<netq-platform/netq-appliance>:~$ ./backuprestore.sh --restore --localdir /opt/<backup-directory>
 ```

This uses the `netq_master_snapshot_<timestamp>.tar.gz` file to restore your data. For more detail about the script and the restoration process, refer to [Restore NetQ](../../Backup-and-Restore-NetQ/Restore-NetQ).

### Verify the Operation of NetQ on Your Appliance

Verify all applications and services are operating properly.
   ```
   cumulus@netq-platform:~$ netq show opta-health
   OPTA is healthy
   ```
{{%notice note%}}

If the results do not indicate the server is healthy after 30 minutes, open a [support ticket](https://cumulusnetworks.com/support/file-a-ticket/) and attach the output of the `opta-support` command.

{{%/notice%}}

### Install and Configure the CLI

The CLI communicates through the API gateway in the NetQ Cloud. To access and configure the CLI on your NetQ Cloud server you will need your username and password to access the NetQ UI to generate an access-key and secret-key. Your credentials and NetQ Cloud addresses were provided by Cumulus Networks via an email titled *Welcome to Cumulus NetQ!*

To configure CLI access:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. From the Main Menu, select *Management* in the **Admin** column.

      {{< figure src="/images/netq/main-menu-mgmt-selected.png" width="400">}}

4. Click **Manage** on the User Accounts card.
5. Select your user and click **Generate AuthKeys**.

      {{< figure src="/images/netq/generate-auth-keys.png" width="700">}}

6. Copy these keys to a safe place.

      {{%notice info%}}
The secret key is only shown once. If you don't copy these, you will need to regenerate them and reconfigure CLI access.

In version 2.2.1 and later, you can save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can store this file wherever you like, but you *must* name the file *credentials.yml*, and make sure it has the following format:
```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```
      {{%/notice%}}

7. Configure access to the CLI:
   - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.
   ```
   cumulus@netq-platform:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-platform:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```
   - In NetQ 2.2.1 or later, if you have created a *credentials.yml* file as noted in the previous step, run the following commands. Be sure to include the **full path** the to file.
   ```
   cumulus@netq-platform:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-platform:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

Now that the NetQ Cloud Appliance is configured, continue with the upgrade by upgrading the NetQ Agents and CLI on your switches and hosts. Follow the instructions in the next section.

## Upgrade the NetQ Agents and CLI on Your Switches and Hosts

The NetQ Agent should be upgraded on each of the existing nodes you want
to monitor. The node can be a:

  - Switch running Cumulus Linux version 3.3.2 or later
  - Server running Red Hat RHEL 7.1, Ubuntu 16.04, Ubuntu 18.04 (NetQ 2.2.2 or later), or CentOS 7
  - Linux virtual machine running any of the above Linux operating
    systems

To upgrade the NetQ Agent you need to install the OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent, the NetQ command
line interface (CLI), and the NetQ library. The library contains modules
used by both the NetQ Agent and the CLI.

  - [Upgrade NetQ Agent on a Cumulus Linux Switch](#upgrade-netq-agent-on-a-cumulus-linux-switch)
  - [Upgrade NetQ Agent on an Ubuntu Server](#upgrade-netq-agent-on-an-ubuntu-server)
  - [Upgrade NetQ Agent on a Red Hat or CentOS Server](#upgrade-netq-agent-on-a-red-hat-or-centos-server)

{{%notice info%}}

If your network uses a proxy server for external connections, you should first
[configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/),
so `apt-get` can access the meta package on the Cumulus Networks repository.

{{%/notice%}}

###  Upgrade NetQ Agent on a Cumulus Linux Switch

A simple process installs the NetQ Agent on a Cumulus switch.

1.  Edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.
    **Note** that NetQ has a separate repository from Cumulus Linux.  

        cumulus@switch:~$ sudo nano /etc/apt/sources.list
        ...
        deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.2
        ...

    {{%notice tip%}}

The repository `deb http://apps3.cumulusnetworks.com/repos/deb
    CumulusLinux-3 netq-latest` can be used if you want to always
    retrieve the latest posted version of NetQ.

    {{%/notice%}}

2.  Update the local `apt` repository, then install the NetQ meta
    package on the switch.

        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install cumulus-netq

3.  Verify the upgrade.

```
cumulus@netq-platform:~$ dpkg -l | egrep "netq-agent|netq-apps"
ii  netq-agent                        2.2.2-cl3u20~1567948619.810054e      amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
ii  netq-apps                         2.2.2-cl3u20~1567948619.810054e      amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux
```

4.  Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl restart rsyslog.service

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.

      {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf-interface). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

      {{%/notice%}}

      In this example, the IP address for the agent server is *192.168.1.254*.

         cumulus@switch:~$ netq config add agent server 192.168.1.254
         cumulus@switch:~$ netq config restart agent

      This command updates the configuration in the `/etc/netq/netq.yml` file.

6.  Optionally, configure the switch or host to run the NetQ CLI.

      *For switches* **with** *Internet access:*

      - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.

   ```
   cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@switch:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

      - In NetQ 2.2.1 and later, if you have created a `credentials.yml` file during step 6 of [Install and Configure the CLI](#install-and-configure-the-cli), run the following commands. Be sure to include the **full path** to the file.

   ```
   cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@switch:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

      *For switches* **without** *Internet access:*

      A CLI proxy is part of the NetQ Cloud image with NetQ 2.2.2 and later. If your switches and hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud server to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud server. Run the following commands, using the IP address of your NetQ Cloud server:

   ```
   cumulus@switch:~$ netq config add cli server <netq-cloud-server-ip-addr>
   Updated cli server <netq-cloud-server-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@switch:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

7.  Repeat these steps for each Cumulus switch, or use an automation
            tool to install and configure the NetQ Agent on multiple Cumulus Linux switches.

### Upgrade NetQ Agent on an Ubuntu Server

To install the NetQ Agent on an Ubuntu server:

1.  Reference and update the local `apt` repository.

      ```
      root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
      ```

2.  Verify or add the relevant Ubuntu repository:

    <details><summary>Ubuntu 16.04</summary>
    Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add
    the following line (if not already present):

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...
    </details>
    <details><summary>Ubuntu 18.04</summary>
    Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add
    the following line:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
        ...
    </details>
      {{%notice note%}}

The use of `netq-latest` in this example means that a `get` to the
            repository always retrieves the latest version of NetQ, even in the
            case where a major version update has been made. If you want to keep
            the repository on a specific version — such as `netq-2.2` — use that
            instead.

      {{%/notice%}}

3.  Install the meta package on the server.

         root@ubuntu:~# apt-get update
         root@ubuntu:~# apt-get install cumulus-netq

4.  Verify the upgrade.

         root@ubuntu:~$ dpkg -l | grep netq
         ii  cumulus-netq                      2.2.2-cl3u17~155d3c5432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
         ii  netq-agent                        2.2.2-cl3u17~1559c814b1.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
         ii  netq-apps                         2.2.2-cl3u17~1559c814b1.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.

      {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf-interface). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific    Port](#configure-the-agent-to-communicate-over-a-specific-port).

      {{%/notice%}}

      In this example, the IP address for the agent server is *192.168.1.254*.

      ```
      user@ubuntu:~# netq config add agent server 192.168.1.254
      Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
      user@ubuntu:~# netq config restart agent
      ```
      This command updates the configuration in the `/etc/netq/netq.yml` file.

6.  Optionally, configure the switch or host to run the NetQ CLI.

       *For switches* **with** *Internet access:*

       - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.

    ```
    root@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

       - In NetQ 2.2.1 and later, if you have created a `credentials.yml` file as noted in during step 6 of [Install and Configure the CLI](#install-and-configure-the-cli), run the following commands. Be sure to include the **full path** the to file.

    ```
    root@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

       *For switches* **without** *Internet access:*

       A CLI proxy is part of the NetQ Cloud image with NetQ 2.2.2 and later. If your switches and hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud server to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud server. Run the following commands, using the IP address of your NetQ Cloud server:

    ```
    root@ubuntu:~# netq config add cli server <netq-cloud-server-ip-addr>
    Updated cli server <netq-cloud-server-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

7.  Repeat these steps for each switch/host running Ubuntu, or use an
            automation tool to install and configure the NetQ Agent on multiple hosts.

### Upgrade NetQ Agent on a Red Hat or CentOS Server

To upgrade the NetQ Agent on a Red Hat or CentOS server:

1.  Reference and update the local `yum` repository.

         root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
         root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1` flag for the two NetQ repositories.

         [cumulus@firewall-2 ~]$ cat /etc/yum.repos.d/cumulus-host-el.repo
         [cumulus-arch-netq-2.2]
         name=Cumulus netq packages
         baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/$basearch
         gpgcheck=1
         enabled=1

         [cumulus-noarch-netq-2.2]
         name=Cumulus netq architecture-independent packages
         baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/noarch
         gpgcheck=1
         enabled=1

         [cumulus-src-netq-2.2]
         name=Cumulus netq source packages
         baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/src
         gpgcheck=1
         enabled=1

3.  Update the NetQ meta packages on the server.

         root@rhel7:~# yum update cumulus-netq.x86_64

4.  Verify the upgrade.

         root@rhel7:~$ yum list installed | grep netq
         ii  cumulus-netq                      2.2.2-cl3u17~155c3c5432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
         ii  netq-agent                        2.2.2-cl3u17~1559b814d1.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
         ii  netq-apps                         2.2.2-cl3u17~1559b814d1.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.

      {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf-interface). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

      {{%/notice%}}

      In this example, the IP address for the agent server is *192.168.1.254*.

         root@rhel7:~# netq config add agent server 192.168.1.254
         Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
         root@rhel7:~# netq config restart agent

6.  Optionally, configure the switch or host to run the NetQ CLI.

       *For switches* **with** *Internet access:*

       - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.

    ```
    root@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

       - In NetQ 2.2.1 and later, if you have created a `credentials.yml` file as noted in during step 6 of [Install and Configure the CLI](#install-and-configure-the-cli), run the following commands. Be sure to include the **full path** the to file.

    ```
    root@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

       *For switches* **without** *Internet access:*

       A CLI proxy is part of the NetQ Cloud image with NetQ 2.2.2 and later. If your switches and hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud server to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud server. Run the following commands, using the IP address of your NetQ Cloud server:

    ```
    root@ubuntu:~# netq config add cli server <netq-cloud-server-ip-addr>
    Updated cli server <netq-cloud-server-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

7.  Repeat these steps for each host running Red Hat or CentOS, or use an  automation tool to install and configure the NetQ Agent on multiple hosts.

## Configure Optional NetQ Agent Settings

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. The code examples shown in this section illustrate how to
configure the NetQ Agent on a Cumulus switch, but it is exactly the same
for the other type of nodes. If you have already configured these
settings, you do not need to do so again.

  - [Configuring the Agent to Use a
    VRF](http://docs.cumulusnetworks.com#AgentVRF)
  - [Configuring the Agent to Communicate over a Specific
    Port](http://docs.cumulusnetworks.com#port)

### Configure the Agent to Use a VRF Interface

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the NetQ Platform only via a
[VRF](/cumulus-linux/Layer-3/Virtual-Routing-and-Forwarding-VRF/), including a
[management VRF](/cumulus-linux/Layer-3/Management-VRF/). To do so, you need to
specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the NetQ Platform over it, configure the agent like this:

    cumulus@leaf01:~$ netq config add agent server 192.168.1.254 vrf mgmt
    cumulus@leaf01:~$ netq config add cli server 192.168.254 vrf mgmt

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent
    cumulus@leaf01:~$ netq config restart cli

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 8981 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@switch:~$ netq config add agent server 192.168.1.254 port 7379

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent

## Upgrade Tips

After you have upgraded NetQ, if you find that some issues remain,
review these commonly encountered scenarios. If NetQ is still not
operating as expected, please open a [support
ticket](https://cumulusnetworks.com/support/file-a-ticket/) with a
detailed description of your issues.

### No IP Address Assigned to the NetQ Cloud Appliance on Boot

A user did not configure an IP address when the system was first booted.
Later the user assigned an IP address to eth0, but the NetQ appliance
does not appear to be functioning.

You must reset  the install daemon and restart the Kubernetes service.
Follow these steps:

1.  Reset the NetQ Appliance install daemon.

        cumulus@switch:~$ sudo systemctl reset-failed

2.  Restart the Kubernetes service.

        cumulus@switch:~$ sudo systemctl restart cts-kubectl-config
