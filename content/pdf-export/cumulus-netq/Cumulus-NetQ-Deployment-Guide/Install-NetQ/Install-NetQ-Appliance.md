---
title: Install the Cumulus NetQ Appliance
author: Cumulus Networks
weight: 411
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---

The Cumulus NetQ appliance provides a complete monitoring solution for your network; the server comes preloaded with a Cumulus Linux image that includes Cumulus NetQ services, a Cumulus Linux license and certified cables and optics.

This topic helps you get your Cumulus NetQ appliance up and running in a few minutes.

## What's in the Box?

Inside the box that was shipped to you, you'll find:

- Your Cumulus NetQ appliance (a Supermicro 6019P-WTR server) with the Cumulus Linux OS, Cumulus NetQ services and license already installed
- Hardware accessories, such as power cables and rack mounting gear (note that network cables and optics ship separately)
- Information regarding your order

If you're looking for hardware specifications (including LED layouts and FRUs like the power supply or fans and accessories like included cables) or safety and environmental information, check out the [user manual](https://www.supermicro.com/manuals/superserver/1U/MNL-1943.pdf) and [quick reference guide](https://www.supermicro.com/QuickRefs/superserver/1U/QRG-1943.pdf).

## Install and Configure the Appliance

After you unbox the appliance, mount it in the rack and connect it to power following the procedures described in your appliance's user manual. Connect the Ethernet cable to the 1G management port (eth0), then power on the appliance.

   {{< figure src="/images/netq/netq-appliance-port-connections.png" >}}

If your network runs DHCP, you can configure Cumulus NetQ and Cumulus Linux over the network. If DHCP isn't enabled, then you configure the appliance using the console cable provided.

When you power on the appliance, you must log in using the default login credentials:

- **Username**: *cumulus*
- **Password**: *CumulusLinux!*

## Configure the Password, Hostname and IP Address

You should change your password for the cumulus account soon after you log in using the `passwd` command.

```
cumulus@netq-appliance:~$ passwd
```

The appliance's default hostname is *cumulus*. You can quickly change it using the Cumulus Linux Network Command Line Utility (NCLU):

```
cumulus@netq-appliance:~$ net add hostname NEW_HOSTNAME
```

The appliance contains at least one dedicated Ethernet management port, named eth0, for out-of-band management. This is where NetQ Agents should send the telemetry data collected from your monitored switches and hosts. By default, eth0 uses DHCPv4 to get its IP address. You can view the address assigned using NCLU:

```
cumulus@netq-appliance:~$ net show interface eth0
    Name  MAC                Speed  MTU   Mode
--  ----  -----------------  -----  ----  ----
UP  eth0  fc:1f:6b:81:2b:62  1G     1500  Mgmt

IP Details
-------------------------  ---------------
IP:                        192.0.2.42/24
IP Neighbor(ARP) Entries:  4
```

If instead, you want to set a static IP address, use the following NCLU command, substituting with your desired IP address:

```
cumulus@netq-appliance:~$ net add interface eth0 address 192.0.2.42/24
```

Review and commit your changes:

```
cumulus@netq-appliance:~$ net pending
cumulus@netq-appliance:~$ net commit
```

{{%notice info%}}

If you have changed the IP address of the NetQ Appliance, you need to
re-register this address with the Kubernetes containers before you can
continue.

1.  Reset all Kubernetes administrative settings. Run the command twice
    to make sure all directories and files have been reset.

    ```
    cumulus@netq-platform:~$ sudo kubeadm reset -f
    ```  

2.  Remove the Kubernetes configuration.  
    ```
    cumulus@netq-platform:~$ sudo rm /home/cumulus/.kube/config
    ```

3.  Reset the NetQ Platform install daemon.  
    ```
    cumulus@netq-platform:~$ sudo systemctl reset-failed
    ```  

4.  Reset the Kubernetes service.  
    ```
    cumulus@netq-platform:~$ sudo systemctl restart cts-kubectl-config
    ```  
    **Note**: Allow 15 minutes for the prompt to return.

5.  Reboot the VM.  
    **Note**: Allow 5-10 minutes for the VM to boot.

{{%/notice%}}

