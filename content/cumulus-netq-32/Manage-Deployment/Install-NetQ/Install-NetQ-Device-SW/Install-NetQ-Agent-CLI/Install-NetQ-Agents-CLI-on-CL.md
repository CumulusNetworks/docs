---
title: Install and Configure the NetQ Agent and CLI on Cumulus Linux Switches
author: Cumulus Networks
weight: 370
toc: 5
---
After installing your Cumulus NetQ software, you can install the NetQ 3.2.1 Agents and CLI on each switch you want to monitor. These can be installed on switches running:

- Cumulus Linux version 3.3.2-3.7.x
- Cumulus Linux version 4.0.0 and later

## Prepare for NetQ Agent and CLI  Installation on a Cumulus Linux Switch

For servers running Cumulus Linux, you need to:

- Install and configure NTP, if needed
- Obtain NetQ software packages

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy]({{<ref "/cumulus-linux-43/System-Configuration/Configuring-a-Global-Proxy" >}}) so <code>apt-get</code> can access the software package in the Cumulus Networks repository.
{{%/notice%}}

### Verify NTP is Installed and Configured

Verify that [NTP]({{<ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time" >}}) is running on the switch. The switch must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

```
cumulus@switch:~$ sudo systemctl status ntp
[sudo] password for cumulus:
● ntp.service - LSB: Start NTP daemon
        Loaded: loaded (/etc/init.d/ntp; bad; vendor preset: enabled)
        Active: active (running) since Fri 2018-06-01 13:49:11 EDT; 2 weeks 6 days ago
          Docs: man:systemd-sysv-generator(8)
        CGroup: /system.slice/ntp.service
                └─2873 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 109:114
```

If NTP is not installed, install and configure it before continuing.  

If NTP is not running:

- Verify the IP address or hostname of the NTP server in the `/etc/ntp.conf` file, and then
- Reenable and start the NTP service using the `systemctl [enable|start] ntp` commands

{{<notice tip>}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (<code>ntp@&lt;vrf-name&gt;</code> versus just <code>ntp</code>) in the above commands.
{{</notice>}}

### Obtain NetQ Agent and CLI Software Packages

To install the NetQ Agent you need to install `netq-agent` on each switch or host. To install the NetQ CLI you need to install `netq-apps` on each switch. These are available from the Cumulus Networks repository.

To obtain the NetQ packages:

Edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.

*Note that NetQ has a separate repository from Cumulus Linux.*

{{< tabs "TabID59" >}}

{{< tab "Cumulus Linux 3.x" >}}

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-3.2
...
```

{{<notice tip>}}
The repository <code>deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-latest</code> can be used if you want to always retrieve the latest posted version of NetQ.
{{</notice>}}

{{< /tab >}}

{{< tab "Cumulus Linux 4.x" >}}

Add the repository:

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-3.2
...
```

{{<notice tip>}}
The repository <code>deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest</code> can be used if you want to always retrieve the latest posted version of NetQ.
{{</notice>}}

Add the `apps3.cumulusnetworks.com` authentication key to Cumulus Linux:

```
cumulus@switch:~$ wget -qO - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -
```

{{< /tab >}}

{{< /tabs >}}

## Install the NetQ Agent on Cumulus Linux Switch

After completing the preparation steps, you can successfully install the agent onto your switch.

To install the NetQ Agent and CLI:

1. Update the local `apt` repository, then install the NetQ software on the switch.

    ```
    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install netq-agent netq-apps
    ```

2. Verify you have the correct version of the Agent and CLI.

    ```
    cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    {{<netq-install/agent-version version="3.2.1" opsys="cl">}}

    ```
    cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    {{<netq-install/cli-version version="3.2.1" opsys="cl">}}

3. Restart `rsyslog` so log files are sent to the correct destination.

    ```
    cumulus@switch:~$ sudo systemctl restart rsyslog.service
    ```

4. Continue with NetQ Agent and CLI configuration in the next section.

## Configure the NetQ Agent and CLI on a Cumulus Linux Switch

After the NetQ Agent and CLI have been installed on the servers you want to monitor, the NetQ Agents must be configured to obtain useful and relevant data.

{{%notice note%}}
The NetQ Agent is aware of and communicates through the designated VRF. If you do not specify one, the default VRF (named *default*) is used. If you later change the VRF configured for the NetQ Agent (using a lifecycle management configuration profile, for example), you might cause the NetQ Agent to lose communication.
{{%/notice%}}

Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the switch, or
- Use the NetQ CLI

### Configure NetQ Agent and CLI Using a Configuration File

You can configure the NetQ Agent and CLI in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

    ```
    cumulus@switch:~$ sudo nano /etc/netq/netq.yml
    ```

2. Locate the *netq-agent* section, or add it.

3. Set the parameters for the agent as follows:
    - port: 31980 (default configuration)
    - server: IP address of the NetQ Appliance or VM where the agent should send its collected data
    - vrf: default (default) or one that you specify

    Your configuration should be similar to this:

    ```
    netq-agent:
    port: 31980
    server: 127.0.0.1
    vrf: default
    ```

4. Locate the *netq-cli* section, or add it.

5. Set the parameters for the CLI based on your deployment type.

    {{< tabs "TabID1" >}}

{{< tab "On-premises Deployments" >}}

Specify the following parameters:

- netq-user: User who can access the CLI
- server: IP address of the NetQ server or NetQ Appliance
- port (default): 32708
<p> </p>
Your YAML configuration file should be similar to this:

```
netq-cli:
netq-user: admin@company.com
port: 32708
server: 192.168.0.254
```

{{< /tab >}}

{{< tab "Cloud Deployments" >}}

Specify the following parameters:

- netq-user: User who can access the CLI
- server: api.netq.cumulusnetworks.com
- port (default): 443
- premises: Name of premises you want to query
<p> </p>
Your YAML configuration file should be similar to this:

```
netq-cli:
netq-user: admin@company.com
port: 443
premises: datacenterwest
server: api.netq.cumulusnetworks.com
```

{{< /tab >}}

{{< /tabs >}}

### Configure NetQ Agent and CLI Using the NetQ CLI

If the CLI is configured, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Appliance or VM.

{{<notice info>}}
If you intend to use VRF, refer to {{<link url="#configure-the-agent-to-use-a-vrf" text="Configure the Agent to Use VRF">}}. If you intend to specify a port for communication, refer to {{<link url="#configure-the-agent-to-communicate-over-a-specific-port" text="Configure the Agent to Communicate over a Specific Port">}}.
{{</notice>}}

Use the following command to configure the NetQ Agent:

```
netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
```

This example uses an IP address of *192.168.1.254* and the default port and VRF for the NetQ Appliance or VM.

```
cumulus@switch:~$ sudo netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
cumulus@switch:~$ sudo netq config restart agent
```

The steps to configure the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment. Follow the instructions for your deployment type.

{{< tabs "TabID91" >}}

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

{{<notice tip>}}
If you have a server cluster deployed, use the IP address of the master server.
{{</notice>}}

{{< /tab >}}

{{< tab "Cloud Deployments" >}}

To access and configure the CLI on your NetQ Cloud Appliance or VM, you must have your username and password to access the NetQ UI to generate AuthKeys. These keys provide authorized access (access key) and user authentication (secret key). Your credentials and NetQ Cloud addresses were provided by Cumulus Networks via an email titled *Welcome to Cumulus NetQ!*

To generate AuthKeys:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> (Main Menu), select *Management* in the **Admin** column.

    {{<figure src="/images/netq/main-menu-admin-mgmt-selected-320.png" width="400">}}

4. Click **Manage** on the User Accounts card.

5. Select your user and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18"/> above the table.

6. Copy these keys to a safe place.

    {{<notice info>}}
The secret key is only shown once. If you do not copy these, you will need to regenerate them and reconfigure CLI access.
    {{</notice>}}

{{<notice tip>}}
You can also save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can:

- store the file wherever you like, for example in <em>/home/cumulus/</em> or <em>/etc/netq</em>
- name the file whatever you like, for example <em>credentials.yml</em>, <em>creds.yml</em>, or <em>keys.yml</em>

BUT, the file must have the following format:

```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```

{{</notice>}}

7. Now that you have your AuthKeys, use the following command to configure the CLI:

    ```
    netq config add cli server <text-gateway-dest> [access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> | cli-keys-file <text-key-file> premises <text-premises-name>] [vrf <text-vrf-name>] [port <text-gateway-port>]
    ```

8. Restart the CLI afterward to activate the configuration.

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

    {{<notice tip>}}
If you have multiple premises and want to query data from a different premises than you originally configured, rerun the <code>netq config add cli server</code> command with the desired premises name. You can only view the data for one premises at a time with the CLI.
    {{</notice>}}

{{< /tab >}}

{{< /tabs >}}

## Configure Advanced NetQ Agent Settings on a Cumulus Linux Switch

A couple of additional options are available for configuring the NetQ Agent. If you are using VRF, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ Agents to communicate with the NetQ Appliance or VM only via a [VRF]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF" >}}), including a [management VRF]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Management-VRF" >}}). To do so, you need to specify the VRF name when configuring the NetQ Agent. For example, if the management VRF is configured and you want the agent to communicate with the NetQ Appliance or VM over it, configure the agent like this:

```
cumulus@leaf01:~$ sudo netq config add agent server 192.168.1.254 vrf mgmt
cumulus@leaf01:~$ sudo netq config restart agent
```

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ Appliance or VM and NetQ Agents. If you want the NetQ Agent to communicate with the NetQ Appliance or VM via a different port, you need to specify the port number when configuring the NetQ Agent, like this:

```
cumulus@leaf01:~$ sudo netq config add agent server 192.168.1.254 port 7379
cumulus@leaf01:~$ sudo netq config restart agent
```
