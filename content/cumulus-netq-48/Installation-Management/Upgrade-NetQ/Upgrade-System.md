---
title: Upgrade NetQ Virtual Machines
author: NVIDIA
weight: 410
toc: 4
---

This page describes how to upgrade your NetQ virtual machines. Note that the upgrade instructions vary depending on NetQ version you’re currently running.

For deployments running:

- 4.7.0, 4.6.0, or 4.5.0: {{<link title="Upgrade NetQ Virtual Machines/#upgrading-from-netq-4.7,-4.6,-or-4.5" text="upgrade directly">}} to NetQ 4.8.0
- 4.4.1, 4.4.0, or 4.3.0: {{<link title="Back Up and Restore NetQ/" text="back up your NetQ data">}} and perform a {{<link title="Install NetQ" text="new installation of NetQ 4.8.0">}}
- 4.2.0 or earlier: upgrade incrementally {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="to version 4.3.0">}}. Then {{<link title="Back Up and Restore NetQ/#back-up-netq-4.4.1-or-earlier" text="back up your NetQ data">}} and perform a {{<link title="Install NetQ" text="new installation of NetQ 4.8.0">}}.

## Upgrading from NetQ 4.7, 4.6, or 4.5

You can upgrade directly to NetQ 4.8.0 if your deployment is currently running version 4.5.0, 4.6.0 or 4.7.0.
### Back up your NetQ Data

Before you upgrade, you can {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}}. This is an optional step for on-premises deployments. NVIDIA automatically creates backups for NetQ cloud deployments.

### Update NetQ Debian Packages

1. Update `/etc/apt/sources.list.d/cumulus-netq.list` to netq-4.8:

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb focal netq-4.8
    ```

2. Update the NetQ `debian` packages. In cluster deployments, update the packages on the master and all worker nodes.

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 https://apps3.cumulusnetworks.com/repos/deb focal InRelease [13.8 kB]
    Get:2 https://apps3.cumulusnetworks.com/repos/deb focal/netq-4.8 amd64 Packages [758 B]
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
    Unpacking netq-agent (4.7.0-ub20.04u43~1690981360.9d32c7a0) ...
    ...
    Unpacking netq-apps (4.7.0-ub20.04u43~1690981360.9d32c7a0) ...
    Setting up netq-apps (4.7.0-ub20.04u43~1690981360.9d32c7a0) ...
    Setting up netq-agent (4.7.0-ub20.04u43~1690981360.9d32c7a0) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```


### Download the Upgrade Software

1. Download the upgrade tarball.

    {{<netq-install/upgrade-image version="4.8">}}

2. Copy the tarball to the `/mnt/installables/` directory on your NetQ VM.

<!--

3. For on-premises deployments, download the configuration backup script, `backup_restore_configs.py`:

<p style="text-indent: 40px; display:inline">a. On the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}, log in to your account.<br></p>
<p style="text-indent: 40px; display:inline">b. Select <b>NVIDIA Licensing Portal</b>.<br></p>
<p style="text-indent: 40px; display:inline">c. Select <b>Software Downloads</b> from the menu.<br></p>
<p style="text-indent: 40px; display:inline">d. Click <b>Product Family</b> and select <b>NetQ</b>.<br></p>
<p style="text-indent: 40px; display:inline">e. Locate the <b>NetQ SW 4.7.0 Upgrade Backup Restore Configs Script</b> file and select <b>Download</b>.<br></p>
<p style="text-indent: 40px; display:inline">f. If prompted, agree to the license agreement and proceed with the download.<br></p>

4.  For on-premises deployments, copy the `backup_restore_configs.py` script to `/home/cumulus/` on your NetQ server and change the permissions:

```
username@hostname:~$ scp ./backup_restore_configs.py cumulus@10.10.10.10:/home/cumulus/
username@hostname:~$ sudo chmod +x /home/cumulus/backup_restore_configs.py
```
-->

### Run the Upgrade

{{%notice note%}}

Perform the following steps using the `cumulus` user account.

{{%/notice%}}
#### Pre-installation Checks

Verify the following items before upgrading NetQ. For cluster deployments, verify steps 1 and 4 on all nodes in the cluster:

1. Confirm your VM is configured with 16 vCPUs. If your VM is configured with fewer than 16 vCPUs, power off your VM, reconfigure your hypervisor to allocate 16 vCPUs, then power the VM on before proceeding.

2. Check if there is sufficient disk space:

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

Confirm that the kubelet process is running with the `sudo systemctl status kubelet` command before proceeding with the upgrade.

#### Upgrade Using the NetQ CLI

Run the appropriate commands for your current version and deployment type:

{{<tabs "4.6.0 or 4.7.0 steps">}}

{{<tab "Upgrade from NetQ 4.7.0">}}

{{<tabs "CLI Upgrade-4.7">}}

{{<tab "On-premises Deployments">}}

{{<tabs "On-prem standalone or cluster-4.7">}}

{{<tab "Standalone">}}

```
cumulus@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-4.8.0.tgz
```

{{</tab>}}

{{<tab "Cluster">}}

```
cumulus@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-4.8.0.tgz
```

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "Cloud Deployments">}}

{{<tabs "Cloud standalone or cluster-4.7">}}

{{<tab "Standalone">}}

Clear the current install state:

```
cumulus@<hostname>:~$ netq bootstrap reset
```

