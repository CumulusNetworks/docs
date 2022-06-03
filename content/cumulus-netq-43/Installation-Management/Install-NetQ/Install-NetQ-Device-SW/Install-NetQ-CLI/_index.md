---
title: Install NetQ CLI
author: NVIDIA
weight: 320
toc: 4
--- 

When installing NetQ {{<version>}}, you are not required to install the NetQ CLI on your NetQ Appliances or VMs, or monitored switches and hosts, but it provides new features, important bug fixes, and the ability to manage your network from multiple points in the network.

After installing your NetQ software and the NetQ {{<version>}} Agent on each switch you want to monitor, you can also install the NetQ CLI on switches running:

- Cumulus Linux 3.7.12 and later
- SONiC 202012 and later
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04

{{<notice note>}}
If your network uses a proxy server for external connections, you should first {{<kb_link latest="cl" url="System-Configuration/Configuring-a-Global-Proxy.md" text="configure a global proxy">}} so <code>apt-get</code> can access the software package in the NetQ repository.
{{</notice>}}

## Prepare for NetQ CLI Installation on a RHEL, CentOS or Ubuntu Server

For servers running RHEL 7, CentOS or Ubuntu OS, you need to:

- Verify you installed the minimum service packages versions
- Verify the server is running `lldpd`
- Install and configure NTP, if needed
- Obtain NetQ software packages

You do not take any of these steps on Cumulus Linux or SONiC.

### Verify Service Package Versions

{{<tabs "Verify Package Versions">}}

Before you install the NetQ Agent on a server, make sure you install and run at least the minimum versions of the following packages:

{{<tab "RHEL7 or CentOS">}}
<!-- vale off -->
- iproute-3.10.0-54.el7\_2.1.x86\_64
- lldpd-0.9.7-5.el7.x86\_64
- ntp-4.2.6p5-25.el7.centos.2.x86\_64
- ntpdate-4.2.6p5-25.el7.centos.2.x86\_64
<!-- vale on -->
{{</tab>}}

{{<tab "Ubuntu">}}

<!-- vale off -->
- iproute 1:4.3.0-1ubuntu3.16.04.1 all
- iproute2 4.3.0-1ubuntu3 amd64
- lldpd 0.7.19-1 amd64
- ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64
<!-- vale on -->

{{</tab>}}

{{</tabs>}}

### Verify What CentOS and Ubuntu Are Running

For CentOS and Ubuntu, make sure you are running lldp**d**, not lldp**ad**. CentOS and Ubuntu do not include `lldpd` by default, even though the installation requires it. In addition, CentOS does not include `wget`, even though the installation requires it.

{{<tabs "Configure NetQ Agent">}}

{{<tab "CentOS">}}

To install this package, run the following commands:

```
root@centos:~# sudo yum -y install epel-release
root@centos:~# sudo yum -y install lldpd
root@centos:~# sudo systemctl enable lldpd.service
root@centos:~# sudo systemctl start lldpd.service
root@centos:~# sudo yum install wget
```

{{</tab>}}

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

{{<tab "RHEL7 or CentOS">}}

1. Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server. Servers must be in time synchronization with the NetQ Appliance or VM to enable useful statistical analysis.

    ```
    root@rhel7:~# sudo yum install ntp
    ```

2. Configure the NTP server.

    1.  Open the `/etc/ntp.conf` file in your text editor of choice.

    2.  Under the *Server* section, specify the NTP server IP address or hostname.

3. Enable and start the NTP service.

    ```
    root@rhel7:~# sudo systemctl enable ntp
    root@rhel7:~# sudo systemctl start ntp
    ```

   {{<notice tip>}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (<code>ntp@&lt;vrf-name&gt;</code> versus just <code>ntp</code>) in the above commands.
   {{</notice>}}

4. Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock synchronized with NTP.

    ```
    root@rhel7:~# ntpq -pn
    remote           refid            st t when poll reach   delay   offset  jitter
    ==============================================================================
    +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
    +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
    2a00:7600::41    .STEP.          16 u    - 1024    0    0.000    0.000   0.000
    \*129.250.35.250 249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243
    ```

{{</tab>}}

{{<tab "Ubuntu">}}

1.  Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server, if not already installed. Servers must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

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
    
{{<tab "Use Chrony (Ubuntu 18.04 only)" >}}

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
    \=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=
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

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{</tabs>}}

### Get the NetQ CLI Software Package for Ubuntu

To install the NetQ Agent on an Ubuntu server, you need to install `netq-apps` on each Ubuntu server. This is available from the NetQ repository.

To get the NetQ CLI package:

