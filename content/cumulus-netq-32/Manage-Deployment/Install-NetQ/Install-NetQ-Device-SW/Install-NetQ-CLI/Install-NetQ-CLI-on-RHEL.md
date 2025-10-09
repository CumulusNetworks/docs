---
title: Install and Configure the NetQ CLI on RHEL and CentOS Servers
author: Cumulus Networks
weight: 350
toc: 5
---
After installing your Cumulus NetQ software and the NetQ 3.2.1 Agents on each switch you want to monitor, you can also install the NetQ CLI on servers running:

- Red Hat RHEL 7.1
- CentOS 7

## Prepare for NetQ CLI Installation on a RHEL or CentOS Server

For servers running RHEL or CentOS, you need to:

- Verify the minimum package versions are installed
- Verify the server is running lldpd
- Install and configure NTP, if needed
- Obtain NetQ software packages

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy]({{<ref "/cumulus-linux-43/System-Configuration/Configuring-a-Global-Proxy" >}}) so <code>apt-get</code> can access the software package in the Cumulus Networks repository.
{{%/notice%}}

### Verify Service Package Versions

Before you install the NetQ CLI on a Red Hat or CentOS server, make sure the following packages are installed and running these minimum versions:

- iproute-3.10.0-54.el7\_2.1.x86\_64
- lldpd-0.9.7-5.el7.x86\_64
- ntp-4.2.6p5-25.el7.centos.2.x86\_64
- ntpdate-4.2.6p5-25.el7.centos.2.x86\_64

### Verify the Server is Running lldpd and wget

Make sure you are running lldp**d**, not lldp**ad**. CentOS does not include `lldpd` by default, nor does it include `wget`, which is required for the installation.

To install this package, run the following commands:

```
root@rhel7:~# sudo yum -y install epel-release
root@rhel7:~# sudo yum -y install lldpd
root@rhel7:~# sudo systemctl enable lldpd.service
root@rhel7:~# sudo systemctl start lldpd.service
root@rhel7:~# sudo yum install wget
```

### Install and Configure NTP

If NTP is not already installed and configured, follow these steps:

1. Install [NTP]({{<ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time" >}}) on the server. Servers must be in time synchronization with the NetQ Appliance or VM to enable useful statistical analysis.

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

4.  Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock is synchronized.

    ```
    root@rhel7:~# ntpq -pn
    remote           refid            st t when poll reach   delay   offset  jitter
    ==============================================================================
    +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
    +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
    2a00:7600::41    .STEP.          16 u    - 1024    0    0.000    0.000   0.000
    \*129.250.35.250 249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243
    ```

## Install NetQ CLI on a RHEL or CentOS Server

A simple process installs the NetQ CLI on a RHEL or CentOS server.

1. Reference and update the local `yum` repository and key.

    ```
    root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
    root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo
    ```

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1` flag for the two NetQ repositories.

    ```
    root@rhel7:~# vi /etc/yum.repos.d/cumulus-host-el.repo
    ...
    [cumulus-arch-netq-3.2]
    name=Cumulus netq packages
    baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-3.2/$basearch
    gpgcheck=1
    enabled=1
    [cumulus-noarch-netq-3.2]
    name=Cumulus netq architecture-independent packages
    baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-3.2/noarch
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

    {{<netq-install/cli-version version="3.2.1" opsys="rh">}}

5. Continue with the next section.

## Configure the NetQ CLI on a RHEL or CentOS Server

Two methods are available for configuring the NetQ CLI on a switch:

- Run NetQ CLI commands on the switch; refer to the next section
- Edit the configuration file on the switch; refer to {{<link url="#configure-netq-cli-using-configuration-file" text="Configure CLI Using File">}}

{{<netq-install/cli-config opsys="rh">}}

### Configure NetQ CLI Using the CLI

The steps to configure the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment. Follow the instructions for your deployment type.

{{< tabs "TabID0" >}}

{{< tab "On-premises Deployments" >}}

Use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [vrf <text-vrf-name>] [port <text-gateway-port>]
```

Restart the CLI afterward to activate the configuration.

This example uses an IP address of 192.168.1.0 and the default port and VRF.

```
root@rhel7:~# sudo netq config add cli server 192.168.1.0
root@rhel7:~# sudo netq config restart cli
```

{{<notice note>}}
If you have a server cluster deployed, use the IP address of the master server.
{{</notice>}}

{{< /tab >}}

{{< tab "Cloud Deployments" >}}

To access and configure the CLI on your NetQ Platform or NetQ Cloud Appliance, you must have your username and password to access the NetQ UI to generate AuthKeys. These keys provide authorized access (access key) and user authentication (secret key). Your credentials and NetQ Cloud addresses were provided by Cumulus Networks via an email titled *Welcome to Cumulus NetQ!*

To generate AuthKeys:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. From the Main Menu, select *Management* in the **Admin** column.

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
    root@rhel7:~# sudo netq config add cli server api.netq.cumulusnetworks.com access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@rhel7:~# sudo netq config restart cli
    Restarting NetQ CLI... Success!
    ```

    This example uses an optional keys file. **Be sure to replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

    ```
    root@rhel7:~# sudo netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /home/netq/nq-cld-creds.yml premises datacenterwest
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@rhel7:~# sudo netq config restart cli
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
    root@rhel7:~# sudo nano /etc/netq/netq.yml
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
