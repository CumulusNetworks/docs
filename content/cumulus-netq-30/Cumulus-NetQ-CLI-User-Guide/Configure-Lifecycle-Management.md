---
title: Configure Lifecycle Management
author: Cumulus Networks
weight: 495
toc: 3
---

{{%notice warning%}}

This topic for network administrators only.

{{%/notice%}}

As an administrator, you want to manage the deployment of Cumulus Networks product software onto your network devices (servers, appliances, and switches) in the most efficient way and with the most information about the process as possible. With this release, NetQ introduces Lifecycle Management (LCM) to the NetQ CLI, which supports Cumulus Linux image, switch, and credential management.

You can read about LCM in the {{<link url="Lifecycle-Management" text="NetQ administrator guide">}}.

## LCM Command Summary

The NetQ CLI provides a number of `netq lcm` commands to perform LCM. The syntax of these commands is:

    netq lcm upgrade name <text-job-name> image-id <text-image-id> license <text-cumulus-license> hostnames <text-switch-hostnames> [order <text-upgrade-order>] [run-before-after]
    netq lcm add credentials (username <text-switch-username> password <text-switch-password> | ssh-key <text-ssh-key>)
    netq lcm add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
    netq lcm del credentials
    netq lcm show credentials [json]
    netq lcm show switches [version <text-cumulus-linux-version>] [json]
    netq lcm show status <text-lcm-job-id> [json]
    netq lcm add image <text-image-path>
    netq lcm del image <text-image-id>
    netq lcm show images [<text-image-id>] [json]
    netq lcm show upgrade-jobs [json]

## Configure Access Credentials

Switch access credentials are needed for performing upgrades. You can choose between basic authentication (username and password) and SSH key-based authentication. These credentials apply to all switches.

