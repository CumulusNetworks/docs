---
title: Upgrade NetQ Appliances and Virtual Machines
author: NVIDIA
weight: 410
toc: 4
---

The first step in upgrading your NetQ installation to NetQ {{<version>}} is upgrading your NetQ appliances or VMs.

## Before You Upgrade
### Back up NetQ Data

This is an optional step for on-premises deployments. Refer to {{<link title="Back Up and Restore NetQ">}}. NetQ Cloud Appliances and VMs create backups automatically.

### Download Software and Update Debian Packages

1. Download the relevant software.

    {{<netq-install/upgrade-image version="4.4">}}

2. Copy the file to the `/mnt/installables/` directory on your appliance or VM.

3. Update `/etc/apt/sources.list.d/cumulus-netq.list` to netq-4.4 as follows:

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-4.4
    ```

4. Update the NetQ `debian` packages.

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 https://apps3.cumulusnetworks.com/repos/deb bionic InRelease [13.8 kB]
    Get:2 https://apps3.cumulusnetworks.com/repos/deb bionic/netq-4.4 amd64 Packages [758 B]
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
    Unpacking netq-agent (4.4.0-ub18.04u40~1667493385.97ef4c9) ...
    ...
    Unpacking netq-apps (4.4.0-ub18.04u40~1667493385.97ef4c9) ...
    Setting up netq-apps (4.4.0-ub18.04u40~1667493385.97ef4c9) ...
    Setting up netq-agent (4.4.0-ub18.04u40~1667493385.97ef4c9) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```
## Run the Upgrade

{{%notice note%}}

Perform the following steps using the `cumulus` user account.

{{%/notice%}}
### Pre-installation Checks

Verify the following items before upgrading NetQ. For cluster deployments, verify steps 1 and 3 on all nodes in the cluster:

1. Check if enough disk space is available before you proceed with the upgrade:

```
cumulus@netq-appliance:~$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       248G   70G  179G  28% /
cumulus@netq-appliance:~$
```

The recommended `Use%` to proceed with installation is under 70%. You can delete previous software tarballs in the `/mnt/installables/` directory to regain some space. If you can not bring disk space to under 70% usage, contact the NVIDIA support team.

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

### Upgrade Using the NetQ CLI

After completing the preparation steps, upgrade your NetQ On-premises, Cloud Appliances, or VMs using the NetQ CLI.

To upgrade your NetQ software:

1. Run the appropriate `netq upgrade` command.

{{<tabs "CLI Upgrade">}}

{{<tab "On-premises Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.4.0.tgz
```

{{</tab>}}

{{<tab "Cloud Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.4.0-opta.tgz
```

{{</tab>}}

{{</tabs>}}

2. After the upgrade completes, confirm the upgrade was successful.

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.4.0
    APPLIANCE_MANIFEST_HASH=d552ed2f70b56e31aad8f35cab9383af4b2fe61abe55939b19b491b4e480d737
    APPLIANCE_VERSION=4.4.0
    ```
