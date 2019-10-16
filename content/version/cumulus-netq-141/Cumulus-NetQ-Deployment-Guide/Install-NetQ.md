---
title: Install NetQ
author: Cumulus Networks
weight: 89
aliases:
 - /display/NETQ141/Install+NetQ
 - /pages/viewpage.action?pageId=10453414
pageID: 10453414
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
This topic provides step-by-step instructions for installing Cumulus
NetQ 1.4 with Cumulus Linux 3.3.2 or later. It provides setup
instructions for the Telemetry Server, for the Cumulus Linux switches,
and for the Linux-based hosts.

Cumulus NetQ core telemetry and analytics capabilities require two
components to be installed to gain access to the network connectivity
and actionable insights NetQ provides:

  - NetQ Telemetry application installed on the Telemetry Server
  - `cumulus-netq` meta package installed on Cumulus<sup>®</sup>
    Linux<sup>®</sup> switches

Optionally, you can:

  - Add greater fabric visibility by installing Net Q, `cumulus-netq`
    meta package, on host servers running CentOS, Red Hat Enterprise, or
    Ubuntu Linux Operating Systems
  - Add local storage and distribution services for the Cumulus Linux
    network operating system (NOS) and provisioning scripts used to
    deploy and upgrade Cumulus Linux and NetQ. See [Cumulus NetQ Image and Provisioning Management User Guide](/version/cumulus-netq-141/Cumulus-NetQ-Image-and-Provisioning-Management-User-Guide/) for details.
  - Add Free Range (FR) Routing capabilities on your hosts.

## Prerequisites

### Hardware Support

