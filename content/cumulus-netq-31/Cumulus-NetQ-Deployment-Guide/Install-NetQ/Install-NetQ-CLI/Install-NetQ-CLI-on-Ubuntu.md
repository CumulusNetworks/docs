---
title: Install and Configure the NetQ CLI on Ubuntu Servers
author: Cumulus Networks
weight: 128
toc: 5
---
After installing your Cumulus NetQ software, you should install the  NetQ 3.1.0 Agents on each switch you want to monitor. NetQ Agents can be installed on servers running:

- Ubuntu 16.04
- Ubuntu 18.04 (NetQ 2.2.2 and later)

## Prepare for NetQ CLI Installation on an Ubuntu Server

For servers running Ubuntu OS, you need to:

- Verify the minimum service packages versions are installed
- Verify the server is running lldpd
- Install and configure network time server, if needed
- Obtain NetQ software packages

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy]({{<ref "/cumulus-linux-43/System-Configuration/Configuring-a-Global-Proxy" >}}) so <code>apt-get</code> can access the software package in the Cumulus Networks repository.
{{%/notice%}}

### Verify Service Package Versions

Before you install the NetQ Agent on an Ubuntu server, make sure the
following packages are installed and running these minimum versions:

- iproute 1:4.3.0-1ubuntu3.16.04.1 all
- iproute2 4.3.0-1ubuntu3 amd64
- lldpd 0.7.19-1 amd64
- ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64

### Verify the Server is Running lldpd

Make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not include `lldpd` by default, which is required for the installation.

To install this package, run the following commands:

```
root@ubuntu:~# sudo apt-get update
root@ubuntu:~# sudo apt-get install lldpd
root@ubuntu:~# sudo systemctl enable lldpd.service
root@ubuntu:~# sudo systemctl start lldpd.service
```

### Install and Configure Network Time Server

If NTP is not already installed and configured, follow these steps:

