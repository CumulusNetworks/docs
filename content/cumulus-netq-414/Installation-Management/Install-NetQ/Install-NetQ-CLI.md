---
title: Install NetQ CLI
author: NVIDIA
weight: 210
toc: 4
--- 

Installing the NetQ CLI on your NetQ VMs, switches, or hosts gives you access to new features and bug fixes, and allows you to manage your network from multiple points in the network.

After installing the NetQ software and agent on each switch you want to monitor, you can also install the NetQ CLI on switches running:

- Cumulus Linux 5.12.1, 5.11.1, or 5.9.2
- Ubuntu 22.04

{{<notice note>}}
If your network uses a proxy server for external connections, you should first {{<kb_link latest="cl" url="System-Configuration/Configuring-a-Global-Proxy.md" text="configure a global proxy">}} so <code>apt-get</code> can access the software package in the NetQ repository.
{{</notice>}}

## Prepare for NetQ CLI Installation on an Ubuntu Server

For servers running the Ubuntu OS, you need to:

- Verify you installed the minimum service packages versions
- Verify the server is running `lldpd`
- Install and configure NTP or PTP, if needed
- Obtain NetQ software packages

These steps are not required for Cumulus Linux.

### Verify Service Package Versions

{{<tabs "Verify Package Versions">}}

Before you install the NetQ CLI on a server, make sure you install and run at least the minimum versions of the following packages:

{{<tab "Ubuntu">}}

<!-- vale off -->
- iproute 1:4.3.0-1ubuntu3.16.04.1 all
- iproute2 4.3.0-1ubuntu3 amd64
- lldpd 0.7.19-1 amd64
- ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64
<!-- vale on -->

{{</tab>}}

{{</tabs>}}

### Verify Ubuntu is Running lldpd

For Ubuntu, make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not include `lldpd` by default, even though the installation requires it.

{{<tabs "Configure NetQ CLI">}}

{{<tab "Ubuntu">}}

To install `lldpd`, run the following commands:

```
root@ubuntu:~# sudo apt-get update
root@ubuntu:~# sudo apt-get install lldpd
root@ubuntu:~# sudo systemctl enable lldpd.service
root@ubuntu:~# sudo systemctl start lldpd.service
```

{{</tab>}}

{{</tabs>}}

### Install and Configure NTP

If NTP is not already installed and configured, follow these steps:

{{<tabs "Install NTP">}}

{{<tab "Ubuntu">}}

1.  Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server, if not already installed. Servers must be in time synchronization with NetQ to enable useful statistical analysis.

    ```
    root@ubuntu:~# sudo apt-get install ntp
    ```

2.  Configure the network time server.

    {{<tabs "TabID0" >}}

{{<tab "Use NTP Configuration File" >}}

1. Open the `/etc/ntp.conf` file in your text editor of choice.

2. Under the *Server* section, specify the NTP server IP address or hostname.