With your NetQ cloud server now set up and configured, you are ready to install the NetQ Agent on each switch and host you want to monitor with NetQ. Follow the instructions in [Install the NetQ Agent](#install-the-netq-agent) for details.

## Intelligent Platform Management Interface - IPMI

The NetQ Appliance comes with Intelligent Platform Management Interface (IPMI). IPMI provides remote access to multiple users at different locations for networking. It also allows a system administrator to monitor system health and manage computer events remotely. For details, please read the [Supermicro IPMI user guide](https://www.supermicro.com/manuals/other/IPMI_Users_Guide.pdf).

## Install the NetQ Agent

The NetQ Agent must be installed on each node you want to monitor. The node can be a:

  - Switch running Cumulus Linux version 3.3.2 or later
  - Server running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7
  - Linux virtual machine running any of the above Linux operating
    systems

To install the NetQ Agent you need to install the OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent, the NetQ command
line interface (CLI), and the NetQ library. The library contains modules
used by both the NetQ Agent and the CLI.

Instructions for installing the meta package on each node type are
included here:

  - [Install NetQ Agent on a Cumulus Linux Switch](#install-netq-agent-on-a-cumulus-linux-switch)
  - [Install NetQ Agent on an Ubuntu Server](#install-netq-on-an-ubuntu-server)
  - [Install NetQ Agent on a Red Hat or CentOS Server](#install-netq-on-a-red-hat-or-centos-server)

{{%notice note%}}

If your network uses a proxy server for external connections, you should
first [configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/)
so `apt-get` can access the meta package on the Cumulus Networks repository.

{{%/notice%}}

### Install NetQ Agent on a Cumulus Linux Switch

A simple process installs the NetQ Agent on a Cumulus switch.

1.  Edit the `/etc/apt/sources.list` file to add the repository for
    Cumulus NetQ.
    **Note**: NetQ has a separate repository from Cumulus Linux.

        cumulus@switch:~$ sudo nano /etc/apt/sources.list
        ...
        deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.1
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

3.  Verify that [NTP](/cumulus-linux/System-Configuration/Setting-Date-and-Time/)
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

4. Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl restart rsyslog.service

5. Configure the NetQ Agent to send telemetry data to the NetQ Appliance.  

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the NetQ hardware is *192.168.1.254*.

        cumulus@switch:~$ netq config add agent server 192.168.1.254
        cumulus@switch:~$ netq config restart agent

6. Optionally, configure the switch or host to run the NetQ CLI.

   ```
   cumulus@switch:~$ netq config add cli server 192.168.1.254
   cumulus@switch:~$ netq config restart cli
   ```

7. Repeat these steps for each Cumulus switch, or use an automation tool to
install NetQ Agent on multiple Cumulus Linux switches.

### Install NetQ Agent on an Ubuntu Server

Before you install the NetQ Agent on an Ubuntu server, make sure the
following packages are installed and running these minimum versions:

  - iproute 1:4.3.0-1ubuntu3.16.04.1 all
  - iproute2 4.3.0-1ubuntu3 amd64
  - lldpd 0.7.19-1 amd64
  - ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64

    {{%notice info%}}

Make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not
    include `lldpd` by default, which is required for the installation.
    To install this package, run the following commands:

    root@ubuntu:~# apt-get update
    root@ubuntu:~# apt-get install lldpd
    root@ubuntu:~# systemctl enable lldpd.service
    root@ubuntu:~# systemctl start lldpd.service

    {{%/notice%}}

To install the NetQ Agent on an Ubuntu server:

1.  Reference and update the local `apt` repository.

        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -

2.  Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add
    the following lines:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...

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

8.  Configure the NetQ Agent to send telemetry data to the NetQ Appliance.  

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the NetQ hardware is
    *192.168.1.254*.

        root@ubuntu:~# netq config add agent server 192.168.1.254
        Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
        root@ubuntu:~# netq config restart agent

9.  Optionally, configure the switch or host to run the NetQ CLI.

            root@ubuntu:~# netq config add cli server 192.168.1.254
            Updated cli server 192.168.1.254 vrf default. Please restart netqd (netq config restart cli).
            root@ubuntu:~# netq config restart cli

10. Repeat these steps for all of your hosts running Ubuntu, or use an
    automation tool to streamline the process.

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
        [cumulus-arch-netq-2.2]
        name=Cumulus netq packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-2.2/$basearch
        gpgcheck=1
        enabled=1
        [cumulus-noarch-netq-2.2]
        name=Cumulus netq architecture-independent packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-2.2/noarch
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

8.  Configure the NetQ Agent to send telemetry data to the NetQ Appliance.  

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the NetQ hardware is
    *192.168.1.254*.

        root@rhel7:~# netq config add agent server 192.168.1.254
        Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
        root@rhel7:~# netq config restart agent

9.  Optionally, configure the switch or host to run the NetQ CLI.

         root@rhel7:~# netq config add cli server 192.168.1.254
         Updated cli server 192.168.1.254 vrf default. Please restart netqd (netq config restart cli).
         root@rhel7:~# netq config restart cli

10. Repeat these steps for all of your hosts running Ubuntu, or use an
    automation tool to streamline the process.

## Configure Optional NetQ Agent Settings

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. The code examples shown in this section illustrate how to
configure the NetQ Agent on a Cumulus switch, but it is exactly the same
for the other type of nodes. Depending on your deployment, follow the
relevant additional instructions after the basic configuration steps:

  - [Configuring the Agent to Use a VRF](#configure-the-agent-to-use-a-vrf)
  - [Configuring the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port)

### Configure the Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the NetQ Platform only via a
[VRF](/cumulus-linux/Layer-3/Virtual-Routing-and-Forwarding-VRF/), including a
[management VRF](/cumulus-linux/Layer-3/Management-VRF/). To do so, you need to
specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the NetQ Platform over it, configure the agent like this:

    cumulus@leaf01:~$ netq config add agent server 192.168.1.254 vrf mgmt
    cumulus@leaf01:~$ netq config add cli server 192.168.254 vrf mgmt

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent
    cumulus@leaf01:~$ netq config restart cli

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@leaf01:~$ netq config add agent server 192.168.1.254 port 7379

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent

## Integrate with Event Notification Tools

If you want to proactively monitor events in your network, you can
integrate NetQ with the PagerDuty or Slack notification tools. To do so
you need to configure both the notification application itself to
receive the messages, and NetQ with what messages to send and where to
send them. Refer to [Integrate NetQ with Event Notification Applications](/cumulus-netq/Cumulus-NetQ-Integration-Guide/integrate-netq-with-notification-applications)
to use the CLI for configuration.

## Set Up Security

When you set up and configured your
Cumulus Linux switches, you likely configured a number of the security
features available. Cumulus recommends the same security measures be
followed for the NetQ Platform in the out-of-band-network. Refer to the
[Securing Cumulus Linux white paper](https://cumulusnetworks.com/learn/web-scale-networking-resources/white-papers/securing-cumulus-linux/) for details.

Your Cumulus Linux switches have a number
of ports open by default. A few additional ports must be opened to run
the NetQ software (refer to [Default Open Ports in Cumulus Linux and NetQ](https://support.cumulusnetworks.com/hc/en-us/articles/228281808-Default-Open-Ports-in-Cumulus-Linux-and-NetQ) article).