1. Reference and update the local `apt` repository.

    ```
    root@ubuntu:~# sudo wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
    ```

2. Add the Ubuntu repository:

    {{<tabs "TabID2" >}}

{{<tab "Ubuntu 18.04" >}}

Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add the following line:

```
root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
...
deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
...
```

{{</tab>}}

{{</tabs>}}

    {{<notice note>}}
The use of <code>netq-latest</code> in these examples means that a <code>get</code> to the repository always retrieves the latest version of NetQ, even for a major version update. If you want to keep the repository on a specific version &mdash; such as <code>netq-4.2</code> &mdash; use that instead.
    {{</notice>}}

## Install NetQ CLI

A simple process installs the NetQ CLI on a switch or host.

{{<tabs "Install NetQ CLI">}}

{{<tab "Cumulus Linux">}}

To install the NetQ CLI you need to install `netq-apps` on each switch. This is available from the NVIDIA networking repository.

{{<notice note>}}
If your network uses a proxy server for external connections, you should first {{<kb_link latest="cl" url="System-Configuration/Configuring-a-Global-Proxy.md" text="configure a global proxy">}} so <code>apt-get</code> can access the software package in the NVIDIA networking repository.
{{</notice>}}

To obtain the NetQ Agent package:

Edit the `/etc/apt/sources.list` file to add the repository for NetQ.

*Note that NetQ has a separate repository from Cumulus Linux.*

{{<tabs "TabID327" >}}

{{<tab "Cumulus Linux 3.7" >}}

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-4.2
...
```

{{<notice tip>}}
You can use the <code>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest</code> repository if you want to always retrieve the latest posted version of NetQ.
{{</notice>}}

{{</tab>}}

{{<tab "Cumulus Linux 4.0 and later" >}}

Cumulus Linux 4.4 and later includes the `netq-apps` package by default.

To add the repository, uncomment or add the following line in `/etc/apt/sources.list`:

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-4.2
...
```

{{<notice tip>}}
You can use the <code>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest</code> repository if you want to always retrieve the latest posted version of NetQ.
{{</notice>}}

{{</tab>}}

{{</tabs>}}

2. Update the local `apt` repository and install the software on the switch.

    ```
    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install netq-apps
    ```

3. Verify you have the correct version of the CLI.

    ```
    cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```
<!-- vale off -->
{{<netq-install/cli-version version="4.2" opsys="cl">}}
<!-- vale on -->
4. Continue with NetQ CLI configuration in the next section.

{{</tab>}}

{{<tab "SONiC">}}

To install the NetQ CLI you need to install `netq-apps` on each switch. This is available from the NVIDIA networking repository.

{{<notice note>}}
If your network uses a proxy server for external connections, you should first {{<kb_link latest="cl" url="System-Configuration/Configuring-a-Global-Proxy.md" text="configure a global proxy">}} so <code>apt-get</code> can access the software package in the NVIDIA networking repository.
{{</notice>}}

To obtain the NetQ Agent package:

1. Edit the `/etc/apt/sources.list` file to add the repository for NetQ.

       admin@switch:~$ sudo nano /etc/apt/sources.list
       ...
       deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb buster netq-4.2
       ...

2. Update the local `apt` repository and install the software on the switch.

       admin@switch:~$ sudo apt-get update
       admin@switch:~$ sudo apt-get install netq-apps

3. Verify you have the correct version of the CLI.

    ```
    admin@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    You should see version 4.2.0 and update 38 in the results. For example:

    - netq-apps_<strong>4.2.0</strong>-deb10u<strong>38</strong>~1652819362.25f4ac06_amd64.deb	

4. Continue with NetQ CLI configuration in the next section.

{{</tab>}}

{{<tab "RHEL7 or CentOS">}}

1. Reference and update the local `yum` repository and key.

    ```
    root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
    root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo
    ```

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1` flag for the two NetQ repositories.

    ```
    root@rhel7:~# vi /etc/yum.repos.d/cumulus-host-el.repo
    ...
    [cumulus-arch-netq-4.2]
    name=Cumulus netq packages
    baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-4.2/$basearch
    gpgcheck=1
    enabled=1
    [cumulus-noarch-netq-4.2]
    name=Cumulus netq architecture-independent packages
    baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-4.2/noarch
    gpgcheck=1
    enabled=1
    ...
    ```

3.  Install the Bash completion and CLI software on the server.

    ```
    root@rhel7:~# sudo yum -y install bash-completion
    root@rhel7:~# sudo yum install netq-apps
    ```

4. Verify you have the correct version of the CLI.

    ```
    root@rhel7:~# rpm -q -netq-apps
    ```
