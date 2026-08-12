---
title: Set Up the NFS Server
author: NVIDIA
weight: 200
toc: 2
---

## Prerequisites

- Run all commands using `sudo`

## Install and Configure the NFS Server

Follow these steps to install and configure the NFS server on Ubuntu:


1. Run `sudo apt update` to update the package list.

2. Install the NFS server package:
```
sudo apt install -y nfs-kernel-server
```

3. Verify that the NFS service is running and in an active state:
```
sudo systemctl status nfs-kernel-server
```

4. Enable the service to start automatically on boot:
```
sudo systemctl enable nfs-kernel-server
```

5. Create the export directory. This directory will be used to store the data from the NetQ cluster:

```
sudo mkdir -p /data/scale-backup
```

6. Set the appropriate ownership and permissions. Replace the `example:examplegroup` placeholder text in the following command:

```
sudo chown example:examplegroup /data/scale-backup
sudo chmod 755 /data/scale-backup
```

7. Configure NFS exports. 

You must set the export directory to the IP addresses of the NetQ cluster. The following examples use the `/data/scale-backup/` path to back up data from a NetQ cluster of three servers with the following IP addresses: 10.87.218.75, 10.87.218.72, 10.87.218.68 

First, edit the `exports` file:

```
sudo vi /etc/exports
```

{{<tabs "tabID57">}}

{{<tab "Export to Specific IP Addresses">}}

```
/data/scale-backup 10.87.218.75(rw,sync,no_root_squash,no_subtree_check)
/data/scale-backup 10.87.218.68(rw,sync,no_root_squash,no_subtree_check)
/data/scale-backup 10.87.218.72(rw,sync,no_root_squash,no_subtree_check)
```
{{</tab>}}
{{<tab "Export to the Entire Subnet">}}

Append `.*` to allow access to all hosts in 10.87.218.*:

```
/data/scale-backup 10.87.218.0/24(rw,sync,no_root_squash,no_subtree_check)
```

{{</tab>}}

{{<tab "Export to Multiple Subnets">}}

```
/data/scale-backup 10.87.218.0/24(rw,sync,no_root_squash,no_subtree_check) \
                   10.104.229.0/24(rw,sync,no_root_squash,no_subtree_check)
```
{{</tab>}}

{{</tabs>}}


9. Apply the export configuration by reloading the exports:

```
sudo exportfs -rav
```

10. Verify the exported paths:

```
showmount -e localhost
```

Expected output:

```
/data/scale-backup 10.87.218.0/24
```
 
11. Confirm that the NFS path is visible from both the backup and restore machines:

```
showmount -e <NFS-SERVER-IP>
```

## Next Steps

- {{<link title="Back Up and Restore Using NFS">}}