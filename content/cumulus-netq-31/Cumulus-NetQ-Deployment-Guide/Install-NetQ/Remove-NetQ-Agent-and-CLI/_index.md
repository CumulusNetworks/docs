---
title: Remove the NetQ Agent and CLI
author: Cumulus Networks
weight: 135
toc: 3
---

If you need to remove the NetQ agent and/or the NetQ CLI from a Cumulus Linux switch or Linux host, follow the steps below.

## Remove the Agent and CLI from a Cumulus Linux Switch or Ubuntu Host

Use the `apt-get purge` command to remove the NetQ agent or CLI package from a Cumulus Linux switch or an Ubuntu host.

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

To verify the packages have been removed from the switch, run:

```
cumulus@switch:~$ dpkg-query -l netq-agent
dpkg-query: no packages found matching netq-agent
cumulus@switch:~$ dpkg-query -l netq-apps
dpkg-query: no packages found matching netq-apps
```

## Remove the Agent and CLI from a RHEL7 or CentOS Host

Use the `yum remove` command to remove the NetQ agent or CLI package from a RHEL7 or CentOS host.

```
root@rhel7:~# sudo yum remove netq-agent netq-apps
Loaded plugins: fastestmirror
Resolving Dependencies
--> Running transaction check
---> Package netq-agent.x86_64 0:3.0.0-rh7u27~1588050478.0e20d33 will be erased
--> Processing Dependency: netq-agent >= 3.0.0 for package: cumulus-netq-3.0.0-rh7u27~1588054943.10fa7f6.x86_64
--> Running transaction check
---> Package cumulus-netq.x86_64 0:3.0.0-rh7u27~1588054943.10fa7f6 will be erased
--> Finished Dependency Resolution

Dependencies Resolved

...

Removed:
  netq-agent.x86_64 0:3.0.0-rh7u27~1588050478.0e20d33

Dependency Removed:
  cumulus-netq.x86_64 0:3.0.0-rh7u27~1588054943.10fa7f6

Complete!

```

{{%notice tip%}}

If you only want to remove the agent or the CLI, but not both, specify just the relevant package in the `yum remove` command.

{{%/notice%}}

To verify the packages have been removed from the switch, run:

```
root@rhel7:~# rpm -q netq-agent
package netq-agent is not installed
root@rhel7:~# rpm -q netq-apps
package netq-apps is not installed
```
