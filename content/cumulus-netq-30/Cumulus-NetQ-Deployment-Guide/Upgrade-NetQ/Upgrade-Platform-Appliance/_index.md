---
title: Upgrade NetQ Appliances and Virtual Machines
author: Cumulus Networks
weight: 141
toc: 4
---
The first step in upgrading your NetQ 2.4.x installation to NetQ 3.0.0 is to upgrade either the NetQ Platform software running on your NetQ On-premises Appliance(s) or VM(s), or the NetQ Collector software running on your NetQ Cloud Appliance(s) or VM(s).

## Prepare for Upgrade

Two important steps are required to prepare for upgrade of your NetQ software:

- Download the necessary software tarballs
- Update the Debian packages on Appliance(s) and VM(s)

Optionally, you can choose to back up your NetQ Data before performing the upgrade.

To complete the preparation:

1. For on-premises deployments only, optionally back up your NetQ 2.4.x data. Refer to {{<link title="Back Up Your NetQ Data">}}.

2. Download the relevant software.

    1. Go to the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads page">}} page, and select *NetQ* from the **Product** list.

    2. Select *3.0* from the **Version** list, and then click *3.0.0* in the submenu.

    3. Select the relevant software from the **HyperVisor/Platform** list:

        If you are upgrading NetQ Platform software for a NetQ On-premises Appliance or VM, select *Appliance*  to download the NetQ-3.0.0.tgz file. If you are upgrading NetQ Collector software for a NetQ Cloud Appliance or VM, select *Appliance (Cloud)* to download the NetQ-3.0.0-opta.tgz file.

        {{< figure src="/images/netq/netq-30-download-options-300.png" width="500" >}}

    4. Scroll down and click **Download** on the relevant image card.

        {{< figure src="/images/netq/netq-30-appliance-onpremcld-dwnld-300.png" width="420" >}}

        {{<notice note>}}
You can ignore the note on the image card because, unlike during installation, you <em>do not</em> need to download the bootstrap file for an upgrade.
        {{</notice>}}

3. Copy the file to the */mnt/installables/* directory on your appliance or VM.

4. Update /etc/apt/sources.list.d/cumulus-netq.list to netq-3.0 as followed

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-3.0
    ```

5. Update the NetQ debian packages using the following three commands.

    ```
    cumulus@<hostname>:~$ sudo dpkg --remove --force-remove-reinstreq cumulus-netq netq-apps netq-agent 2>/dev/null
    [sudo] password for cumulus:
    (Reading database ... 71621 files and directories currently installed.)
    Removing netq-apps (2.4.1-ub18.04u26~1581351889.c5ec3e5) ...
    Removing netq-agent (2.4.1-ub18.04u26~1581351889.c5ec3e5) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 http://apps3.cumulusnetworks.com/repos/deb bionic InRelease [13.8 kB]
    Get:2 http://apps3.cumulusnetworks.com/repos/deb bionic/netq-3.0 amd64 Packages [758 B]
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
    Unpacking netq-agent (3.0.0-ub18.04u27~1588242914.9fb5b87) ...
    ...
    Unpacking netq-apps (3.0.0-ub18.04u27~1588242914.9fb5b87) ...
    Setting up netq-apps (3.0.0-ub18.04u27~1588242914.9fb5b87) ...
    Setting up netq-agent (3.0.0-ub18.04u27~1588242914.9fb5b87) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```

Now that you have all of the software components prepared, you can upgrade your NetQ On-premises Appliance or VM, or your NetQ Cloud Appliance or VM, using the NetQ Admin UI, in the next section. Alternately, you can upgrade using the CLI here: {{<link title="#Upgrade Using the NetQ CLI" text="Upgrade Using the NetQ CLI">}}.

## Upgrade Using the NetQ Admin UI

Upgrading your NetQ On-premises or Cloud Appliance(s) or VMs is simple using the Admin UI.

To upgrade your NetQ software:

1. Upgrade the Admin UI application.

    {{< tabs "TabID100" >}}

    {{< tab "On-premises Deployments" >}}

    cumulus@<hostname>:~$ netq bootstrap master upgrade /mnt/installables/NetQ-3.0.0.tgz
    2020-04-28 15:39:37.016710: master-node-installer: Extracting tarball /mnt/installables/NetQ-3.0.0.tgz
    2020-04-28 15:44:48.188658: master-node-installer: Upgrading NetQ Admin container
    2020-04-28 15:47:35.667579: master-node-installer: Removing old images
    -----------------------------------------------
    Successfully bootstrap-upgraded the master node

    {{< /tab >}}

    {{< tab "Cloud Deployments" >}}

    netq bootstrap master upgrade /mnt/installables/NetQ-3.0.0-opta.tgz

    {{< /tab >}}

    {{< /tabs >}}

2. Open the Admin UI by entering *http://\<hostname-or-ipaddress\>:8443* in your browser address field.

3. Click **Upgrade**.

    {{<figure src="/images/netq/adminui-upgrade-begin-300.png" width="700" caption="On-premises deployment (cloud deployment only has Node and Pod cards)">}}

4. Enter *NetQ-3.0.0.tgz* or *NetQ-3.0.0-opta.tgz* and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/adminui-upgrade-enter-tar-300.png" width="700">}}

    {{<notice tip>}}
The <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/> is only visible after you enter your tar file information.
    {{</notice>}}

5. Monitor the progress. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-circle-down.svg" height="18" width="18"/> to monitor each step in the jobs.

    The following example is for an on-premises upgrade. The jobs for a cloud upgrade are slightly different.

    {{<figure src="/images/netq/adminui-upgrade-progress-241.png" width="700">}}

6. When it completes, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/> to be returned to the Health dashboard.

7. You can verify that you are on the correct version by viewing what is listed under the Cumulus logo.

## Upgrade Using the NetQ CLI

Upgrading your NetQ On-premises or Cloud Appliance(s) or VMs is simple using the NetQ CLI.

To upgrade:

1. Run the appropriate `netq upgrade` command.

    {{< tabs "TabID155" >}}

    {{< tab "On-premises Deployments" >}}

    netq upgrade bundle /mnt/installables/NetQ-3.0.0.tgz

    {{< /tab >}}

    {{< tab "Cloud Deployments" >}}

    netq upgrade bundle /mnt/installables/NetQ-3.0.0-opta.tgz

    {{< /tab >}}

    {{< /tabs >}}

2. After the upgrade is completed, confirm the upgrade was successful.

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=3.0.0
    APPLIANCE_MANIFEST_HASH=d40ca38672
    APPLIANCE_VERSION=3.0.0
    ```
