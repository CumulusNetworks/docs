---
title: Install the Cumulus NetQ Cloud Appliance
author: Cumulus Networks
weight: 413
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---

The Cumulus NetQ Cloud Appliance provides secure streaming of telemetry data collected by NetQ Agents to the NetQ Cloud; the server comes preloaded with a Cumulus Linux image that includes basic Cumulus NetQ services,  Cumulus Linux license, and certified cables and optics.

This topic helps you get your Cumulus NetQ Cloud Appliance up and running in a few minutes.

## What's in the Box?

Inside the box that was shipped to you, you'll find:

- Your Cumulus NetQ Cloud Appliance (a Supermicro SuperServer E300-9D) with the Cumulus Linux OS, Cumulus NetQ services and licenses already installed
- Hardware accessories, such as power cables and rack mounting gear (note that network cables and optics ship separately)
- Information regarding your order

If you're looking for hardware specifications (including LED layouts and FRUs like the power supply or fans and accessories like included cables) or safety and environmental information, check out the appliance's [user manual](https://www.supermicro.com/manuals/superserver/mini-itx/MNL-2094.pdf).

## Install Workflow

Install and set up your NetQ Appliance and switch and host Agents using the following steps:

{{< figure src="/images/netq/install-flow-nqcldappl-cloud-nq222.png" width="600" >}}

## Install the Appliance

After you unbox the appliance, mount it in the rack and connect it to power following the procedures described in your appliance's [user manual](https://www.supermicro.com/manuals/superserver/mini-itx/MNL-2094.pdf). Connect the Ethernet cable to the 10G management port (eth0), then power on the appliance.

{{< figure src="/images/netq/netq-cloud-appl-port-connections.png" width="700" >}}

If your network runs DHCP, you can configure Cumulus NetQ and Cumulus Linux over the network. If DHCP isn't enabled, then you configure the appliance using the console cable provided.

## Configure the Password, Hostname, and IP Address

Change the password and specify the hostname and IP address for the appliance before installing the NetQ software.

1. Log in to the appliance using the default login credentials:

   - **Username**: *cumulus*
   - **Password**: *CumulusLinux!*


2. Change your password for the cumulus account using the `passwd` command.

```
cumulus@netq-appliance:~$ passwd
```

3. The appliance's default hostname is *cumulus*. You can easily change it using the Cumulus Linux Network Command Line Utility (NCLU):

```
cumulus@netq-appliance:~$ net add hostname NEW_HOSTNAME
```

4. Identify the IP address.
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

## Download and Install the NetQ Cloud Software

Be sure to use the correct instructions as they have changed for the NetQ 2.2.2 release.

<details>
<summary>NetQ 2.2.2</summary>

1. Download and install the tarball file.

   The config-key was provided to you by Cumulus Networks via an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new) to have it sent to you again.

   **Note**: Be sure to replace the interface and key values with values appropriate for your configuration. This example uses eth0 and a sample key.

```
cumulus@netq-appliance:~$ netq install opta interface eth0 tarball download config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

</details>
<details>
<summary>NetQ 2.2.0 or 2.2.1</summary>

1. On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.

2. Click *2.2* from the **Version** list box, and then select *2.2.x* from the submenu.

      **Note**: You must choose 2.2.x. Earlier versions do not support this appliance.

      {{< figure src="/images/netq/NetQ-22-Download-Options-222.png" width="600" >}}

3. Select *Appliance (Cloud)* from the **Hypervisor/Platform** list box.

      {{< figure src="/images/netq/NetQ-Cloud-Appl-SW-Dwnld-222.png" width="250" >}}

4. Click **Upgrade** to download the installer bundle.

      **Note**: The download option only provides the OS which is pre-installed on the appliance.


5. Copy the downloaded package (*NetQ-2.2.x-opta.tgz*) into the */mnt/installables/* directory.

      **Note**: The name of the package needs to be replaced with the exact version you have downloaded. Instead of 2.2.x, you would enter 2.2.1 for example.

      ```
      cumulus@netq-appliance:~$ sudo cp /home/usr/dir/NetQ-2.2.x-opta.tgz /mnt/installables/
      ```

6. Install the software using the interface you defined above and your config-key.

      The config-key was provided to you by Cumulus Networks via an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new) to have it sent to you again.

      **Note**: Be sure to replace the interface and key values with values appropriate for your configuration. These examples use eth0 and a sample key.

      <details><summary>NetQ v2.2.1</span></summary>

      ```
      cumulus@netq-appliance:~$ netq install opta interface eth0 tarball NetQ-2.2.1-opta.tgz config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
      opta-installer: Resetting OPTA
      opta-installer: Checking for installer directory
      opta-installer: Checking minimum RAM requirements
      opta-installer: Checking for minimum CPU requirements
      opta-installer: Checking for Python 2.7
      opta-installer: Checking for Kubernetes v1.11.5
      opta-installer: Checking for Docker /usr/bin/docker
      ...
      Successfully installed the opta
      ```

      </details>

      <details><summary>NetQ v2.2.0</span></summary>

      ```
      cumulus@netq-appliance:~$ netq install opta interface eth0 tarball NetQ-2.2.0-opta.tgz key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
      opta-installer: Resetting OPTA
      opta-installer: Checking for installer directory
      opta-installer: Checking minimum RAM requirements
      opta-installer: Checking for minimum CPU requirements
      opta-installer: Checking for Python 2.7
      opta-installer: Checking for Kubernetes v1.11.5
      opta-installer: Checking for Docker /usr/bin/docker
      ...
      Successfully installed the opta
      ```

      </details>
</details>

{{%notice info%}}

If you changed the IP address or interface of the appliance to something other than what it was assigned previously, you must inform NetQ of the change.

If you changed the IP address, but kept the interface the same (for example, eth0), re-run the `netq install opta interface` command using your config-key:

   *For NetQ 2.2.1 or 2.2.2*

```
cumulus@netq-appliance:~$ netq install opta interface eth0 tarball NetQ-2.2.x-opta.tgz config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```
   *For NetQ 2.2.0*

```
cumulus@netq-appliance:~$ netq install opta interface eth0 tarball NetQ-2.2.x-opta.tgz key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

