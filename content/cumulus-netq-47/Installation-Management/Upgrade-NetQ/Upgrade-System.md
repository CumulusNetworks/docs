---
title: Upgrade NetQ Virtual Machines
author: NVIDIA
weight: 410
toc: 4
---

This page describes how to upgrade your NetQ virtual machines. Note that the upgrade instructions vary depending on NetQ version you’re currently running.

<!--

If your current NetQ version is:

- **4.2.0 or earlier**: perform an incremental {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="upgrade to version 4.3.0">}} before you {{<link title="Upgrade NetQ" text="back up your data">}} and perform a new installation of NetQ 4.5.0. Then {{<link title="Upgrade NetQ Virtual Machines/#upgrading-from-netq-4.5.0-or-later" text="follow the steps below">}}.
- **4.3.0 to 4.4.1**: {{<link title="Upgrade NetQ Virtual Machines/#upgrading-from-netq-4.4.1-or-earlier" text="follow these steps">}}.
- **4.5.0 or later**: {{<link title="Upgrade NetQ Virtual Machines/#upgrading-from-netq-4.5.0-or-later" text="Follow these steps">}}.

-->

## Upgrading from NetQ 4.4.1 or Earlier

Upgrading to NetQ 4.7.0 from a NetQ version below 4.5.0 requires a new installation of the NetQ virtual machine. Perform the following steps to upgrade:

1. For on-premises deployments, {{<link title="Back Up and Restore NetQ" text="back up your existing NetQ data">}}. NetQ Cloud Appliances and VMs create backups automatically.

2. Follow the {{<link title="Install the NetQ System" text="installation process">}} for your deployment model.

3. For on-premises deployments, {{<link title="Back Up and Restore NetQ/#restore-your-netq-data" text="restore your NetQ data">}}.


## Upgrading from NetQ 4.5.0 or Later

You can upgrade to NetQ 4.7.0 if your deployment is currently running version 4.5.0 or later.
### Back up your NetQ Data

{{<link title="Back Up and Restore NetQ" text="Backing up your NetQ data">}} is an optional step for on-premises deployments. NetQ cloud deployments create backups automatically.

### Update NetQ Debian Packages

1. Update `/etc/apt/sources.list.d/cumulus-netq.list` to netq-4.7:

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb focal netq-4.7
    ```

2. Update the NetQ `debian` packages.

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 https://apps3.cumulusnetworks.com/repos/deb focal InRelease [13.8 kB]
    Get:2 https://apps3.cumulusnetworks.com/repos/deb focal/netq-4.7 amd64 Packages [758 B]
    Hit:3 http://archive.ubuntu.com/ubuntu focal InRelease
    Get:4 http://security.ubuntu.com/ubuntu focal-security InRelease [88.7 kB]
    Get:5 http://archive.ubuntu.com/ubuntu focal-updates InRelease [88.7 kB]
    ...
    Reading package lists... Done
    ```

    ```
    cumulus@<hostname>:~$ sudo apt-get install -y netq-agent netq-apps
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    ...
    The following NEW packages will be installed:
    netq-agent netq-apps
    ...
    Fetched 39.8 MB in 3s (13.5 MB/s)
    ...
    Unpacking netq-agent (4.6.0-ub20.04u42~1682429296.e13e0426) ...
    ...
    Unpacking netq-apps (4.6.0-ub20.04u42~1682429296.e13e0426) ...
    Setting up netq-apps (4.6.0-ub20.04u42~1682429296.e13e0426) ...
    Setting up netq-agent (4.6.0-ub20.04u42~1682429296.e13e0426) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```


### Download the Upgrade Tarball

1. Download the relevant software.

    {{<netq-install/upgrade-image version="4.7">}}

2. Copy the file to the `/mnt/installables/` directory on your NetQ VM.
### Run the Upgrade

{{%notice note%}}

Perform the following steps using the `cumulus` user account.

{{%/notice%}}
#### Pre-installation Checks

Verify the following items before upgrading NetQ. For cluster deployments, verify steps 1 and 4 on all nodes in the cluster:

1. Confirm your VM is configured with 16 vCPUs. If your VM is configured with fewer than 16 vCPUs, power off your VM, reconfigure your hypervisor to allocate 16 vCPUs, then power the VM on before proceeding with the following steps.

2. Check if enough disk space is available before you proceed with the upgrade:

```
cumulus@<hostname>:~$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       248G   70G  179G  28% /
cumulus@netq-appliance:~$
```
NVIDIA recommends proceeding with the installation only if the `Use%` is less than 70%. You can delete previous software tarballs in the `/mnt/installables/` directory to regain some space. If you cannot decrease disk usage to under 70%, contact the NVIDIA support team.

