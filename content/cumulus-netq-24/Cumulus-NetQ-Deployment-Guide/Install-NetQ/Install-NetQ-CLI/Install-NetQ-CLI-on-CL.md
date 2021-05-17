---
title: Install and Configure the NetQ CLI on Cumulus Linux Switches
author: Cumulus Networks
weight: 126
toc: 5
---
After installing your Cumulus NetQ software and the NetQ 2.4.1 Agent on each switch you want to monitor, you can also install the NetQ CLI on switches running:

- Cumulus Linux version 3.3.2-3.7.x
- Cumulus Linux version 4.0.0 and later

## Install the NetQ CLI Installation on a Cumulus Linux Switch

A simple process installs the NetQ CLI on a Cumulus Linux switch.

To install the NetQ CLI you need to install `netq-apps` on each switch. This is available from the Cumulus Networks repository.

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy]({{<ref "/cumulus-linux-43/System-Configuration/Configuring-a-Global-Proxy" >}}) so `apt-get` can access the software package in the Cumulus Networks repository.
{{%/notice%}}

To obtain the NetQ Agent package:

1. Edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.

    *Note that NetQ has a separate repository from Cumulus Linux.*

    {{< tabs "TabID0" >}}

{{< tab "Cumulus Linux 3.x" >}}

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.4
...
```

{{%notice tip%}}
The repository `deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest` can be used if you want to always retrieve the latest posted version of NetQ.
{{%/notice%}}

{{< /tab >}}

{{< tab "Cumulus Linux 4.x" >}}

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-2.4
...
```

{{%notice tip%}}
The repository `deb http://apps3.cumulusnetworks.com/repos/deb     CumulusLinux-4 netq-latest` can be used if you want to always retrieve the latest posted version of NetQ.
{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

2. Update the local `apt` repository and install the software on the switch.

    ```
    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install netq-apps
    ```

3. Verify you have the correct version of the CLI.

    ```
    cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    You should see version 2.4.1 and update 26 or later in the results. For example:

    - For Cumulus Linux 3.3.2-3.7.x:  
      - netq-apps_2.4.1-cl3u26~1581350572.c5ec3e5_armel.deb
      - netq-apps_2.4.1-cl3u26~1581350537.c5ec3e5_amd64.deb
    - For Cumulus Linux 4.0.0:
      - netq-apps_2.4.1-cl4u26~1581350349.c5ec3e5a_armel.deb
      - netq-apps_2.4.1-cl4u26~1581350238.c5ec3e5a_amd64.deb

4. Continue with NetQ CLI configuration in the next section.

## Configure the NetQ CLI on a Cumulus Linux Switch

Two methods are available for configuring the NetQ CLI on a switch:

- Run NetQ CLI commands on the switch; refer to the next section
- Edit the configuration file on the switch; refer to {{<link title="#Configure NetQ CLI Using a Configuration File">}}

### Configure NetQ CLI Using the CLI

The steps to configure the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment. Follow the instructions for your deployment type.

{{< tabs "TabID2" >}}

{{< tab "On-premises Deployments" >}}

Use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [vrf <text-vrf-name>] [port <text-gateway-port>]
```

Restart the CLI afterward to activate the configuration.

This example uses an IP address of 192.168.1.0 and the default port and VRF.

```
cumulus@switch:~$ sudo netq config add cli server 192.168.1.0
cumulus@switch:~$ sudo netq config restart cli
```

{{%notice tip%}}
If you have a server cluster deployed, use the IP address of the master server.
{{%/notice%}}

{{< /tab >}}

{{< tab "Cloud Deployments" >}}

To access and configure the CLI on your NetQ Platform or NetQ Cloud Appliance, you must have your username and password to access the NetQ UI to generate AuthKeys. These keys provide authorized access (access key) and user authentication (secret key). Your credentials and NetQ Cloud addresses were provided by Cumulus Networks via an email titled *Welcome to Cumulus NetQ!*

To generate AuthKeys:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. From the Main Menu, select *Management* in the **Admin** column.

    {{< figure src="/images/netq/main-menu-mgmt-selected-240.png" width="400">}}

4. Click **Manage** on the User Accounts card.

5. Select your user and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18"/> above the table.

6. Copy these keys to a safe place.

    {{%notice info%}}
The secret key is only shown once. If you don't copy these, you will need to regenerate them and reconfigure CLI access.
    {{%/notice%}}

    {{%notice tip%}}
You can also save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can:

- store the file wherever you like, for example in */home/cumulus/* or */etc/netq*
- name the file whatever you like, for example *credentials.yml*, *creds.yml*, or *keys.yml*

BUT, the file must have the following format:

```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```
    {{%/notice%}}

Now that you have your AuthKeys, use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> | cli-keys-file <text-key-file> premises <text-premises-name>] [vrf <text-vrf-name>] [port <text-gateway-port>]
```

Restart the CLI afterward to activate the configuration.

This example uses the individual access key, a premises of *datacenterwest*,  and the default Cloud address, port and VRF.  **Be sure to replace the key values with your generated keys if you are using this example on your server.**

```
cumulus@switch:~$ sudo netq config add cli server api.netq.cumulusnetworks.com access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

cumulus@switch:~$ sudo netq config restart cli
Restarting NetQ CLI... Success!
```

This example uses an optional keys file. **Be sure to replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

```
cumulus@switch:~$ sudo netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /home/netq/nq-cld-creds.yml premises datacenterwest
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

cumulus@switch:~$ netq config restart cli
Restarting NetQ CLI... Success!
```

{{%notice tip%}}
If you have multiple premises and want to query data from a different premises than you originally configured, rerun the `netq config add cli server` command with the desired premises name. You can only view the data for one premises at a time with the CLI.
{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

### Configure NetQ CLI Using a Configuration File

You can configure the NetQ CLI in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

    ```
    root@rhel7:~# sudo nano /etc/netq/netq.yml
    ```

2. Locate the *netq-cli* section, or add it.

3. Set the parameters for the CLI as follows:

    | Parameter | On-premises | Cloud |
    | ----| ---- | ---- |
    | netq-user | User who can access the CLI | User who can access the CLI |
    | server | IP address of the NetQ server or NetQ Appliance | api.netq.cumulusnetworks.com |
    | port (default) | 32708 | 443 |
    | premises | NA | Name of premises you want to query |

    An on-premises configuration should be similar to this:

    ```
    netq-cli:
    netq-user: admin@company.com
    port: 32708
    server: 192.168.0.254
    ```

    A cloud configuration should be similar to this:

    ```
    netq-cli:
    netq-user: admin@company.com
    port: 443
    premises: datacenterwest
    server: api.netq.cumulusnetworks.com
    ```
