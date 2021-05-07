---
title: Beginners Guide to Getting Started with Cumulus Linux
author: NVIDIA
weight: 103
toc: 3
---

This simple document provides a checklist for users like network administrators, who may be new to Linux in general, or Cumulus Linux specifically. Refer to this list when you power on your Cumulus Linux switch for the first time. It links to Cumulus Linux technical documentation, other knowledge base articles, and to external sites, and covers topics like configuration, comparing Cumulus Linux to other vendors' CLI, and validated design guides.

## Adding and Managing User Accounts

1.  Learn about {{<kb_link url="cumulus-linux-43/System-Configuration/Authentication,-Authorization-and-Accounting/User-Accounts/" text="user accounts" >}}
3.  {{<kb_link url="cumulus-linux-43/System-Configuration/Authentication,-Authorization-and-Accounting/Using-sudo-to-Delegate-Privileges/" text="Use sudo to delegate privileges" >}}
4.  {{<kb_link url="knowledge-base/Setup-and-Getting-Started/Default-User-Name-and-Password-in-Cumulus-Linux/" text="What is the default password in Cumulus Linux?" >}}
5.  Optional: Configure LDAP for centralized user management
    - {{<kb_link url="cumulus-linux-43/System-Configuration/Authentication,-Authorization-and-Accounting/LDAP-Authentication-and-Authorization/" text="LDAP authentication and authorization" >}}
    - {{<kb_link url="knowledge-base/Security/Authentication/LDAP-on-Cumulus-Linux-Using-Server-2008-Active-Directory/" text="LDAP authentication and authorization with Active Directory" >}}

## Editing Files in Linux

