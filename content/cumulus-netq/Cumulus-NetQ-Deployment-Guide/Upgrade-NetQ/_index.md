---
title: Upgrade NetQ
author: Cumulus Networks
weight: 73
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
If you installed Cumulus NetQ 2.4.0 *prior* to January 24, 2020, then Cumulus recommends that you perform an update to prevent a potential memory issue with the NetQ Agent.

If you installed Cumulus NetQ 2.4.0 *after* January 24, 2020, you do not need to upgrade the software.

The update includes changes to the `netq-apps` and `netq-agent` components. No update is needed for the KVM or VMware virtual machines or the Bootstrap images.

## Upgrade NetQ on Server Running Ubuntu ##

The following instructions are applicable to both on-premises and cloud deployments.

To upgrade NetQ:

1. Log in to your NetQ Platform or Appliance.

2. Update your NetQ repository.

```
cumulus@<hostname>:~$ sudo apt-get update
```

3. Install the updated components.

```
cumulus@<hostname>:~$ sudo apt-get install -y netq-apps netq-agent
```

4. Restart the NetQ Agent.

```
cumulus@<hostname>:~$ netq config restart agent
```

5. Restart the CLI.

```
cumulus@<hostname>:~$ netq config restart cli
```

## Update NetQ on Server Running Cumulus Linux ##

The following instructions are applicable to both Cumulus Linux 3.x and 4.x, and for both on-premises and cloud deployments.

To upgrade NetQ:

1. Log in to your NetQ Platform or Appliance.

2. Update your NetQ repository.

```
cumulus@<hostname>:~$ sudo apt-get update
```

3. Update the NetQ Agent.

```
cumulus@<hostname>:~$ sudo apt-get install -y netq-agent
```

4. Restart the NetQ Agent.

```
cumulus@<hostname>:~$ netq config restart agent
```

5. Optionally update the CLI.

```
cumulus@<hostname>:~$ sudo apt-get install -y netq-apps
```

6. Restart the CLI.

```
cumulus@<hostname>:~$ netq config restart cli
```
