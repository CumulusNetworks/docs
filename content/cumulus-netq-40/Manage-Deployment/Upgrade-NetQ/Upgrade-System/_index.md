---
title: Upgrade NetQ Appliances and Virtual Machines
author: NVIDIA
weight: 410
toc: 4
---
The first step in upgrading your NetQ installation to NetQ {{<version>}} is to upgrade your NetQ appliances or VMs. This topic describes how to upgrade this for both on-premises and remote deployments.

## Prepare for Upgrade

Three important steps are required to prepare for upgrade of your NetQ Platform:

- Download the necessary software tarballs
- Update the Debian packages on physical server and VMs
- For Cloud VM deployments, increase the root volume disk image size

Optionally, you can choose to back up your NetQ Data before performing the upgrade.

To complete the preparation:

1. For on-premises deployments only, optionally back up your NetQ data. Refer to {{<link title="Back Up and Restore NetQ">}}.

2. Download the relevant software.

    {{<netq-install/upgrade-image version="4.0">}}

3. Copy the file to the `/mnt/installables/` directory on your appliance or VM.

4. Update `/etc/apt/sources.list.d/cumulus-netq.list` to netq-4.0 as follows:

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-4.0
    ```

5. Update the NetQ `debian` packages.

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 http://apps3.cumulusnetworks.com/repos/deb bionic InRelease [13.8 kB]
    Get:2 http://apps3.cumulusnetworks.com/repos/deb bionic/netq-4.0 amd64 Packages [758 B]
    Hit:3 http://archive.ubuntu.com/ubuntu bionic InRelease
    Get:4 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
    Get:5 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
    ...
    Get:24 http://archive.ubuntu.com/ubuntu bionic-backports/universe Translation-en [1900 B]
    Fetched 4651 kB in 3s (1605 kB/s)
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
    Unpacking netq-agent (4.0.0-ub18.04u33~1614767175.886b337) ...
    ...
    Unpacking netq-apps (4.0.0-ub18.04u33~1614767175.886b337) ...
    Setting up netq-apps (4.0.0-ub18.04u33~1614767175.886b337) ...
    Setting up netq-agent (4.0.0-ub18.04u33~1614767175.886b337) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ``````

6. If you are upgrading NetQ as a VM in the cloud from version 3.1.0 or earlier, you must increase the root volume disk image size for proper operation of the lifecycle management feature.

    {{<tabs "TabID89" >}}

{{<tab "VMware" >}}

1. Check the size of the existing disk in the VM to confirm it is 32 GB. In this example, the number of 1 MB blocks is 31583, or 32 GB.

    ```
    cumulus@netq-310-cloud:~$ df -hm /
    Filesystem     1M-blocks  Used Available Use% Mounted on
    /dev/sda1          31583  4771     26797  16% /
    ```

2. Shutdown the VM.

    {{<figure src="/images/netq/upgrade-root-disk-shutdown-vm-320.png" width="700" caption="Shutting down VMware VM using Shut down button in ESX">}}

3. After the VM is shutdown (Shut down button is grayed out), click **Edit**.

    {{<figure src="/images/netq/upgrade-root-disk-edit-vm-320.png" width="700">}}

4. In the **Edit settings** > **Virtual Hardware** > **Hard disk** field, change the 32 to 64 on the server hosting the VM.

    {{<figure src="/images/netq/upgrade-root-disk-edit-size-320.png" width="400">}}

5. Click **Save**.

6. Start the VM, log back in.

7. From step 1 we know the name of the root disk is */dev/sda1*. Use that to run the following commands on the partition.

    ```
    cumulus@netq-310-cloud:~$ sudo growpart /dev/sda 1
    CHANGED: partition=1 start=227328 old: size=66881503 end=67108831 new: size=133990367,end=134217695

    cumulus@netq-310-cloud:~$ sudo resize2fs /dev/sda1
    resize2fs 1.44.1 (24-Mar-2018)
    Filesystem at /dev/sda1 is mounted on /; on-line resizing required
    old_desc_blocks = 4, new_desc_blocks = 8
    The filesystem on /dev/sda1 is now 16748795 (4k) blocks long.
    ```

6. Verify the disk is now configured with 64 GB. In this example, the number of 1 MB blocks is now 63341, or 64 GB.

    ```
    cumulus@netq-310-cloud:~$ df -hm /
    Filesystem     1M-blocks  Used Available Use% Mounted on
    /dev/sda1          63341  4772     58554   8% /
    ```

{{</tab>}}

{{<tab "KVM" >}}

1. Check the size of the existing hard disk in the VM to confirm it is 32 GB. In this example, the number of 1 MB blocks is 31583, or 32 GB.

    ```
    cumulus@netq-310-cloud:~$ df -hm /
    Filesystem     1M-blocks  Used Available Use% Mounted on
    /dev/vda1          31583  1192     30375   4% /
    ```

2. Shutdown the VM.

3. Check the size of the existing disk on the server hosting the VM to confirm it is 32 GB. In this example, the size is shown in the **virtual size** field.

    ```
    root@server:/var/lib/libvirt/images# qemu-img info netq-3.1.0-ubuntu-18.04-tscloud-qemu.qcow2
    image: netq-3.1.0-ubuntu-18.04-tscloud-qemu.qcow2
    file format: qcow2
    virtual size: 32G (34359738368 bytes)
    disk size: 1.3G
    cluster_size: 65536
    Format specific information:
        compat: 1.1
        lazy refcounts: false
        refcount bits: 16
        corrupt: false
    ```

4. Add 32 GB to the image.

    ```
    root@server:/var/lib/libvirt/images# qemu-img resize netq-3.1.0-ubuntu-18.04-tscloud-qemu.qcow2 +32G
    Image resized.
    ```

5. Verify the change.

    ```
    root@server:/var/lib/libvirt/images# qemu-img info netq-3.1.0-ubuntu-18.04-tscloud-qemu.qcow2
    image: netq-3.1.0-ubuntu-18.04-tscloud-qemu.qcow2
    file format: qcow2
    virtual size: 64G (68719476736 bytes)
    disk size: 1.3G
    cluster_size: 65536
    Format specific information:
        compat: 1.1
        lazy refcounts: false
        refcount bits: 16
        corrupt: false
    ```

6. Start the VM and log back in.

7. From step 1 you know the name of the root disk is */dev/vda 1*. Use that to run the following commands on the partition.

    ```
    cumulus@netq-310-cloud:~$ sudo growpart /dev/vda 1
    CHANGED: partition=1 start=227328 old: size=66881503 end=67108831 new: size=133990367,end=134217695

    cumulus@netq-310-cloud:~$ sudo resize2fs /dev/vda1
    resize2fs 1.44.1 (24-Mar-2018)
    Filesystem at /dev/vda1 is mounted on /; on-line resizing required
    old_desc_blocks = 4, new_desc_blocks = 8
    The filesystem on /dev/vda1 is now 16748795 (4k) blocks long.
    ```

8. Verify the disk is now configured with 64 GB. In this example, the number of 1 MB blocks is now 63341, or 64 GB.

```
cumulus@netq-310-cloud:~$ df -hm /
Filesystem     1M-blocks  Used Available Use% Mounted on
/dev/vda1          63341  1193     62132   2% /
```

{{</tab>}}

{{</tabs>}}

You can now upgrade your appliance using the NetQ Admin UI, in the next section. Alternately, you can upgrade using the CLI here: {{<link title="#Upgrade Your Platform Using the NetQ CLI" text="Upgrade Your Platform Using the NetQ CLI">}}.

## Run the Upgrade

You can upgrade the NetQ platform in one of two ways:

- Using the `netq upgrade` CLI command, which works with any supported older versions
- Using the NetQ Admin UI, which works only if you are upgrading from version 3.1.1 or later

### Upgrade Using the NetQ CLI

After completing the {{<link url="#prepare-for-upgrade" text="preparation steps">}}, upgrading your NetQ On-premises, Cloud Appliances or VMs is simple using the NetQ CLI.

To upgrade your NetQ software:

1. Run the appropriate `netq upgrade` command.

{{<tabs "CLI Upgrade">}}

{{<tab "On-premises Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.0.0.tgz
```

