---
title: Upgrade the NetQ Platform
author: Cumulus Networks
weight: 141
aliases:
 - /display/NETQ/Upgrade+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 4
---
The first step in upgrading your NetQ 2.4.0 installation to NetQ 2.4.1 is to upgrade your NetQ Platform. This topic describes how to upgrade this for both on-premises and cloud deployments.

## Prepare for Upgrade

Two important steps are required to prepare for upgrade of your NetQ Platform:

- Download the necessary software tarballs
- Update the Debian packages on the hardware

Optionally, you can choose to back up your NetQ Data before performing the upgrade.

To complete the preparation:

1. Optionally back up your NetQ 2.4.0 data. Refer to [Back Up Your NetQ Data](../../Backup-and-Restore-NetQ/Backup-NetQ/).

2. Download the relevant software.

    1. Go to the {{<exlink url="https://cumulusnetworks.com/downloads/" text="Cumulus Downloads">}} page, and select *NetQ* from the **Product** list.

    2. Select *2.4* from the **Version** list, and then click
        *2.4.1* from the submenu.

    3. Select the relevant software from the **HyperVisor/Platform** list:

        {{< figure src="/images/netq/netq-24-download-options-241.png" width="500" >}}
         
        | Your Deployment Type | Hypervisor/Platform Selection | Downloaded Filename |
        | ---- | ---- | ---- |
        | NetQ On-premises Platform running KVM | KVM | NetQ-2.4.1.tgz |
        | NetQ Cloud Platform running KVM | KVM (Cloud) | NetQ-2.4.1-opta.tgz |
        | NetQ On-premises Platform running VMware | VMware | NetQ-2.4.1.tgz |
        | NetQ Cloud Platform running VMware | VMware (Cloud) | NetQ-2.4.1-opta.tgz |
        | NetQ Appliance (on-premises) | Appliance | NetQ-2.4.1.tgz |
        | NetQ Cloud Appliance | Appliance (Cloud) | NetQ-2.4.1-opta.tgz |

    4. Scroll down and click **Download**. For example: The NetQ Appliance images.

        {{< figure src="/images/netq/netq-24-appliance-onpremcld-dwnld-241.png" width="420" >}}

3. Copy the file to the */mnt/installables/* directory on your hardware.

4. Update the NetQ debian packages.

```
sudo dpkg --remove --force-remove-reinstreq netq-apps netq-agent 2>/dev/null
sudo apt-get update
sudo apt-get install -y netq-agent netq-apps
```

You can now upgrade your platform using the NetQ Admin UI, in the next section, or the {{<link title="#Upgrade Your Hardware Using the NetQ CLI" text="NetQ CLI">}}.

## Upgrade Your Platform Using the NetQ Admin UI

After completing the preparation steps, upgrading your NetQ Platform(s) or NetQ Appliance(s) is simple using the Admin UI.

To upgrade your NetQ software:

1. Run the bootstrap CLI to upgrade the Admin UI itself.

    <details><summary>On-premises Deployments</summary>

    ```
    netq bootstrap master upgrade /mnt/installables/NetQ-2.4.1.tgz
    ```

    </details>
    <details><summary>Cloud Deployments</summary>

    ```
    netq bootstrap master upgrade /mnt/installables/NetQ-2.4.1-opta.tgz
    ```

    </details>

2. Open the Admin UI by entering `https://<hostname-or-ipaddress>:8443` in your browser address field.

3. Click **Begin Upgrade**.

4. Backup?

4. Enter *NetQ-2.4.1.tgz* or *NetQ-2.4.1-opta.tgz* and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg", height="18", width="18"/>.

    {{<figure src="/images/netq/adminui-upgrade-enter-tar-241.png" width="700">}}

    {{%notice tip%}}
The <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg", height="18", width="18"/> is only visible after you enter your tar file information.
    {{%/notice%}}

5. xxx

6. Activate the NetQ Software.

7. Restore?

## Upgrade Your Platform Using the NetQ CLI

After completing the preparation steps, upgrading your NetQ Platform(s) or NetQ Appliance(s) is simple using the NetQ CLI.

To upgrade your hardware:

1. Run the appropriate `netq upgrade` command.

    <details><summary>On-premises Deployments</summary>

    ```
    netq upgrade bundle /mnt/installables/NetQ-2.4.1.tgz
    ```

    </details>
    <details><summary>Cloud Deployments</summary>

    ```
    netq upgrade bundle /mnt/installables/NetQ-2.4.1-opta.tgz
    ```

    </details>

2. After the upgrade is completed, confirm the upgrade was successful.

```
cat /etc/app-release
```

    The output should look like this:

    |  | On-premises | Cloud |
    | ---- | ---- | ---- |
    | <strong>NetQ Platform</strong> | <ul><li>KVM: <br>    APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=E9361...12BE7<br>APPLIANCE_NAME="&lt;NetQ Platform Name&gt;"</li><li>VMware:<br>APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=7916C...6D0EF<br>APPLIANCE_NAME="&lt;NetQ Platform Name&gt;"</li></ul> | <ul><li>KVM: <br> APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=383E9...F4371<br>APPLIANCE_NAME="&lt;NetQ Cloud Platform Name&gt;"</li><li>VMware: <br> APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=E6176...A3EA1<br>APPLIANCE_NAME="&lt;NetQ Cloud Platform Name&gt;"</li></ul> |
    | <strong>NetQ Appliance</strong> | APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=ADB58...E6732<br>APPLIANCE_NAME="NetQ Appliance" | APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=4F50D...57FE1<br>APPLIANCE_NAME="NetQ Cloud Appliance" |

## Add More Nodes to Your Server Cluster

<!-- Post install/upgrade topic? -->

When you have a three-server cluster already configured, you can add more worker nodes to your NetQ configuration, up to a total of nine worker nodes, using the Admin UI.

To add more worker nodes:

1. Open the Admin UI by entering `https://<master-hostname-or-ipaddress>:8443` in your browser address field.

2. Click **Cluster** to view your current configuration.

    {{<figure src="/images/netq/adminui-cluster-tab-241.png" width="700">}}

3. Click **Add Worker Node**.

4. Enter the *private* IP address of the server you want to add.

5. Click **Add**.

6. anything else?

6. Repeat this process to add more worker nodes as needed.

## Update Your Cloud Configuration Key

<!-- Post install/upgrade topic? -->

There are occasions where you might want to update your cloud service configuration key. For example, if you mistyped the key during installation and now your existing key does not work, or you received a new key for your premises from Cumulus Networks.

To update the configuration key, run the following command with your new key.

```
cumulus@switch:~$ netq install opta activate-job config-key <text-opta-key>
```
