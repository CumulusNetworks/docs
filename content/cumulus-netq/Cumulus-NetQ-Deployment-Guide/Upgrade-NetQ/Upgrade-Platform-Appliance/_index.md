---
title: Upgrade NetQ Hardware
author: Cumulus Networks
weight: 125
aliases:
 - /display/NETQ/Upgrade+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 
---
The first step in upgrading your NetQ 2.4.0 installation to NetQ 2.4.1 is to upgrade your NetQ Platform(s) or NetQ Appliance(s). This topic describes how to upgrade these hardware platforms for both on-premises and cloud deployments.

## Prepare for Upgrade

Two important steps are required to prepare your hardware for upgrade:

- Download the necessary software tarballs
- Update the Debian packages on the hardware

Optionally, you can choose to back up your NetQ Data before performing the upgrade.

To complete the preparation:

1. Log in to your NetQ Platform or Appliance.

2. Optionally back up your NetQ 2.4.0 data. Refer to {{<link title="Back Up Your NetQ Data">}}.

3. Download the relevant software.

    1. Go to the {{<exlink url="https://cumulusnetworks.com/downloads/" text="Cumulus Downloads">}} page, and select *NetQ* from the **Product** list.

    2. Select *2.4* from the **Version** list, and then click
        *2.4.1* from the submenu.

    3. Select the relevant software from the **HyperVisor/Platform** list:

        {{< figure src="/images/netq/netq-24-download-options-240b.png" width="500" >}}
         
        | Your Deployment Type | Hypervisor/Platform Selection | Downloaded Filename |
        | ---- | ---- | ---- |
        | NetQ On-premises Platform running KVM | KVM | NetQ-2.4.1.tgz |
        | NetQ Cloud Platform running KVM | KVM (Cloud) | NetQ-2.4.1-opta.tgz |
        | NetQ On-premises Platform running VMware | VMware | NetQ-2.4.1.tgz |
        | NetQ Cloud Platform running VMware | VMware (Cloud) | NetQ-2.4.1-opta.tgz |
        | NetQ Appliance (on-premises) | Appliance | NetQ-2.4.1.tgz |
        | NetQ Cloud Appliance | Appliance (Cloud) | NetQ-2.4.1-opta.tgz |

    4. Scroll down and click **Upgrade**. For example: (reviewer note: this image will be updated)

        {{< figure src="/images/netq/netq-24-appliance-dwnld-240.png" width="200" >}}

4. Copy the file to the */mnt/installables/* directory on your hardware.

5. Update the NetQ debian packages.

```
sudo dpkg --remove --force-remove-reinstreq netq-apps netq-agent 2>/dev/null
sudo apt-get update
sudo apt-get install -y netq-agent netq-apps
```

You can now upgrade your hardware using the NetQ Admin UI, in the next section, or the {{<link title="#Upgrade Your Hardware Using the NetQ CLI" text="NetQ CLI">}}.

## Upgrade Your Hardware Using the NetQ Admin UI

After completing the preparation steps, upgrading your NetQ Platform(s) or NetQ Appliance(s) is simple using the Admin UI.

To upgrade your hardware:

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

2. Open the Admin UI by entering `https://<platform-or-appliance-ipaddress>:8443` in your browser address field.

3. Follow the instructions in the UI. (reviewer note: need to view mirage to select some screen shots and basic steps)

## Upgrade Your Hardware Using the NetQ CLI

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

    The output should look like this: (reviewer note: what name is used for the platform servers? user defined? is the hash the same for both on-prem upgrades, and different, but the same for both cloud upgrades?)

    |  | On-premises | Cloud |
    | ---- | ---- | ---- |
    | <strong>NetQ Platform</strong> | APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=xxx<br>APPLIANCE_NAME="&lt;NetQ Platform Name&gt;" | APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=xxx<br>APPLIANCE_NAME="&lt;NetQ Cloud Platform Name&gt;" |
    | <strong>NetQ Appliance</strong> | APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=xxx<br>APPLIANCE_NAME="NetQ Appliance" | APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=xxx<br>APPLIANCE_NAME="NetQ Cloud Appliance" |
