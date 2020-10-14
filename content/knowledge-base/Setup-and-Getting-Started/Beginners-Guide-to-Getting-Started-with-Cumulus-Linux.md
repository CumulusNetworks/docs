---
title: Beginners Guide to Getting Started with Cumulus Linux
author: Cumulus Networks
weight: 103
toc: 3
---

This simple document provides a checklist for users like network administrators, who may be new to Linux in general, or Cumulus Linux specifically. Refer to this list when you power on your Cumulus Linux switch for the first time. It links to Cumulus Linux technical documentation, other knowledge base articles, and to external sites, and covers topics like configuration, comparing Cumulus Linux to other vendors' CLI, and validated design guides.

## Adding and Managing User Accounts

1.  Learn about [user accounts](https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts/)
3.  [Use sudo to delegate privileges](https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/Using-sudo-to-Delegate-Privileges/)
4.  [What is the default password in Cumulus Linux?](https://docs.cumulusnetworks.com/knowledge-base/Setup-and-Getting-Started/Default-User-Name-and-Password-in-Cumulus-Linux/)
5.  Optional: Configure LDAP for centralized user management
    - [LDAP authentication and authorization](https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/LDAP-Authentication-and-Authorization/)
    - [LDAP authentication and authorization with Active Directory](https://docs.cumulusnetworks.com/knowledge-base/Security/Authentication/LDAP-on-Cumulus-Linux-Using-Server-2008-Active-Directory/)

## Editing Files in Linux

Learn how to use the nano text editor ([cheat sheet --- external link](http://www.cheatography.com/hkellaway/cheat-sheets/nano-text-editor/))

- Alternative: Learn how to use [vi for beginners](https://docs.cumulusnetworks.com/knowledge-base/Demos-and-Training/Training/vi-for-Beginners/)
- Alternative: Learn how to use Zile (emacs light) ([external link](http://www.gnu.org/software/zile/))
- Alternative: Install any other editor by [adding a Debian package](https://docs.cumulusnetworks.com/cumulus-linux/Installation-Management/Adding-and-Updating-Packages/#add-packages-from-another-repository)

## Customizing the Switch

1.  Initial configuration
    - [Install the Cumulus Linux license](https://docs.cumulusnetworks.com/cumulus-linux/Quick-Start-Guide/#install-the-license)
    - [Set the hostname and time zone](https://docs.cumulusnetworks.com/cumulus-linux/Quick-Start-Guide/#configure-the-hostname-and-timezone)
    - [Define a DNS server](https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Management-VRF/#management-vrf-and-dns)
    - [Write a message of the day](https://wiki.debian.org/motd)

          cumulus@switch:~$ sudo vi /etc/motd

    - [Configure NTP and clock](https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Setting-Date-and-Time/)
    - [Configure the management Interface](https://docs.cumulusnetworks.com/cumulus-linux/Quick-Start-Guide/#wired-ethernet-management)
    - [Add an IP address to loopback interface](https://docs.cumulusnetworks.com/cumulus-linux/Quick-Start-Guide/#configure-a-loopback-interface)
    - [Configure a DHCP relay agent](https://docs.cumulusnetworks.com/cumulus-linux-42/Layer-1-and-Switch-Ports/DHCP/DHCP-Relays/)
2.  Configure [external system logging](https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/#send-log-files-to-a-syslog-server)

## ACL/IP Rules

1.  [Allow SSH from specific subnets only](https://support.cumulusnetworks.com/hc/en-us/community/posts/203381337-I-want-to-only-allow-SSH-from-specific-subnets-how-can-I-do-this-)
2.  [[Cumulus Linux ACL example rules](https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Netfilter-ACLs/#example-configuration)

## Networking with Cumulus Linux

1.  [Configuring and managing network interfaces](https://docs.cumulusnetworks.com/cumulus-linux/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/)
2.  [VLAN-aware bridge mode for large-scale layer 2 environments](https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode/)
3.  [Configuring switch port attributes](https://docs.cumulusnetworks.com/cumulus-linux/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/)
4.  [Network troubleshooting](https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Network-Troubleshooting/)

## Monitoring the Switch

- [Monitoring interface administrative state and physical state on Cumulus Linux](https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Monitoring/Monitor-Interface-Administrative-State-and-Physical-State-on-Cumulus-Linux/)
- [Monitoring interfaces and transceivers using ethtool](https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Troubleshooting-Network-Interfaces/Monitoring-Interfaces-and-Transceivers-Using-ethtool/)
- [Resource diagnostics using cl-resource-query](https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Resource-Diagnostics-Using-cl-resource-query/)
- [Monitoring system hardware](https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Monitoring-System-Hardware/)
- [Monitoring switch hardware using SNMP](https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Simple-Network-Management-Protocol-SNMP/)
- [Exposing CPU and memory information via SNMP](https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Monitoring/Expose-CPU-and-Memory-Information-via-SNMP/)
- [Relevant log files in Cumulus Linux](https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Monitoring-Best-Practices/#logging201787896)
- [Using the NCLU command line utility as a troubleshooting tool](https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Network-Troubleshooting/Using-NCLU-to-Troubleshoot-Your-Network-Configuration/)

## Installers and Upgrades (Cumulus Linux and Packages)

1.  [Adding and updating packages](https://docs.cumulusnetworks.com/cumulus-linux/Installation-Management/Adding-and-Updating-Packages/)
2.  [Upgrading Cumulus Linux](https://docs.cumulusnetworks.com/cumulus-linux/Installation-Management/Upgrading-Cumulus-Linux/)
3.  [What files should I back up when updating Cumulus Linux via image install?](https://docs.cumulusnetworks.com/cumulus-linux/Installation-Management/Upgrading-Cumulus-Linux/#before-you-upgrade)

## Suggested Further Reading

### More Networking On Cumulus Linux

1.  [Manually putting all switch ports into a single VLAN](https://docs.cumulusnetworks.com/cumulus-linux/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/#use-globs-for-port-lists)
2.  [Reserved MAC address range for use with Cumulus Linux](https://docs.cumulusnetworks.com/cumulus-linux-42/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/#reserved-mac-address-range)

    - [Reserved range for VRR](https://docs.cumulusnetworks.com/cumulus-linux-42/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP/#vrr)

3.  [Network topology](https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Network-Topology/)
4.  [Link Layer Discovery Protocol LLDP](https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/)
5.  [Bonding - Link Aggregation](https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Bonding-Link-Aggregation/)
6.  [MLAG](https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/)
7.  [Routing](https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Routing/)
8.  [Configuring FRRouting](https://docs.cumulusnetworks.com/cumulus-linux/Layer-3/Configuring-FRRouting/)

### General Useful Links

- [Cumulus Linux technical documentation](https://docs.cumulusnetworks.com/cumulus-linux/)
- [Quick start guide](https://docs.cumulusnetworks.com/cumulus-linux/Quick-Start-Guide/)
- [Interoperability and conversion guides](https://docs.cumulusnetworks.com/knowledge-base/Demos-and-Training/Interoperability/)
- [General license questions](https://docs.cumulusnetworks.com/knowledge-base/Support/Licensing/)
- [Release notes for the latest Cumulus Linux version](https://docs.cumulusnetworks.com/cumulus-linux/Whats-New/rn/)

### Cumulus Networks Validated Design Guides

- [Big Data Validated Design](https://cumulusnetworks.com/media/cumulus/pdf/technical/validated-design-guides/Big-Data-Cumulus-Linux-Validated-Design-Guide.pdf)[\
    ](https://cumulusnetworks.com/media/cumulus/pdf/technical/validated-design-guides/Big-Data-Cumulus-Linux-Validated-Design-Guide.pdf)
- [OpenStack Validated Design](https://cumulusnetworks.com/media/cumulus/pdf/technical/validated-design-guides/OpenStack-Cumulus-Linux-Validated-Design-Guide.pdf)
- [VMware VSphere Validated Design](https://cumulusnetworks.com/media/cumulus/pdf/technical/validated-design-guides/VMware-vSphere-Cumulus-Linux-Validated-Design-Guide.pdf)