Learn how to use the nano text editor ([cheat sheet --- external link](http://www.cheatography.com/hkellaway/cheat-sheets/nano-text-editor/))

- Alternative: Learn how to use {{<kb_link url="knowledge-base/Demos-and-Training/Training/vi-for-Beginners/" text="vi for beginners" >}}
- Alternative: Learn how to use Zile (emacs light) ([external link](http://www.gnu.org/software/zile/))
- Alternative: Install any other editor by {{<kb_link url="cumulus-linux-43/Installation-Management/Adding-and-Updating-Packages/#add-packages-from-another-repository" text="adding a Debian package" >}}

## Customizing the Switch

1.  Initial configuration
    - {{<kb_link url="cumulus-linux-43/Quick-Start-Guide/#install-the-license" text="Install the Cumulus Linux license" >}}
    - {{<kb_link url="cumulus-linux-43/Quick-Start-Guide/#configure-the-hostname-and-time-zone" text="Set the hostname and time zone" >}}
    - {{<kb_link url="cumulus-linux-43/Layer-3/VRFs/Management-VRF/#management-vrf-and-dns" text="Define a DNS server" >}}
    - [Write a message of the day](https://wiki.debian.org/motd)

          cumulus@switch:~$ sudo vi /etc/motd

    - {{<kb_link url="cumulus-linux-43/System-Configuration/Setting-Date-and-Time/" text="Configure NTP and clock" >}}
    - {{<kb_link url="cumulus-linux-43/Quick-Start-Guide/#wired-ethernet-management" text="Configure the management Interface" >}}
    - {{<kb_link url="cumulus-linux-43/Quick-Start-Guide/#configure-a-loopback-interface" text="Add an IP address to loopback interface" >}}
    - {{<kb_link url="cumulus-linux-42/Layer-1-and-Switch-Ports/DHCP/DHCP-Relays/" text="Configure a DHCP relay agent" >}}
2.  Configure {{<kb_link url="cumulus-linux-43/Monitoring-and-Troubleshooting/#send-log-files-to-a-syslog-server" text="external system logging" >}}

## ACL/IP Rules

1.  {{<kb_link url="cumulus-linux-43/System-Configuration/Netfilter-ACLs/#example-configuration" text="Cumulus Linux ACL example rules" >}}

## Networking with Cumulus Linux

1.  {{<kb_link url="cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/" text="Configuring and managing network interfaces" >}}
2.  {{<kb_link url="cumulus-linux-43/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode/" text="VLAN-aware bridge mode for large-scale layer 2 environments" >}}
3.  {{<kb_link url="cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/" text="Configuring switch port attributes" >}}
4.  {{<kb_link url="cumulus-linux-43/Monitoring-and-Troubleshooting/Network-Troubleshooting/" text="Network troubleshooting" >}}

## Monitoring the Switch

- {{<kb_link url="knowledge-base/Configuration-and-Usage/Monitoring/Monitor-Interface-Administrative-State-and-Physical-State-on-Cumulus-Linux/" text="Monitoring interface administrative state and physical state on Cumulus Linux" >}}
- {{<kb_link url="cumulus-linux-43/Monitoring-and-Troubleshooting/Troubleshooting-Network-Interfaces/Monitoring-Interfaces-and-Transceivers-Using-ethtool/" text="Monitoring interfaces and transceivers using ethtool" >}}
- {{<kb_link url="cumulus-linux-43/Monitoring-and-Troubleshooting/Resource-Diagnostics-Using-cl-resource-query/" text="Resource diagnostics using cl-resource-query" >}}
- {{<kb_link url="cumulus-linux-43/Monitoring-and-Troubleshooting/Monitoring-System-Hardware/" text="Monitoring system hardware" >}}
- {{<kb_link url="cumulus-linux-43/Monitoring-and-Troubleshooting/Simple-Network-Management-Protocol-SNMP/" text="Monitoring switch hardware using SNMP" >}}
- {{<kb_link url="knowledge-base/Configuration-and-Usage/Monitoring/Expose-CPU-and-Memory-Information-via-SNMP/" text="Exposing CPU and memory information via SNMP" >}}
- {{<kb_link url="cumulus-linux-43/Monitoring-and-Troubleshooting/Monitoring-Best-Practices/#logging201787896" text="Relevant log files in Cumulus Linux" >}}
- {{<kb_link url="cumulus-linux-43/Monitoring-and-Troubleshooting/Network-Troubleshooting/Using-NCLU-to-Troubleshoot-Your-Network-Configuration/" text="Using the NCLU command line utility as a troubleshooting tool" >}}

## Installers and Upgrades (Cumulus Linux and Packages)

1.  {{<kb_link url="cumulus-linux-43/Installation-Management/Adding-and-Updating-Packages/" text="Adding and updating packages" >}}
2.  {{<kb_link url="cumulus-linux-43/Installation-Management/Upgrading-Cumulus-Linux/" text="Upgrading Cumulus Linux" >}}
3.  {{<kb_link url="cumulus-linux-43/Installation-Management/Upgrading-Cumulus-Linux/#before-you-upgrade" text="What files should I back up when updating Cumulus Linux via image install?" >}}

## Suggested Further Reading

### More Networking On Cumulus Linux

1.  {{<kb_link url="cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/#use-globs-for-port-lists" text="Manually putting all switch ports into a single VLAN" >}}
2.  {{<kb_link url="cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/#reserved-mac-address-range" text="Reserved MAC address range for use with Cumulus Linux" >}}

    - {{<kb_link url="cumulus-linux-43/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP/#vrr" text="Reserved range for VRR" >}}

3.  {{<kb_link url="cumulus-linux-43/Layer-2/Link-Layer-Discovery-Protocol/" text="Link Layer Discovery Protocol LLDP" >}}
4.  {{<kb_link url="cumulus-linux-43/Layer-2/Bonding-Link-Aggregation/" text="Bonding - Link Aggregation" >}}
5.  {{<kb_link url="cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/" text="MLAG" >}}
6.  {{<kb_link url="cumulus-linux-43/Layer-3/Routing/" text="Routing" >}}
7.  {{<kb_link url="cumulus-linux-43/Layer-3/FRRouting/Configure-FRRouting" text="Configuring FRRouting" >}}

### General Useful Links

- {{<kb_link url="cumulus-linux-43/" text="Cumulus Linux technical documentation" >}}
- {{<kb_link url="cumulus-linux-43/Quick-Start-Guide/" text="Quick start guide" >}}
- {{<kb_link url="knowledge-base/Demos-and-Training/Interoperability/" text="Interoperability and conversion guides" >}}
- {{<kb_link url="knowledge-base/Support/Licensing/" text="General license questions" >}}
- {{<kb_link url="cumulus-linux-43/Whats-New/rn/" text="Release notes for the latest Cumulus Linux version" >}}
