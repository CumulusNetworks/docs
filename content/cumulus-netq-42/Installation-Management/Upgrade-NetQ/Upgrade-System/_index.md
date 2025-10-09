---
title: Upgrade NetQ Appliances and Virtual Machines
author: NVIDIA
weight: 410
toc: 4
---

The first step in upgrading your NetQ installation to NetQ {{<version>}} is upgrading your NetQ appliances or VMs.

## Prepare for Upgrade

Before you upgrade, complete the following steps:

- Download the necessary software tarballs
- Update the Debian packages on physical server and VMs

Optionally, you can choose to back up your NetQ Data before performing the upgrade.

To complete the preparation:

1. For on-premises deployments only, optionally back up your NetQ data. Refer to {{<link title="Back Up and Restore NetQ">}}.

2. Download the relevant software.

    {{<netq-install/upgrade-image version="4.2">}}

3. Copy the file to the `/mnt/installables/` directory on your appliance or VM.

4. Update `/etc/apt/sources.list.d/cumulus-netq.list` to netq-4.2 as follows:

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-4.2
    ```

5. Update the NetQ `debian` packages.

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 https://apps3.cumulusnetworks.com/repos/deb bionic InRelease [13.8 kB]
    Get:2 https://apps3.cumulusnetworks.com/repos/deb bionic/netq-4.2 amd64 Packages [758 B]
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
    Unpacking netq-agent (4.2.0-ub18.04u38~1652817271.25f4ac0) ...
    ...
    Unpacking netq-apps (4.2.0-ub18.04u38~1652817271.25f4ac0) ...
    Setting up netq-apps (4.2.0-ub18.04u38~1652817271.25f4ac0) ...
    Setting up netq-agent (4.2.0-ub18.04u38~1652817271.25f4ac0) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```
## Run the Upgrade

{{%notice note%}}
Verify the following items before upgrading NetQ. For cluster deployments, verify steps 1 and 3 on all nodes in the cluster:

1. Check if enough disk space is available before you proceed with the upgrade:

```
cumulus@netq-appliance:~$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       248G   70G  179G  28% /
cumulus@netq-appliance:~$
```

The recommended `Use%` to proceed with installation is under 70%.

You can delete previous software tarballs in the `/mnt/installables/` directory to regain some space.
If you can not bring disk space to under 70% usage, contact the NVIDIA support team.

2. Run the `netq show opta-health` command and check that all pods are in the `READY` state. If not, contact the NVIDIA support team.

3. Check if the certificates have expired:

```
cumulus@netq-appliance:~$ sudo grep client-certificate-data /etc/kubernetes/kubelet.conf | cut -d: -f2 | xargs | base64 -d | openssl x509 -dates -noout | grep notAfter | cut -f2 -d=
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

If any issue occurs, contact the NVIDIA Support team.

{{%/notice%}}
### Upgrade Using the NetQ CLI

After completing the {{<link url="#prepare-for-upgrade" text="preparation steps">}}, upgrading your NetQ On-premises, Cloud Appliances or VMs is simple using the NetQ CLI.

To upgrade your NetQ software:

1. Run the appropriate `netq upgrade` command.

{{<tabs "CLI Upgrade">}}

{{<tab "On-premises Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.2.0.tgz
```

{{</tab>}}

{{<tab "Cloud Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.2.0-opta.tgz
```

{{</tab>}}

{{</tabs>}}

2. After the upgrade completes, confirm the upgrade was successful.

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.2.0
    APPLIANCE_MANIFEST_HASH=25f4ac06
    APPLIANCE_VERSION=4.2.0
    ```
