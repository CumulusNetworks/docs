---
title: NetQ Service Console
author: Cumulus Networks
weight: 15
aliases:
 - /display/NETQ110/NetQ+Service+Console
 - /pages/viewpage.action?pageId=7111316
pageID: 7111316
product: Cumulus NetQ
version: "1.1"
imgData: cumulus-netq-110
siteSlug: cumulus-netq-110
old: true
---
The NetQ Telemetry Server provides access to the NetQ Service Console, a
graphical user interface (GUI) for NetQ. The service console in turn
provides terminal access to any node in the fabric.

{{%notice info%}}

The Cumulus NetQ Service Console utilizes elements of Portainer. You can
read the Portainer license file
[here](https://github.com/portainer/portainer/blob/develop/LICENSE).

{{%/notice%}}

## Connecting to the Service Console</span>

To connect to the service console, open a browser, and go to the IP
address of the [telemetry
server](/cumulus-netq-110/Getting-Started-with-NetQ/). You are
prompted to log in with the username and password for the service
console. You can use the same credentials that you use to access the
telemetry server VM. The service console user accounts are managed in
the telemetry server itself, just like any Linux user account.

{{% imgOld 0 %}}

## Getting Service Console Information</span>

The lower lefthand corner of the service console window displays
information about

{{% imgOld 1 %}}

  - **IP**: The IP address of the telemetry server VM. In the default
    configuration, the IP field is empty. To have this field display the
    IP address, edit `/etc/cts/redis/host.conf` and set the `HOST_IP`
    variable to the telemetry server's IP address, then restart the
    `netq-gui` service with `sudo systemctl restart netq-gui.service`.

  - **Hostname**: The hostname of the telemetry server VM. if you change
    the hostname and don't restart the `netq-gui` service, the hostname
    won't change in the service console.

  - **Role**: The role that the NetQ database is in, which currently can
    be *master* only, as there is only one Redis server, which is the
    primary.

  - **Redis availability**: Indicates whether or not the Redis database
    on the telemetry server VM is reachable.

## Accessing the NetQ Command Line</span>

The service console provides access to a standard Bash shell, so you can
run NetQ commands - or any Linux command - directly on a given node.

{{%notice tip%}}

The console is connected to the NetQ CLI container within the telemetry
server; it is not connected to the shell of the telemetry server itself.
As such, the `netq-shell` command does not work in the console; it is
intended to run regular NetQ commands.

{{%/notice%}}

In the Services window of the console, click **Launch console**.

{{% imgOld 2 %}}

You can run any NetQ commands within the console, such as `netq show
agents`:

{{% imgOld 3 %}}

When you're finished with the session, click **Back to Services** to
close the console.