3. Enable and start the NTP service.

    ```
    root@ubuntu:~# sudo systemctl enable ntp
    root@ubuntu:~# sudo systemctl start ntp
    ```

   {{<notice tip>}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (<code>ntp@&lt;vrf-name&gt;</code> versus just <code>ntp</code>) in the above commands.
   {{</notice>}}

4. Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock synchronized with NTP.

    ```
    root@ubuntu:~# ntpq -pn
    remote           refid            st t when poll reach   delay   offset  jitter
    ==============================================================================
    +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
    +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
    2a00:7600::41    .STEP.          16 u    - 1024    0    0.000    0.000   0.000
    \*129.250.35.250 249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

{{</tab>}}
    
{{</tabs>}}

{{</tab>}}

{{</tabs>}}

### Get the NetQ CLI Software Package for Ubuntu

To install the NetQ CLI on an Ubuntu server, you need to install `netq-apps` on each Ubuntu server. This is available from the NetQ repository.

To get the NetQ CLI package:

1. Reference and update the local `apt` repository.

    ```
    root@ubuntu:~# sudo wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
    ```

2. Add the Ubuntu repository. Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-jammy.list` and add the following line:

```
root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-jammy.list
...
deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb jammy netq-latest
...
```

{{<notice note>}}
The use of <code>netq-latest</code> in these examples means that a <code>get</code> to the repository always retrieves the latest version of NetQ, even for a major version update. If you want to keep the repository on a specific version &mdash; such as <code>netq-4.4</code> &mdash; use that instead.
{{</notice>}}

## Install NetQ CLI

Follow these steps to install the NetQ CLI on a switch or host.

{{<tabs "Install NetQ CLI">}}

{{<tab "Cumulus Linux 5.9.0 or later">}}

Cumulus Linux 4.4 and later includes the `netq-apps` package by default. To upgrade the NetQ CLI to the latest version:

1. Add the repository by uncommenting or adding the following line in `/etc/apt/sources.list`:

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-d12 netq-latest
...
```

{{<notice tip>}}
You can specify a NetQ CLI version in the repository configuration. The following example shows the repository configuration to retrieve NetQ CLI v4.14: <pre>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-d12 netq-4.14</pre>
{{</notice>}}


2. Update the local `apt` repository and install the software on the switch.

    ```
    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install netq-apps
    ```

3. Verify you have the correct version of the CLI.

    ```
    cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-apps
    ```
You should see version 4.14.0 and updated 51 in the results: netq-apps_<strong>4.14.0</strong>-cld12u<strong>51</strong>~1744815975.8dbbbd20c_amd64.deb

4. Continue with NetQ CLI configuration in the next section.

{{</tab>}}

end here

{{<tab "Cumulus Linux 4.4.0 to 5.8.0">}}

Cumulus Linux 4.4 and later includes the `netq-apps` package by default. To upgrade the NetQ CLI to the latest version:

1. Add the repository by uncommenting or adding the following line in `/etc/apt/sources.list`:

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest
...
```

{{<notice tip>}}
You can specify a NetQ CLI version in the repository configuration. The following example shows the repository configuration to retrieve NetQ CLI v4.14: <pre>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-4.14</pre>
{{</notice>}}


2. Update the local `apt` repository and install the software on the switch.

    ```
    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install netq-apps
    ```

3. Verify you have the correct version of the CLI.

    ```
    cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-apps
    ```
You should see version 4.14.0 and update 51 in the results: 

- Cumulus Linux 5.8.0 or earlier, ARM platforms: netq-apps_<strong>4.14.0</strong>-cl4u<strong>51</strong>~11744815873.8dbbbd20c_armel.deb
- Cumulus Linux 5.8.0 or earlier, amd64 platforms: netq-apps_<strong>4.14.0</strong>-cl4u<strong>51</strong>~1744816035.8dbbbd20c_amd64.deb

4. Continue with NetQ CLI configuration in the next section.

{{</tab>}}

{{<tab "Ubuntu 22.04">}}

1.  Install the CLI software on the server.

    ```
    root@ubuntu:~# sudo apt-get update
    root@ubuntu:~# sudo apt-get install netq-apps
    ```

2. Verify you have the correct version of the CLI.

    ```
    root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-apps
    ```
<!-- vale off -->
{{<netq-install/cli-version version="4.14" opsys="ub">}}
<!-- vale on -->
3. Continue with NetQ CLI configuration in the next section.

{{</tab>}}

{{</tabs>}}

## Configure the NetQ CLI

By default, you do not configure the NetQ CLI during the NetQ installation. The configuration resides in the `/etc/netq/netq.yml` file. Until the CLI is configured on a device, you can only run `netq config` and `netq help` commands, and you must use `sudo` to run them.

At minimum, you need to configure the NetQ CLI and NetQ Agent to communicate with the telemetry server. To do so, configure the NetQ Agent and the NetQ CLI so that they are running in the VRF where the routing tables have connectivity to the telemetry server (typically the management VRF).

{{<tabs "Configure CLI with CLI">}}

{{<tab "On-premises Deployments">}}

<!-- vale off -->
To access and configure the CLI for your on-premises NetQ deployment, you must generate AuthKeys. You'll need your username and password to generate them. These keys provide authorized access (access key) and user authentication (secret key). 
<!-- vale on -->

To generate AuthKeys:

1. Enter your on-premises NetQ hostname or IP address into your browser to open the NetQ UI login page.

2. Enter your username and password.

3. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu**, then select **Management**.

    {{<figure src="/images/netq/side-nav-admin-411.png" alt="" width="300">}}

4. On the User Accounts card, select **Manage**.

5. Select your user and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18"/> **Generate keys** above the table.

6. Copy these keys to a safe place. Select `Copy` to obtain the CLI configuration command to use on your devices. 

    {{<notice info>}}
The secret key is only shown once. If you do not copy these, you will need to regenerate them and reconfigure CLI access.
    {{</notice>}}

{{<notice tip>}}
You can also save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can:

- Store the file wherever you like, for example in <em>/home/cumulus/</em> or <em>/etc/netq</em>
- Name the file whatever you like, for example <em>credentials.yml</em>, <em>creds.yml</em>, or <em>keys.yml</em>

The file **must** have the following format:
```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```
{{</notice>}}

7. Enter the AuthKeys to configure the CLI. Alternately, use the following command:

    ```
    netq config add cli server <text-gateway-dest> [access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> | cli-keys-file <text-key-file> premises <text-premises-name>] [vrf <text-vrf-name>] [port <text-gateway-port>]
    ```

8. Restart the CLI to activate the configuration.

    The following example uses the individual access key, a premises of *datacenterwest*, and the default Cloud address, port and VRF.  **Replace the key values with your generated keys if you are using this example on your server.**

    ```
    sudo netq config add cli server netqhostname.labtest.net access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
    Updated cli server netqhostname.labtest.net vrf default port 443. Please restart netqd (netq config restart cli)

    sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    This example uses an optional keys file. **Replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

    ```
    sudo netq config add cli server netqhostname.labtest.net cli-keys-file /home/netq/nq-cld-creds.yml premises datacenterwest
    Updated cli server netqhostname.labtest.net vrf default port 443. Please restart netqd (netq config restart cli)

    sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    {{%notice tip%}}
If you have multiple premises and want to query data from a different premises than you originally configured, rerun the `netq config add cli server` command with the desired premises name. You can only view the data for one premises at a time with the CLI.
{{%/notice%}}

{{</tab>}}

{{<tab "Cloud Deployments">}}

<!-- vale off -->
To access and configure the CLI for your NetQ cloud deployment, you must generate AuthKeys. You'll need your username and password to generate them. These keys provide authorized access (access key) and user authentication (secret key). Your credentials and NetQ cloud addresses were obtained during your {{<link title="Access the NetQ UI#log-in-to-netq" text="initial login to the NetQ cloud">}} and premises activation.
<!-- vale on -->

To generate AuthKeys:

1. Enter **netq.nvidia.com** into your browser to open the NetQ UI login page.

2. Enter your username and password.

3. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu**, then select **Management**.

    {{<figure src="/images/netq/side-nav-admin-411.png" alt="" width="300">}}

4. On the User Accounts card, select **Manage**.

5. Select your user and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18"/> **Generate keys** above the table.

6. Copy these keys to a safe place. Select `Copy` to obtain the CLI configuration command to use on your devices. 

    {{<notice info>}}
The secret key is only shown once. If you do not copy these, you will need to regenerate them and reconfigure CLI access.
    {{</notice>}}

{{<notice tip>}}
You can also save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can:

- store the file wherever you like, for example in <em>/home/cumulus/</em> or <em>/etc/netq</em>
- name the file whatever you like, for example <em>credentials.yml</em>, <em>creds.yml</em>, or <em>keys.yml</em>

The file **must** have the following format:

```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```

{{</notice>}}

7. Insert the AuthKeys onto your device to configure the CLI. Alternately, use the following command.

    ```
    netq config add cli server <text-gateway-dest> [access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> | cli-keys-file <text-key-file> premises <text-premises-name>] [vrf <text-vrf-name>] [port <text-gateway-port>]
    ```

8. Restart the CLI to activate the configuration.

    The following example uses the individual access key, a premises of *datacenterwest*, and the default Cloud address, port and VRF.  **Replace the key values with your generated keys if you are using this example on your server.**

    ```
    sudo netq config add cli server api.netq.cumulusnetworks.com access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    The following example uses an optional keys file. **Replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

    ```
    sudo netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /home/netq/nq-cld-creds.yml premises datacenterwest
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    {{%notice tip%}}
If you have multiple premises and want to query data from a different premises than you originally configured, rerun the `netq config add cli server` command with the desired premises name. You can only view the data for one premises at a time with the CLI.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}