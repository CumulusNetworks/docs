---
title: Install and Configure the NetQ Agent on Ubuntu Servers
author: Cumulus Networks
weight: 120
toc: 5
---
After installing your Cumulus NetQ software, you should install the  NetQ 2.4.1 Agents on each server you want to monitor. NetQ 2.4 Agents can be installed on servers running:

- Ubuntu 16.04
- Ubuntu 18.04 (NetQ 2.2.2 and later)

## Prepare for NetQ Agent Installation on an Ubuntu Server

For servers running Ubuntu OS, you need to:

- Verify the minimum service packages versions are installed
- Verify the server is running lldpd
- Install and configure network time server, if needed
- Obtain NetQ software packages

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy]({{<ref "/cumulus-linux-43/System-Configuration/Configuring-a-Global-Proxy" >}}) so `apt-get` can access the agent package on the Cumulus Networks repository.
{{%/notice%}}

### Verify Service Package Versions

For proper operation of  the NetQ Agent on an Ubuntu server, make sure the following packages are installed and running these minimum versions:

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

1. Install [NTP]({{<ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time" >}}) on the server, if not already installed. Servers must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

```
root@ubuntu:~# sudo apt-get install ntp
```

2. Configure the network time server.

   {{< tabs "TabID0" >}}

{{< tab "Use NTP Configuration File" >}}

   1. Open the `/etc/ntp.conf` file in your text editor of choice.

   2. Under the *Server* section, specify the NTP server IP address or hostname.

   3. Enable and start the NTP service.

       ```
       root@ubuntu:~# sudo systemctl enable ntp
       root@ubuntu:~# sudo systemctl start ntp
       ```

   {{%notice tip%}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (`ntp@<vrf-name>` versus just `ntp`) in the above commands.
   {{%/notice%}}

   4. Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock is synchronized.

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

          root@ubuntu:~# sudo apt install chrony

   2. Start the chrony service.

          root@ubuntu:~# sudo /usr/local/sbin/chronyd

   3. Verify it installed successfully.

          root@ubuntu:~# chronyc activity
          200 OK
          8 sources online
          0 sources offline
          0 sources doing burst (return to online)
          0 sources doing burst (return to offline)
          0 sources with unknown address

   4. View the time servers chrony is using.

          root@ubuntu:~# chronyc sources
          210 Number of sources = 8

          MS Name/IP address         Stratum Poll Reach LastRx Last sample
          ===============================================================================
          ^+ golem.canonical.com           2   6   377    39  -1135us[-1135us] +/-   98ms
          ^* clock.xmission.com            2   6   377    41  -4641ns[ +144us] +/-   41ms
          ^+ ntp.ubuntu.net              2   7   377   106   -746us[ -573us] +/-   41ms
          ...

      Open the *chrony.conf* configuration file (by default at */etc/chrony/*) and edit if needed.

      Example with individual servers specified:

          server golem.canonical.com iburst
          server clock.xmission.com iburst
          server ntp.ubuntu.com iburst
          driftfile /var/lib/chrony/drift
          makestep 1.0 3
          rtcsync

      Example when using a pool of servers:

          pool pool.ntp.org iburst
          driftfile /var/lib/chrony/drift
          makestep 1.0 3
          rtcsync

   5. View the server chrony is currently tracking.

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

{{< /tab >}}

{{< /tabs >}}

### Obtain NetQ Agent Software Package

To install the NetQ Agent you need to install `netq-agent` on each server. This is available from the Cumulus Networks repository.

To obtain the NetQ Agent package:

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

    {{%notice note%}}
The use of `netq-latest` in these examples means that a `get` to the repository always retrieves the latest version of NetQ, even in the case where a major version update has been made. If you want to keep the repository on a specific version - such as `netq-2.3` - use that instead.
{{%/notice%}}

## Install NetQ Agent on an Ubuntu Server

After completing the preparation steps, you can successfully install the agent software onto your server.

To install the NetQ Agent:

1. Install the software packages on the server.

    ```
    root@ubuntu:~# sudo apt-get update
    root@ubuntu:~# sudo apt-get install netq-agent
    ```

2. Verify you have the correct version of the Agent.

    ```
    root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    You should see version 2.4.1 and update 26 in the results. For example:

    - netq-agent_2.4.1-ub18.04u26~1581351889.c5ec3e5_amd64.deb, or
    - netq-agent_2.4.1-ub16.04u26~1581350451.c5ec3e5_amd64.deb

3. Restart `rsyslog` so log files are sent to the correct destination.

    ```
    root@ubuntu:~# sudo systemctl restart rsyslog.service
    ```

4. Continue with NetQ Agent Configuration in the next section.

## Configure the NetQ Agent on an Ubuntu Server

After the NetQ Agents have been installed on the servers you want to monitor, the NetQ Agents must be configured to obtain useful and relevant data. Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the device, or
- Use the NetQ CLI.

### Configure the NetQ Agents Using a Configuration File

You can configure the NetQ Agent in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

    ```
    root@ubuntu:~# sudo nano /etc/netq/netq.yml
    ```

2. Locate the *netq-agent* section, or add it.

3. Set the parameters for the agent as follows:
    - port: 31980 (default) or one that you specify
    - server: IP address of the NetQ server or appliance where the agent should send its collected data
    - vrf: default (default) or one that you specify

    Your configuration should be similar to this:

    ```
    netq-agent:
        port: 31980
        server: 127.0.0.1
        vrf: default
    ```

### Configure NetQ Agents Using the NetQ CLI

If the CLI is configured, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Server or Appliance. If it is not configured, refer to {{<link title="Install and Configure the NetQ CLI on Ubuntu Servers#configure-the-netq-cli-on-an-ubuntu-server" text="Configure the NetQ CLI on an Ubuntu Server">}} and then return here.

{{%notice info%}}
If you intend to use VRF, skip to {{<link url="#configure-the-netq-agent-to-use-a-vrf" text="Configure the Agent to Use VRF">}}. If you intend to specify a port for communication, skip to {{<link url="#configure-the-netq-agent-to-communicate-over-a-specific-port" text="Configure the Agent to Communicate over a Specific Port">}}.
{{%/notice%}}

Use the following command to configure the NetQ Agent:

```
netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
```

This example uses an IP address of *192.168.1.254* and the default port and VRF for the NetQ hardware.

```
root@ubuntu:~# sudo netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
root@ubuntu:~# sudo netq config restart agent
```

## Configure Advanced NetQ Agent Settings

A couple of additional options are available for configuring the NetQ Agent. If you are using VRF, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the NetQ Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ Agents to communicate with the NetQ Platform only via a [VRF]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF" >}}), including a [management VRF]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Management-VRF" >}}). To do so, you need to specify the VRF name when configuring the NetQ Agent. For example, if the management VRF is configured and you want the agent to communicate with the NetQ Platform over it, configure the agent like this:

```
root@ubuntu:~# sudo netq config add agent server 192.168.1.254 vrf mgmt
root@ubuntu:~# sudo netq config restart agent
```

### Configure the NetQ Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ Platform and NetQ Agents. If you want the NetQ Agent to communicate with the NetQ Platform via a different port, you need to specify the port number when configuring the NetQ Agent like this:

```
root@ubuntu:~# sudo netq config add agent server 192.168.1.254 port 7379
root@ubuntu:~# sudo netq config restart agent
```
