---
title: NetQ Service Console
author: Cumulus Networks
weight: 21
aliases:
 - /display/NETQ10/NetQ+Service+Console
 - /pages/viewpage.action?pageId=6488214
pageID: 6488214
product: Cumulus NetQ
version: 1.0.0
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
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
server](/version/cumulus-netq-10/Getting-Started-with-NetQ). You are
prompted to log in with the username and password for the service
console. The default account is the *admin* user, and its default
password is *CumulusNetQ\!*.

{{% imgOld 0 %}}

## Configuring Users</span>

By default, the service console is configured with an administrator
account named *admin*, but you can add more users as needed. To add a
new user:

1.  In the Service Console, click **Users**.
    
    {{% imgOld 1 %}}

2.  Enter the username in the **Username** field.

3.  Enter that user's password in the **Password** and **Confirm
    Password** fields.

4.  If this user account is to be an administrator to the service
    console, enable the **Administrator** toggle.

5.  Click **Add user** to create the account.

### Other User Account Actions</span>

You can edit a user's role. On the **Users** tab, select the account
under **Users**, then click **Edit**.

You can delete a user account. On the **Users** tab, select the account
under **Users**, then click **Remove**. You cannot delete the last
remaining administrator account.

To change an account password, click the **Password** tab.

## Accessing the NetQ Command Line</span>

The service console provides access to a standard Bash shell, so you can
run NetQ commands - or any Linux command - directly on a given node.

{{%notice tip%}}

The console is connected to the NetQ CLI container within the telemetry
server; it is not connected to the shell of the telemetry server itself.
As such, the `netq-shell` command does not work in the console; it is
intended to run regular NetQ commands.

{{%/notice%}}

{{% imgOld 2 %}}

In the Services window of the console, click **Launch console**, then
click **Connect**.

{{% imgOld 3 %}}

You can run any NetQ commands within the console, such as `netq show
agents`:

{{% imgOld 4 %}}

When you're finished with the session, click **Disconnect** to close the
console.
