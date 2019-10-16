---
title: Upgrade NetQ Software on Your NetQ Cloud Appliance
author: Cumulus Networks
weight: 131
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

{{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/upgrade-wkflow-in-place-cloud-nqcldappl-222.png"  width="500" >}}

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
Upgrading NetQ involves downloading and installing the new version of NetQ software, and upgrading and configuring the NetQ Agents.

{{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/upgrade-wkflow-disk-img-cloud-nqcldappl-222.png" width="700" >}}

### Download the NetQ Software Image

The next step is to obtain the new image.

1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.

2.  Click *2.2* from the **Version** list box, and then select
  *2.2.2* from the submenu.

3.  From the **Hypervisor/Platform** list box, select *Appliance (Cloud)*.

      {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/NetQ-22-Download-Options-222.png" width="500" >}}

4.  Click **Download**.

      {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/netq-22-nqappl-dwnld-222.png" width="200" >}}

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

      {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/main-menu-mgmt-selected.png" width="400">}}

4. Click **Manage** on the User Accounts card.
5. Select your user and click **Generate AuthKeys**.

      {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/generate-auth-keys.png" width="700">}}

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

Now that the NetQ Cloud Appliance is configured, continue with the upgrade by upgrading the NetQ Agents and CLI on your switches and hosts. Follow the instructions in [Install NetQ Agents and CLI on Your Switches](../../Install-NetQ/Install-NetQ-Agents-and-CLI-on-Switches).

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