{{</tab>}}

{{<tab "Cloud Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.0.0-opta.tgz
```

{{</tab>}}

{{</tabs>}}

2. After the upgrade completes, confirm the upgrade was successful.

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.0.0
    APPLIANCE_MANIFEST_HASH=74ac3017d5
    APPLIANCE_VERSION=4.0.0
    ```

### Upgrade Using the NetQ Admin UI

If you are upgrading from NetQ 3.1.1 or later, after completing the {{<link url="#prepare-for-upgrade" text="preparation steps">}}, upgrading your NetQ On-premises or Cloud Appliances or VMs is simple using the Admin UI.

To upgrade your NetQ software:

1. Run the bootstrap CLI to upgrade the Admin UI application.

    {{<tabs "Upgrade Old Platforms">}}

{{<tab "On-premises Deployments">}}

```
cumulus@<hostname>:~$ netq bootstrap master upgrade /mnt/installables/NetQ-4.0.0.tgz
2020-04-28 15:39:37.016710: master-node-installer: Extracting tarball /mnt/installables/NetQ-4.0.0.tgz
2020-04-28 15:44:48.188658: master-node-installer: Upgrading NetQ Admin container
2020-04-28 15:47:35.667579: master-node-installer: Removing old images
-----------------------------------------------
Successfully bootstrap-upgraded the master node
```

{{</tab>}}

{{<tab "Remote Deployments">}}

```
netq bootstrap master upgrade /mnt/installables/NetQ-4.0.0-opta.tgz
```

{{</tab>}}

{{</tabs>}}

2. Open the Admin UI by entering *http://\<hostname-or-ipaddress\>:8443* in your browser address field.

3. Enter your NetQ credentials to enter the application.

    The default username is *admin* and the default password in *admin*.

    {{<figure src="/images/netq/adminui-health-tab-onprem-320.png" width="700" caption="On-premises deployment">}}

    {{<figure src="/images/netq/adminui-health-tab-cloud-330.png" width="700" caption="Remote (cloud) deployment">}}

4. Click **Upgrade** in the upper right corner.

5. Enter *NetQ-4.0.0.tgz* or *NetQ-4.0.0-opta.tgz* and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/adminui-upgrade-enter-tar-330.png" width="700">}}

    {{<notice tip>}}
The <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/> is only visible after you enter your tar file information.
    {{</notice>}}

6. Monitor the progress. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-circle-down.svg" height="18" width="18"/> to monitor each step in the jobs.

    The following example is for an on-premises upgrade. The jobs for a cloud upgrade are slightly different.

    {{<figure src="/images/netq/adminui-upgrade-progress-4.0.0.png" width="700">}}

7. When it completes, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/> to be returned to the Health dashboard.
