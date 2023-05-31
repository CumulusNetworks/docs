---
title: Upgrade NetQ Virtual Machines
author: NVIDIA
weight: 410
toc: 4
---

## Upgrading from NetQ 4.5.0

You can upgrade directly to NetQ 4.6.0 if your deployment is currently running version 4.5.0. If your deployment is on a release earlier than 4.5.0, see [Upgrading from Earlier Releases](#upgrading-from-earlier-releases).
### Back up your NetQ Data

{{<link title="Back Up and Restore NetQ" text="Backing up your NetQ data">}} is an optional step for on-premises deployments. NetQ cloud deployments create backups automatically.

### Download Software and Update Debian Packages

1. Download the relevant software.

    {{<netq-install/upgrade-image version="4.6">}}

2. Copy the file to the `/mnt/installables/` directory on your appliance or VM.

3. Update `/etc/apt/sources.list.d/cumulus-netq.list` to netq-4.6 as follows:

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb focal netq-4.6
    ```

4. Update the NetQ `debian` packages.

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 https://apps3.cumulusnetworks.com/repos/deb focal InRelease [13.8 kB]
    Get:2 https://apps3.cumulusnetworks.com/repos/deb focal/netq-4.6 amd64 Packages [758 B]
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
### Run the Upgrade

{{%notice note%}}

Perform the following steps using the `cumulus` user account.

{{%/notice%}}
#### Pre-installation Checks

Verify the following items before upgrading NetQ. For cluster deployments, verify steps 1 and 4 on all nodes in the cluster:

1. Confirm your VM is configured with 16 vCPUs. If your VM is configured with fewer than 16 vCPUs, power off your VM, reconfigure your hypervisor to allocate 16 vCPUs, then power the VM on before proceeding with the following steps.

2. Check if enough disk space is available before you proceed with the upgrade:

```
cumulus@netq-appliance:~$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       248G   70G  179G  28% /
cumulus@netq-appliance:~$
```
NVIDIA recommends proceeding with the installation only if the `Use%` is less than 70%. You can delete previous software tarballs in the `/mnt/installables/` directory to regain some space. If you cannot decrease disk usage to under 70%, contact the NVIDIA support team.

3. Run the `netq show opta-health` command and check that all pods are in the `READY` state. If the pods are in a state other than `READY`, contact the NVIDIA support team.

4. Check if the certificates have expired:

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

#### Upgrade Using the NetQ CLI

After completing the preparation steps, upgrade your NetQ on-premises or cloud VMs using the NetQ CLI.

To upgrade your NetQ software:

1. Run the appropriate `netq upgrade` command.

{{<tabs "CLI Upgrade">}}

{{<tab "On-premises Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.6.0.tgz
```

{{</tab>}}

{{<tab "Cloud Deployments">}}

```
netq upgrade bundle /mnt/installables/NetQ-4.6.0-opta.tgz
```

{{</tab>}}

{{</tabs>}}

2. After the upgrade command completes, confirm the upgrade was successful.

On-premises VM:

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.6.0
    APPLIANCE_MANIFEST_HASH=1c3b0266c12606d2bd4ce482afa30d118a2c84a07850fda3376c716514edce05
    APPLIANCE_VERSION=4.6.0
    APPLIANCE_NAME=NetQ On-premises Appliance
    ```

Cloud VM:

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.6.0
    APPLIANCE_MANIFEST_HASH=9a654b495a3175500f9a09f5af52e6f79c33706143a39f54b980a43a254fa2dd
    APPLIANCE_VERSION=4.6.0
    APPLIANCE_NAME=NetQ Cloud Appliance
    ```

3. To complete the upgrade to 4.6.0, retag and restart the following pods:

Cloud VM:

```
sudo docker tag localhost:5000/fluend-aggregator-opta:1.14.3 docker-registry:5000/fluend-aggregator-opta:1.14.3
sudo docker push docker-registry:5000/fluend-aggregator-opta:1.14.3
sudo kubectl get pods -n default|grep -i fluend-aggregator-opta|awk '{print $1}'|xargs kubectl delete pod -n default
```

On-premises VM:

```
sudo docker tag localhost:5000/fluend-aggregator-opta:1.14.3 docker-registry:5000/fluend-aggregator-opta:1.14.3
sudo docker push docker-registry:5000/fluend-aggregator-opta:1.14.3
sudo kubectl get pods -n default|grep -i fluend-aggregator-opta|awk '{print $1}'|xargs kubectl delete pod -n default

sudo docker tag localhost:5000/cp-schema-registry:7.2.0 docker-registry:5000/cp-schema-registry:7.2.0
sudo docker push docker-registry:5000/cp-schema-registry:7.2.0
sudo kubectl get pods -n default|grep -i cp-schema-registry|awk '{print $1}'|xargs kubectl delete pod -n default

sudo docker tag localhost:5000/cp-kafka:7.2.0 docker-registry:5000/cp-kafka:7.2.0
sudo docker push docker-registry:5000/cp-kafka:7.2.0
sudo kubectl get pods -n default|grep -i kafka-broker|awk '{print $1}'|xargs kubectl delete pod -n default
```

## Upgrading from Earlier Releases

Upgrading to NetQ 4.6.0 from a NetQ release earlier than 4.5.0 requires a new installation of the NetQ virtual machine. Perform the following steps to upgrade:

1. For on-premises deployments, {{<link title="Back Up and Restore NetQ" text="back up your existing NetQ data">}}. NetQ cloud deployments create backups automatically.

2. Follow the {{<link title="Install the NetQ System" text="installation process">}} for your deployment model.

3. For on-premises deployments, {{<link title="Back Up and Restore NetQ/#restore-your-netq-data" text="restore your NetQ data">}}.