NetQ is supported on a variety of hardware. Refer to the [Cumulus
Hardware Compatibility
List](https://cumulusnetworks.com/products/hardware-compatibility-list/)
for the hardware supported and descriptions of the available options.

### Operating System Support

NetQ 1.4 is supported on the following operating systems:

  - Cumulus Linux 3.3.2 and later
  - Ubuntu 16.04
  - Red Hat<sup>®</sup> Enterprise Linux (RHEL) 7.1
  - CentOS 7

### NetQ Application Support

  - The NetQ Telemetry application is supported on NetQ 1.0 and later.
  - The NetQ Service Console is supported on NetQ 1.0 and later.
  - The NetQ Telemetry, Image and Provisioning Management Server (IPM)
    application (an early access feature) is available with NetQ 1.4 and
    later.

## Install Workflow

Installation of NetQ involves installing the Telemetry Server, and
installing and configuring the NetQ Agents. Additional steps are needed
to install NetQ in a [High
Availability](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Configure-Optional-NetQ-Capabilities)
configuration or to [Integrate NetQ with Event Notification Applications](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Configure-Optional-NetQ-Capabilities). This flow chart shows the three required steps (the numbered
items) and the optional steps to install and setup NetQ to start
validating your network.

{{% imgOld 0 %}}

## Install the NetQ Telemetry Server

The NetQ Telemetry Server is comprised of the following components:

  - **NetQ Telemetry application**: network monitoring and analytics
    functionality
  - **NetQ Telemetry CLI**: command line user interface for monitoring
    network and administering NetQ through a terminal session
  - [NetQ Service Console](/version/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/NetQ-Service-Console):
    web console user interface for monitoring and administering NetQ
    with the NetQ Shell
  - **Redis**: primary data base storage for collected data
  - **InfluxDB**: secondary data base storage for network snapshots
  - **Authorization**: secure access functionality

The server is available in one of two formats, as a:

  - VMware ESXi™ 6.5 virtual machine (VM)
  - KVM/QCOW (QEMU Copy on Write) image for use on CentOS, Ubuntu and
    RHEL hosts

{{%notice note%}}

Cumulus Networks recommends you install the Telemetry Server on an
out-of-band management network to ensure it can monitor in-band network
issues without being affected itself. Ideally, you should run the
Telemetry Server on a separate, powerful server for maximum usability
and performance. For more information on system requirements, [read this chapter](Methods-for-Diagnosing-Network-Issues.html#src-10453530_MethodsforDiagnosingNetworkIssues-matrix).

{{%/notice%}}

{{%notice tip%}}

The NetQ Telemetry Server components reside in containers in the VM.
These containers are completely separate from any containers you may
have on the hosts you are monitoring with NetQ. The NetQ containers do
not overwrite the host containers and vice versa.

{{%/notice%}}

To install the Telemetry Server VM:

1.  Download the NetQ Telemetry Server (TS) VM.

    1.  On the [Cumulus
        Downloads](https://cumulusnetworks.com/downloads/) page, select
        *NetQ* from the **Product** list box.

    2.  Optionally, select the latest available version from the
        **Version** list box.

    3.  Optionally, select the hypervisor you wish to use from the
        **Hypervisor** list box.

        {{% imgOld 1 %}}

    4.  Scroll down to review the images that match your selection
        criteria, and click **Download** for the VM you want.

        {{% imgOld 2 %}}

2.  Import the VM into your
    [KVM](https://docs.cumulusnetworks.com/display/VX/Vagrant+and+Libvirt+with+KVM+or+QEMU)
    or
    [VMware](https://docs.cumulusnetworks.com/display/VX/VMware+vSphere+-+ESXi+5.5)
    hypervisor.  
    This step is shown using KVM with Virtual Machine Manager.

    1.  Open Virtual Machine Manager.

    2.  Import the image.

        1.  Select **File** \> **New Virtual Machine**, or click the New
            VM icon.

        2.  Select **Import existing disk image**.

        3.  Click **Forward**.

            {{< figure src="/images/netq/vmm-create-new-vm.png" width="350" >}}

    3.  Place the image in the `/var/lib` directory.

        1.  Select the Cumulus image you just downloaded.

        2.  Click **Choose Volume**.

            {{< figure src="/images/netq/vmm-choose-storage-volume.png" width="450" >}}

        3.  Type, or browse for, the location where you want to store
            the volume. The directory must already exist.

            {{< figure src="/images/netq/vmm-create-virtual-machine.png" width="450" >}}

        4.  Select **Generic** for the **OS type** and **Version**.

        5.  Click **Forward**.

    4.  Allocate the amount of memory and number of CPUs you want
        available to this VM.

        {{%notice note%}}

The amount of RAM recommended for the NetQ TS is dependent on
your configuration and a number of other criteria; refer to the
[Methods for Diagnosing Network Issues](/version/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/Resolve-Issues/Methods-for-Diagnosing-Network-Issues) topic for more information.

        {{%/notice%}}

        {{< figure src="/images/netq/vmm-choose-memory-and-cpu.png" width="450" >}}

        1.  Increase or decrease the amount of **Memory** and **number
            of CPUs** using the + and - symbols to best meet your
            environment needs.

        2.  Click **Forward**.

    5.  Prepare for installation.

        1.  Provide a unique and useful name for the VM.

        2.  Select **Customize configuration before install**.

        3.  Click **Finish** to open the configuration options.

               {{< figure src="/images/netq/vmm-install-prep.png" width="450" >}}

    6.  Configure custom CPU parameters.

        1.  Click **CPUs**.

        2.  Increase or decrease the **Current** and **Maximum
            allocation** of CPUs using the + and - symbols to best meet
            your environment needs.

        3.  Select **Copy host CPU configuration**.

        4.  Click **Apply**.  

            {{< figure src="/images/netq/vmm-config-cpu.png" width="450" >}}

    7.  Configure custom network interface card (NIC) parameters.

        1.  Click **NIC**.

        2.  Select the **Network source**.

        3.  Select or type the **Device model**.

        4.  Verify the **MAC address** for the NIC.

        5.  Click **Apply**.

            {{< figure src="/images/netq/vmm-config-vni.png" width="450" >}}

3.  Verify NetQ TS VM has started.  
    If the VM did not start automatically, click **Begin
    Installation**.  
    There are two default user accounts you can use to log in:

      - The primary username is *admin*, and its associated password is
        *CumulusNetQ\!*.
      - An alternate username is *cumulus*, and its associated password
        is *CumulusLinux\!*.

4.  Note the external IP address of the switch where the TS is running.
    It is needed to configure the NetQ Agents on each node you want to
    monitor.

    {{%notice tip%}}

The TS obtains its IP address from DHCP. To determine the assigned
IP address, log in to the TS and run `ifconfig eth0`. Use the `inet
addr` or `int6 addr` for the TS IP address based on whether you are
running IPv4 or IPv6.

     cumulus@cumulus:~$ ifconfig eth0
     eth0   Link encap:Ethernet HWaddr 52:54:00:b8:1e:05
            inet addr:192.168.0.254 Bcast:192.168.0.255 Mask:255.255.255.0
            inet6 addr: fe80::5054:ff:feb8:1e05/64 Scope:Link
            UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
            RX packets:8752 errors:0 dropped:1 overruns:0 frame:0
            TX packets:340 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:567055 (553.7 KiB) TX bytes:34284 (33.4 KiB)

For HA mode, you need to note the IP addresses of all three
instances of the TS.

If you need the TS to have a static IP address, manually assign one:

- Edit the ` /etc/network/interfaces` file.

      `root@ts1:~# vi /etc/network/interfaces`

- Add the `address` and `gateway` lines to the eth0 configuration,
  specifying the TS's IP address and the IP address of the
  gateway.

      `auto eth0
      iface eth0
          address 198.51.100.10
          gateway 198.51.100.1`

- Save the file and exit.

    {{%/notice%}}

### Install Options

Two options are available when installing NetQ that require additional
configuration:

  - High Availability mode
  - Integration with third-party notification applications

Once the NetQ Telemetry Server is installed, if you are interested in
using the Telemetry Server in high availability (HA) mode, follow the
instructions in [Configure High Availability Mode](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Configure-Optional-NetQ-Capabilities).

In either standard or HA mode, if you want to proactively monitor events
in your network, you can integrate NetQ with PagerDuty, Slack, Elastic,
or Splunk. To do so you need to configure both the notification
application itself to receive the messages, and the NetQ Notifier with
what messages to send and where to send them, *after* installing the
NetQ Agents. See [Integrate NetQ with Event Notification Applications](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Configure-Optional-NetQ-Capabilities).

## Install the NetQ Agent

The NetQ Agent must be installed on each node you want to monitor. The
node can be a:

  - Switch running Cumulus Linux version 3.3.2 or later
  - Server running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7
  - Linux virtual machine running any of the above Linux operating
    systems

To install the NetQ Agent you need to install an OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent, the NetQ command
line interface (CLI), and the NetQ library. The library contains modules
used by both the NetQ Agent and the CLI.

Instructions for installing the meta package on each node type are
included here:

  - [Install NetQ Agent on a Cumulus Linux Switch](#src-10453414_InstallNetQ-AgentCL)
  - [Install NetQ Agent on an Ubuntu Server](#src-10453414_InstallNetQ-AgentUbuntu)
  - [Install NetQ Agent on a Red Hat or CentOS Server](#src-10453414_InstallNetQ-AgentRHC)

{{%notice note%}}

If your network uses a proxy server for external connections, you should
first configure a [global proxy](/display/NETQ141/Configuring+a+Global+Proxy) so
`apt-get` can access the meta package on the Cumulus Networks repository.

{{%/notice%}}

### Install NetQ Agent on a Cumulus Linux Switch

A simple two-step process installs the NetQ Agent on a Cumulus switch.

1.  On a switch, edit `/etc/apt/sources.list` to add the repository for
    Cumulus NetQ. Note that NetQ has a separate repository from Cumulus
    Linux.

        cumulus@leaf01:~$ sudo nano /etc/apt/sources.list
        ...
        deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-1.4
        ...

    {{%notice tip%}}

The repository `deb http://apps3.cumulusnetworks.com/repos/deb
CumulusLinux-3 netq-latest` can be used if you want to always
retrieve the latest posted version of NetQ.

    {{%/notice%}}

2.  Update the local `apt` repository, then install the NetQ meta
    package on the switch.

        cumulus@leaf01:~$ sudo apt-get update && sudo apt-get install cumulus-netq

Repeat these steps for each node, or use an automation tool to install
NetQ Agent on multiple nodes. Refer to [Deployment
Appendices](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Deployment-Appendices)
for an example Ansible playbook.

### Install NetQ Agent on an Ubuntu Server

Before you install the NetQ Agent on an Ubuntu server, make sure the
following packages are installed and running these minimum versions:

  - iproute 1:4.3.0-1ubuntu3.16.04.1 all
  - iproute2 4.3.0-1ubuntu3 amd64
  - lldpd 0.7.19-1 amd64
  - ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64
  - docker-ce 17.06.1\~ce-0\~ubuntu amd64

    {{%notice note%}}

This package is required only if you plan to monitor Docker
instances on the host; otherwise do not install it.

    {{%/notice%}}

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
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial roh-3
        ...

    {{%notice note%}}

The use of `netq-latest` in this example means that a get to the
repository always retrieves the last version of NetQ, even in the
case where a major version update has been made. If you want to keep
the repository on a specific version — such as `netq-1.4` — use that
instead.

    {{%/notice%}}

3.  Install NTP on the server.

        root@ubuntu:~# apt install ntp
        root@ubuntu:~# systemctl enable ntp
        root@ubuntu:~# systemctl start ntp

4.  Install the meta package on the server.

        root@ubuntu:~# apt-get update ; apt-get install cumulus-netq

5.  Restart the NetQ daemon.

        root@ubuntu:~# systemctl enable netqd ; systemctl restart netqd

### Install NetQ Agent on a Red Hat or CentOS Server

Before you install the NetQ Agent on a Red Hat or CentOS server, make
sure the following packages are installed and running these minimum
versions:

  - iproute-3.10.0-54.el7\_2.1.x86\_64

  - lldpd-0.9.7-5.el7.x86\_64

    {{%notice info%}}

Make sure you are running lldp**d**, not lldp**ad**.

CentOS does not include `lldpd` by default, nor does it include
`wget`, which is required for the installation. To install this
package, run the following commands:

     root@centos:~# yum -y install epel-release
     root@centos:~# yum -y install lldpd
     root@centos:~# systemctl enable lldpd.service
     root@centos:~# systemctl start lldpd.service
     root@centos:~# yum install wget

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
        [cumulus-arch-netq-1.1]
        name=Cumulus netq packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-1.1/$basearch
        gpgcheck=1
        enabled=1
        [cumulus-noarch-netq-1.1]
        name=Cumulus netq architecture-independent packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-1.1/noarch
        gpgcheck=1
        enabled=1
        ...

3.  Install NTP on the server.

        root@rhel7:~# yum install ntp
        root@rhel7:~# systemctl enable ntpd
        root@rhel7:~# systemctl start ntpd

4.  Install the Bash completion and NetQ meta packages on the server.

        root@rhel7:~# yum -y install bash-completion
        root@rhel7:~# yum install cumulus-netq

5.  Restart the NetQ daemon.

        root@rhel7:~# systemctl enable netqd ; systemctl restart netqd

## Set Up the NetQ Agents

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. The code examples shown in this section illustrate how to
configure the NetQ Agent on a Cumulus switch acting as a host, but it is
exactly the same for the other
type of nodes. Depending on your deployment, follow the relevant
additional instructions after the basic configuration steps:

  - [Basic Configuration](#src-10453414_InstallNetQ-basic)
  - [Configuring the Agent to Use a VRF](#src-10453414_InstallNetQ-AgentVRF)
  - [Configuring the Agent to Communicate over a Specific Port](#src-10453414_InstallNetQ-port)
  - [Enabling Docker for Container Environments](#src-10453414_InstallNetQ-AgentDocker)

### Basic Configuration

This is the minimum configuration required to properly monitor your
nodes.

1.  Verify that [NTP](/display/NETQ141/Setting+Date+and+Time) is running
    on the host node. Nodes must be in time synchronization with the
    Telemetry Server to enable useful statistical analysis.

        cumulus@switch:~$ sudo systemctl status ntp
        [sudo] password for cumulus:
        ● ntp.service - LSB: Start NTP daemon
           Loaded: loaded (/etc/init.d/ntp; bad; vendor preset: enabled)
           Active: active (running) since Fri 2018-06-01 13:49:11 EDT; 2 weeks 6 days ago
             Docs: man:systemd-sysv-generator(8)
           CGroup: /system.slice/ntp.service
                   └─2873 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 109:114

2.  Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl status ntp

3.  Link the host node to the TS you configured above.  
    In this code example, the IP address for the TS is *198.168.1.254.*
    Note: Run `ifconfig eth0` on the TS if you forgot to write down the
    address.

        cumulus@switch:~$ netq config add server 198.168.1.254

    This command updates the configuration in the `/etc/netq/netq.yml`
    file and enables the NetQ CLI.

4.  Restart NetQ Agent.

        cumulus@switch:~$ netq config restart agent

    {{%notice note%}}

If you see the following error, it means you haven't added the
telemetry server or the server wasn't configured:

  Error: Please specify IP address of DB server

    {{%/notice%}}

5.  Verify NetQ Agent can reach the TS.

        cumulus@switch:~$ netq config show server
         
        Server         Port    Vrf    Status
        -------------  ------  -----  --------
        198.168.1.254  6379    mgmt   ok 

### Configure the Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the telemetry server only via a
[VRF](/display/NETQ141/Virtual+Routing+and+Forwarding+-+VRF), including
a [management VRF](/display/NETQ141/Management+VRF). To do so, you need
to specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the telemetry server over it, configure the agent like this:

    cumulus@leaf01:~$ netq config add server 198.168.1.254 vrf mgmt

You then restart the agent as described in the previous section:

    cumulus@leaf01:~$ netq config restart agent

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 6379 for communication between the telemetry
server and NetQ Agents. If you want the NetQ Agent to communicate with
the telemetry server via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@switch:~$ netq config add server 198.168.1.254 port 7379

{{%notice tip%}}

If you are using NetQ in high availability mode, you can only configure
it on port 6379 or 26379.

{{%/notice%}}

### Enabling Docker for Container Environments

Before enabling Docker, you must first install Docker. The code examples
used here were created on an Ubuntu 16.04 host.

To install and enable Docker:

1.  Add the Docker repository key.

        root@host:~# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

2.  Install the Docker repository.

        root@host:~# echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

3.  Update the package lists.

        root@host:~# apt-get update

4.  Install Docker on the Ubuntu host.

        root@host:~# apt-get install -y docker-ce

5.  Check that the Docker service is running on the Ubuntu 16.04 host.

        root@host:~# systemctl status docker
        ● docker.service - Docker Application Container Engine
           Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
           Active: active (running) since Wed 2017-10-18 02:51:48 UTC; 1min 42s ago
             Docs: https://docs.docker.com
         Main PID: 18661 (dockerd)
           CGroup: /system.slice/docker.service
                   ├─18661 /usr/bin/dockerd -H fd://
                   └─18666 docker-containerd -l unix:///var/run/docker/libcontainerd/docker-containerd.sock --metrics-interval=0 --start-timeout 2m --state-dir /var/run/docker/libcontainerd/containerd --shim docker-containerd-shim --runtime docker-runc

6.  **Optional:** Add the docker group to your user account to be able
    to run docker commands without using `sudo`.

        user@host:~$ sudo adduser ${USER} docker

    {{%notice note%}}

Adding groups to different users requires a logout and login to take
effect.

    {{%/notice%}}

7.  Enable Docker by adding the following three lines to the `netq.yml`
    file on the container host. This command also sets how often to pull
    data from the container to every 15 seconds.

        root@host:~# vi /etc/cts/netq/netq.yml

        ...
        docker:
          enable: true
          poll_period: 15
        ...

## Set Up Security

When you set up and configured your
Cumulus Linux switches, you likely configured a number of the security
features available. Cumulus recommends the same security measures be
followed for the Telemetry Server in the out-of-band-network. Refer to
the [Securing Cumulus Linux white paper](https://cumulusnetworks.com/learn/web-scale-networking-resources/white-papers/securing-cumulus-linux/) for details.

Your Cumulus Linux switches have a number
of ports open (refer to [Default Open Ports in Cumulus
Linux](https://support.cumulusnetworks.com/hc/en-us/articles/228281808-Default-Open-Ports-in-Cumulus-Linux)
article).