3. Run the `netq show opta-health` command and check that all pods are in the `READY` state. If the pods are in a state other than `READY`, contact the NVIDIA support team.

4. Check if the certificates have expired:

```
cumulus@<hostname>:~$ sudo grep client-certificate-data /etc/kubernetes/kubelet.conf | cut -d: -f2 | xargs | base64 -d | openssl x509 -dates -noout | grep notAfter | cut -f2 -d=
Dec 18 17:53:16 2021 GMT
cumulus@netq-appliance:~$
```

If the date in the above output is in the past, run the following commands before proceeding with the upgrade:
```
sudo cp /etc/kubernetes/kubelet.conf /etc/kubernetes/kubelet.conf.bak
sudo sed -i 's/client-certificate-data.*/client-certificate: \/var\/lib\/kubelet\/pki\/kubelet-client-current.pem/g' /etc/kubernetes/kubelet.conf
sudo sed -i 's/client-key.*/client-key: \/var\/lib\/kubelet\/pki\/kubelet-client-current.pem/g' /etc/kubernetes/kubelet.conf
sudo systemctl restart kubelet
```

Check if the kubelet process is running with the `sudo systemctl status kubelet` command before proceeding with the upgrade.

#### Upgrade Using the NetQ CLI

1. Prepare your NetQ VM for the upgrade:

Run the `netq bootstrap reset keep-db purge-images` command to clear the current install state and save the current database.  In cluster deployments, run this command on the master and all worker VMs.

2. Run the appropriate `netq install` command for your deployment.

{{<tabs "CLI Upgrade">}}

{{<tab "On-premises Deployments">}}

{{<tabs "On-prem standalone or cluster">}}

{{<tab "Standalone">}}

```
cumulus@<hostname>:~$ netq install standalone full interface <interface-name> bundle /mnt/installables/NetQ-4.7.0.tgz
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}

{{</tab>}}

{{<tab "Cluster">}}

Run the following command on your master node to initialize the cluster. Copy the output of the command to use on your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster master-init
   Please run the following command on all worker nodes:
   netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```

Run the `netq install cluster worker-init <ssh-key>` command from the output on each of your worker nodes.

Run the following command on your master node using the IP addresses of your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster full interface <interface-name> bundle /mnt/installables/NetQ-4.7.0.tgz workers <worker-1-ip> <worker-2-ip>
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "Cloud Deployments">}}

{{<tabs "Cloud standalone or cluster">}}

{{<tab "Standalone">}}

Run the following command on your NetQ cloud appliance with the config key obtained from the email you received from NVIDIA titled NetQ Access Link. You can also {{<link title="Configure Premises" text="obtain the configuration key using the NetQ UI">}}.

```
cumulus@<hostname>:~$ netq install opta standalone full interface <interface-name> bundle /mnt/installables/NetQ-4.7.0-opta.tgz config-key <your-config-key> [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}
{{</tab>}}

{{<tab "Cluster">}}

Run the following command on your master node to initialize the cluster. Copy the output of the command to use on your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster master-init
   Please run the following command on all worker nodes:
   netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```

Run the `netq install cluster worker-init <ssh-key>` command from the output on each of your worker nodes.

Run the following command on your master NetQ cloud appliance using the IP addresses of your worker nodes and the config key obtained from the email you received from NVIDIA titled NetQ Access Link. You can also {{<link title="Configure Premises" text="obtain the configuration key using the NetQ UI">}}.

```
cumulus@<hostname>:~$ netq install opta cluster full interface <interface-name> bundle /mnt/installables/NetQ-4.7.0-opta.tgz config-key <your-config-key> workers <worker-1-ip> <worker-2-ip> [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{</tabs>}}

3. After the upgrade command completes, confirm the upgrade was successful.

{{<tabs "TabID230" >}}

{{<tab "On-premises VM" >}}

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.6.0
    APPLIANCE_MANIFEST_HASH=1c3b0266c12606d2bd4ce482afa30d118a2c84a07850fda3376c716514edce05
    APPLIANCE_VERSION=4.6.0
    APPLIANCE_NAME=NetQ On-premises Appliance
    ```
{{</tab>}}

{{<tab "Cloud VM" >}}


    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.6.0
    APPLIANCE_MANIFEST_HASH=9a654b495a3175500f9a09f5af52e6f79c33706143a39f54b980a43a254fa2dd
    APPLIANCE_VERSION=4.6.0
    APPLIANCE_NAME=NetQ Cloud Appliance
    ```
{{</tab>}}

{{</tabs>}}