<!-- vale off -->
    {{<netq-install/cli-version version="4.1.0" opsys="rh">}}
<!-- vale on -->
5. Continue with the next section.

{{</tab>}}

{{<tab "Ubuntu">}}

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
{{<netq-install/cli-version version="4.2" opsys="ub">}}
<!-- vale on -->
3. Continue with NetQ CLI configuration in the next section.

{{</tab>}}

{{</tabs>}}

## Configure the NetQ CLI

Two methods are available for configuring the NetQ CLI:

- Run NetQ CLI commands on the switch
- Edit the configuration file on the switch

By default, you do not configure the NetQ CLI during the NetQ installation. The configuration resides in the `/etc/netq/netq.yml` file.

While the CLI is not configured, you can run only `netq config` commands and `netq help` commands, and you must use `sudo` to run them.

At minimum, you need to configure the NetQ CLI and NetQ Agent to communicate with the telemetry server. To do so, configure the NetQ Agent and the NetQ CLI so that they are running in the VRF where the routing tables have connectivity to the telemetry server. Typically this is the management VRF.

To configure the NetQ CLI, run the following command, then restart the NetQ CLI. This example assumes the telemetry server is reachable via the IP address 10.0.1.1 over port 32000 and the management VRF (*mgmt*).

    sudo netq config add cli server 10.0.1.1 vrf mgmt port 32000
    sudo netq config restart cli

Restarting the CLI stops the current running instance of `netqd` and starts `netqd` in the specified VRF.

To configure the NetQ Agent, read {{<link url="Install-NetQ-Agents/#configure-advanced-netq-agent-settings" text="Configure Advanced NetQ Agent Settings">}}.

### Configure NetQ CLI Using the CLI

The steps to configure the CLI are different depending on whether you installed the NetQ software for an on-premises or cloud deployment. Follow the instructions for your deployment type.

{{<tabs "Configure CLI with CLI">}}

{{<tab "On-premises Deployments">}}

<!-- vale off -->
To access and configure the CLI for your on-premise NetQ deployment, you must have your username and password to access the NetQ UI to generate AuthKeys. These keys provide authorized access (access key) and user authentication (secret key). 
<!-- vale on -->

To generate AuthKeys:

1. In your Internet browser, enter your on-premise NetQ appliance hostnme or IP address into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> (Main Menu), select *Management* under **Admin**.

    {{<figure src="/images/netq/main-menu-admin-mgmt-selected-410.png" width="300">}}

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
    sudo netq config add cli server netqhostname.labtest.net access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
    Updated cli server netqhostname.labtest.net vrf default port 443. Please restart netqd (netq config restart cli)

    sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    This example uses an optional keys file. **Be sure to replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

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
To access and configure the CLI on your NetQ Cloud Appliance or VM, you must have your username and password to access the NetQ UI to generate AuthKeys. These keys provide authorized access (access key) and user authentication (secret key). Your credentials and NetQ Cloud addresses were obtained during {{<link title="Access the NetQ UI#log-in-to-netq" text="first login to the NetQ Cloud">}} and premise activation.
<!-- vale on -->

To generate AuthKeys:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> (Main Menu), select *Management* under **Admin**.

    {{<figure src="/images/netq/main-menu-admin-mgmt-selected-410.png" width="300">}}

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
    sudo netq config add cli server api.netq.cumulusnetworks.com access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    This example uses an optional keys file. **Be sure to replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

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

### Configure NetQ CLI Using Configuration File

You can configure the NetQ CLI in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

    ```
    sudo nano /etc/netq/netq.yml
    ```
<!-- vale off -->
2. Locate the *netq-cli* section, or add it.
<!-- vale on -->
3. Set the parameters for the CLI.

    {{<tabs "TabID1" >}}

{{<tab "On-premises Deployments" >}}

Specify the following parameters:

- netq-user: User who can access the CLI
- server: IP address of the NetQ server or NetQ Appliance
- port (default): 32708

Your YAML configuration file should be similar to this:

```
netq-cli:
netq-user: admin@company.com
port: 32708
server: 192.168.0.254
```

{{</tab>}}

{{<tab "Cloud Deployments" >}}

Specify the following parameters:

- netq-user: User who can access the CLI
- server: api.netq.cumulusnetworks.com
- port (default): 443
- premises: Name of premises you want to query

Your YAML configuration file should be similar to this:

```
netq-cli:
netq-user: admin@company.com
port: 443
premises: datacenterwest
server: api.netq.cumulusnetworks.com
```

{{</tab>}}

{{</tabs>}}