If you changed the interface (for example, eth0 to eth1), run the `netq install opta interface` command with the new interface and your config-key:

   *For NetQ 2.2.1 or 2.2.2*

```
cumulus@netq-appliance:~$ netq install opta interface eth1 tarball NetQ-2.2.x-opta.tgz config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

   *For NetQ 2.2.0*

```
cumulus@netq-appliance:~$ netq install opta interface eth1 tarball NetQ-2.2.x-opta.tgz key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

{{%/notice%}}
{{%notice note%}}

You can optionally override selected default installation parameters using the `file <text-config-file>` option. By default, the data directory is `/mnt`, the Kubernetes pods are assigned to network addresses in the 10.244.0.0/16 range, the node name is *cumulus.netq*, and the scratch directory is `/tmp`. The override file must be in YAML format and written as shown in this example:

```
data-dir: /usr/share
pod-network-dir: 10.1.1.0/16
node-name: company-name.netq
scratch-dir: /tmp/netq
```

The `text-config-file` value is then the full path to the YAML file; for example `/home/username/overwrite-default.yml`.

{{%/notice%}}

### Verify Cloud Installation

Now that your appliance is installed and configured, you can verify that all applications and services are operating properly.

   ```
   cumulus@<netq-appliance-hostname>:~$ netq show opta-health
   OPTA is healthy
   ```

## Configure CLI Access on Appliance

The CLI communicates through the API gateway in the NetQ Cloud. To access and configure the CLI on your NetQ Cloud server you will need your username and password to access the NetQ UI to generate an access-key and secret-key. Your credentials and NetQ Cloud addresses were provided by Cumulus Networks via an email titled *Welcome to Cumulus NetQ!*

To configure CLI access:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. From the Main Menu, select *Management* in the **Admin** column.

      {{< figure src="/images/netq/main-menu-mgmt-selected.png" width="400">}}

4. Click **Manage** on the User Accounts card.
5. Select your user and click **Generate AuthKeys**.

      {{< figure src="/images/netq/generate-auth-keys.png" width="700">}}

6. Copy these keys to a safe place.

      {{%notice info%}}
The secret key is only shown once. If you don't copy these, you will need to regenerate them and reconfigure CLI access.

In version 2.2.1 and later, you can save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can store this file wherever you like, give it a name, such as, *credentials.yml*, and make sure it has the following format:

```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```
      {{%/notice%}}

