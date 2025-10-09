---
title: Uninstall NetQ
author: NVIDIA
weight: 560
toc: 3
---
This page outlines how to remove the NetQ software from your system server and switches.

## Remove the NetQ Agent and CLI

{{<tabs "Remove NetQ Agent and CLI">}}

{{<tab "Cumulus Linux Switch or Ubuntu Host">}}

Use the `apt-get purge` command to remove the NetQ Agent or CLI package from a Cumulus Linux switch or an Ubuntu host:

```
cumulus@switch:~$ sudo apt-get update
cumulus@switch:~$ sudo apt-get purge netq-agent netq-apps
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages will be REMOVED:
  netq-agent* netq-apps*
0 upgraded, 0 newly installed, 2 to remove and 0 not upgraded.
After this operation, 310 MB disk space will be freed.
Do you want to continue? [Y/n] Y
Creating pre-apt snapshot... 2 done.
(Reading database ... 42026 files and directories currently installed.)
Removing netq-agent (3.0.0-cl3u27~1587646213.c5bc079) ...
/usr/sbin/policy-rc.d returned 101, not running 'stop netq-agent.service'
Purging configuration files for netq-agent (3.0.0-cl3u27~1587646213.c5bc079) ...
dpkg: warning: while removing netq-agent, directory '/etc/netq/config.d' not empty so not removed
Removing netq-apps (3.0.0-cl3u27~1587646213.c5bc079) ...
/usr/sbin/policy-rc.d returned 101, not running 'stop netqd.service'
Purging configuration files for netq-apps (3.0.0-cl3u27~1587646213.c5bc079) ...
dpkg: warning: while removing netq-apps, directory '/etc/netq' not empty so not removed
Processing triggers for man-db (2.7.0.2-5) ...
grep: extra.services.enabled: No such file or directory
Creating post-apt snapshot... 3 done.
```

{{%notice tip%}}

If you only want to remove the agent or the CLI, but not both, specify just the relevant package in the `apt-get purge` command.

{{%/notice%}}

To verify the removal of the packages from the switch, run:

```
cumulus@switch:~$ dpkg-query -l netq-agent
dpkg-query: no packages found matching netq-agent
cumulus@switch:~$ dpkg-query -l netq-apps
dpkg-query: no packages found matching netq-apps
```
{{</tab>}}

{{<tab "RHEL7 or CentOS Host">}}

Use the `yum remove` command to remove the NetQ agent or CLI package from a RHEL7 or CentOS host:

```
root@rhel7:~# sudo yum remove netq-agent netq-apps
Loaded plugins: fastestmirror
Resolving Dependencies
--> Running transaction check
---> Package netq-agent.x86_64 0:3.1.0-rh7u28~1594097110.8f00ba1 will be erased
--> Processing Dependency: netq-agent >= 3.2.0 for package: cumulus-netq-3.1.0-rh7u28~1594097110.8f00ba1.x86_64
--> Running transaction check
---> Package cumulus-netq.x86_64 0:3.1.0-rh7u28~1594097110.8f00ba1 will be erased
--> Finished Dependency Resolution

Dependencies Resolved

...

Removed:
  netq-agent.x86_64 0:3.1.0-rh7u28~1594097110.8f00ba1

Dependency Removed:
  cumulus-netq.x86_64 0:3.1.0-rh7u28~1594097110.8f00ba1

Complete!

```

{{%notice tip%}}

If you only want to remove the agent or the CLI, but not both, specify just the relevant package in the `yum remove` command.

{{%/notice%}}

To verify the removal of the packages from the switch, run:

```
root@rhel7:~# rpm -q netq-agent
package netq-agent is not installed
root@rhel7:~# rpm -q netq-apps
package netq-apps is not installed
```

{{</tab>}}

{{</tabs>}}

## Uninstall NetQ from the System Server

First remove the data collected to free up used disk space. Then remove the software.

1. Log in to the NetQ system server.

2. Remove the data:

  ```
  netq bootstrap reset purge-db
  ```

3. Remove the software with `apt-get purge`:

  ```
  cumulus@switch:~$ sudo apt-get update
  cumulus@switch:~$ sudo apt-get purge netq-agent netq-apps
  ```

4. Verify the removal of the packages from the switch:

  ```
  cumulus@switch:~$ dpkg-query -l netq-agent
  dpkg-query: no packages found matching netq-agent
  cumulus@switch:~$ dpkg-query -l netq-apps
  dpkg-query: no packages found matching netq-apps
  ```

5. Delete the virtual machine according to the usual VMware or KVM practice.

  {{<tabs "TabID130" >}}

{{<tab "VMware ESX" >}}

Delete a virtual machine from the host computer using one of the following methods:

- Right-click the name of the virtual machine in the **Favorites** list, then select **Delete from Disk**.
- Select the virtual machine and choose **VM** > **Delete from disk**.

{{</tab>}}

{{<tab "KVM" >}}

Delete a virtual machine from the host computer using one of the following methods:

- Run `virsch undefine <vm-domain> --remove-all-storage`
- Run `virsh undefine <vm-domain> --wipe-storage`
{{</tab>}}

{{</tabs>}}
