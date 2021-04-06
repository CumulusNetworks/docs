---
title: Upgrade the NetQ Platform
author: Cumulus Networks
weight: 141
toc: 4
---
The first step in upgrading your NetQ 2.4.0 installation to NetQ 2.4.1 is to upgrade your NetQ Platform. This topic describes how to upgrade this for both on-premises and cloud deployments.

## Prepare for Upgrade

Two important steps are required to prepare for upgrade of your NetQ Platform:

- Download the necessary software tarballs
- Update the Debian packages on the hardware

Optionally, you can choose to back up your NetQ Data before performing the upgrade.

To complete the preparation:

1. Optionally back up your NetQ 2.4.0 data. Refer to {{<link title="Back Up Your NetQ Data">}}.

2. Download the relevant software.

    1. Go to the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads page">}} page, and select *NetQ* from the **Product** list.

    2. Select *2.4* from the **Version** list, and then click
        *2.4.1* from the submenu.

    3. Select the relevant software from the **HyperVisor/Platform** list:

        If you are upgrading NetQ Platform software for a NetQ On-premises Appliance or VM, select *Appliance*  to download the NetQ-2.4.1.tgz file. If you are upgrading NetQ Collector software for a NetQ Cloud Appliance or VM, select *Appliance (Cloud)* to download the NetQ-2.4.1-opta.tgz file.

        {{< figure src="/images/netq/netq-24-download-options-241.png" width="500" >}}

    4. Scroll down and click **Download**. For example: The NetQ Appliance images.

        {{< figure src="/images/netq/netq-24-appliance-onpremcld-dwnld-241.png" width="420" >}}

        {{<notice note>}}
You can ignore the note on the image card because, unlike during installation, you <em>do not</em> need to download the bootstrap file for an upgrade.
        {{</notice>}}

3. Copy the file to the */mnt/installables/* directory on your hardware.

4. Update the NetQ debian packages using the following three commands.

    ```
    cumulus@<hostname>:~$ sudo dpkg --remove --force-remove-reinstreq netq-apps netq-agent 2>/dev/null
    [sudo] password for cumulus:
    (Reading database ... 71621 files and directories currently installed.)
    Removing netq-apps (2.4.0-ub18.04u24~1577405296.fcf3c28) ...
    Removing netq-agent (2.4.0-ub18.04u24~1577405296.fcf3c28) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 http://apps3.cumulusnetworks.com/repos/deb bionic InRelease [13.8 kB]
    Get:2 http://apps3.cumulusnetworks.com/repos/deb bionic/netq-2.4 amd64 Packages [758 B]
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
    Unpacking netq-agent (2.4.1-ub18.04u26~1581351889.c5ec3e5) ...
    ...
    Unpacking netq-apps (2.4.1-ub18.04u26~1581351889.c5ec3e5) ...
    Setting up netq-apps (2.4.1-ub18.04u26~1581351889.c5ec3e5) ...
    Setting up netq-agent (2.4.1-ub18.04u26~1581351889.c5ec3e5) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```

You can now upgrade your platform using the NetQ Admin UI, in the next section. Alternately, you can upgrade using the CLI here: {{<link title="#Upgrade Your Platform Using the NetQ CLI">}}.

## Upgrade Your Platform Using the NetQ Admin UI

After completing the preparation steps, upgrading your NetQ Platform(s) or NetQ Appliance(s) is simple using the Admin UI.

To upgrade your NetQ software:

1. Run the bootstrap CLI to upgrade the Admin UI itself.

    {{< tabs "TabID0" >}}

{{< tab "On-premises Deployments" >}}

```
cumulus@<hostname>:~$ netq bootstrap master upgrade /mnt/installables/NetQ-2.4.1.tgz
2020-02-28 15:39:37.016710: master-node-installer: Extracting tarball /mnt/installables/NetQ-2.4.1.tgz
2020-02-28 15:44:48.188658: master-node-installer: Upgrading NetQ Admin container
2020-02-28 15:47:35.667579: master-node-installer: Removing old images
-----------------------------------------------
Successfully bootstrap-upgraded the master node
```

{{< /tab >}}

{{< tab "Cloud Deployments" >}}

```
netq bootstrap master upgrade /mnt/installables/NetQ-2.4.1-opta.tgz
```
{{< /tab >}}

{{< /tabs >}}

2. Open the Admin UI by entering **http://\<hostname-or-ipaddress\>:8443** in your browser address field.

3. Click **Upgrade**.

    {{<figure src="/images/netq/adminui-upgrade-begin-241.png" width="700">}}

4. Enter *NetQ-2.4.1.tgz* or *NetQ-2.4.1-opta.tgz* and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/adminui-upgrade-enter-tar-241.png" width="700">}}

    {{%notice tip%}}
The <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/> is only visible after you enter your tar file information.
    {{%/notice%}}

5. Monitor the progress. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-circle-down.svg" height="18" width="18"/> to monitor each step in the jobs.

    The following example is for an on-premises upgrade. The jobs for a cloud upgrade are slightly different.

    {{<figure src="/images/netq/adminui-upgrade-progress-241.png" width="700">}}

5. When it completes, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/> to be returned to the Health dashboard.

## Upgrade Your Platform Using the NetQ CLI

After completing the preparation steps, upgrading your NetQ Platform(s) or NetQ Appliance(s) is simple using the NetQ CLI.

To upgrade your hardware:

1. Run the appropriate `netq upgrade` command.

    {{< tabs "TabID2" >}}

{{< tab "On-premises Deployments" >}}

```
netq upgrade bundle /mnt/installables/NetQ-2.4.1.tgz
```

{{< /tab >}}

{{< tab "Cloud Deployments" >}}

```
netq upgrade bundle /mnt/installables/NetQ-2.4.1-opta.tgz
```

{{< /tab >}}

{{< /tabs >}}

2. After the upgrade is completed, confirm the upgrade was successful.

    ```
    cat /etc/app-release
    ```

    The output should look like this:

    |  | On-premises | Cloud |
    | ---- | ---- | ---- |
    | <strong>NetQ Platform</strong> | <ul><li>KVM:<br>APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=E9361...12BE7<br>APPLIANCE_NAME="&lt;NetQ Platform Name&gt;"</li><li>VMware:<br>APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=7916C...6D0EF<br>APPLIANCE_NAME="&lt;NetQ Platform Name&gt;"</li></ul> | <ul><li>KVM: <br> APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=383E9...F4371<br>APPLIANCE_NAME="&lt;NetQ Cloud Platform Name&gt;"</li><li>VMware: <br> APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=E6176...A3EA1<br>APPLIANCE_NAME="&lt;NetQ Cloud Platform Name&gt;"</li></ul> |
    | <strong>NetQ Appliance</strong> | APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=ADB58...E6732<br>APPLIANCE_NAME="NetQ Appliance" | APPLIANCE_VERSION=2.4.1<br>APPLIANCE_MANIFEST_HASH=4F50D...57FE1<br>APPLIANCE_NAME="NetQ Cloud Appliance" |