To configure username/password authentication for the _cumulus_ user with the password _CumulusLinux!_, run:

    netq lcm add credentials (username cumulus password CumulusLinux!

To configure access credentials using a public SSH key, run: 

    netq lcm add credentials ssh-key PUBLIC_SSH_KEY

## Configure Switch Roles

Four pre-defined switch roles are available, based on Clos architecture:

- Superspine
- Spine
- Leaf
- Exit

Switch roles are used to:

- Identify switch dependencies and determine the order in which switches are upgraded.
- Determine when to stop if an upgrade fails.

For more information about managing switch roles, see {{<link url="Lifecycle-Management/#role-management" text="Role Management">}}.

To configure one or more switches for a given role, run `netq lcm add role` command. For example, to configure leaf01 through leaf04 in the _leaf_ role, run:

    netq lcm add role leaf switches leaf01,leaf02,leaf03,leaf04

### Show Switch Roles

To see the roles of the switches in the fabric, run `netq lcm show switches`. You can filter the list by a particular version by running `netq lcm show switches version X.Y.Z`.

```
cumulus@leaf01:mgmt-vrf:~$ netq lcm show switches
Hostname          Role       IP Address                MAC Address        CPU      CL Version           NetQ Version             Last Changed
----------------- ---------- ------------------------- ------------------ -------- -------------------- ------------------------ -------------------------
fw1               exit       192.168.200.61            44:38:39:00:01:8C  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 18:22:05 2020
                                                                                                        c5bc079
spine02           spine      192.168.200.22            44:38:39:00:01:92  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 17:51:28 2020
                                                                                                        c5bc079
spine03           spine      192.168.200.23            44:38:39:00:01:70  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 17:51:30 2020
                                                                                                        c5bc079
leaf03            leaf       192.168.200.13            44:38:39:00:01:84  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 18:07:06 2020
                                                                                                        c5bc079
border02          exit       192.168.200.64            44:38:39:00:01:7C  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 18:17:22 2020
                                                                                                        c5bc079
leaf04            leaf       192.168.200.14            44:38:39:00:01:8A  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 18:06:36 2020
                                                                                                        c5bc079
fw2               exit       192.168.200.62            44:38:39:00:01:8E  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 18:36:30 2020
                                                                                                        c5bc079
leaf01            leaf       192.168.200.11            44:38:39:00:01:7A  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 18:07:48 2020
                                                                                                        c5bc079
spine01           spine      192.168.200.21            44:38:39:00:01:82  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 17:55:56 2020
                                                                                                        c5bc079
spine04           spine      192.168.200.24            44:38:39:00:01:6C  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 17:49:26 2020
                                                                                                        c5bc079
border01          exit       192.168.200.63            44:38:39:00:01:74  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 18:18:31 2020
                                                                                                        c5bc079
leaf02            leaf       192.168.200.12            44:38:39:00:01:78  x86_64   3.7.12               3.0.0-cl3u27~1587646213. Mon Apr 27 18:06:36 2020
```

## Upload Cumulus Linux Install Images

After installing NetQ 3.0, there are no Cumulus Linux images in the LCM repository. You can upload Cumulus Linux binary images to a local LCM repository for use with installation and upgrade of your switches.

For more information about Cumulus Linux images and LCM, read {{<link url="Lifecycle-Management/#image-management" text="Image Management">}}.

1. Download the version of Cumulus Linux you plan to use to upgrade the switches from the {{<exlink url="https://cumulusnetworks.com/downloads/#product=Cumulus%20Linux" text="Cumulus Networks web site">}}.

1. Upload the image onto an accessible part of your network.

       cumulus@switch:~$ netq lcm add image /path/to/download/cumulus-linux-3.7.12-bcm-amd64.bin






1. Add the cumulus user credentials to the switch.

       cumulus@switch:~$ netq lcm add credentials username cumulus password CumulusLinux!

1. Get the Cumulus Linux install image ID. Determine the image ID intended to upgrade the switches and copy it.

       cumulus@switch:~$ netq lcm show images
       ID                        Name            CL Version           CPU      ASIC            Last Changed
       ------------------------- --------------- -------------------- -------- --------------- -------------------------
       cl_image_69ce56d15b7958de cumulus-linux-3 3.7.12               x86_64   VX              Fri Apr 24 15:20:02 2020
       5bb8371e9c4bf2fc9131da9a5 .7.12-vx-amd64.
       7b13853e2a60ca109238b22   bin
       cl_image_1187bd949568aba7 cumulus-linux-3 3.7.11               x86_64   VX              Fri Apr 24 14:55:13 2020
       eff1b37b1dec394cb832ceb4d .7.11-vx-amd64.
       94e234d9a1f62deb279c405   bin

## Upgrade Cumulus Linux on a Switch

Perform the upgrade.

       cumulus@switch:~$ netq lcm upgrade name upgrade-00 image-id cl_image_69ce56d15b7958de5bb8371e9c4bf2fc9131da9a57b13853e2a60ca109238b22 license LICENSE hostnames spine01,spine02 order spine

## Rerunning an Upgrade Job

If the upgrade job fails, and you would like to rerun the upgrade job, you need to run the upgrade job with a new unique name. You need to get the history of all previous upgrade jobs to ensure that the new upgrade job will not have a duplicate name.

```
cumulus@switch:~$ netq lcm show upgrade-jobs
Job ID       Name            CL Version           Pre-Check Status                 Warnings         Errors       Start Time
------------ --------------- -------------------- -------------------------------- ---------------- ------------ --------------------
job_upgrade_ 3.7.12 Upgrade  3.7.12               WARNING                                                        Fri Apr 24 20:27:47
fda24660-866                                                                                                     2020
9-11ea-bda5-
ad48ae2cfafb
job_upgrade_ DataCenter      3.7.12               WARNING                                                        Mon Apr 27 17:44:36
81749650-88a                                                                                                     2020
e-11ea-bda5-
ad48ae2cfafb
job_upgrade_ Upgrade to CL3. 3.7.12               COMPLETED                                                      Fri Apr 24 17:56:59
4564c160-865 7.12                                                                                                2020
3-11ea-bda5-
ad48ae2cfafb
```

## Show Upgrade Jobs and Their Status

To see a history of previous upgrades that have been run, run `netq lcm show upgrade-jobs`:

```
cumulus@leaf01:mgmt-vrf:~$ netq lcm show upgrade-jobs
Job ID       Name            CL Version           Pre-Check Status                 Warnings         Errors       Start Time
------------ --------------- -------------------- -------------------------------- ---------------- ------------ --------------------
job_upgrade_ 3.7.12 Upgrade  3.7.12               WARNING                                                        Fri Apr 24 20:27:47
fda24660-866                                                                                                     2020
9-11ea-bda5-
ad48ae2cfafb
job_upgrade_ DataCenter      3.7.12               WARNING                                                        Mon Apr 27 17:44:36
81749650-88a                                                                                                     2020
e-11ea-bda5-
ad48ae2cfafb
job_upgrade_ Upgrade to CL3. 3.7.12               COMPLETED                                                      Fri Apr 24 17:56:59
4564c160-865 7.12                                                                                                2020
3-11ea-bda5-
ad48ae2cfafb
```

Then, to see details a particular upgrade job, run:

```
cumulus@switch:~$ netq lcm show status job_upgrade_fda24660-8669-11ea-bda5-ad48ae2cfafb
Hostname    CL Version    Backup Status    Backup Start Time         Restore Status    Restore Start Time        Upgrade Status    Upgrade Start Time
----------  ------------  ---------------  ------------------------  ----------------  ------------------------  ----------------  ------------------------
spine02     3.7.12        COMPLETED        Fri Apr 24 20:28:17 2020  COMPLETED         Fri Apr 24 20:31:53 2020  COMPLETED         Fri Apr 24 20:28:28 2020
spine03     3.7.12        COMPLETED        Fri Apr 24 20:28:17 2020  COMPLETED         Fri Apr 24 20:31:53 2020  COMPLETED         Fri Apr 24 20:28:28 2020
leaf03      3.7.12        COMPLETED        Fri Apr 24 20:33:26 2020  COMPLETED         Fri Apr 24 20:37:10 2020  COMPLETED         Fri Apr 24 20:33:37 2020
fw1         3.7.12        COMPLETED        Fri Apr 24 20:38:48 2020  COMPLETED         Fri Apr 24 20:42:05 2020  COMPLETED         Fri Apr 24 20:38:58 2020
```
