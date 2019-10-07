---
title: Install the Cumulus NetQ Cloud Appliance
author: Cumulus Networks
weight: 413
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
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

Download and install the tarball file. The config-key was provided to you by Cumulus Networks via an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new) to have it sent to you again.

**Note**: Be sure to replace the interface and key values with values appropriate for your configuration. This example uses eth0 and a sample key.

```
cumulus@netq-appliance:~$ netq install opta interface eth0 tarball download config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

{{%notice info%}}

If you changed the IP address or interface of the appliance to something other than what it was assigned previously, you must inform NetQ of the change.

If you changed the IP address, but kept the interface the same (for example, eth0), re-run the `netq install opta interface` command using your config-key:

```
cumulus@netq-appliance:~$ netq install opta interface eth0 tarball NetQ-2.3.x-opta.tgz config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

If you changed the interface (for example, eth0 to eth1), run the `netq install opta interface` command with the new interface and your config-key:

```
cumulus@netq-appliance:~$ netq install opta interface eth1 tarball NetQ-2.3.x-opta.tgz config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
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
cumulus@netq-appliance:~$ netq show opta-health
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

In version 2.2.1 and later, you can save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can:

- store the file wherever you like, for example in */home/cumulus/* or */etc/netq*
- name the file whatever you like, for example *credentials.yml*, *creds.yml*, or *keys.yml*

BUT, the file must have the following format:

```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```
      {{%/notice%}}

7. Run the following command using your generated keys:
   - In NetQ 2.3.x, run the following commands. Replace the key values with your generated keys.
   ```
   cumulus@netq-appliance:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-appliance:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```
   - In NetQ 2.2.1 and later, if you have created a keys file as noted in the previous step, run the following commands. Be sure to include the full path the to file.
   ```
   cumulus@netq-appliance:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-appliance:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```
With your NetQ cloud server set up and configured, you are ready to install the NetQ Agent on each switch and host you want to monitor with NetQ. Follow the instructions in [Install NetQ Agents and CLI on Switches](../Install-NetQ-Agents-and-CLI-on-Switches) for details.

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
