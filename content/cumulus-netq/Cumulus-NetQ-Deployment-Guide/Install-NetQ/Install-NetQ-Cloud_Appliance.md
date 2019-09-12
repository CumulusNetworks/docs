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

## Install and Configure the Appliance

After you unbox the appliance, mount it in the rack and connect it to power following the procedures described in your appliance's [user manual](https://www.supermicro.com/manuals/superserver/mini-itx/MNL-2094.pdf). Connect the Ethernet cable to the 10G management port (eth0), then power on the appliance.

{{< figure src="/images/netq/netq-cloud-appl-port-connections.png" >}}

If your network runs DHCP, you can configure Cumulus NetQ and Cumulus Linux over the network. If DHCP isn't enabled, then you configure the appliance using the console cable provided.

## Download the NetQ Cloud Software

1. On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.

2. Click *2.2* from the **Version** list box, and then select *2.2.x* from the submenu.

      **Note**: You must choose 2.2.x. Earlier versions do not support this appliance.

      {{< figure src="/images/netq/NetQ-22-Download-Options-v2.png" width="500" >}}

3. Select *Appliance (Cloud)* from the **Hypervisor/Platform** list box.

      {{< figure src="/images/netq/NetQ-Cloud-Appl-SW-Dwnld-v2.png" width="250" >}}

4. Click **Upgrade** to download the installer bundle.

      **Note**: The download option only provides the OS which is pre-installed on the appliance.

## Log In and Configure the Appliance

1. Power on the appliance and log in using the default credentials:

   - **Username**: *cumulus*
   - **Password**: *CumulusLinux!*

2. Change your password for the cumulus account using the `passwd` command.

   ```
   cumulus@netq-appliance:~$ passwd
   ```

3. The appliance's default hostname is *cumulus*. You can change it using the Cumulus Linux Network Command Line Utility (NCLU):

   ```
   cumulus@netq-appliance:~$ net add hostname NEW_HOSTNAME
   ```

4. Copy the downloaded package (*NetQ-2.2.x-opta.tgz*) into the */mnt/installables/* directory.

      **Note**: The name of the package needs to be replaced with the exact version you have downloaded. Instead of 2.2.x, you would enter 2.2.1 for example.

      ```
      cumulus@netq-appliance:~$ sudo cp /home/usr/dir/NetQ-2.2.x-opta.tgz /mnt/installables/
      ```
5. Identify the IP address and interface where NetQ Agents should send the telemetry data collected from your monitored switches and hosts.

   - If you are using a dynamic address (DHCP), you can view the IP address assigned to the appliance using the Cumulus Linux Network Command Line Utility (NCLU):

      ```
      cumulus@netq-appliance:~$ net show interface eth0
      Name  MAC                Speed  MTU   Mode
      --  ----  -----------------  -----  ----  ----
      UP  eth0  fc:1f:6b:81:2b:62  1G     1500  Mgmt

      IP Details
      -------------------------  ---------------
      IP:                        192.0.2.42/24
      IP Neighbor(ARP) Entries:  4
      ...
      ```
   - If you want to use a static IP address and interface, use the following NCLU command:

      ```
      cumulus@netq-appliance:~$ net add interface eth0 address 192.0.2.42/24</pre>
      ```

         **Note**: The example here uses eth0 as the interface, but you could use eth1 instead.

6. Review and commit your changes:

   ```
   cumulus@netq-appliance:~$ net pending
   cumulus@netq-appliance:~$ net commit
   ```

## Install the NetQ software

1. Install the software using the interface you defined in the previous step and your config-key. The config-key was provided to you by Cumulus Networks via an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new).

      **Note**: In the following examples, be sure to replace the interface and key values with values appropriate for your configuration. These examples use eth0 and a sample key.

      <details><summary><span style="color:teal">NetQ v2.2.0</span></summary>

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

      <details><summary><span style="color:teal">NetQ v2.2.1</span></summary>

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

2. Verify all applications and services are operating properly.

   ```
   cumulus@<netq-appliance-hostname>:~$ netq show opta-health
   OPTA is healthy
   ```

{{%notice info%}}

If you changed the IP address or interface of the appliance to something other than what it was assigned previously, you must inform NetQ of the change.

If you changed the IP address, but kept the interface the same (for example, eth0), re-run the `netq install opta interface` command using your config-key:

```
cumulus@netq-appliance:~$ netq install opta interface eth0 tarball NetQ-2.2.x-opta.tgz key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

If you changed the interface (for example, eth0 to eth1), run the `netq install opta interface` command with the new interface and your config-key:

```
cumulus@netq-appliance:~$ netq install opta interface eth1 tarball NetQ-2.2.x-opta.tgz key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

{{%/notice%}}

### Configure CLI Access

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

In version 2.2.1, you can save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can store this file wherever you like, give it a name, such as, *credentials.yml*, and make sure it has the following format:
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
   - In NetQ 2.2.1, if you have created a *credentials.yml* file as noted in the previous step, run the following commands. Be sure to include the full path the to file.
   ```
   cumulus@netq-appliance:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-appliance:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```
With your NetQ cloud server now set up and configured, you are ready to install the NetQ Agent on each switch and host you want to monitor with NetQ. Follow the instructions in [Install the NetQ Agent and CLI on Switches](../Install-NetQ-Agents-and-CLI-on-Switches) for details.

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