7. Run the following command using your generated keys:
   - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.
   ```
   cumulus@netq-appliance:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-appliance:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```
   - In NetQ 2.2.1 and later, if you have created a *credentials.yml* file as noted in the previous step, run the following commands. Be sure to include the full path the to file.
   ```
   cumulus@netq-appliance:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-appliance:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

## Install and Configure the NetQ Agent and CLI Access

Whether using the NetQ Appliance or your own hardware, the NetQ Agent
must be installed on each node you want to monitor. The node can be a:

  - Switch running Cumulus Linux version 3.3.2 or later
  - Servers running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7 (Cumulus NetQ 2.2.1 and earlier)
  - Servers running Red Hat RHEL 7.1, Ubuntu 16.04, Ubuntu 18.04, or CentOS 7 (Cumulus NetQ 2.2.2 and later)
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

4.  Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl restart rsyslog.service

5.  Configure the NetQ Agent to send telemetry data to the NetQ Cloud Appliance.  

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the NetQ hardware is
    *192.168.1.254*.

        cumulus@switch:~$ netq config add agent server 192.168.1.254
        cumulus@switch:~$ netq config restart agent

6.  Optionally, configure the switch or host to run the NetQ CLI.

    *For switches* **with** *Internet access:*

      - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.
      ```
      cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
      Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
      Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

      cumulus@switch:~$ netq config restart cli
      Restarting NetQ CLI... Success!
      ```
      - In NetQ 2.2.1 and later, if you have created a *credentials.yml* file as noted in the previous step, run the following commands. Be sure to include the full path the to file.
      ```
      cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
      Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
      Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

      cumulus@switch:~$ netq config restart cli
      Restarting NetQ CLI... Success!
      ```
    *For switches* **without** *Internet access:*

      A CLI proxy is part of the NetQ Cloud Appliance with NetQ 2.2.2 and later. If your switches and hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud Appliance to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud Appliance. Run the following commands, using the IP address of your NetQ Cloud Appliance:
```
cumulus@nswitch:~$ netq config add cli server <netq-cloud-appliance-ip-addr>
Updated cli server <netq-cloud-appliance-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

cumulus@switch:~$ netq config restart cli
Restarting NetQ CLI... Success!
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

2.  Add the Ubuntu repository:

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

The use of `netq-latest` in these example means that a `get` to the
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

8.  Configure the NetQ Agent to send telemetry data to the NetQ Cloud Appliance.  

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the NetQ hardware is
    *192.168.1.254*.

   ```
   root@ubuntu:~# netq config add agent server 192.168.1.254
   Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
   root@ubuntu:~# netq config restart agent
   ```

9.  Optionally, configure the switch or host to run the NetQ CLI.

    *For hosts* **with** *Internet access:*

      - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.

         ```
         root@ubuntu:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
         Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
         Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

         root@ubuntu:~$ netq config restart cli
         Restarting NetQ CLI... Success!
         ```
      - In NetQ 2.2.1 and later, if you have created a *credentials.yml* file as noted in the previous step, run the following commands. Be sure to include the full path the to file.

         ```
         root@ubuntu:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
         Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
         Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

         root@ubuntu:~$ netq config restart cli
         Restarting NetQ CLI... Success!
         ```
    *For hosts* **without** *Internet access:*

       A CLI proxy is part of the NetQ Cloud Appliance with NetQ 2.2.2 and later. If your hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud Appliance to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud Appliance. Run the following commands, using the IP address of your NetQ Cloud Appliance:

```
root@ubuntu:~$ netq config add cli server <netq-cloud-appliance-ip-addr>
Updated cli server <netq-cloud-appliance-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

root@ubuntu:~$ netq config restart cli
Restarting NetQ CLI... Success!
```

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

8.  Configure the NetQ Agent to send telemetry data to the NetQ Cloud Appliance.  

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

   {{%/notice%}}

    In this example, the IP address for the NetQ hardware is
    *192.168.1.254*.

        root@rhel7:~# netq config add agent server 192.168.1.254
        Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
        root@rhel7:~# netq config restart agent

9.  Optionally, configure the switch or host to run the NetQ CLI.

    *For hosts* **with** *Internet access:*

      - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.

         ```
         root@rhel7:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
         Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
         Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

         root@rhel7:~$ netq config restart cli
         Restarting NetQ CLI... Success!
         ```
      - In NetQ 2.2.1 and later, if you have created a *credentials.yml* file as noted in the previous step, run the following commands. Be sure to include the full path the to file.

         ```
         root@rhel7:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
         Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
         Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

         root@rhel7:~$ netq config restart cli
         Restarting NetQ CLI... Success!
         ```

      *For hosts* **without** *Internet access:*

      A CLI proxy is part of the NetQ Cloud Appliance with NetQ 2.2.2 and later. If your hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud Appliance to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud Appliance. Run the following commands, using the IP address of your NetQ Cloud Appliance:

```
root@rhel7:~$ netq config add cli server <netq-cloud-appliance-ip-addr>
Updated cli server <netq-cloud-appliance-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

root@rhel7:~$ netq config restart cli
Restarting NetQ CLI... Success!
```

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

## Intelligent Platform Management Interface - IPMI

The NetQ Appliance comes with Intelligent Platform Management Interface (IPMI). IPMI provides remote access to multiple users at different locations for networking. It also allows a system administrator to monitor system health and manage computer events remotely. For details, please read the [Supermicro IPMI user guide](https://www.supermicro.com/manuals/other/IPMI_Users_Guide.pdf).

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