Run the following install command on your NetQ cloud VM with the config key obtained from the email you received from NVIDIA titled NetQ Access Link. You can also {{<link title="Configure Premises" text="obtain the configuration key using the NetQ UI">}}.

```
cumulus@<hostname>:~$ netq install opta standalone full interface <interface-name> bundle /mnt/installables/NetQ-4.8.0-opta.tgz config-key <your-config-key> [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}

{{</tab>}}

{{<tab "Cluster">}}

Clear the current install state on your master node:

```
cumulus@<hostname>:~$ netq bootstrap reset
```

Run the following command on your master node to initialize the cluster. Copy the output of the command to use on your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster master-init
   Please run the following command on all worker nodes:
   netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```

Run the `netq install cluster worker-init <ssh-key>` command from the output on each of your worker nodes.

Run the following command on your master NetQ cloud VM using the IP addresses of your worker nodes and the config key obtained from the email you received from NVIDIA titled NetQ Access Link. You can also {{<link title="Configure Premises" text="obtain the configuration key using the NetQ UI">}}.

```
cumulus@<hostname>:~$ netq install opta cluster full interface <interface-name> bundle /mnt/installables/NetQ-4.8.0-opta.tgz config-key <your-config-key> workers <worker-1-ip> <worker-2-ip> [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "Upgrade from NetQ 4.6.0 or 4.5.0">}}

{{<tabs "CLI Upgrade-4.6">}}

{{<tab "On-premises Deployments">}}

{{<tabs "On-prem standalone or cluster-4.6">}}

{{<tab "Standalone">}}

Clear the install state and save the current database:

```
cumulus@<hostname>:~$ netq bootstrap reset keep-db purge-images
```

Run the install command to install the new tarball:

```
cumulus@<hostname>:~$ netq install standalone full interface <interface-name> bundle /mnt/installables/NetQ-4.8.0.tgz
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}

{{</tab>}}

{{<tab "Cluster">}}

Clear the install state on your master node and save the current database:

```
cumulus@<hostname>:~$ netq bootstrap reset keep-db purge-images
```

Run the following command on your master node to initialize the cluster. Copy the output of the command to use on your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster master-init
   Please run the following command on all worker nodes:
   netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```

Run the {{<link title="install/#netq-install-cluster-worker-init" text="netq install cluster worker-init <ssh-key>">}} command from the output on each of your worker nodes.

Next, run the {{<link title="install/#netq-install-cluster-full" text="netq install cluster full">}} command on your master node using the IP addresses of your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster full interface <interface-name> bundle /mnt/installables/NetQ-4.8.0.tgz workers <worker-1-ip> <worker-2-ip>
```

{{%notice note%}}
You can specify the IPv4 or IPv6 address instead of the interface name. Refer to the {{<link title="install/#netq-install-cluster-full" text="command line reference">}} for the full syntax.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "Cloud Deployments">}}

{{<tabs "Cloud standalone or cluster-4.6">}}

{{<tab "Standalone">}}

Clear the current install state:

```
cumulus@<hostname>:~$ netq bootstrap reset
```

Run the following install command on your NetQ cloud VM with the config key obtained from the email you received from NVIDIA titled NetQ Access Link. You can also {{<link title="Configure Premises" text="obtain the configuration key using the NetQ UI">}}.

```
cumulus@<hostname>:~$ netq install opta standalone full interface <interface-name> bundle /mnt/installables/NetQ-4.8.0-opta.tgz config-key <your-config-key> [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}
{{</tab>}}

{{<tab "Cluster">}}

Clear the current install state on your master node:

```
cumulus@<hostname>:~$ netq bootstrap reset
```

Run the following command on your master node to initialize the cluster. Copy the output of the command to use on your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster master-init
   Please run the following command on all worker nodes:
   netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```

Run the `netq install cluster worker-init <ssh-key>` command from the output on each of your worker nodes.

Run the following command on your master NetQ cloud VM using the IP addresses of your worker nodes and the config key obtained from the email you received from NVIDIA titled NetQ Access Link. You can also {{<link title="Configure Premises" text="obtain the configuration key using the NetQ UI">}}.

```
cumulus@<hostname>:~$ netq install opta cluster full interface <interface-name> bundle /mnt/installables/NetQ-4.8.0-opta.tgz config-key <your-config-key> workers <worker-1-ip> <worker-2-ip> [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

{{%notice note%}}
You can specify the IP address instead of the interface name. To do so, use `ip-addr <IP address>` in place of the interface referenced with `interface <interface-name>` above.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{</tabs>}}


Confirm the upgrade was successful:

{{<tabs "TabID230" >}}

{{<tab "On-premises VM" >}}

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.7.0
    APPLIANCE_MANIFEST_HASH=8869b5423dfcc441ea56a3c89e680b1b2ad61f6887edccb11676bac893073beb
    APPLIANCE_VERSION=4.7.0
    APPLIANCE_NAME=NetQ On-premises Appliance
    ```
{{</tab>}}

{{<tab "Cloud VM" >}}


    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.7.0
    APPLIANCE_MANIFEST_HASH=0f282bd6eb5ac43c6b7b7a2a0df42281b20912ffead1eb2ba8afafd5a428db7c
    APPLIANCE_VERSION=4.7.0
    APPLIANCE_NAME=NetQ Cloud Appliance
    ```
{{</tab>}}

{{</tabs>}}

## Next Steps

- {{<link title="Upgrade NetQ Agents">}}