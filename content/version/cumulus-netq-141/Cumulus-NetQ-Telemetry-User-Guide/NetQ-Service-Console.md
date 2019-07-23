---
title: NetQ Service Console
author: Cumulus Networks
weight: 53
aliases:
 - /display/NETQ141/NetQ+Service+Console
 - /pages/viewpage.action?pageId=10453456
pageID: 10453456
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
The NetQ Telemetry Server provides access to the NetQ Service Console, a
graphical user interface (GUI) for NetQ. The Service Console provides a
command line interface for running NetQ commands.

{{%notice info%}}

The Cumulus NetQ Service Console utilizes elements of Portainer. You can
read the Portainer license file
[here](https://github.com/portainer/portainer/blob/develop/LICENSE).

{{%/notice%}}

## Connect to the Service Console</span>

To connect to the Service Console:

1.  Open an Internet browser.

2.  In the Address Bar, type \<telemetry-server-ip-address:port\>; for
    example, *http://172.28.128.20:9000.*  
    If you don't know or remember the IP address of your Telemetry
    Server, refer to the [Install
    NetQ](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
    chapter for details. The default port is 9000.
    
    {{% imgOld 0 %}}

3.  Enter your username and password to open the Service Console.  
    You can use the same credentials that you use to access the
    Telemetry Server VM. The Service Console user accounts are managed
    in the Telemetry Server itself, just like any Linux user account.
    
    {{% imgOld 1 %}}

### View Service Console Information</span>

The lower lefthand corner of the Service Console window displays
information about the Telemetry Server:

{{% imgOld 2 %}}

  - **IP**: The IP address of the Telemetry Server VM. In the default
    configuration, the IP field is empty. To have this field display the
    IP address, edit `/etc/cts/redis/host.conf` and set the `HOST_IP`
    variable to the Telemetry Server's IP address, then restart the
    `netq-gui` service with `sudo systemctl restart netq-gui.service`.

  - **Hostname**: The hostname of the Telemetry Server VM. The hostname
    is based on the *%H* environment value in the `systemd` service
    configuration. If you change the hostname, you should restart the
    `netq-gui` service so the new hostname displays in the Service
    Console.

  - **Role**: The role that the NetQ database is in, which currently can
    be *master* or *replica*, if high availability (HA) mode is enabled.
    If it's not enabled, *master* appears here. If the role is set to
    *replica*, this indicates that the node is part of an HA cluster,
    since there is no replica in a non-HA environment.

  - **High Availability**: A check mark appears if HA mode is enabled
    and **** the current node is the *master* node. **** This also
    determines that the master referred to in the role above is also the
    master for the Redis cluster in HA mode.

  - **Redis availability**: Indicates whether or not the Redis database
    on the Telemetry Server VM is reachable.

  - **Version**: Indicates the Service Console version installed. This
    should match your NetQ version.

## Access the NetQ Command Line</span>

The Service Console runs within the NetQ CLI container. You can use it
to connect to the NetQ command line locally within the container. You
can also use it to access the container's `/etc/cts/netq` directory to
edit or add configuration files under /`config.d`. You cannot use it to
connect to the NetQ CLI on a remote system; nor can you access the
container's `systemd` services or alter anything else in the container.
The filesystem exposed in the console window is actually the container's
filesystem.

In the Services window of the console, verify the NetQ CLI **State** is
*running*, then click **Launch console**.

{{% imgOld 3 %}}

You are logged in to the Telemetry Server with root user privileges.

## Run NetQ Commands</span>

You can run all NetQ `check` and `show` commands, agent configuration
commands, and the `trace` and `resolve` commands from within the
console, just as you would if you were logged directly into the network
switch or server . Check commands color the output text green to
indicate successful results, and red or yellow to indicate errors or
warnings.

**Example**: Run `netq show agents`

{{% imgOld 4 %}}

{{%notice tip%}}

If the output from a given command it too wide for the current console
window causing the data rows to wrap over lines, widen the console
window by clicking and dragging the right edge of the window and then
rerun the command for a cleaner view.

{{%/notice%}}

**Example**: Run `netq check bgp, netq check agents` and `netq check
ntp`

{{% imgOld 5 %}}

Note that in this example, BGP is not configured, so no information was
found, NetQ Agents status is all good, and that multiple nodes are not
time synchronized (which you would want to fix\!).

## Exit the Service Console</span>

When you're finished with the session, click **Back to Services** to
close the console window, then click **log out** to close the Service
Console.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
