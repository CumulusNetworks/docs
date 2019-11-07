---
title: Install the NetQ Agent and CLI on Switches
author: Cumulus Networks
weight: 415
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
---
After installing or upgrading your Cumulus NetQ software, you should install the corresponding version of the NetQ Agents on each node you want to monitor. The node can be a:

- Switch running Cumulus Linux version 3.3.2 or later
- Server running Red Hat RHEL 7.1
- Server running Ubuntu 16.04
- Server running Ubuntu 18.04 (NetQ 2.2.2 and later)
- Server running CentOS 7

This topic describes how to perform the installation and configuration. If you are upgrading, you can skip some of the steps which do not need to be performed a second time.

## Install a NetQ Agent

To install the NetQ Agent you need to install the OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent and NetQ applications.

Instructions for installing the meta package on each node type are
included here:

  - [Install NetQ Agent on a Cumulus Linux Switch](#install-netq-agent-on-a-cumulus-linux-switch)
  - [Install NetQ Agent on an Ubuntu Server](#install-netq-agent-on-an-ubuntu-server)
  - [Install NetQ Agent on a Red Hat or CentOS Server](#install-netq-agent-on-a-red-hat-or-centos-server)

{{%notice note%}}

If your network uses a proxy server for external connections, you should
first [configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/)
so `apt-get` can access the meta package on the Cumulus Networks repository.

{{%/notice%}}

### Install NetQ Agent on a Cumulus Linux Switch

A simple process installs the NetQ Agent on a Cumulus switch.

1.  Edit the `/etc/apt/sources.list` file to add the repository for
    Cumulus NetQ. ***Note*** that NetQ has a separate repository from
    Cumulus Linux.

        cumulus@switch:~$ sudo nano /etc/apt/sources.list
        ...
        deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.3
        ...

    {{%notice tip%}}

The repository `deb http://apps3.cumulusnetworks.com/repos/deb
    CumulusLinux-3 netq-latest` can be used if you want to always
    retrieve the latest posted version of NetQ.

    {{%/notice%}}

2.  Update the local `apt` repository, then install the NetQ meta
    package on the switch.

        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install cumulus-netq

3.  Verify that [NTP](../../../../cumulus-linux/System-Configuration/Setting-Date-and-Time/)
    is running on the host node. Nodes must be in time synchronization with the
    NetQ Platform to enable useful statistical analysis.

        cumulus@switch:~$ sudo systemctl status ntp
        [sudo] password for cumulus:
        ● ntp.service - LSB: Start NTP daemon
           Loaded: loaded (/etc/init.d/ntp; bad; vendor preset: enabled)
           Active: active (running) since Fri 2018-06-01 13:49:11 EDT; 2 weeks 6 days ago
             Docs: man:systemd-sysv-generator(8)
           CGroup: /system.slice/ntp.service
                   └─2873 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 109:114

4.  Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl restart rsyslog.service

5. Continue with [NetQ Agent configuration](#configure-your-netq-agents).

### Install NetQ Agent on an Ubuntu Server

Before you install the NetQ Agent on an Ubuntu server, make sure the
following packages are installed and running these minimum versions:

  - iproute 1:4.3.0-1ubuntu3.16.04.1 all
  - iproute2 4.3.0-1ubuntu3 amd64
  - lldpd 0.7.19-1 amd64
  - ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64

    {{%notice info%}}

Make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not include `lldpd` by default, which is required for the installation.

To install this package, run the following commands:

```
root@ubuntu:~# apt-get update
root@ubuntu:~# apt-get install lldpd
root@ubuntu:~# systemctl enable lldpd.service
root@ubuntu:~# systemctl start lldpd.service
```
    {{%/notice%}}

To install the NetQ Agent on an Ubuntu server:

1.  Reference and update the local `apt` repository.

        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -

2. Add the Ubuntu repository:

    <details><summary>Ubuntu 16.04</summary>
    Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add
    the following line:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...
    </details>
    <details><summary>Ubuntu 18.04</summary>
    Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add
    the following line:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
        ...
    </details>
    {{%notice note%}}

The use of `netq-latest` in this example means that a `get` to the
    repository always retrieves the latest version of NetQ, even in the
    case where a major version update has been made. If you want to keep
    the repository on a specific version — such as `netq-2.2` — use that
    instead.

    {{%/notice%}}

3.  Install NTP on the server, if not already installed.

        root@ubuntu:~# sudo apt-get install ntp

4.  Configure the NTP server.

    1.  Open the `/etc/ntp.conf` file in your text editor of choice.

    2.  Under the Server section, specify the NTP server IP address or
        hostname.

5.  Enable and start the NTP service.

        root@ubuntu:~# sudo systemctl enable ntp.service
        root@ubuntu:~# sudo systemctl start ntp.service

6.  Verify NTP is operating correctly. Look for an asterisk (\*) or a
    plus sign (+) that indicates the clock is synchronized.

        root@ubuntu:~# ntpq -pn
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
        +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
         2a00:7600::41   .STEP.          16 u    - 1024    0    0.000    0.000   0.000
        \*129.250.35.250  249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

7.  Install the meta package on the server.

        root@ubuntu:~# apt-get update
        root@ubuntu:~# apt-get install cumulus-netq

8.  Continue with [NetQ Agent Configuration](#configure-your-netq-agents)

### Install NetQ Agent on a Red Hat or CentOS Server

Before you install the NetQ Agent on a Red Hat or CentOS server, make
sure the following packages are installed and running these minimum
versions:

  - iproute-3.10.0-54.el7\_2.1.x86\_64
  - lldpd-0.9.7-5.el7.x86\_64

    {{%notice info%}}

Make sure you are running lldp**d**, not lldp**ad**. CentOS does not include `lldpd` by default, nor does it include `wget`, which is required for the installation.

To install this package, run the following commands:

```
root@rhel7:~# yum -y install epel-release
root@rhel7:~# yum -y install lldpd
root@rhel7:~# systemctl enable lldpd.service
root@rhel7:~# systemctl start lldpd.service
root@rhel7:~# yum install wget
```
    {{%/notice%}}

  - ntp-4.2.6p5-25.el7.centos.2.x86\_64
  - ntpdate-4.2.6p5-25.el7.centos.2.x86\_64

To install the NetQ Agent on a Red Hat or CentOS server:

1.  Reference and update the local `yum` repository.

        root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
        root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1`
    flag for the two NetQ repositories.

        root@rhel7:~# vi /etc/yum.repos.d/cumulus-host-el.repo
        ...
        [cumulus-arch-netq-2.3]
        name=Cumulus netq packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-2.3/$basearch
        gpgcheck=1
        enabled=1
        [cumulus-noarch-netq-2.3]
        name=Cumulus netq architecture-independent packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-2.3/noarch
        gpgcheck=1
        enabled=1
        ...

3.  Install NTP on the server.

        root@rhel7:~# yum install ntp

4.  Configure the NTP server.

    1.  Open the `/etc/ntp.conf` file in your text editor of choice.
    2.  Under the Server section, specify the NTP server IP address or
        hostname.

5.  Enable and start the NTP service.

        root@rhel7:~# sudo systemctl enable ntpd.service
        root@rhel7:~# sudo systemctl start ntpd.service

6.  Verify NTP is operating correctly. Look for an asterisk (\*) or a
    plus sign (+) that indicates the clock is synchronized.

        root@rhel7:~# ntpq -pn
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
        +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
         2a00:7600::41   .STEP.          16 u    - 1024    0    0.000    0.000   0.000
        \*129.250.35.250  249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

7.  Install the Bash completion and NetQ meta packages on the server.

        root@rhel7:~# yum -y install bash-completion
        root@rhel7:~# yum install cumulus-netq

8.  Continue with [NetQ Agent Configuration](#configure-your-netq-agents).

## Configure Your NetQ Agents

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the device, or
- Configure and run NetQ CLI commands on the device.

### Configure NetQ Agents Using a Configuration File

You can configure the NetQ Agent in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice.
2. Locate the *netq-agent* section, or add it.
3. Set the parameters for the agent as follows:
    - port: 31980 (default configuration)
    - server: IP address of the NetQ server or appliance where the agent should send its collected data
    - vrf: default (default configuration) 

Your configuration should be similar to this:

```
netq-agent:
  port: 31980
  server: 127.0.0.1
  vrf: default
```

### Configure NetQ Agents Using the NetQ CLI

The NetQ CLI was installed when you installed the NetQ Agent; however, to use it to configure your NetQ Agents, you must first configure the CLI to communicate with your NetQ server or appliance.

#### Configure the NetQ CLI

 Note that the steps to install the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment.

Configuring the CLI for *on-premises* deployments requires only two commands:

```
netq config add cli server <ip-address-of-netq-server-or-appliance>
netq config restart cli
```

Configuring the CLI for *cloud* deployments also only requires two commands; however, there are a couple of additional options that you can apply:

- In NetQ 2.2.2 and later, if your nodes do not have Internet access, you can use the CLI proxy that is available on the NetQ cloud server or NetQ Cloud Appliance.
- In NetQ 2.2.1 and later, you can:
    - save your access credentials in a file and reference that file here to simplify the configuration commands
    - specify which premises you want to query

*For switches with Internet access* run the following commands, being sure to replace the key values with your generated keys.

```
$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

$ netq config restart cli
Restarting NetQ CLI... Success!
```

Or, if you have created a keys file as noted in the installation procedures for the NetQ Cloud server or Appliance, run the following commands. Be sure to include the *full path* the to file.

```
$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /<full-path>/credentials.yml port 443
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

$ netq config restart cli
Restarting NetQ CLI... Success!
```

If you have multiple premises, be sure to include which premises you want to query. Rerun this command to query a different premises.

```
$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> premises <premises-name> port 443
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

$ netq config restart cli
Restarting NetQ CLI... Success!
```

*For switches without Internet access*, you can use the CLI proxy that is part of the NetQ Cloud Server or Appliance with NetQ 2.2.2 and later to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud Server or Appliance. Run the following commands, using the IP address of the proxy:

```
$ netq config add cli server <proxy-ip-addr>
Updated cli server <proxy-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

$ netq config restart cli
Restarting NetQ CLI... Success!
```

#### Configure the NetQ Agent

Now that the CLI is configured, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Server or Appliance.

{{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

{{%/notice%}}

The same commands are used no matter the operating system (Cumulus Linux, Ubuntu, etc.). This example uses an IP address of *192.168.1.254* for the NetQ hardware.

```
$ netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
$ netq config restart agent
```

#### Configure the Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the NetQ Platform only via a
[VRF](/cumulus-linux/Layer-3/Virtual-Routing-and-Forwarding-VRF/), including a
[management VRF](/cumulus-linux/Layer-3/Management-VRF/). To do so, you need to
specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the NetQ Platform over it, configure the agent like this:

```
cumulus@leaf01:~$ netq config add agent server 192.168.1.254 vrf mgmt
cumulus@leaf01:~$ netq config restart agent
```

#### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

```
cumulus@leaf01:~$ netq config add agent server 192.168.1.254 port 7379
cumulus@leaf01:~$ netq config restart agent
```