1.  Install [NTP]({{<ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time" >}}) on the server, if not already installed. Servers must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

    ```
    root@ubuntu:~# sudo apt-get install ntp
    ```

2.  Configure the network time server.

    {{< tabs "TabID0" >}}

{{< tab "Use NTP Configuration File" >}}

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

4. Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock is synchronized.

    ```
    root@ubuntu:~# ntpq -pn
    remote           refid            st t when poll reach   delay   offset  jitter
    ==============================================================================
    +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
    +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
    2a00:7600::41    .STEP.          16 u    - 1024    0    0.000    0.000   0.000
    \*129.250.35.250 249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

{{< /tab >}}
    
{{< tab "Use Chrony (Ubuntu 18.04 only)" >}}

1. Install chrony if needed.

    ```
    root@ubuntu:~# sudo apt install chrony
    ```

2. Start the chrony service.

    ```
    root@ubuntu:~# sudo /usr/local/sbin/chronyd
    ```

3. Verify it installed successfully.

    ```
    root@ubuntu:~# chronyc activity
    200 OK
    8 sources online
    0 sources offline
    0 sources doing burst (return to online)
    0 sources doing burst (return to offline)
    0 sources with unknown address
    ```

4. View the time servers chrony is using.

    ```
    root@ubuntu:~# chronyc sources
    210 Number of sources = 8

    MS Name/IP address         Stratum Poll Reach LastRx Last sample
    ===============================================================================
    ^+ golem.canonical.com           2   6   377    39  -1135us[-1135us] +/-   98ms
    ^* clock.xmission.com            2   6   377    41  -4641ns[ +144us] +/-   41ms
    ^+ ntp.ubuntu.net              2   7   377   106   -746us[ -573us] +/-   41ms
    ...
    ```

    Open the *chrony.conf* configuration file (by default at */etc/chrony/*) and edit if needed.

    Example with individual servers specified:

    ```
    server golem.canonical.com iburst
    server clock.xmission.com iburst
    server ntp.ubuntu.com iburst
    driftfile /var/lib/chrony/drift
    makestep 1.0 3
    rtcsync
    ```

    Example when using a pool of servers:

    ```
    pool pool.ntp.org iburst
    driftfile /var/lib/chrony/drift
    makestep 1.0 3
    rtcsync
    ```

5. View the server chrony is currently tracking.

    ```
    root@ubuntu:~# chronyc tracking
    Reference ID    : 5BBD59C7 (golem.canonical.com)
    Stratum         : 3
    Ref time (UTC)  : Mon Feb 10 14:35:18 2020
    System time     : 0.0000046340 seconds slow of NTP time
    Last offset     : -0.000123459 seconds
    RMS offset      : 0.007654410 seconds
    Frequency       : 8.342 ppm slow
    Residual freq   : -0.000 ppm
    Skew            : 26.846 ppm
    Root delay      : 0.031207654 seconds
    Root dispersion : 0.001234590 seconds
    Update interval : 115.2 seconds
    Leap status     : Normal
    ```

{{< /tab >}}

{{< /tabs >}}

### Obtain NetQ CLI Software Package

To install the NetQ Agent you need to install `netq-apps` on each server. This is available from the Cumulus Networks repository.

To obtain the NetQ CLI package:

1. Reference and update the local `apt` repository.

    ```
    root@ubuntu:~# sudo wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
    ```

2. Add the Ubuntu repository:

    {{< tabs "TabID2" >}}

{{< tab "Ubuntu 16.04" >}}

Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add the following line:

```
root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
...
deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
...
```

{{< /tab >}}

{{< tab "Ubuntu 18.04" >}}

Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add the following line:

```
root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
...
deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
...
```

{{< /tab >}}

{{< /tabs >}}

    {{<notice note>}}
The use of <code>netq-latest</code> in these examples means that a <code>get</code> to the repository always retrieves the latest version of NetQ, even in the case where a major version update has been made. If you want to keep the repository on a specific version - such as <code>netq-3.0</code> - use that instead.
    {{</notice>}}

## Install NetQ CLI on an Ubuntu Server

A simple process installs the NetQ CLI on an Ubuntu server.

1.  Install the CLI software on the server.

    ```
    root@ubuntu:~# sudo apt-get update
    root@ubuntu:~# sudo apt-get install netq-apps
    ```

4. Verify you have the correct version of the CLI.

    ```
    root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-apps
    ```

    {{<netq-install/cli-version version="3.1.0" opsys="ub">}}

5. Continue with NetQ CLI configuration in the next section.

## Configure the NetQ CLI on an Ubuntu Server

Two methods are available for configuring the NetQ CLI on a switch:

- Run NetQ CLI commands on the switch; refer to the next section
- Edit the configuration file on the switch; refer to {{<link url="#configure-netq-cli-using-configuration-file" text="Configure CLI Using File">}}

### Configure NetQ CLI Using the CLI

The steps to configure the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment. Follow the instruction for your deployment type.

{{< tabs "TabID4" >}}
{{< tab "On-premises Deployments" >}}

Use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [vrf <text-vrf-name>] [port <text-gateway-port>]
```

Restart the CLI afterward to activate the configuration.

This example uses an IP address of 192.168.1.0 and the default port and VRF.

```
root@ubuntu:~# sudo netq config add cli server 192.168.1.0
root@ubuntu:~# sudo netq config restart cli
```

{{<notice tip>}}
If you have a server cluster deployed, use the IP address of the master server.
{{</notice>}}

{{< /tab >}}

{{< tab "Cloud Deployments" >}}

To access and configure the CLI on your NetQ Platform or NetQ Cloud Appliance, you must have your username and password to access the NetQ UI to generate AuthKeys. These keys provide authorized access (access key) and user authentication (secret key). Your credentials and NetQ Cloud addresses were provided by Cumulus Networks via an email titled *Welcome to Cumulus NetQ!*

To generate AuthKeys:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. From the Main Menu, select *Management* in the **Admin** column.

    {{< figure src="/images/netq/main-menu-admin-mgmt-selected-300.png" width="400">}}

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
    root@ubuntu:~# sudo netq config add cli server api.netq.cumulusnetworks.com access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    This example uses an optional keys file. **Be sure to replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

    ```
    root@ubuntu:~# sudo netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /home/netq/nq-cld-creds.yml premises datacenterwest
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    {{<notice tip>}}
Rerun this command if you have multiple premises and want to query a different premises.
    {{</notice>}}

{{< /tab >}}

{{< /tabs >}}

### Configure NetQ CLI Using Configuration File

You can configure the NetQ CLI in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

    ```
    root@ubuntu:~# sudo nano /etc/netq/netq.yml
    ```

2. Locate the *netq-cli* section, or add it.

3. Set the parameters for the CLI.

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
