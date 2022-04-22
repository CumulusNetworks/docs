---
title: Upgrade NetQ Appliances and Virtual Machines
author: NVIDIA
weight: 410
toc: 4
---

The first step in upgrading your NetQ installation to NetQ {{<version>}} is to upgrade your NetQ appliances or VMs. This topic describes how to upgrade this for both on-premises and remote deployments.

## Prepare for Upgrade

You must complete the following three important steps to prepare to upgrade your NetQ Platform:

- Download the necessary software tarballs
- Update the Debian packages on physical server and VMs

Optionally, you can choose to back up your NetQ Data before performing the upgrade.

To complete the preparation:

1. For on-premises deployments only, optionally back up your NetQ data. Refer to {{<link title="Back Up and Restore NetQ">}}.

2. Download the relevant software.

    {{<netq-install/upgrade-image version="4.1">}}

3. Copy the file to the `/mnt/installables/` directory on your appliance or VM.

4. Update `/etc/apt/sources.list.d/cumulus-netq.list` to netq-4.1 as follows:

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-4.1
    ```

5. Update the NetQ `debian` packages.

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 https://apps3.cumulusnetworks.com/repos/deb bionic InRelease [13.8 kB]
    Get:2 https://apps3.cumulusnetworks.com/repos/deb bionic/netq-4.1 amd64 Packages [758 B]
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
    Unpacking netq-agent (4.1.0-ub18.04u33~1621860085.c5a5d7e) ...
    ...
    Unpacking netq-apps (4.1.0-ub18.04u33~1621860085.c5a5d7e) ...
    Setting up netq-apps (4.1.0-ub18.04u33~1621860085.c5a5d7e) ...
    Setting up netq-agent (4.1.0-ub18.04u33~1621860085.c5a5d7e) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```

### Upgrade Using the NetQ CLI

After completing the {{<link url="#prepare-for-upgrade" text="preparation steps">}}, upgrading your NetQ On-premises, Cloud Appliances or VMs is simple using the NetQ CLI.

To upgrade your NetQ software:

1. Run the appropriate `netq upgrade` command.

{{<tabs "CLI Upgrade">}}

{{<tab "On-premises Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.1.0.tgz
```

{{</tab>}}

{{<tab "Cloud Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.1.0-opta.tgz
```

{{</tab>}}

{{</tabs>}}

2. After the upgrade completes, confirm the upgrade was successful.

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.1.0
    APPLIANCE_MANIFEST_HASH=85575c98a3
    APPLIANCE_VERSION=4.1.0
    ```
