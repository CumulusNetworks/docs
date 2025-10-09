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

You can read more about LCM in the {{<link url="Lifecycle-Management" text="NetQ administrator guide">}}.

## LCM Command Summary

The NetQ CLI provides a number of `netq lcm` commands to perform LCM. The syntax of these commands is:

    netq lcm upgrade name <text-job-name> cl-version <text-cumulus-linux-version> netq-version <text-netq-version> hostnames <text-switch-hostnames> [run-restore-on-failure] [run-before-after]
    netq lcm add credentials username <text-switch-username> (password <text-switch-password> | ssh-key <text-ssh-key>)
    netq lcm add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
    netq lcm del credentials
    netq lcm show credentials [json]
    netq lcm show switches [version <text-cumulus-linux-version>] [json]
    netq lcm show status <text-lcm-job-id> [json]
    netq lcm add cl-image <text-image-path>
    netq lcm del cl-image <text-image-id>
    netq lcm add netq-image <text-image-path>
    netq lcm del netq-image <text-image-path>
    netq lcm show images [<text-image-id>] [json]
    netq lcm show upgrade-jobs [json]

## Upgrade Steps

To upgrade Cumulus Linux on your switches, you need to do the following:

1. Configure {{<link url="#configure-access-credentials" text="access credentials">}} to the switches.
1. Configure {{<link url="#configure-switch-roles" text="switch roles">}} to determine the order in which the switches get upgraded.
1. Upload the {{<link url="#upload-cumulus-linux-install-images" text="Cumulus Linux install image">}}.
1. Run {{<link url="#upgrade-cumulus-linux-on-a-switch" text="the upgrade">}}.

## Configure Access Credentials

Switch access credentials are needed for upgrading Cumulus Linux on the switches. You can choose between basic authentication (username and password) and SSH key-based authentication. These credentials apply to all switches.

To configure basic authentication for the _cumulus_ user with the password _CumulusLinux!_, run:

    netq lcm add credentials username cumulus password CumulusLinux!

To configure authentication using a public SSH key, run:

    netq lcm add credentials ssh-key PUBLIC_SSH_KEY

### View Credentials

A switch can have just one set of credentials. To see the credentials, run `netq lcm show credentials`.

If an SSH key is used for the credentials, the public key is displayed in the command output:

```
cumulus@switch:~$ netq lcm show credentials
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
SSH              MY-SSH-KEY                                       Tue Apr 28 19:08:52 2020
```

If a username and passord is used for the credentials, the username is displayed in the command output but the password is masked:

```
cumulus@leaf01:mgmt-vrf:~$ netq lcm show credentials 
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
BASIC                           cumulus          **************   Tue Apr 28 19:10:27 2020
```

### Remove Credentials

To remove the credentials, run `netq lcm del credentials`.

## Configure Switch Roles

Four pre-defined switch roles are available. Their names are based on Clos architecture:

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

After installing NetQ, there are no Cumulus Linux images in the LCM repository. You can upload Cumulus Linux binary images to a local LCM repository for use with installation and upgrade of your switches.

For more information about Cumulus Linux images and LCM, read {{<link url="Lifecycle-Management/#image-management" text="Image Management">}}.

1. Download the version of Cumulus Linux you plan to use to upgrade the switches from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox download">}} site.

1. Upload the image onto an accessible part of your network. The following example uses the Cumulus Linux 3.7.12 disk image, named `cumulus-linux-3.7.12-bcm-amd64.bin`.

       cumulus@switch:~$ netq lcm add cl-image /path/to/download/cumulus-linux-3.7.12-bcm-amd64.bin

## Upload Cumulus NetQ Install Images

After installing NetQ, there are no Cumulus NetQ images in the LCM repository. You can upload Cumulus NetQ binary images to a local LCM repository for use with installation and upgrade of your switches.

For more information about Cumulus NetQ images and LCM, read {{<link url="Lifecycle-Management/#image-management" text="Image Management">}}.

1. Download the version of Cumulus NetQ you plan to use to upgrade the switches from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads">}} site.

