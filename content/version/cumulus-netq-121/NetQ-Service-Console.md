---
title: NetQ Service Console
author: Cumulus Networks
weight: 15
aliases:
 - /display/NETQ121/NetQ+Service+Console
 - /pages/viewpage.action?pageId=8356557
pageID: 8356557
product: Cumulus NetQ
version: 1.2.1
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---
The NetQ Telemetry Server provides access to the NetQ Service Console, a
graphical user interface (GUI) for NetQ. The service console provides a
command line interface for running NetQ commands.

{{%notice info%}}

The Cumulus NetQ Service Console utilizes elements of Portainer. You can
read the Portainer license file
[here](https://github.com/portainer/portainer/blob/develop/LICENSE).

{{%/notice%}}

## <span>Connecting to the Service Console</span>

To connect to the service console, open a browser, and go to the IP
address of the [telemetry
server](/version/cumulus-netq-121/Getting-Started-with-NetQ/). The
default port is 9000 (<http://172.28.128.20:9000).>

{{% imgOld 0 %}}

You are prompted to log in with the username and password for the
service console. You can use the same credentials that you use to access
the telemetry server VM. The service console user accounts are managed
in the telemetry server itself, just like any Linux user account.

{{% imgOld 1 %}}

## <span>Getting Service Console Information</span>

The lower lefthand corner of the service console window displays
information about the telemetry server:

{{% imgOld 2 %}}

  - **IP**: The IP address of the telemetry server VM. In the default
    configuration, the IP field is empty. To have this field display the
    IP address, edit `/etc/cts/redis/host.conf` and set the `HOST_IP`
    variable to the telemetry server's IP address, then restart the
    `netq-gui` service with `sudo systemctl restart netq-gui.service`.

  - **Hostname**: The hostname of the telemetry server VM. The hostname
    is based on the *%H* environment value in the `systemd` service
    configuration. If you change the hostname, you should restart the
    `netq-gui` service so the new hostname displays in the service
    console.

  - **Role**: The role that the NetQ database is in, which currently can
    be *master* or *replica*, if [high availability (HA)
    mode](/version/cumulus-netq-121/Getting-Started-with-NetQ/Configuring-High-Availability-Mode)
    is enabled. If it's not enabled, *master* appears here. If the role
    is set to *replica*, this indicates that the node is part of an HA
    cluster, since there is no replica in a non-HA environment.

  - **High Availability**: A check mark appears if [high availability
    mode](/version/cumulus-netq-121/Getting-Started-with-NetQ/Configuring-High-Availability-Mode)
    is enabled and **** the current node is the *master* node. **** This
    also determines that the master referred to in the role above is
    also the master for the Redis cluster in HA mode.

  - **Redis availability**: Indicates whether or not the Redis database
    on the telemetry server VM is reachable.

## <span>Accessing the NetQ Command Line</span>

The service console runs within the NetQ CLI container. You can use it
to connect to the NetQ command line locally within the container. You
can also use it to access the container's `/etc/cts/netq` directory to
edit or add configuration files under /`config.d`.

However, you cannot use it to connect to the NetQ CLI on a remote
system; neither can you access the container's `systemd` services nor
alter anything else in the container. The filesystem exposed in the
console window is actually the container's filesystem.

In the Services window of the console, click **Launch console**.

{{% imgOld 3 %}}

You can run any NetQ check and show commands within the console, such as
`netq show agents`:

{{% imgOld 4 %}}

When you're finished with the session, click **Back to Services** to
close the console.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
