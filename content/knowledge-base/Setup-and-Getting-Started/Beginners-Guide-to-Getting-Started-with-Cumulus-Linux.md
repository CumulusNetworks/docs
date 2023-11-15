---
title: Beginners Guide to Getting Started with Cumulus Linux
author: NVIDIA
weight: 103
toc: 3
---

This simple document provides a checklist for users like network administrators, who might be new to Linux itself, or just to Cumulus Linux specifically. Refer to this list when you power on your Cumulus Linux switch for the first time. It links to Cumulus Linux technical documentation, other knowledge base articles, and to external sites, and covers topics like configuration, comparing Cumulus Linux to other vendors' CLI, and validated design guides.

## Adding and Managing User Accounts

1.  Learn about [user accounts]({{<ref "/cumulus-linux-43/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts" >}})
3.  [Use sudo to delegate privileges]({{<ref "/cumulus-linux-43/System-Configuration/Authentication-Authorization-and-Accounting/Using-sudo-to-Delegate-Privileges" >}})
4.  [What is the default password in Cumulus Linux?]({{<ref "/knowledge-base/Setup-and-Getting-Started/Default-User-Name-and-Password-in-Cumulus-Linux" >}})
5.  Optional: Configure LDAP for centralized user management
    - [LDAP authentication and authorization]({{<ref "/cumulus-linux-43/System-Configuration/Authentication-Authorization-and-Accounting/LDAP-Authentication-and-Authorization" >}})
    - [LDAP authentication and authorization with Active Directory]({{<ref "/knowledge-base/Security/Authentication/LDAP-on-Cumulus-Linux-Using-Server-2008-Active-Directory" >}})

## Editing Files in Linux

Learn how to use the nano text editor ([cheat sheet --- external link](http://www.cheatography.com/hkellaway/cheat-sheets/nano-text-editor/))

- Alternative: Learn how to use [vi for beginners]({{<ref "/knowledge-base/Demos-and-Training/Training/vi-for-Beginners" >}})
- Alternative: Learn how to use Zile (emacs light) ([external link](http://www.gnu.org/software/zile/))
- Alternative: Install any other editor by [adding a Debian package]({{<ref "/cumulus-linux-43/Installation-Management/Adding-and-Updating-Packages#add-packages-from-another-repository" >}})

## Customizing the Switch

1.  Initial configuration
    - [Install the Cumulus Linux license]({{<ref "/cumulus-linux-43/Quick-Start-Guide#install-the-license" >}})
    - [Set the hostname and time zone]({{<ref "/cumulus-linux-43/Quick-Start-Guide#configure-the-hostname-and-time-zone" >}})
    - [Define a DNS server]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Management-VRF#management-vrf-and-dns" >}})
    - [Write a message of the day](https://wiki.debian.org/motd)

          cumulus@switch:~$ sudo vi /etc/motd

    - [Configure NTP and clock]({{<ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time" >}})
    - [Configure the management Interface]({{<ref "/cumulus-linux-43/Quick-Start-Guide#wired-ethernet-management" >}})
    - [Add an IP address to loopback interface]({{<ref "/cumulus-linux-43/Quick-Start-Guide#configure-a-loopback-interface" >}})
    - [Configure a DHCP relay agent]({{<ref "/cumulus-linux-42/Layer-1-and-Switch-Ports/DHCP/DHCP-Relays" >}})
2.  Configure [external system logging]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting#send-log-files-to-a-syslog-server" >}})

## ACL/IP Rules

1.  [Cumulus Linux ACL example rules]({{<ref "/cumulus-linux-43/System-Configuration/Netfilter-ACLs#example-configuration" >}})

## Networking with Cumulus Linux

1.  [Configuring and managing network interfaces]({{<ref "/cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management" >}})
2.  [VLAN-aware bridge mode for large-scale layer 2 environments]({{<ref "/cumulus-linux-43/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode" >}})
3.  [Configuring switch port attributes]({{<ref "/cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes" >}})
4.  [Network troubleshooting]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Network-Troubleshooting" >}})

## Monitoring the Switch

- [Monitoring interface administrative state and physical state on Cumulus Linux]({{<ref "/knowledge-base/Configuration-and-Usage/Monitoring/Monitor-Interface-Administrative-State-and-Physical-State-on-Cumulus-Linux" >}})
- [Monitoring interfaces and transceivers using ethtool]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Troubleshooting-Network-Interfaces/Monitoring-Interfaces-and-Transceivers-Using-ethtool" >}})
- [Resource diagnostics using cl-resource-query]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Resource-Diagnostics-Using-cl-resource-query" >}})
- [Monitoring system hardware]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Monitoring-System-Hardware" >}})
- [Monitoring switch hardware using SNMP]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Simple-Network-Management-Protocol-SNMP" >}})
- [Exposing CPU and memory information via SNMP]({{<ref "/knowledge-base/Configuration-and-Usage/Monitoring/Expose-CPU-and-Memory-Information-via-SNMP" >}})
- [Relevant log files in Cumulus Linux]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Monitoring-Best-Practices#logging201787896" >}})
- [Using the NCLU command line utility as a troubleshooting tool]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Network-Troubleshooting/Using-NCLU-to-Troubleshoot-Your-Network-Configuration" >}})

## Installers and Upgrades (Cumulus Linux and Packages)

1.  [Adding and updating packages]({{<ref "/cumulus-linux-43/Installation-Management/Adding-and-Updating-Packages" >}})
2.  [Upgrading Cumulus Linux]({{<ref "/cumulus-linux-43/Installation-Management/Upgrading-Cumulus-Linux" >}})
3.  [What files should to back up when updating Cumulus Linux via image install]({{<ref "/cumulus-linux-43/Installation-Management/Upgrading-Cumulus-Linux#before-you-upgrade" >}})

## Suggested Further Reading

### More Networking On Cumulus Linux

1.  [Manually putting all switch ports into a single VLAN]({{<ref "/cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management#use-globs-for-port-lists" >}})
2.  [Reserved MAC address range for use with Cumulus Linux]({{<ref "/cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG#reserved-mac-address-range" >}})

    - [Reserved range for VRR]({{<ref "/cumulus-linux-43/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP#vrr" >}})

3.  [Link Layer Discovery Protocol LLDP]({{<ref "/cumulus-linux-43/Layer-2/Link-Layer-Discovery-Protocol" >}})
4.  [Bonding - Link Aggregation]({{<ref "/cumulus-linux-43/Layer-2/Bonding-Link-Aggregation" >}})
5.  [MLAG]({{<ref "/cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}})
6.  [Routing]({{<ref "/cumulus-linux-43/Layer-3/Routing" >}})
7.  [Configuring FRRouting]({{<ref "/cumulus-linux-43/Layer-3/FRRouting/Configure-FRRouting" >}})

### General Useful Links

- [Cumulus Linux technical documentation]({{<ref "/cumulus-linux-43" >}})
- [Quick start guide]({{<ref "/cumulus-linux-43/Quick-Start-Guide" >}})
- [Interoperability and conversion guides]({{<ref "/knowledge-base/Demos-and-Training/Interoperability" >}})
- [General license questions]({{<ref "/knowledge-base/Support/Licensing" >}})
- [Release notes for the latest Cumulus Linux version]({{<ref "/cumulus-linux-43/Whats-New/rn" >}})
