---
title: Install the Cumulus NetQ Appliance
author: Cumulus Networks
weight: 411
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
---

The Cumulus NetQ appliance provides a complete monitoring solution for your network; the server comes preloaded with a Cumulus Linux image that includes Cumulus NetQ services, a Cumulus Linux license and certified cables and optics.

This topic helps you get your Cumulus NetQ appliance up and running in a few minutes.

## What's in the Box?

Inside the box that was shipped to you, you'll find:

- Your Cumulus NetQ appliance (a Supermicro 6019P-WTR server) with the Cumulus Linux OS, Cumulus NetQ services and license already installed
- Hardware accessories, such as power cables and rack mounting gear (note that network cables and optics ship separately)
- Information regarding your order

If you're looking for hardware specifications (including LED layouts and FRUs like the power supply or fans and accessories like included cables) or safety and environmental information, check out the [user manual](https://www.supermicro.com/manuals/superserver/1U/MNL-1943.pdf) and [quick reference guide](https://www.supermicro.com/QuickRefs/superserver/1U/QRG-1943.pdf).

## Install Workflow

Install and set up your NetQ Appliance and switch and host Agents using the following steps:

{{< figure src="/images/netq/install-flow-nqappl-on-prem-nq222.png" width="600" >}}

## Install the Appliance

After you unbox the appliance:

1. Mount the appliance in the rack
2. Connect it to power following the procedures described in your appliance's user manual.
3. Connect the Ethernet cable to the 1G management port (eth0).
4. Power on the appliance.

   {{< figure src="/images/netq/netq-appliance-port-connections.png" width="700" >}}

If your network runs DHCP, you can configure Cumulus NetQ and Cumulus Linux over the network. If DHCP is not enabled, then you configure the appliance using the console cable provided.

## Configure the Password, Hostname and IP Address

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

{{%notice info%}}

If you have changed the IP address or hostname of the NetQ Appliance, you need to
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

{{%/notice%}}

With your NetQ cloud server now set up and configured, you are ready to install the NetQ Agent on each switch and host you want to monitor with NetQ. Follow the instructions in [Install the NetQ Agent and CLI on Switches](../Install-NetQ-Agents-and-CLI-on-Switches) for details.

## Intelligent Platform Management Interface - IPMI

The NetQ Appliance comes with Intelligent Platform Management Interface (IPMI). IPMI provides remote access to multiple users at different locations for networking. It also allows a system administrator to monitor system health and manage computer events remotely. For details, please read the [Supermicro IPMI user guide](https://www.supermicro.com/manuals/other/IPMI_Users_Guide.pdf).

## Integrate with Event Notification Tools

If you want to proactively monitor events in your network, you can
integrate NetQ with the PagerDuty or Slack notification tools. To do so
you need to configure both the notification application itself to
receive the messages, and NetQ with what messages to send and where to
send them. Refer to [Integrate NetQ with Notification Applications](../../../Cumulus-NetQ-Integration-Guide/Integrate-NetQ-with-Notification-Applications)
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