1. Upload the Cumulus NetQ packages onto an accessible part of your network. The following example uses the Cumulus NetQ 3.1.0 debian packages, named `netq-apps_3.1.0-ub18.04u27~1588242914.9fb5b87_amd64.deb` and `netq-agent_3.1.0-ub18.04u27~1588242914.9fb5b87_amd64.deb`.

    ```
    cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-apps_3.1.0-ub18.04u27~1588242914.9fb5b87_amd64.deb
    cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-agent_3.1.0-ub18.04u27~1588242914.9fb5b87_amd64.deb
    ```

## Upgrade Cumulus Linux on a Switch

LCM provides the ability to upgrade Cumulus Linux on switches on your network through NetQ. Once the image is uploaded and the switch credentials are configured, you can upgrade the operating system. To do you, you need:

- A Cumulus Linux license file accessible over the network.
- A Cumulus Linux install image accessible over the network.
- The ID for the Cumulus Linux image.
- The names of the switches you plan to upgrade.

To upgrade one or more switches:

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

1. Perform the upgrade:

       cumulus@switch:~$ netq lcm upgrade name upgrade-3712 cl-version 3.7.12 netq-version 3.1.0 hostnames spine01,spine02 order spine

You can assign an order for which switches to upgrade based on the switch roles defined above. For example, to upgrade the spines before the leafs, add the `order ROLE1,ROLE2` option to the command:

    cumulus@switch:~$ netq lcm upgrade name upgrade-3712 cl-version 3.7.12 netq-version 3.1.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf

If the switches have not been assigned a role, then do not use the `order` option. So in this example, if switches spine01 and spine02 have not been assigned the _spine_ role, then do not specify the `order spine` option.

You can decide to run LCM before and after the upgrade by adding the `run-before-after` option to the command:

    cumulus@switch:~$ netq lcm upgrade name upgrade-3712 cl-version 3.7.12 netq-version 3.1.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-before-after

You can decide to restore LCM when a failure occurs by adding the `run-restore-on-failure` option to the command:

    cumulus@switch:~$ netq lcm upgrade name upgrade-3712 cl-version 3.7.12 netq-version 3.1.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-restore-on-failure

## Running an Upgrade Job Again

Every upgrade job requires a unique name. If the upgrade job fails, you need to provide a new name for the job in order to run the upgrade job again. You can get the history of all previous upgrade jobs to ensure that the new upgrade job does not have a duplicate name.

To see a history of previous upgrades that have been run, run `netq lcm show upgrade-jobs`:

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

To see details a particular upgrade job, run `netq lcm show status job-ID`:

```
cumulus@switch:~$ netq lcm show status job_upgrade_fda24660-8669-11ea-bda5-ad48ae2cfafb
Hostname    CL Version    Backup Status    Backup Start Time         Restore Status    Restore Start Time        Upgrade Status    Upgrade Start Time
----------  ------------  ---------------  ------------------------  ----------------  ------------------------  ----------------  ------------------------
spine02     3.7.12        COMPLETED        Fri Apr 24 20:28:17 2020  COMPLETED         Fri Apr 24 20:31:53 2020  COMPLETED         Fri Apr 24 20:28:28 2020
spine03     3.7.12        COMPLETED        Fri Apr 24 20:28:17 2020  COMPLETED         Fri Apr 24 20:31:53 2020  COMPLETED         Fri Apr 24 20:28:28 2020
leaf03      3.7.12        COMPLETED        Fri Apr 24 20:33:26 2020  COMPLETED         Fri Apr 24 20:37:10 2020  COMPLETED         Fri Apr 24 20:33:37 2020
fw1         3.7.12        COMPLETED        Fri Apr 24 20:38:48 2020  COMPLETED         Fri Apr 24 20:42:05 2020  COMPLETED         Fri Apr 24 20:38:58 2020
```

## Back Up and Restore

To back up and restore the switches themselves, use the `config-backup` and `config-restore` commands in Cumulus Linux directly on the switches. For more information, read the [Cumulus Linux user guide]({{<ref "/cumulus-linux-43/Installation-Management/Back-up-and-Restore" >}}).
