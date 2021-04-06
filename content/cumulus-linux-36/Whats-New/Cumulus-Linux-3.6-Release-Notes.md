---
title: Cumulus Linux 3.6 Release Notes
author: Cumulus Networks
weight: 7
---

These release notes support Cumulus Linux 3.6.0, 3.6.1, and 3.6.2 and describe currently available features and known issues.

## Stay up to Date

- Subscribe to our {{<exlink url="https://lists.cumulusnetworks.com/listinfo/cumulus-product-bulletin" text="product bulletin">}} mailing list to receive important announcements and updates about issues that arise in our products.
- Subscribe to our {{<exlink url="https://lists.cumulusnetworks.com/listinfo/cumulus-security-announce" text="security announcement">}} mailing list to receive alerts whenever we update our software for security issues.

## What's New in Cumulus Linux 3.6.2

Cumulus Linux 3.6.2 contains the following new features, platforms, and improvements:

- {{<exlink url="https://cumulusnetworks.com/hcl" text="Facebook Voyager">}} (DWDM) (100G Tomahawk) now generally available
- NCLU commands available for {{<link url="Traditional-Bridge-Mode" text="configuring traditional mode bridges">}}
- {{<link url="Virtual-Routing-and-Forwarding-VRF/#configuring-static-route-leaking-with-evpn" text="VRF static route leaking with EVPN">}} symmetric routing
- New {{<link url="Virtual-Routing-and-Forwarding-VRF/#enabling-vrf-route-leaking" text="vrf_route_leak_enable option">}} used to enable VRF route leaking

## What's New in Cumulus Linux 3.6.2

Cumulus Linux 3.6.1 contains bug fixes and security fixes.

## What's New in Cumulus Linux 3.6.0

Cumulus Linux 3.6.0 contains a number of new platforms, features and improvements:

- New {{<exlink url="https://cumulusnetworks.com/hcl" text="platforms">}} include:
    - Dell S4128T-ON (10GBASE-T Maverick)
    - Dell S5048-ON (25G Tomahawk+)
    - Delta AG-5648v1 (25G Tomahawk+)
    - Edgecore AS7312-54XS (Tomahawk+)
    - Facebook Voyager (100G Tomahawk/DWDM) Early Access
    - Penguin Arctica 1600CS (100G Spectrum)
    - Penguin Arctica 3200CS (100G Spectrum)
    - Penguin Arctica 4808X (10G Spectrum)
- {{<link url="Policy-based-Routing" text="Policy-based routing">}}
- {{<link url="Virtual-Routing-and-Forwarding-VRF/#vrf-route-leaking" text="VRF route leaking">}}
- {{<link url="Setting-Date-and-Time/#precision-time-protocol-ptp-boundary-clock" text="PTP boundary clock">}} on Mellanox switches
- {{<link url="GRE-Tunneling" text="GRE tunneling">}} on Mellanox switches
- New {{<link url="#rn873" text="ports.conf file validator">}} finds syntax errors and provides a reason for each invalid line. Error messages are shown when you run the `net commit` command.
- Support for the combination of the `local-as` and `allowas-in` commands
- OSPFv3 enhancements:
    - Validated interoperability with other routers at a scale of 120 neighbors
    - New NCLU commands to configure {{<link url="Open-Shortest-Path-First-v3-OSPFv3-Protocol/#configuring-the-ospfv3-area" text="OSPFv3">}}
- EVPN Enhancements:
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#evpn-type-5-routing-with-asymmetric-routing" text="Type-5 routes with asymmetric routing">}}
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#originating-default-evpn-type-5-routes" text="Originate default EVPN type-5 routes">}}
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#filtering-evpn-routes-based-on-type" text="Filter EVPN routes based on type">}}
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#controlling-which-rib-routes-are-injected-into-evpn" text="Control which RIB routes are injected into EVPN">}}
- Cumulus Linux 3.6 is the last release to support Quanta IX2 (25G Tomahawk)

## Licensing

Cumulus Linux is licensed on a per-instance basis. Each network system
is fully operational, enabling any capability to be utilized on the
switch with the exception of forwarding on switch panel ports. Only eth0
and console ports are activated on an un-licensed instance of Cumulus
Linux. Enabling front panel ports requires a license.

You should have received a license key from Cumulus Networks or an
authorized reseller. To install the license, read the {{<link url="Quick-Start-Guide">}}.

## Installing Version 3.6

If you are upgrading from version 3.0.0 or later, use {{<exlink url="https://wiki.debian.org/apt-get" text="apt-get">}} to update the software.

Cumulus Networks recommends you use the `-E` option with `sudo` whenever
you run any `apt-get` command. This option preserves your environment
variables, such as HTTP proxies, before you install new packages or
upgrade your distribution.

1.  Retrieve the new version packages: `cumulus@switch:~$ sudo -E apt-get update`
2.  If you are using any {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Support/Support-Offerings/Early-Access-Features-Defined/" text="early access features">}} from an older release, remove them with: `cumulus@switch:~$ sudo -E apt-get remove EA_PACKAGENAME`
3.  Upgrade the release: `cumulus@switch:~$ sudo -E apt-get upgrade`
4.  To include additional Cumulus Linux packages not present in your current version, run the command: `cumulus@switch:~$ apt-get install nclu hostapd python-cumulus-restapi linuxptp` 

    If you already have the latest version of a package installed, you see messages similar to: `nclu is already the newest version`. You might also see additional packages being installed due to dependencies.
5.  Reboot the switch: `cumulus@switch:~$ sudo reboot`

{{%notice note%}}

If you see errors for expired GPG keys that prevent you from upgrading packages when upgrading to Cumulus Linux 3.6 from 3.5.1 or earlier, follow the steps in {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Installing-and-Upgrading/Upgrading/Update-Expired-GPG-Keys/" text="Upgrading Expired GPG Keys">}}.

{{%/notice%}}

{{%notice note%}}

In Cumulus Linux 3.6.0, the upgrade process has changed. During an upgrade to 3.6.0 from 3.5 or earlier, certain services might be stopped. These services are not restarted until after the switch reboots, which results in some functionality being lost during the upgrade process.

{{%/notice%}}

During the upgrade, you will see messages similar to the following:

    /usr/sbin/policy-rc.d returned 101, not running 'stop switchd.service'
    /usr/sbin/policy-rc.d returned 101, not running 'start switchd.service'

At the end of the upgrade, if a reboot is required, you see the following message:

    *** Caution: Service restart prior to reboot could cause unpredictable behavior
    *** System reboot required ***

**Do not restart services manually until after rebooting**, or services will fail.

For upgrades post 3.6.0, if no reboot is required after the upgrade completes, the upgrade will stop and restart all upgraded services and will log messages in the `/var/log/syslog` file similar to the ones shown below. (In the examples below, only the `frr` package was upgraded.)

    Policy: Service frr.service action stop postponed
    Policy: Service frr.service action start postponed
    Policy: Restarting services: frr.service
    Policy: Finished restarting services
    Policy: Removed /usr/sbin/policy-rc.d
    Policy: Upgrade is finished

For additional information about upgrading, see {{<link url="Upgrading-Cumulus-Linux" text="Upgrading Cumulus Linux">}}.

### New Install or Upgrading from Versions Older than 3.0.0

If you are upgrading from a version older than 3.0.0, or installing
Cumulus Linux for the first time, download the {{<exlink url="https://support.mellanox.com/s/" text="Cumulus Linux 3.6.0 installer">}} for Broadcom or Mellanox switches from the Cumulus Networks website, then use {{<exlink url="http://onie.github.io/onie/" text="ONIE">}} to perform a complete install, following the instructions in the {{<link url="Quick-Start-Guide">}}.

{{%notice note%}}

This method is **destructive**; any configuration files on the switch are **not** saved; copy them to a different server before upgrading via ONIE.

{{%/notice%}}

{{%notice note%}}

After you install, run `apt-get update`, then `apt-get upgrade` on your switch to make sure you update Cumulus Linux to include any important or other package updates.

{{%/notice%}}

### Updating a Deployment that Has MLAG Configured

If you are using {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} to dual connect two switches in your environment, and those switches are still running Cumulus Linux 2.5 ESR or any other release earlier than 3.0.0, the switches will not be dual-connected after you upgrade the first switch. To ensure a smooth upgrade, follow these steps:

1.  Disable `clagd` in the `/etc/network/interfaces` file (set `clagd-enable` to *no*), then restart the `switchd`, networking, and FRR services.  

        cumulus@switch:~$ sudo systemctl restart switchd.service
        cumulus@switch:~$ sudo systemctl restart networking.service
        cumulus@switch:~$ sudo systemctl restart frr.service

2.  If you are using BGP, notify the BGP neighbors that the switch is going down:  

        cumulus@switch:~$ sudo vtysh -c "config t" -c "router bgp" -c "neighbor X.X.X.X shutdown"

3.  Stop the Quagga (if upgrading from a version earlier than 3.2.0) or
    FRR service (if upgrading from version 3.2.0 or later):  

        cumulus@switch:~$ sudo systemctl stop [quagga|frr].service 

4.  Bring down all the front panel ports:  

        cumulus@switch:~$ sudo ip link set swp<#> down

5.  Run `cl-img-select -fr` to boot the switch in the secondary role
    into ONIE, then reboot the switch.

6.  Install Cumulus Linux 3.6 onto the secondary switch using ONIE. At
    this time, all traffic is going to the switch in the primary role.

7.  After the install, copy the license file and all the {{<link url="Upgrading-Cumulus-Linux" text="configuration files">}} you backed up, then restart the `switchd`, networking, and Quagga services. All traffic is still going to the primary switch.  

        cumulus@switch:~$ sudo systemctl restart switchd.service
        cumulus@switch:~$ sudo systemctl restart networking.service
        cumulus@switch:~$ sudo systemctl restart quagga.service

8.  Run `cl-img-select -fr` to boot the switch in the primary role into ONIE, then reboot the switch. Now, all traffic is going to the switch in the *secondary role* that you just upgraded to version 3.6.

9.  Install Cumulus Linux 3.6 onto the *primary switch* using ONIE.

10. After the install, copy the license file and all the {{<link url="Upgrading-Cumulus-Linux" text="configuration files">}} you backed up.

11. Follow the steps for {{<link url="Upgrading-from-Quagga-to-FRRouting" text="upgrading from Quagga to FRRouting">}}.

12. Enable `clagd` again in the `/etc/network/interfaces` file (set
    `clagd-enable` to *yes*), then run `ifreload -a`.  

        cumulus@switch:~$ sudo ifreload -a

13. Bring up all the front panel ports:  

        cumulus@switch:~$ sudo ip link set swp<#> up

14. Now the two switches are dual-connected again and traffic flows to both switches.

{{%notice warning%}}

**Perl, Python and BDB Modules**

Any Perl scripts that use the `DB_File` module or Python scripts that use the `bsddb` module won't run under Cumulus Linux 3.6.

{{%/notice%}}

## Issues Fixed in Cumulus Linux 3.6.2

The following is a list of issues fixed in Cumulus Linux 3.6.2 from earlier versions of Cumulus Linux.

<table>

<tbody>
<tr class="odd">
<th>Release Note ID</th>
<th>Summary</th>
<th>Description</th>
</tr>
<tr class="even">
<td><span id="RN763"></span> <a href="#RN763"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-763 (CM-16139)</td>
<td>OSPFv3 does not handle ECMP properly</td>
<td><p>IPv6 ECMP is not working as expected in OSPFv3.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN799"></span> <a href="#RN799"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-799 (CM-16493)</td>
<td>No way to configure IPv6 link-local addrgenmode using ifupdown2 or NCLU</td>
<td><p>You cannot use NCLU or <code>ifupdown2</code> to enable or disable of the IPv6 link-local eui-64 format.</p>
<p>To work around this limitation, you can use the following <code>iproute2</code> command:</p>
<pre><code>cumulus@switch:~$ sudo ip link set swpX addrgenmode {eui-64|none}</code></pre>
<p>Note: This command does not persist across a reboot of the switch.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN827"></span> <a href="#RN827"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-827 (CM-14300)</td>
<td>cl-acltool counters for implicit accept do not work for IPv4 on management (ethX) interfaces</td>
<td><p>The iptables are not counting against the default INPUT chain rule for packets ingressing ethX interfaces.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN875"></span> <a href="#RN875"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-875 (CM-20779)</td>
<td>On Mellanox switches, withdrawal of one ECMP next-hop results in the neighbor entry for that next hop to be missing from hardware</td>
<td><p>On a Mellanox switch, when you withdraw one ECMP next hop, the neighbor entry for that next hop is missing from the hardware.</p>
<p>To work around this issue, manually delete the ARP entry from kernel with the <code>arp -d</code> command to repopulate it in the hardware.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="rn880"></span> <a href="#rn880"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-880 (CM-20672)</td>
<td>In Mellanox buffer monitoring, packet statistics per priority ignore priority 7</td>
<td><p>The buffer monitoring tool on Mellanox switches only shows priority 0 thru 6 for the all_packet_pg statistics; priority 7 is not shown.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN882"></span> <a href="#RN882"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-882 (CM-20648)</td>
<td>When using VRF route leaking on a Mellanox switch, forwarded packets are copied to the CPU several times</td>
<td><p>When using VRF Route leaking on Mellanox switches in a VLAN-unaware bridge configuration, the packets for a locally attached leaked host are software forwarded.</p>
<p>To work around this issue, use a VLAN-aware bridge configuration.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN883"></span> <a href="#RN883"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-883 (CM-20644)</td>
<td>If the PTP services are running when switchd is restarted, the PTP services need to be restarted</td>
<td><p>When using PTP and <code>switchd.service</code> is restarted, the PTP services need to be restarted after <code>switchd.service</code> with the following commands:</p>
<pre><code>systemctl reset-failed ptp4l.service phc2sys.service
systemctl restart  ptp4l.service phc2sys.service</code></pre>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN889"></span> <a href="#RN889"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-889 (CM-20450)</td>
<td>Issuing the 'net add routing import-table' command results in an FRR service crash</td>
<td><p>The FRR service crashes when you run the <code>net add routing import-table</code> command.</p>
<p>To work around this issue, do not use the NCLU.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN891"></span> <a href="#RN891"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-891 (CM-20684)</td>
<td>On Mellanox switches, attempts to configure a VRF with a nexthop from another VRF results in an sx_sdk daemon crash and loss of forwarding functionality</td>
<td><p>VRF Route Leaking is not supported on Mellanox platforms in CL 3.6.0. Attempts to configure a VRF with a nexthop from another VRF can result in an <code>sx_sdk</code> daemon crash and loss of forwarding functionality.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN902"></span> <a href="#RN902"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-902 (CM-19699)</td>
<td>BGP scaling not hashing southbound traffic from Infra switches</td>
<td><p>When routing traffic from Infra switches back through VXLAN, Infra switches are choosing one spine to send all flows through.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN947"></span> <a href="#RN947"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-947 (CM-20992)</td>
<td>RS FEC configuration cleared and not re-installed on switchd restart, leaving links down</td>
<td><p>During <code>switchd</code> restart, the RS FEC configuration is not re-installed to the interfaces to which it was previously applied.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN954"></span> <a href="#RN954"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-954 (CM-21062)</td>
<td>Redundant NCLU commands to configure the DHCP relay exits with return code 1</td>
<td><p>When using the NCLU command to add a redundant DHCP relay, the command exits with an error instead of displaying a message that the DHCP relay server configuration already contains the IP address.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN964"></span> <a href="#RN964"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-964 (CM-21319)</td>
<td>When upgrading to Cumulus Linux 3.6, static routes in the default VRF are associated with other VRFs</td>
<td><p>When you upgrade to Cumulus Linux 3.6.x, static routes configured in the <code>frr.conf</code> file become associated with the VRF configured above them.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN966"></span> <a href="#RN966"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-966 (CM-21297)</td>
<td>TACACS authenticated users in 'netshow' or 'netedit' groups cannot issue 'net' commands after upgrade to Cumulus Linux 3.6</td>
<td><p>When upgrading from a previous release to Cumulus Linux 3.6, TACACS-authenticated users mapped to tacacs0 thru tacacs15 users with the netshow or netedit user groups cannot run <code>net</code> commands and they see the following error:</p>
<pre><code>ERROR: You do not have permission to execute that command</code></pre>
<p>This behavior is seen when upgrading with simple authentication only and occurs without a restricted shell for command authorization being enabled.</p>
<p>This problem is not present on a binary install of 3.6.0 or 3.6.1 and only happens when upgrading from previous releases.</p>
<p>To work around this issue, edit the <code>/etc/netd.conf</code> file, add the <code>tacacs</code> user group to the <code>groups_with_show</code> list, and add the <code>tacacs15</code> user to the <code>users_with_edit</code> list as below:</p>
<pre><code># Control which users/groups are allowed to run &quot;add&quot;, &quot;del&quot;,
# &quot;clear&quot;, &quot;abort&quot;, and &quot;commit&quot; commands.
users_with_edit = root, cumulus, vagrant, tacacs15
groups_with_edit = netedit

\# Control which users/groups are allowed to run &quot;show&quot; commands.
users_with_show = root, cumulus, vagrant
groups_with_show = netshow, netedit, tacacs</code></pre>
<p>After making this change, restart <code>netd</code> with the <code>sudo systemctl restart netd</code> command.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN970"></span> <a href="#RN970"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-970 (CM-21203)</td>
<td>VXLAN and tcam_resource_profile set to acl-heavy, causes the switch to crash</td>
<td><p>Changing <code>tcam_resource_profile</code> to <code>acl-heavy</code> on a switch with VXLAN enabled and attempting to apply the configuration with a <code>switchd</code> restart, causes <code>switchd</code> to fail to restart, <code>netd</code> to crash, the switch to become temporarily unresponsive, and a cl-support to be generated.</p>
<p>To work around this issue, remove the <code>acl-heavy</code> profile or the VXLAN configuration.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN972"></span> <a href="#RN972"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-972 (CM-21003)</td>
<td>Cumulus Linux does not forward PTP traffic by default</td>
<td><p>A switch running Cumulus Linux 3.6.0 or later does not forward transit precision time protocol (PTP) packets as PTP is not enabled by default in Cumulus Linux.</p>
<p>To work around this issue, downgrade the switch to Cumulus Linux 3.5.3.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN974"></span> <a href="#RN974"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-974 (CM-21383)</td>
<td>Mellanox does not install traps for multicast groups registered to the Kernel</td>
<td><p>Mellanox switches do not install traps in hardware to send multicast traffic to the kernel, even after registering the multicast group.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN976"></span> <a href="#RN976"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-976 (CM-21335)</td>
<td>EVPN route map with match VNI causes FRR core</td>
<td><p>Applying a route map using <code>match evpn vni &lt;xyz&gt;</code> to a neighbor or peer-group causes FRR to core.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN977"></span> <a href="#RN977"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-977 (CM-21508)</td>
<td>EVPN best path not reinstalled after EVPN type 2 MAC route is withdrawn</td>
<td><p>A remote VRR MAC that is normally learned through an EVPN Type-2 route is learned locally on a host-facing port. This is then propagated through a new Type-2 MAC route throughout the environment and remote access switch pairs install the erroneous route.</p>
<p>To work around this issue, re-send the EVPN update from the infra pair by changing the VRR MAC or clearing the session.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN986"></span> <a href="#RN986"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-986 (CM-21256)</td>
<td>ARP storm in VXLAN symmetric routing</td>
<td><p>With VXLAN symmetric routing, it is possible to generate an ARP packet storm when SVI addresses are common across different racks.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN987"></span> <a href="#RN987"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-987 (CM-20938)</td>
<td>Debian Security Advisory DSA-4196-1 CVE-2018-1087 CVE-2018-8897 for the linux kernel package</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4196-1 and affect the Linux kernel.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>--------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4196-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>May 08, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package: linux</p>
<p>CVE ID: CVE-2018-1087 CVE-2018-8897</p>
<p>Debian Bug: 897427 897599 898067 898100</p>
<p>Several vulnerabilities have been discovered in the Linux kernel that may lead to a privilege escalation or denial of service.</p>
<p>CVE-2018-1087</p>
<p>Andy Lutomirski discovered that the KVM implementation did not properly handle #DB exceptions while deferred by MOV SS/POP SS, allowing an unprivileged KVM guest user to crash the guest or potentially escalate their privileges.</p>
<p>CVE-2018-8897</p>
<p>Nick Peterson of Everdox Tech LLC discovered that #DB exceptions that are deferred by MOV SS or POP SS are not properly handled, allowing an unprivileged user to crash the kernel and cause a denial of service.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 3.16.56-1+deb8u1. This update includes various fixes for regressions from 3.16.56-1 as released in DSA-4187-1 (Cf. #897427, #898067 and #898100).</p>
<p>For the stable distribution (stretch), these problems have been fixed in version 4.9.88-1+deb9u1. The fix for CVE-2018-1108 applied in DSA-4188-1 is temporarily reverted due to various regression, cf. #897599.</p>
<p>For the detailed security status of linux, refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/linux" class="external-link">https://security-tracker.debian.org/tracker/linux</a></p></td>
</tr>
<tr class="odd">
<td><span id="RN988"></span> <a href="#RN988"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-988 (CM-20834)</td>
<td>Debian Security Advisory DSA 4187-1 for linux kernel</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4187-1 and affect the Linux kernel.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>--------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4187-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Ben Hutchings</p>
<p>May 01, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package: linux</p>
<p>CVE ID: CVE-2015-9016 CVE-2017-0861 CVE-2017-5715 CVE-2017-5753 CVE-2017-13166 CVE-2017-13220 CVE-2017-16526 CVE-2017-16911 CVE-2017-16912 CVE-2017-16913 CVE-2017-16914 CVE-2017-18017 CVE-2017-18203 CVE-2017-18216 CVE-2017-18232 CVE-2017-18241 CVE-2018-1066 CVE-2018-1068 CVE-2018-1092 CVE-2018-5332 CVE-2018-5333 CVE-2018-5750 CVE-2018-5803 CVE-2018-6927 CVE-2018-7492 CVE-2018-7566 CVE-2018-7740 CVE-2018-7757 CVE-2018-7995 CVE-2018-8781 CVE-2018-8822 CVE-2018-1000004 CVE-2018-1000199</p>
<p>Several vulnerabilities have been discovered in the Linux kernel that may lead to a privilege escalation, denial of service or information leaks.</p>
<p>CVE-2015-9016</p>
<p>Ming Lei reported a race condition in the multiqueue block layer (blk-mq). On a system with a driver using blk-mq (mtip32xx, null_blk, or virtio_blk), a local user might be able to use this for denial of service or possibly for privilege escalation.</p>
<p>CVE-2017-0861</p>
<p>Robb Glasser reported a potential use-after-free in the ALSA (sound) PCM core. We believe this was not possible in practice.</p>
<p>CVE-2017-5715</p>
<p>Multiple researchers have discovered a vulnerability in various processors supporting speculative execution, enabling an attacker controlling an unprivileged process to read memory from arbitrary addresses, including from the kernel and all other processes running on the system.</p>
<p>This specific attack has been named Spectre variant 2 (branch target injection) and is mitigated for the x86 architecture (amd64 and i386) by using the "retpoline" compiler feature which allows indirect branches to be isolated from speculative execution.</p>
<p>CVE-2017-5753</p>
<p>Multiple researchers have discovered a vulnerability in various processors supporting speculative execution, enabling an attacker controlling an unprivileged process to read memory from arbitrary addresses, including from the kernel and all other processes running on the system.</p>
<p>This specific attack has been named Spectre variant 1 (bounds-check bypass) and is mitigated by identifying vulnerable code sections (array bounds checking followed by array access) and replacing the array access with the speculation-safe array_index_nospec() function.</p>
<p>More use sites will be added over time.</p>
<p>CVE-2017-13166</p>
<p>A bug in the 32-bit compatibility layer of the v4l2 ioctl handling code has been found. Memory protections ensuring user-provided buffers always point to userland memory were disabled, allowing destination addresses to be in kernel space. On a 64-bit kernel a local user with access to a suitable video device can exploit this to overwrite kernel memory, leading to privilege escalation.</p>
<p>CVE-2017-13220</p>
<p>Al Viro reported that the Bluetooth HIDP implementation could dereference a pointer before performing the necessary type check. A local user could use this to cause a denial of service.</p>
<p>CVE-2017-16526</p>
<p>Andrey Konovalov reported that the UWB subsystem may dereference an invalid pointer in an error case. A local user might be able to use this for denial of service.</p>
<p>CVE-2017-16911</p>
<p>Secunia Research reported that the USB/IP vhci_hcd driver exposed kernel heap addresses to local users. This information could aid the exploitation of other vulnerabilities.</p>
<p>CVE-2017-16912</p>
<p>Secunia Research reported that the USB/IP stub driver failed to perform a range check on a received packet header field, leading to an out-of-bounds read. A remote user able to connect to the USB/IP server could use this for denial of service.</p>
<p>CVE-2017-16913</p>
<p>Secunia Research reported that the USB/IP stub driver failed to perform a range check on a received packet header field, leading to excessive memory allocation. A remote user able to connect to the USB/IP server could use this for denial of service.</p>
<p>CVE-2017-16914</p>
<p>Secunia Research reported that the USB/IP stub driver failed to check for an invalid combination of fields in a received packet, leading to a null pointer dereference. A remote user able to connect to the USB/IP server could use this for denial of service.</p>
<p>CVE-2017-18017</p>
<p>Denys Fedoryshchenko reported that the netfilter xt_TCPMSS module failed to validate TCP header lengths, potentially leading to a use-after-free. If this module is loaded, it could be used by a remote attacker for denial of service or possibly for code execution.</p>
<p>CVE-2017-18203</p>
<p>Hou Tao reported that there was a race condition in creation and deletion of device-mapper (DM) devices. A local user could potentially use this for denial of service.</p>
<p>CVE-2017-18216</p>
<p>Alex Chen reported that the OCFS2 filesystem failed to hold a necessary lock during nodemanager sysfs file operations, potentially leading to a null pointer dereference. A local user could use this for denial of service.</p>
<p>CVE-2017-18232</p>
<p>Jason Yan reported a race condition in the SAS (Serial-AttachedSCSI) subsystem, between probing and destroying a port. This could lead to a deadlock. A physically present attacker could use this to cause a denial of service.</p>
<p>CVE-2017-18241</p>
<p>Yunlei He reported that the f2fs implementation does not properly initialise its state if the "noflush_merge" mount option is used. A local user with access to a filesystem mounted with this option could use this to cause a denial of service.</p>
<p>CVE-2018-1066</p>
<p>Dan Aloni reported to Red Hat that the CIFS client implementation would dereference a null pointer if the server sent an invalid response during NTLMSSP setup negotiation. This could be used by a malicious server for denial of service.</p>
<p>CVE-2018-1068</p>
<p>The syzkaller tool found that the 32-bit compatibility layer of ebtables did not sufficiently validate offset values. On a 64-bit kernel, a local user with the CAP_NET_ADMIN capability (in any user namespace) could use this to overwrite kernel memory, possibly leading to privilege escalation. Debian disables unprivileged user namespaces by default.</p>
<p>CVE-2018-1092</p>
<p>Wen Xu reported that a crafted ext4 filesystem image would trigger a null dereference when mounted. A local user able to mount arbitrary filesystems could use this for denial of service.</p>
<p>CVE-2018-5332</p>
<p>Mohamed Ghannam reported that the RDS protocol did not sufficiently validate RDMA requests, leading to an out-of-bounds write. A local attacker on a system with the rds module loaded could use this for denial of service or possibly for privilege escalation.</p>
<p>CVE-2018-5333</p>
<p>Mohamed Ghannam reported that the RDS protocol did not properly handle an error case, leading to a null pointer dereference. A local attacker on a system with the rds module loaded could possibly use this for denial of service.</p>
<p>CVE-2018-5750</p>
<p>Wang Qize reported that the ACPI sbshc driver logged a kernel heap address. This information could aid the exploitation of other vulnerabilities.</p>
<p>CVE-2018-5803</p>
<p>Alexey Kodanev reported that the SCTP protocol did not range-check the length of chunks to be created. A local or remote user could use this to cause a denial of service.</p>
<p>CVE-2018-6927</p>
<p>Li Jinyue reported that the FUTEX_REQUEUE operation on futexes did not check for negative parameter values, which might lead to a denial of service or other security impact.</p>
<p>CVE-2018-7492</p>
<p>The syzkaller tool found that the RDS protocol was lacking a null pointer check. A local attacker on a system with the rds module loaded could use this for denial of service.</p>
<p>CVE-2018-7566</p>
<p>Fan LongFei reported a race condition in the ALSA (sound) sequencer core, between write and ioctl operations. This could lead to an out-of-bounds access or use-after-free. A local user with access to a sequencer device could use this for denial of service or possibly for privilege escalation.</p>
<p>CVE-2018-7740</p>
<p>Nic Losby reported that the hugetlbfs filesystem's mmap operation did not properly range-check the file offset. A local user with access to files on a hugetlbfs filesystem could use this to cause a denial of service.</p>
<p>CVE-2018-7757</p>
<p>Jason Yan reported a memory leak in the SAS (Serial-Attached SCSI) subsystem. A local user on a system with SAS devices could use this to cause a denial of service.</p>
<p>CVE-2018-7995</p>
<p>Seunghun Han reported a race condition in the x86 MCE (Machine Check Exception) driver. This is unlikely to have any security impact.</p>
<p>CVE-2018-8781</p>
<p>Eyal Itkin reported that the udl (DisplayLink) driver's mmap operation did not properly range-check the file offset. A local user with access to a udl framebuffer device could exploit this to overwrite kernel memory, leading to privilege escalation.</p>
<p>CVE-2018-8822</p>
<p>Dr Silvio Cesare of InfoSect reported that the ncpfs client implementation did not validate reply lengths from the server. An ncpfs server could use this to cause a denial of service or remote code execution in the client.</p>
<p>CVE-2018-1000004</p>
<p>Luo Quan reported a race condition in the ALSA (sound) sequencer core, between multiple ioctl operations. This could lead to a deadlock or use-after-free. A local user with access to a sequencer device could use this for denial of service or possibly for privilege escalation.</p>
<p>CVE-2018-1000199</p>
<p>Andy Lutomirski discovered that the ptrace subsystem did not sufficiently validate hardware breakpoint settings. Local users can use this to cause a denial of service, or possibly for privilege escalation, on x86 (amd64 and i386) and possibly other architectures.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 3.16.56-1.</p>
<p>For the detailed security status of linux, refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/linux" class="external-link">https://security-tracker.debian.org/tracker/linux</a></p></td>
</tr>
<tr class="even">
<td><span id="RN1005"></span> <a href="#RN1005"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1005 (CM-21490)</td>
<td>On Mellanox switches, when a ERSPAN forwarding rule is defined and non-atomic update mode is enabled, traffic is blocked</td>
<td><p>When ERSPAN is enabled on a Mellanox switch and non_atomic_update_mode = TRUE, traffic through the switch is blocked.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1007"></span> <a href="#RN1007"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1007 (CM-21599)</td>
<td>With ECMP rebalance enabled for PIM, multicast stream loss might occur following a link failure</td>
<td><p>If you shut down the RPF nexthop switch after the last hop router builds the SPT, the switch might not failover to the alternate ECMP RPF nexthop.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN1008"></span> <a href="#RN1008"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1008 (CM-21396)</td>
<td>The 'net del interface bridge vids' command removes the interface from the bridge ports list</td>
<td><p>If you run the <code>net del interface &lt;interface&gt; bridge vids</code> command, the interface is removed from the bridge ports list instead of inheriting the characteristics of the bridge.</p>
<p>To work around this issue, add the interface back to the bridge with the <code>net add bridge bridge ports &lt;interface&gt;</code> command.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1009"></span> <a href="#RN1009"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1009 (CM-21474)</td>
<td>Multiple sx_core: lag_id errors in syslog</td>
<td><p>On Mellanox swtiches, when the input port of a sampled packet is a bond interface, you see multiple <code>sx_core: lag_id</code> errors in syslog.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN1010"></span> <a href="#RN1010"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1010 (CM-21352)</td>
<td>Debian Security Advisory DSA-4212-1 CVE-2018-11235 for the git package</td>
<td><p>The following CVE was announced in Debian Security Advisory DSA-4212-1 and affects the git package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4212-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>May 29, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>--------------------------------------------------------------------------</p>
<p>Package : git</p>
<p>CVE ID : CVE-2018-11235</p>
<p>Etienne Stalmans discovered that git, a fast, scalable, distributed revision control system, is prone to an arbitrary code execution vulnerability exploitable via specially crafted submodule names in a .gitmodules file.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 1:2.1.4-2.1+deb8u6.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 1:2.11.0-3+deb9u3.</p>
<p>We recommend that you upgrade your git packages.</p>
<p>For the detailed security status of git please refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/git" class="external-link">https://security-tracker.debian.org/tracker/git</a></p></td>
</tr>
<tr class="odd">
<td><span id="RN1011"></span> <a href="#RN1011"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1011 (CM-21350)</td>
<td>Debian Security Advisory DSA 4224-1 CVE-2018-12020 for the gnupg package</td>
<td><p>The following CVE was announced in Debian Security Advisory DSA-4224-1 and affects the gnupg package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4224-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>June 08, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>--------------------------------------------------------------------------</p>
<p>Package : gnupg</p>
<p>CVE ID : CVE-2018-12020</p>
<p>Marcus Brinkmann discovered that GnuGPG performed insufficient sanitisation of file names displayed in status messages, which could be abused to fake the verification status of a signed email.</p>
<p>Details can be found in the upstream advisory at <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2018q2/000425.html" class="external-link">https://lists.gnupg.org/pipermail/gnupg-announce/2018q2/000425.html</a></p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 1.4.18-7+deb8u5.</p>
<p>For the detailed security status of gnupg, refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/gnupg" class="external-link">https://security-tracker.debian.org/tracker/gnupg</a></p></td>
</tr>
<tr class="even">
<td><span id="RN1012"></span> <a href="#RN1012"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1012 (CM-21351)</td>
<td>Debian Security Advisory DSA 4222-1 CVE-2018-12020 for the gnupg2 package</td>
<td><p>The following CVE was announced in Debian Security Advisory DSA-4222-1 and affects the gnupg2 package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4222-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>June 08, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : gnupg2</p>
<p>CVE ID : CVE-2018-12020</p>
<p>Marcus Brinkmann discovered that GnuGPG performed insufficient sanitisation of file names displayed in status messages, which could be abused to fake the verification status of a signed email.</p>
<p>Details can be found in the upstream advisory at <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2018q2/000425.html" class="external-link">https://lists.gnupg.org/pipermail/gnupg-announce/2018q2/000425.html</a></p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 2.0.26-6+deb8u2.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 2.1.18-8~deb9u2.</p>
<p>For the detailed security status of gnupg2 please refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/gnupg2" class="external-link">https://security-tracker.debian.org/tracker/gnupg2</a></p></td>
</tr>
<tr class="odd">
<td><span id="RN1013"></span> <a href="#RN1013"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1013 (CM-20926)</td>
<td>Debian Security Advisory DSA-4195-1 CVE-2018-0494 for the wget package</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4195-1 and affect the wget package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4195-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>May 08, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : wget</p>
<p>CVE ID : CVE-2018-0494</p>
<p>Debian Bug : 898076</p>
<p>Harry Sintonen discovered that wget, a network utility to retrieve files from the web, does not properly handle '\r\n' from continuation lines while parsing the Set-Cookie HTTP header. A malicious web server could use this flaw to inject arbitrary cookies to the cookie jar file, adding new or replacing existing cookie values.</p>
<p>For the oldstable distribution (jessie), this problem has been fixedin version 1.16-1+deb8u5.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 1.18-5+deb9u2.</p>
<p>We recommend that you upgrade your wget packages.</p>
<p>For the detailed security status of wget please refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/wget" class="external-link">https://security-tracker.debian.org/tracker/wget</a></p></td>
</tr>
<tr class="even">
<td><span id="RN1014"></span> <a href="#RN1014"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1014 (CM-21349)</td>
<td>Debian Security Advisory DSA-4226-1 CVE-2018-12015 for the perl package</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4226-1 and affect the perl package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4226-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>June 12, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : perl</p>
<p>CVE ID : CVE-2018-12015</p>
<p>Debian Bug : 900834</p>
<p>Jakub Wilk discovered a directory traversal flaw in the Archive::Tar module, allowing an attacker to overwrite any file writable by the extracting user via a specially crafted tar archive.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 5.20.2-3+deb8u11.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 5.24.1-3+deb9u4.</p>
<p>We recommend that you upgrade your perl packages.</p>
<p>For the detailed security status of perl, refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/perl" class="external-link">https://security-tracker.debian.org/tracker/perl</a></p></td>
</tr>
<tr class="odd">
<td><span id="RN1015"></span> <a href="#RN1015"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1015 (CM-20865)</td>
<td>clagd memory growth during oversubscription test</td>
<td><p>During an oversubscription test where more than 100G of traffic is destined for an MLAG host bond, the host bond bounces and MLAG memory usage grows to over 1.2GB. After stopping Ixia traffic and protocols, the <code>clagd</code> service still holds more than 1GB of memory.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN1016"></span> <a href="#RN1016"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1016 (CM-20803)</td>
<td>Debian Security Advisory DSA-4186-1 CVE-2018-1000164 for gunicorn package</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4186-1 and affect the gunicorn package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4186-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Moritz Muehlenhoff</p>
<p>April 28, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>--------------------------------------------------------------------------</p>
<p>Package : gunicorn</p>
<p>CVE ID : CVE-2018-1000164</p>
<p>It was discovered that gunicorn, an event-based HTTP/WSGI server was susceptible to HTTP Response splitting.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 19.0-1+deb8u1.</p>
<p>We recommend that you upgrade your gunicorn packages.</p>
<p>For the detailed security status of gunicorn please refer to its security tracker page at:</p>
<p><a href="https://security-tracker.debian.org/tracker/gunicorn" class="external-link">https://security-tracker.debian.org/tracker/gunicorn</a></p></td>
</tr>
<tr class="odd">
<td><span id="RN1017"></span> <a href="#RN1017"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1017 (CM-21348)</td>
<td>Debian Security Advisory DSA-4217-1 CVE-2018-9273 CVE-2018-7320 CVE-2018-7334 CVE-2018-7335 CVE-2018-7419 CVE-2018-9261 CVE-2018-9264 CVE-2018-11358 CVE-2018-11360 CVE-2018-11362 for wireshark</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4217-1 and affect the wireshark package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4217-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Moritz Muehlenhoff</p>
<p>June 03, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : wireshark</p>
<p>CVE ID : CVE-2018-9273 CVE-2018-7320 CVE-2018-7334 CVE-2018-7335 CVE-2018-7419 CVE-2018-9261 CVE-2018-9264 CVE-2018-11358 CVE-2018-11360 CVE-2018-11362</p>
<p>It was discovered that Wireshark, a network protocol analyzer, contained several vulnerabilities in the dissectors for PCP, ADB, NBAP, UMTS MAC,</p>
<p>IEEE 802.11, SIGCOMP, LDSS, GSM A DTAP and Q.931, which result in denial of service or the execution of arbitrary code.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 1.12.1+g01b65bf-4+deb8u14.</p>
<p>For the stable distribution (stretch), these problems have been fixed in version 2.2.6+g32dac6a-2+deb9u3.</p>
<p>For the detailed security status of wireshark, refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/wireshark" class="external-link">https://security-tracker.debian.org/tracker/wireshark</a></p></td>
</tr>
<tr class="even">
<td><span id="RN1018"></span> <a href="#RN1018"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1018 (CM-20799)</td>
<td>Cannot use NCLU to add or delete RADIUS client IP addresses for 802.1X interfaces</td>
<td><p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1019"></span> <a href="#RN1019"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1019 (CM-21156)</td>
<td>Debian Security Advisory DSA-4211-1 CVE-2017-18266 for xdg-utils package</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4211-1 and affect the xdg-utils package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4211-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Luciano Bello</p>
<p>May 25, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : xdg-utils</p>
<p>CVE ID : CVE-2017-18266</p>
<p>Debian Bug : 898317</p>
<p>Gabriel Corona discovered that xdg-utils, a set of tools for desktop environment integration, is vulnerable to argument injection attacks. If the environment variable BROWSER in the victim host has a "%s" and the victim opens a link crafted by an attacker with xdg-open, the malicious party could manipulate the parameters used by the browser when opened. This manipulation could set, for example, a proxy to which the network traffic could be intercepted for that particular execution.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 1.1.0~rc1+git20111210-7.4+deb8u1.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 1.1.1-1+deb9u1.</p>
<p>For the detailed security status of xdg-utils, refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/xdg-utils" class="external-link">https://security-tracker.debian.org/tracker/xdg-utils</a></p></td>
</tr>
<tr class="even">
<td><span id="RN1020"></span> <a href="#RN1020"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1020 (CM-21098)</td>
<td>Debian Security Advisory DSA-4208-1 CVE-2018-1122 CVE-2018-1123 CVE-2018-1124 CVE-2018-1125 CVE-2018-1126 for procps top, ps command</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4208-1 and affect the procps package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4208-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>May 22, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : procps</p>
<p>CVE ID : CVE-2018-1122 CVE-2018-1123 CVE-2018-1124 CVE-2018-1125 CVE-2018-1126</p>
<p>Debian Bug : 899170</p>
<p>The Qualys Research Labs discovered multiple vulnerabilities in procps, a set of command line and full screen utilities for browsing procfs. The Common Vulnerabilities and Exposures project identifies the following problems:</p>
<p>CVE-2018-1122</p>
<p>top reads its configuration from the current working directory if no $HOME was configured. If top were started from a directory writable by the attacker (such as /tmp) this could result in local privilege escalation.</p>
<p>CVE-2018-1123</p>
<p>Denial of service against the ps invocation of another user.</p>
<p>CVE-2018-1124</p>
<p>An integer overflow in the file2strvec() function of libprocps couldresult in local privilege escalation.</p>
<p>CVE-2018-1125</p>
<p>A stack-based buffer overflow in pgrep could result in denial of service for a user using pgrep for inspecting a specially crafted process.</p>
<p>CVE-2018-1126</p>
<p>Incorrect integer size parameters used in wrappers for standard allocators could cause integer truncation and lead to integer overflow issues.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 2:3.3.9-9+deb8u1.</p>
<p>For the stable distribution (stretch), these problems have been fixed in version 2:3.3.12-3+deb9u1.</p>
<p>For the detailed security status of procps, refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/procps" class="external-link">https://security-tracker.debian.org/tracker/procps</a></p>
<p>A full readable description of the vulnerabilities is here: <a href="https://www.qualys.com/2018/05/17/procps-ng-audit-report-advisory.txt" class="external-link">https://www.qualys.com/2018/05/17/procps-ng-audit-report-advisory.txt</a></p>
<p>They are all local issues only, Denial of Service, and a top privilege escalation.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1022"></span> <a href="#RN1022"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1022 (CM-20697)</td>
<td>Debian Security Advisory DSA-4176-1 CVE-2018-2755 CVE-2018-2761 CVE-2018-2771 CVE-2018-2773 CVE-2018-2781 CVE-2018-2813 CVE-2018-2817 CVE-2018-2818 CVE-2018-2819 for the mysql package</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4211-1 and affect the mysql library and common packages.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>--------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4176-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>April 20, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>--------------------------------------------------------------------------</p>
<p>Package : mysql-5.5</p>
<p>CVE ID : CVE-2018-2755 CVE-2018-2761 CVE-2018-2771 CVE-2018-2773 CVE-2018-2781 CVE-2018-2813 CVE-2018-2817 CVE-2018-2818 CVE-2018-2819</p>
<p>Several issues have been discovered in the MySQL database server. The vulnerabilities are addressed by upgrading MySQL to the new upstream version 5.5.60, which includes additional changes. Please see the MySQL 5.5 Release Notes and Oracle's Critical Patch Update advisory for further details:</p>
<p><a href="https://dev.mysql.com/doc/relnotes/mysql/5.5/en/news-5-5-60.html" class="external-link">https://dev.mysql.com/doc/relnotes/mysql/5.5/en/news-5-5-60.html</a></p>
<p><a href="http://www.oracle.com/technetwork/security-advisory/cpuapr2018-3678067.html" class="external-link">http://www.oracle.com/technetwork/security-advisory/cpuapr2018-3678067.html</a></p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 5.5.60-0+deb8u1.</p>
<p>We recommend that you upgrade your mysql-5.5 packages.</p>
<p>For the detailed security status of mysql-5.5 please refer to its security tracker page at:</p>
<p><a href="https://security-tracker.debian.org/tracker/mysql-5.5" class="external-link">https://security-tracker.debian.org/tracker/mysql-5.5</a></p>
<p>Further information about Debian Security Advisories, how to apply these updates to your system and frequently asked questions can be found at: <a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a></p></td>
</tr>
<tr class="even">
<td><span id="RN1023"></span> <a href="#RN1023"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1023 (CM-20138)</td>
<td>NCLU errors out on a breakout port when the port is already configured in a bridge</td>
<td><p>It's been reported that splitting a switch port removes it from the bridge.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1024"></span> <a href="#RN1024"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1024 (CM-21047)</td>
<td>cl-support takes a long time to complete when a large amount of space is allocated to /var/log/lastlog</td>
<td><p>When there is a lot of space allocated to <code>/var/log/lastlog</code>, cl-support takes a long time to run (sometimes more than an hour).</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN1026"></span> <a href="#RN1026"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1026 (CM-21012)</td>
<td>Debian Security Advisory DSA-4202-1 CVE-2018-1000301 for the curl package</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4202-1 and affect the curl package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4202-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Alessandro Ghedini</p>
<p>May 16, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : curl</p>
<p>CVE ID : CVE-2018-1000301</p>
<p>Debian Bug : 898856</p>
<p>OSS-fuzz, assisted by Max Dymond, discovered that cURL, an URL transfer library, could be tricked into reading data beyond the end of a heap based buffer when parsing invalid headers in an RTSP response.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 7.38.0-4+deb8u11.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 7.52.1-5+deb9u6.</p>
<p>For the detailed security status of curl, refer to its security tracker page at: <a href="https://security-tracker.debian.org/tracker/curl" class="external-link">https://security-tracker.debian.org/tracker/curl</a></p></td>
</tr>
<tr class="odd">
<td><span id="RN1028"></span> <a href="#RN1028"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1028 (CM-20728)</td>
<td>Errors occur when installing TOS matched rules in ip6tables</td>
<td><p>The following error occurs when trying to install a TOS matched rule in ip6tables:</p>
<pre><code>Installing acl policy
error: hw sync failed (Cannot process ip6tables,FORWARD,2,TOS match extension is supported only for iptables)
Rolling back ..
failed.</code></pre>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
<tr class="even">
<td><span id="RN1029"></span> <a href="#RN1029"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1029 (CM-21564)</td>
<td>NCLU configuration fails to commit due to invalid value for ip-forward or ip6-forward</td>
<td><p>After upgrading to Cumulus Linux 3.6.1 on Facebook Backpack switches, NCLU configuration fails to commit because of the default <code>ip-forward</code> and <code>ip6-forward</code> configuration.</p>
<p>This issue is fixed in Cumulus Linux 3.6.2.</p></td>
</tr>
</tbody>
</table>

# New Known Issues in Cumulus Linux 3.6.2

The following issues are new to Cumulus Linux and affect the current
release.

<table>

<tbody>
<tr class="odd">
<th>Release Note ID</th>
<th>Summary</th>
<th>Description</th>
</tr>
<tr class="even">
<td><span id="RN975"></span> <a href="#RN975"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-975 (CM-21658)</td>
<td>candidate EVPN best path not re-installed after EVPN type-2 MAC route is withdrawn</td>
<td><p>If hosts nodes reflect or bridge a frame received from access switch pairs back to the switches, a remote VRR virtual MAC that is normally learned through an EVPN type-2 MAC+IP (centralized advertise-default-gw) route is learned locally on a host-facing port. This is then propagated through a new type-2 MAC route throughout the environment and remote access switch pairs install the erroneous route.</p>
<p>To work around this issue, resend the EVPN update from the infra pair by changing the VRR MAC or clear the session.</p>
<p>This is a known issue that is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="RN979"></span> <a href="#RN979"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-979 (CM-21691)</td>
<td>When removing a dot1x configured port from a traditional bridge, the net pending command does not show the changes</td>
<td><p>When removing a dot1x configured port from a traditional bridge, the <code>net pending</code> command does not show the pending changes; however, the port is removed from the bridge when you issue the <code>net commit</code> command.</p>
<p>This is a known issue and should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="RN980"></span> <a href="#RN980"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-980 (CM-21653)</td>
<td>Incorrect VLAN translation tags on double tagged bridge interfaces</td>
<td><p>A bridge with double tag translation configured on a member interface correctly maps the VLAN tags in the outgoing ARP request frame, but incorrectly maps the VLAN tags on the incoming ARP reply.</p>
<p>This is a known issue that is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="RN982"></span> <a href="#RN982"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-982 (CM-21598)</td>
<td>IGMP configuration does not persist through a switch reboot</td>
<td><p>The order of the query interval and maximum response time parameters in an IGMP interface configuration together with an insufficient response time value causes the IGMP configuration to be lost during a switch reboot. The maximum response time cannot be greater than or equal to the query interval, and the maximum response time must be read before the interval.</p>
<p>To work around this issue temporarily, move the query interval parameter to follow the <code>query-max-response-time</code> parameter and set the <code>query-max-response-time</code> to a value less than the query interval. You must repeat this workaround each time FRR writes to the <code>frr.conf</code> file.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN989"></span> <a href="#RN989"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-989 (CM-9695)</td>
<td>cl-resource-query: ACL metrics are displayed as 0 on a Mellanox switch</td>
<td><p>ACL-related metrics reported by <code>cl-resource-query</code> on a Mellanox MLX-2700 switch return all ACL metrics as 0. For example:</p>
<pre><code>cumulus@mlx-2700-08:~$ sudo cl-resource-query 
Host entries:              34,   0% of maximum value   5120
IPv4 neighbors:             8
IPv6 neighbors:            13
IPv4 entries:           32768,  82% of maximum value  39936
IPv6 entries:               0,   0% of maximum value  15360
IPv4 Routes:            32768
IPv6 Routes:                0
Total Routes:           32768, 100% of maximum value  32768
ECMP nexthops:             64,   0% of maximum value 209664
MAC entries:                0,   0% of maximum value 409600
Ingress ACL entries:        0,   0% of maximum value      0
Ingress ACL counters:       0,   0% of maximum value      0
Ingress ACL meters:         0,   0% of maximum value      0
Ingress ACL slices:         0,   0% of maximum value      0
Egress ACL entries:         0,   0% of maximum value      0
Egress ACL counters:        0,   0% of maximum value      0
Egress ACL meters:          0,   0% of maximum value      0
Egress ACL slices:          0,   0% of maximum value      0</code></pre>
<p>To work around this issue, run the Mellanox <code>sx_api_resource_manager_dump_all.py</code> debug utility:</p>
<pre><code>cumulus@mlx-2700-08:~$ sudo sx_api_resource_manager_dump_all.py &gt; tmp-cl-resq
cumulus@mlx-2700-08:~$ cat tmp-cl-resq
[+] opening sdk 
[0/1847]
sx_api_open handle:0x14c3724 , rc 0 

 HW Table Utilization

Utilization for HW resource TCAM  is 42.9
Utilization for HW resource KVD Hash is 69.9
Utilization for HW resource KVD Linear is 49.9
Utilization for HW resource PGT is 0.0
Utilization for HW resource Flow Counter is 0.0
Utilization for HW resource ACL Regions is 1.0

Logical Free Entries Count

\============================================================
|                                Resource|   Free Entries|
\============================================================
|                           UC MAC Table |          67181|
|                           MC MAC Table |          67181|
|                      FIB IPV4 UC Table |         132628|
|                      FIB IPV6 UC Table |          95802|
|                      FIB IPV4 MC Table |           2288|
|                         ARP IPV4 Table |          32569|
|                         ARP IPV6 Table |          12292|
|                 Unicast Adjacency Table|           8197|
|                    L2 MC VECTORS Table |           6999|
|             ACL Extended Actions Table |           8197|
|                           ACL PBS Table|           8197|
|                              eRIF List |           8197|
|                               ILM Table|          67181|
|                              VLAN Table|              1|
|                            VPorts Table|          67181|
|                               FID Table|          16362|
|             Policy Based MPLS ILM Table|           8197|
|                             ACL Regions|            396|
|                       ACL Rules 18B Key|           2254|
|                       ACL Rules 32B Key|           1024|
|                       ACL Rules 54B Key|           1022|
|                       RIF Counter Basic|           3276|
|                    RIF Counter Enhanced|           1092|
|                            Flow Counter|           2048|
|                       ACL GROUPS Table |            396|

Logical Table Utilization

\================================================================================================
|                 Resource|       HW Table|Logical Entries |     HW Entries| Utilization(%)|
\================================================================================================
|            UC MAC Table |       KVD Hash|             43|             43|            0.0|
|       FIB IPV4 UC Table |       KVD Hash|             89|          65790|           26.5|
|       FIB IPV6 UC Table |       KVD Hash|             51|          28926|           11.6|
|       FIB IPV4 MC Table |          TCAM |              0|            192|            1.1|
|          ARP IPV4 Table |       KVD Hash|            199|          32768|           13.2|
|          ARP IPV6 Table |       KVD Hash|           4092|          32768|          179.6|
|  Unicast Adjacency Table|     KVD Linear|           8187|           8187|           49.9|
|             VPorts Table|       KVD Hash|              0|             22|            0.0|
|                FID Table|       KVD Hash|             22|             22|            0.0|
|              ACL Regions|    ACL Regions|              4|              4|            1.0|
|        ACL Rules 18B Key|          TCAM |              2|             64|            0.3|
|        ACL Rules 54B Key|          TCAM |              2|           5760|           35.1|
|        ACL GROUPS Table |ACL Group Table|              4|            400|          100.0|
cumulus@mlx-2700-08:~$</code></pre>
<p>This is a known issue and should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="RN990"></span> <a href="#RN990"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-990 (CM-19647)</td>
<td>With EVPN symmetric routing on a Trident II+ or Maverick switch, forwarding with overlay ECMP routes does not work</td>
<td><p>Packets from a host to a destination that is reachable through a VXLAN overlay ECMP path might not get forwarded. The forwarding might work if the underlying ECMP members point to the CPU, because of software forwarding.</p>
<p>The issue is seen on a leaf switch connected to the host sending the traffic. The issue can also been seen on a leaf switch connecting towards the destination where that egress route is ECMP.</p>
<p>Depending upon your network topology, one way to work around this issue is to use an as-path prepend so that one of the type 5 routes sent has a longer as-path:</p>
<pre><code> address-family ipv4 unicast
   distance bgp 190 200 190
-  network 0.0.0.0/0 route-map apply_med
+  network 0.0.0.0/0 route-map apply_aspath_prepend

+route-map apply_aspath_prepend permit 10
+ match ip address prefix-list default_route
+ set as-path prepend last-as 1
+end

You can see that the AS &quot;1&quot; is added to the as-path:

cumulus@switch:~$ net show bgp vrf internal ipv4 unicast
\==================================

BGP table version is 16, local router ID is 172.18.5.12

Status codes: s suppressed, d damped, h history, * valid, &gt; best, = multipath,

              i internal, r RIB-failure, S Stale, R Removed

Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path

*  0.0.0.0          172.16.3.4                             0 65000 65021 0 i

*                   172.16.3.4                             0 65000 65021 0 i

*                   172.16.3.4                             0 65000 65020 0 i

*                   172.16.3.4                             0 65000 65020 0 i

*                   172.16.3.3                             0 65000 65019 i

*                   172.16.3.3                             0 65000 65019 i

*                   172.16.3.3                             0 65000 65018 i

*&gt;                  172.16.3.3                             0 65000 65018 i</code></pre>
<p>This results in having just one route in the FIB:</p>
<pre><code>===========================
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR,
       &gt; - selected route, * - FIB route

VRF internal:
B&gt;* 0.0.0.0/0 [20/0] via 172.16.3.4, vlan4000 onlink, 00:12:06</code></pre></td>
</tr>
<tr class="even">
<td><span id="RN991"></span> <a href="#RN991"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-991 (CM-20316)</td>
<td>arp_accept and arp_ignore do not work for SVIs if a bridge has VXLAN interfaces</td>
<td><p>On a Cumulus Linux switch, if a bridge has VXLAN interfaces, then the <code>arp_accept</code> and <code>arp_ignore</code> options do not work for any switch virtual interfaces (SVIs).</p>
<p>To work around this issue, disable ARP suppression on the VXLAN interfaces. For example, if the VXLAN is named vni100, disable ARP suppression on it with the following command:</p>
<pre><code>cumulus@switch:~$ net add vxlan vni100 bridge arp-nd-suppress off
cumulus@switch:~$ net commit</code></pre>
<p>This issue should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="RN992"></span> <a href="#RN992"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-992 (CM-20570)</td>
<td>Disabled services started after running `net del all` then `net commit`</td>
<td><p>After running the <code>net del all</code> command to remove the configuration, then committing the change with <code>net commit</code>, NCLU enables every service and restarts them. You must manually disable those services again.</p>
<p>This is a known issue and should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="RN993"></span> <a href="#RN993"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-993 (CM-20585)</td>
<td>Routes learned via EVPN clouds do not get summarized</td>
<td><p>Routes that are learned from an EVPN cloud don't get summarized. Only routes that reside on or are owned by a switch get summarized.</p>
<p>This is a known issue and should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="RN994"></span> <a href="#RN994"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-994 (CM-21332)</td>
<td>switchd doesn't assign a gport for a VLAN subinterface</td>
<td><p>When two VLAN subinterfaces are bridged to each other in a traditional mode bridge, <code>switchd</code> doesn't assign a gport to the subinterface, even though a gport is expected for each VLAN subinterface.</p>
<p>To work around this issue, you can do one of two things:</p>
<ul>
<li>Add a VXLAN on the bridge so it doesn't require real tunnel IP address.</li>
<li>Separate the ingress and egress functions across two physical ports.</li>
</ul>
<p>This issue should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="RN995"></span> <a href="#RN995"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-995 (CM-21373)</td>
<td>Debian Security advisory DSA-4231-1/CVE-2018-0495 for libgcrypt20 package</td>
<td><p>Debian issued the following security advisory, DSA-4231-1, which affects the libgcrypt20 package. This advisory applies only to Debian Stretch release.</p>
<p>Debian Jessie, upon which Cumulus Linux 3.0 - 3.6.2 is based, is vulnerable, but the vulnerability has not been fixed upstream in Debian yet.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4231-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>June 17, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : libgcrypt20</p>
<p>CVE ID : CVE-2018-0495</p>
<p>It was discovered that Libgcrypt is prone to a local side-channel attack allowing recovery of ECDSA private keys.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 1.7.6-2+deb9u3.</p>
<p>We recommend that you upgrade your libgcrypt20 packages.</p>
<p>For the detailed security status of libgcrypt20 please refer to its security tracker page at:</p>
<p><a href="https://security-tracker.debian.org/tracker/libgcrypt20" class="external-link">https://security-tracker.debian.org/tracker/libgcrypt20</a></p>
<p>This issue will be fixed in a future version of Cumulus Linux when a fix made available for Debian Jessie.</p></td>
</tr>
<tr class="odd">
<td><span id="RN996"></span> <a href="#RN996"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-996 (CM-21379)</td>
<td>Floating static route is not installed into the FIB when the primary route becomes unavailable</td>
<td><p>If a primary route becomes unavailable (for example, you run <code>ifdown</code> on the switch port), the backup route remains inactive and is not installed into FIB.</p>
<p>To work around this issue, configure routes as ECMP:</p>
<pre><code>cumulus@switch:~$ net del routing route 4.1.1.0/24 1.1.1.1 10
cumulus@switch:~$ net add routing route 4.1.1.0/24 1.1.1.1
cumulus@switch:~$ net commit</code></pre>
<p>This issue should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="RN997"></span> <a href="#RN997"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-997 (CM-21393)</td>
<td>A VXLAN implementation is using a UDP source port lower than 1024</td>
<td><p>Because VXLAN encapsulation uses a full range of source ports, it is possible for Cumulus Linux switches to generate packets with UDP source ports numbered lower than 1023. This might result in the traffic being mishandled in your network if you have rules in place to handle this traffic differently. For example, you might have DSCP setup for this port range.</p>
<p>To work around this issue, avoid using the well known port range for sourcing VXLAN traffic.</p>
<p>This issue should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="RN998"></span> <a href="#RN998"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-998 (CM-21398)</td>
<td>Creating a MGMT ACL via NCLU results in a FORWARD entry</td>
<td><p>If you use NCLU to configure an ACL for eth0, you cannot designate it as an INPUT rule; the rule is automatically created as a FORWARD rule in the <code>/etc/cumulus/acl/policy.d/50_nclu_acl.rules</code> file.</p>
<p>This issue should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="RN999"></span> <a href="#RN999"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-999 (CM-21422)</td>
<td>The NCLU `net show config` command shows the configuration that is pending and not the one that was committed</td>
<td><p>If you have any pending changes in the NCLU buffer, when you run <code>net show config command</code> or <code>net show config interface &lt;interface&gt;</code>, the output displays the pending configuration, not the one that was previously committed.</p>
<p>This issue should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1000"></span> <a href="#RN1000"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1000 (CM-21454)</td>
<td>Creating a new traditional mode bridge causes temporary traffic loss</td>
<td><p>Sometimes when creating a new bridge in traditional mode, an outage of 20-30 seconds can occur when running <code>ifreload</code>. This issue is more noticeable if you add and remove traditional bridges multiple times a day. The outage is long enough to drop BGP and OSPF sessions running through the switch. However, <code>ifreload</code> debug logs show everything is normal, that no interfaces are going down.</p>
<p>This issue should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="RN1002"></span> <a href="#RN1002"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1002 (CM-21556)</td>
<td>FRR next-hop resolution changes are not updated when applying a VRF to an interface after routes are configured in FRR</td>
<td><p>When adding new SVIs and static VRF routes in FRR, the appropriate VRF is applied to the interface in the kernel <em>after</em> the static routes are configured in FRR. When the kernel interface changes to the appropriate VRF, FRR next-hop resolution is not updated with the valid connected next-hop interface.</p>
<p>To work around this issue, remove and re-add the static routes.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1003"></span> <a href="#RN1003"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1003 (CM-21511)</td>
<td>IGMP queries are not sent if a VXLAN is declared before the bridge in /etc/network/interfaces</td>
<td><p>If a VNI is configured before the bridge in <code>/etc/network/interfaces</code>, the switch does not send IGMP queries.</p>
<p>To work around this issue, edit the <code>/etc/network/interfaces</code> file to define the bridge before the VNI. For example:</p>
<pre><code># The primary network interface
auto eth0
iface eth0 inet dhcp

auto lo
iface lo inet loopback
    address 10.26.10.11/32

auto swp9
iface swp9
  bridge-access 100

auto swp10
iface swp10
    bridge-access 100 

auto bridge
iface bridge
   bridge-ports swp9 swp10 vni-10
   bridge-vids 100
   bridge-vlan-aware yes
   bridge-mcquerier 1

auto vni-10
iface vni-10
    vxlan-id 10
    vxlan-local-tunnelip 10.0.0.11
    bridge-access 100

auto bridge.100
vlan bridge.100
  bridge-igmp-querier-src 123.1.1.1

auto vlan100
iface vlan100
    address 10.26.100.2/24
    vlan-id 100
    vlan-raw-device bridge</code></pre>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN1004"></span> <a href="#RN1004"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1004 (CM-21496)</td>
<td>Scalability of redistribute neighbor limits the number of supported hosts</td>
<td><p>A Cumulus Linux switch cannot manage Docker containers running on 500 hosts. Entries in table 10 start to expire and are removed from the table.</p>
<p>To work around this issue, modify the ebtable rules for <code>set-rate</code> and <code>set-burst</code>, increasing their values until the issue is resolved. For example, configure <code>set-rate=1200</code> and <code>set-burst=300</code>.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1006"></span> <a href="#RN1006"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1006 (CM-20644)</td>
<td>The ptp4l and phc2sys services are enabled by default resulting in repeated syslog messages</td>
<td><p>In Cumulus Linux 3.6.1 and later, the ptp4l and phc2sys services are enabled by default. If you are not using PTP or PTP is not configured, the logs are repeatedly filled with messages similar to the following.</p>
<pre><code>2018-06-20T15:38:44.490543+00:00 cumulus phc2sys: [1542.230] Waiting for ptp4l...
2018-06-20T15:38:44.491160+00:00 cumulus phc2sys: [1542.230] uds: sendto failed: No such file or directory
2018-06-20T15:38:45.491747+00:00 cumulus phc2sys: [1543.231] Waiting for ptp4l...
2018-06-20T15:38:45.492259+00:00 cumulus phc2sys: [1543.231] uds: sendto failed: No such file or directory
2018-06-20T15:38:46.492925+00:00 cumulus phc2sys: [1544.233] Waiting for ptp4l...
2018-06-20T15:38:46.493440+00:00 cumulus phc2sys: [1544.233] uds: sendto failed: No such file or directory</code></pre>
<p>To work around this issue in Cumulus Linux 3.6.2, add <code>StartLimitInterval</code> to both the ptp4l and phc2sys services as shown below:</p>
<pre><code>sudo mkdir -p /etc/systemd/system/ptp4l.service.d /etc/systemd/system/phc2sys.service.d
sudo sh -c &#39;/bin/echo -e &quot;[Service]\nStartLimitInterval=375&quot; &gt; /etc/systemd/system/phc2sys.service.d/startinterval.conf&#39;
sudo sh -c &#39;/bin/echo -e &quot;[Service]\nStartLimitInterval=375&quot; &gt; /etc/systemd/system/ptp4l.service.d/startinterval.conf&#39;
sudo systemctl daemon-reload</code></pre>
<p>This issue should be fixed in a future release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="RN1027"></span> <a href="#RN1027"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1027 (CM-21707)</td>
<td>On Maverick switches, enabling auto-negotiation on 10G (all) and 1G SFP RJ45 breaks the link</td>
<td><p>On a Maverick switch, if auto-negotiation is configured on a 10G interface and the installed module does not support auto-negotiation (for example, 10G DAC, 10G Optical, 1G RJ45 SFP), the link breaks.</p>
<p>To work around this issue, disable auto-negotiation on interfaces where it is not supported. See the <a href="https://docs.cumulusnetworks.com/cumulus-linux-36/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/#interface-configuration-recommendations" class="external-link">Interface Configuration Recommendations</a> for information about configuring auto-negotiation.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1062"></span> <a href="#RN1062"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1062 (CM-22863)</td>
<td>Input chain ACLs do not apply in hardware on Broadcom platforms</td>
<td><p>Input chain ACLs do not apply in hardware on Broadcom platforms and input packets are processed against rules in the kernel instead. This can result in rules with the drop action not applying in hardware and the packets reaching the kernel.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN1168"></span> <a href="#RN1168"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1168 (CM-22538)</td>
<td>If the /etc/network/interfaces alias is different from the frr.conf description, an /etc/frr/daemons error occurs when deleting the interface</td>
<td><p>When deleting an interface using NCLU, if the <code>/etc/network/interfaces</code> alias is different than the <code>/etc/frr/frr.conf</code> description, the <code>net commit</code> command returns the following error:</p>
<p>"/etc/frr/daemons was modified by another user."</p>
<p>Despite this error being returned, the change still goes through, and the description gets removed from the <code>frr.conf</code> file.</p>
<p>This issue is fixed in Cumulus Linux 3.7.0.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1200"></span> <a href="#RN1200"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1200 (CM-21566)</td>
<td>Changing BGP autonomous system numbers (ASN) when using EVPN stops programming of VXLAN forwarding entries</td>
<td><p>If you change the ASN configuration on a switch running EVPN then reload the FRR service (using <code>sudo systemctl reload frr</code> or via <code>net commit</code>), the programming of VXLAN forwarding entries breaks.</p>
<p>To avoid this issue when making this change, restart the FRR process (using <code>sudo systemctl restart frr</code>) instead.</p>
<p>This issue is fixed in Cumulus Linux 3.7.0.</p></td>
</tr>
<tr class="even">
<td><span id="RN1315"></span> <a href="#RN1315"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1315 (CM-24330)</td>
<td>On a Mellanox switch, when you change the VRF membership on an SVI with VRR configured, the VRR MAC is not programmed into hardware</td>
<td><p>On a Mellanox switch, when you change the VRF membership of an interface with VRR enabled, the VRR MAC address is not properly programmed into hardware.</p>
<p>To work around this issue, delete and recreate the interface using <code>ifup</code> and <code>ifdown</code>.</p>
<p>This is a known issue that is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1334"></span> <a href="#RN1334"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1334 (CM-24316)</td>
<td>MSTP ignores BPDU from a dual-connected system</td>
<td><p>MSTP ignores BPDU from a dual-connected system.</p>
<p>This is a known issue that is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="RN1455"></span> <a href="#RN1455"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1455 (CM-24858)</td>
<td>On Broadcom switches,TPID programming is not reset on configuration change</td>
<td><p>On the Broadcom switch, TPID programming is not reset when there is a configuration change. As a result, you see unexpected packet drops.</p>
<p>This is a known issue that is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="RN1485"></span> <a href="#RN1485"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1485 (CM-20864)</td>
<td>The NCLU command to configure route leaking fails if the VRF is named 'red'</td>
<td><p>The NCLU command to configure route leaking fails if the VRF is named red. This is not a problem if the VRF is named RED (uppercase letters) or has a name other than red.</p>
<p>To work around this issue, rename the VRF or run the vtysh command instead.</p>
<p>This is a known issue that is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="RN1524"></span> <a href="#RN1524"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-1524 (CM-25754)</td>
<td>ARP replies are not forwarded as VXLAN over VXLAN</td>
<td><p>A port that is used as both a double tag interface and a VXLAN access side interface does not forward correctly; VXLAN decapsulation is does not occur.</p>
<p>This is a known issue that is currently being investigated.</p></td>
</tr>
</tbody>
</table>

## Issues Fixed in Cumulus Linux 3.6.1

The following is a list of issues fixed in Cumulus Linux 3.6.1 from
earlier versions of Cumulus Linux.

<table>

<tbody>
<tr class="odd">
<th>Release Note ID</th>
<th>Summary</th>
<th>Description</th>
</tr>
<tr class="even">
<td><span id="rn766"></span> <a href="#rn766"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-766 (CM-19006)</td>
<td>On the Broadcom Trident II+ and Maverick platform, in an external VXLAN routing environment, the switch does not rewrite MAC addresses and TTL, so packets are dropped by the next hop</td>
<td><p>On the Broadcom Trident II+ and Maverick based switch, in an external VXLAN routing environment, when a lookup is done on the external-facing switch (exit/border leaf) after VXLAN decapsulation, the switch does not rewrite the MAC addresses and TTL; for through traffic, packets are dropped by the next hop instead of correctly routing from a VXLAN overlay network into a non-VXLAN external network (for example, to the Internet).</p>
<p>This issue affects all traffic from VXLAN overlay hosts that need to be routed after VXLAN decapsulation on an exit/border leaf, including:</p>
<ul>
<li>Traffic destined to external networks (through traffic)</li>
<li>Traffic destined to the exit leaf SVI address</li>
</ul>
<p>To work around this issue, modify the external-facing interface for each VLAN sub-interface by creating a temporary VNI and associating it with the existing VLAN ID.</p>
<p>For example, if the expected interface configuration is:</p>
<pre><code>auto swp3.2001
iface swp3.2001
    vrf vrf1
    address 45.0.0.2/24
# where swp3 is the external facing port and swp3.2001 is the VLAN sub-interface

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge ports vx-4001
    bridge-vids 4001

auto vx-4001
iface vx-4001
    vxlan-id 4001
    &lt;... usual vxlan config ...&gt;
    bridge-access 4001
\# where vnid 4001 represents the L3 VNI

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1</code></pre>
<p>Modify the configuration as follows:</p>
<pre><code>auto swp3
iface swp3
    bridge-access 2001
# associate the port (swp3) with bridge 2001

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge ports swp3 vx-4001 vx-16000000
    bridge-vids 4001 2001
\# where vx-4001 is the existing VNI and vx-16000000 is a new temporary VNI
\# this is now bridging the port (swp3), the VNI (vx-4001),
\# and the new temporary VNI (vx-16000000)
\# the bridge VLAN IDs are now 4001 and 2001

auto vlan2001
iface vlan2001
    vlan-id 2001
    vrf vrf1
    address 45.0.0.2/24
    vlan-raw-device bridge
\# create a VLAN 2001 with the associated VRF and IP address

auto vx-16000000
iface vx-16000000
    vxlan-id 16000000
    bridge-access 2001
    &lt;... usual vxlan config ...&gt;
\# associate the temporary VNI (vx-16000000) with bridge 2001

auto vx-4001
iface vx-4001
    vxlan-id 4001
    &lt;... usual vxlan config ...&gt;
    bridge-access 4001
\# where vnid 4001 represents the L3 VNI

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1</code></pre></td>
</tr>
<tr class="odd">
<td><span id="RN860"></span> <a href="#RN860"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-860 (CM-20695)</td>
<td>Tab completion with 'net add vxlan' command produces traceback in the log</td>
<td><p>When using tab completion with the <code>net add vxlan</code> command, the following traceback appears in the log:</p>
<div class="preformatted panel" style="border-width: 1px;">
<div class="preformattedContent panelContent">
<pre><code>ERROR: &#39;name&#39;
Traceback (most recent call last):
File &quot;/usr/lib/python2.7/dist-packages/nclu/__init__.py&quot;, line 789, in get_lldp
lldp[value[&#39;name&#39;]] = value[&#39;chassis&#39;][0][&#39;name&#39;][0][&#39;value&#39;]
KeyError: &#39;name&#39;</code></pre>
</div>
</div>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="even">
<td><span id="RN876"></span> <a href="#RN876"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-876 (CM-20776)</td>
<td>EVPN symmetric IRB with numbered neighbors omits the NEXTHOP attribute when advertising to an external router</td>
<td><p>With EVPN symmetric routing (including type-5 routes) you can only advertise host routes or prefix routes learned through EVPN to a VRF peer if EVPN peering uses BGP unnumbered. If the BGP peering is numbered, the <code>NEXTHOP of MP_REACH</code> attribute is not included, which causes the neighbor to reply with a BGP notification.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="odd">
<td><span id="RN887"></span> <a href="#RN887"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-887 (CM-20474)</td>
<td>VXLAN Encapsulation drops ARP QinQ tunneled packets</td>
<td><p>When an ARP request or response (or IPv6 NS/NA) packet with double VLAN tags (such as 802.1Q over 802.1Q), is sent to a VXLAN overlay, the outer VLAN tag is stripped during VXLAN encapsulation. If the receiving VTEP is a Broadcom Trident II + platform, the post VXLAN decapsulated packet is incorrectly directed to the control plane. As the packet traverses the linux kernel VXLAN interface into the VLAN-aware bridge device, the exposed inner VLAN tag is incorrectly used for VLAN filtering against the outer VLAN set, causing the packet to be discarded.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="even">
<td><span id="rn890"></span> <a href="#rn890"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-890 (CM-20415)</td>
<td>On Maverick QCT LY7, Tomahawk+ AS7312 and DNI AG5648 switches, sysfs tree differences cause portwd startup failure</td>
<td><p>Inserting a 1000 BASE-T RJ-45 SFP adapter into a Maverick QCT LY7, Tomahawk + AS7312 or DNI AG5648 switch causes <code>portwd</code> to fail to start, resulting in the switch being unusable.</p>
<p>To work around this issue, do not use 1000BASE-T RJ-45 modules on the impacted switches.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="odd">
<td><span id="RN897"></span> <a href="#RN897"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-897 (CM-20086)</td>
<td>FRR doesn't support hostnames starting with a digit</td>
<td><p>NCLU reports an error attempting to configure FRR when the configured hostname begins with a digit:</p>
<div class="preformatted panel" style="border-width: 1px;">
<div class="preformattedContent panelContent">
<pre><code>unknown: buffer_flush_available: write error on fd -1: Bad file descriptor</code></pre>
</div>
</div>
<p>To work around this issue, change the hostname of the switch to begin with an alphabetic character; not a digit.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="even">
<td><span id="RN904"></span> <a href="#RN904"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-904 (CM-20800)</td>
<td>NCLU net add and net del commands missing for EVPN type-5 default originate</td>
<td><p>The NCLU <code>net add</code> and <code>net del</code> commands are missing for the default originate EVPN type-five route feature.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="odd">
<td><span id="RN907"></span> <a href="#RN907"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-907 (CM-20829)</td>
<td>netd fails on start after apt upgrade to 3.6.0 with "ImportError: No module named time"</td>
<td><p>When you use the <code>apt-get upgrade</code> command to upgrade to Cumulus Linux 3.6.0 and you select to keep the currently-installed version of <code>netd.conf</code> (by typing N at the prompt), <code>netd</code> fails to start after reboot and you see errors in the logs when you try to restart <code>netd</code>.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="even">
<td><span id="RN933"></span> <a href="#RN933"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-933 (CM-20781)</td>
<td>NCLU 'net add bgp neighbor' command with swp1, swp2, or swp1-2 causes TB NameError</td>
<td><p>Issuing the <code>net add bgp neighbor</code> command with swp1, swp2 or swp1-2 causes the following error:</p>
<div class="preformatted panel" style="border-width: 1px;">
<div class="preformattedContent panelContent">
<pre><code>TB NameError: global name &#39;ifname_expand_glob&#39; is not defined.</code></pre>
</div>
</div>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="odd">
<td><span id="RN935"></span> <a href="#RN935"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-935 (CM-20772)</td>
<td>ACL rule unable to match interface eth0 when belonging to VRF</td>
<td><p>ACL rules do not block incoming packets when interface eth0 belongs to a VRF.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="even">
<td><span id="RN936"></span> <a href="#RN936"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-936 (CM-20418)</td>
<td>ACL to only allow ARP prevents ARP on SVIs</td>
<td><p>ACL rules that only allow ARP packets prevent ARP packets from reaching SVIs.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="odd">
<td><span id="RN937"></span> <a href="#RN937"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-937 (CM-19301)</td>
<td>Increase maximum sflow sampling ratio</td>
<td><p>The maximum sflow sampling ratio is too low and might overload the switch CPU.</p>
<p>This is fixed in Cumulus Linux 3.6.1. The ratio is increased to 1:100000 in hsflowd.</p></td>
</tr>
<tr class="even">
<td><span id="RN944"></span> <a href="#RN944"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-944 (CM-20841)</td>
<td>netd fails to start for apt-upgrade from 3.3.2 to 3.6.0</td>
<td><p>When upgrading from Cumulus Linux 3.3.2 to 3.6.0 using the <code>netd.conf</code> file from version 3.3.2, <code>netd</code> fails to start and displays the error <code>ImportError: No module named frr-reload</code>.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="odd">
<td><span id="RN945"></span> <a href="#RN945"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-945 (CM-20311)</td>
<td>Security: DSA-4157-1 for openssl issues CVE-2017-3738 CVE-2018-0739</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4157-1, and affect the openssl package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p>
<p>--------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4157-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>March 29, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>--------------------------------------------------------------------------</p>
<p>Package : openssl</p>
<p>CVE ID : CVE-2017-3738 CVE-2018-0739</p>
<p>Multiple vulnerabilities have been discovered in OpenSSL, a Secure Sockets Layer toolkit. The Common Vulnerabilities and Exposures project identifies the following issues:</p>
<p>CVE-2017-3738</p>
<p>David Benjamin of Google reported an overflow bug in the AVX2 Montgomery multiplication procedure used in exponentiation with 1024-bit moduli.</p>
<p>CVE-2018-0739</p>
<p>It was discovered that constructed ASN.1 types with a recursive definition could exceed the stack, potentially leading to a denial of service.</p>
<p>Details can be found in the upstream advisory:</p>
<p><a href="https://www.openssl.org/news/secadv/20180327.txt" class="external-link">https://www.openssl.org/news/secadv/20180327.txt</a></p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 1.0.1t-1+deb8u8. The oldstable distribution is not affected by CVE-2017-3738.</p>
<p>For the stable distribution (stretch), these problems have been fixed in version 1.1.0f-3+deb9u2.</p>
<p>We recommend that you upgrade your openssl packages.</p>
<p>For the detailed security status of openssl please refer to its security tracker page at:</p>
<p><a href="https://security-tracker.debian.org/tracker/openssl" class="external-link">https://security-tracker.debian.org/tracker/openssl</a></p></td>
</tr>
<tr class="even">
<td><span id="RN946"></span> <a href="#RN946"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-946 (CM-20603)</td>
<td>Security: DSA-4172-1 for perl issues CVE-2018-6797 CVE-2018-6798 CVE-2018-6913</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4172-1 and affect the perl package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p>
<p>--------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4172-1 security@debian.org</p>
<p><a href="https://www.debian.org/security/" class="external-link">https://www.debian.org/security/</a> Salvatore Bonaccorso</p>
<p>April 14, 2018 <a href="https://www.debian.org/security/faq" class="external-link">https://www.debian.org/security/faq</a></p>
<p>--------------------------------------------------------------------------</p>
<p>Package : perl</p>
<p>CVE ID : CVE-2018-6797 CVE-2018-6798 CVE-2018-6913</p>
<p>Multiple vulnerabilities were discovered in the implementation of the Perl programming language. The Common Vulnerabilities and Exposures project identifies the following problems:</p>
<p>CVE-2018-6797</p>
<p>Brian Carpenter reported that a crafted regular expression could cause a heap buffer write overflow, with control over the bytes written.</p>
<p>CVE-2018-6798</p>
<p>Nguyen Duc Manh reported that matching a crafted locale dependent regular expression could cause a heap buffer read overflow and potentially information disclosure.</p>
<p>CVE-2018-6913</p>
<p>GwanYeong Kim reported that 'pack()' could cause a heap buffer write overflow with a large item count.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 5.20.2-3+deb8u10. The oldstable distribution (jessie) update contains only a fix for CVE-2018-6913.</p>
<p>For the stable distribution (stretch), these problems have been fixed in version 5.24.1-3+deb9u3.</p>
<p>We recommend that you upgrade your perl packages.</p>
<p>For the detailed security status of perl please refer to its security tracker page at:</p>
<p><a href="https://security-tracker.debian.org/tracker/perl" class="external-link">https://security-tracker.debian.org/tracker/perl</a></p></td>
</tr>
<tr class="odd">
<td><span id="RN949"></span> <a href="#RN949"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-949 (CM-21038)</td>
<td>VRF stops working when /etc/resolv.conf does not exist</td>
<td><p>When upgrading to Cumulus Linux 3.6.0, if the <code>/etc/resolv.conf</code> file does not exist and eth0 is configured with a static IP address, the switch fails to start VRFs after reboot.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="even">
<td><span id="RN958"></span> <a href="#RN958"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-958 (CM-21095)</td>
<td>NCLU 'net add bgp neighbor ' command does not create or enable the interface if it is not previously defined</td>
<td><p>When you run the <code>net add bgp neighbor &lt;interface&gt;</code> command, the interface is only added if previously defined.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
<tr class="odd">
<td><span id="RN962"></span> <a href="#RN962"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-962 (CM-21026)</td>
<td>DHCP request packets in VXLAN decapsulation do not go to CPU</td>
<td><p>On Broadcom platforms configured with a VXLAN centralized routing gateway, DHCP discover packets are not correctly processed for DHCP relay.</p>
<p>This issue is fixed in Cumulus Linux 3.6.1.</p></td>
</tr>
</tbody>
</table>

## New Known Issues in Cumulus Linux 3.6.1

The following issues are new to Cumulus Linux and affect the current release.

<table>

<tbody>
<tr class="odd">
<th>Release Note ID</th>
<th>Summary</th>
<th>Description</th>
</tr>
<tr class="even">
<td><span id="RN875"></span> <a href="#RN875"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-875 (CM-20779)</td>
<td>On Mellanox switches, withdrawal of one ECMP next-hop results in the neighbor entry for that next hop to be missing from hardware</td>
<td><p>On a Mellanox switch, when you withdraw one ECMP next hop, the neighbor entry for that next hop is missing from the hardware.</p>
<p>To work around this issue, manually delete the ARP entry from kernel with the <code>arp -d</code> command to repopulate it in the hardware.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="RN938"></span> <a href="#RN938"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-938 (CM-20979)</td>
<td>Removing a VLAN from a bridge configured with VXLAN results in an outage</td>
<td><p>Removing a VLAN from a bridge configured with VXLAN causes a network service outage until the configuration change is reverted with the <code>net rollback last</code> command.</p>
<p>To work around this issue, remove the VNI interface first, then remove the unused VLAN from the bridge.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN939"></span> <a href="#RN939"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-939 (CM-20944)</td>
<td>On Maverick switches, random links might not come up on boot when enabling RS FEC with 100G AOC cables</td>
<td><p>On Maverick 100G switches, after enabling FEC on links with 100G AOC cables, random links do not come up after a reboot.</p>
<p>To work around this issue, disable FEC on 100G AOC links.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN940"></span> <a href="#RN940"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-940 (CM-20813)</td>
<td>On Mellanox switches, packets are not mirrored on matching '-out-interface bond0' SPAN rules</td>
<td><p>Span rules that match the out-interface as a bond do not mirror packets.</p>
<p>This is a regression of an earlier issue and is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN941"></span> <a href="#RN941"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-941 (CM-20806)</td>
<td>When configuring layer 2 VPN EVPN in vtysh, if the route-target matches the VNI and AS number, the configuration does not display the route target</td>
<td><p>When configuring layer 2 VPN EVPN in vtysh, if a <code>route-target</code> matches both the AS number and the VNI number, the route target does not display in the configuration. This is currently the default behavior.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN942"></span> <a href="#RN942"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-942 (CM-20693)</td>
<td>In NCLU, you can only set the community number in a route map</td>
<td><p>In NCLU, you can only set the community number in a route map. You cannot set other community options such as <code>no-export</code>, <code>no-advertise</code>, or <code>additive</code>.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN943"></span> <a href="#RN943"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-943 (CM-20639)</td>
<td>The neighbor table and EVPN routes are not updated on receiving GARP from an IP address that moved to a new MAC address</td>
<td><p>After moving an IP address to a new host, the neighbor table and EVPN routes do not update properly after receiving a GARP from the new MAC address to which the previously-active IP address has been moved.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN947"></span> <a href="#RN947"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-947 (CM-20992)</td>
<td>RS FEC configuration cleared and not re-installed on switchd restart, leaving links down</td>
<td><p>During <code>switchd</code> restart, the RS FEC configuration is not re-installed to the interfaces to which it was previously applied.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN948"></span> <a href="#RN948"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-948 (CM-17494)</td>
<td>The default arp_ignore mode does not prevent reachable neighbor entries for hosts not on the connected subnet</td>
<td><p>In certain cases, a peer device sends an ARP request from a source IP address that is not on the connected subnet and the switch creates a STALE neighbor entry. Eventually, the switch attempts to keep the entry fresh and sends ARP requests to the host. If the host responds, the switch has REACHABLE neighbor entries for hosts that are not on the connected subnet.</p>
<p>To work around this issue, change the value of <code>arp_ignore</code> to 2. See <a href="https://docs.cumulusnetworks.com/cumulus-linux-36/Layer-3/Address-Resolution-Protocol-ARP/" class="external-link">Default ARP Settings in Cumulus Linux</a> for more information.</p></td>
</tr>
<tr class="odd">
<td><span id="RN951"></span> <a href="#RN951"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-951 (CM-21048)</td>
<td>NCLU command fails to delete the VRF static route</td>
<td><p>The NCLU command <code>net del routing route</code> does not delete a static route within a VRF.</p>
<p>To work around this issue, delete the VRF static route using <code>vtysh</code>, either directly in configuration mode or with <code>vtysh -c</code>.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN952"></span> <a href="#RN952"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-952 (CM-21090)</td>
<td>NCLU 'net show bridge macs' command improperly displays the 'never' keyword</td>
<td><p>When you use the <code>net show bridge macs</code> command and a MAC address has just been updated, the <code>never</code> keyword improperly displays in the command output.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN953"></span> <a href="#RN953"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-953 (CM-21082)</td>
<td>Virtual device counters not working as expected</td>
<td><p>Virtual device counters are not working as expected. The TX counter increments but the RX counter does not.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN954"></span> <a href="#RN954"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-954 (CM-21062)</td>
<td>Redundant NCLU commands to configure the DHCP relay exits with return code 1</td>
<td><p>When using the NCLU command to add a redundant DHCP relay, the command exits with an error instead of displaying a message that the DHCP relay server configuration already contains the IP address.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN955"></span> <a href="#RN955"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-955 (CM-21060)</td>
<td>NCLU 'net show configuration' output is out of order</td>
<td><p>When you run the <code>net show configuration</code> command after upgrading to Cumulus Linux 3.6, the interfaces display are out of order in the command output.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN956"></span> <a href="#RN956"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-956 (CM-21055)</td>
<td>On Mellanox switches, the destination MAC of ERSPAN GRE packets is set to all zeros</td>
<td><p>On Mellanox switches, the destination MAC of ERSPAN GRE packets is set to all zeros; therefore, the packets are dropped by the first transient switch.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN959"></span> <a href="#RN959"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-959 (CM-21167)</td>
<td>BGP aggregate created but left inactive in the routing table</td>
<td><p>If you use BGP to generate an aggregate, the aggregate shows up in the BGP table but is listed in zebra as inactive.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="RN960"></span> <a href="#RN960"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-960 (CM-21154)</td>
<td>Deleting an interface with the NCLU command does not remove the interface in frr.conf</td>
<td><p>When you use NCLU to delete an interface, the associated configuration is not removed from the <code>frr.conf</code> file.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="RN963"></span> <a href="#RN963"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-963 (CM-21362)</td>
<td>Bringing down a bridge member interface sets the interface MTU to 1500 and the bridge MTU to 1500</td>
<td><p>When you bring down an interface for a bridge member, the MTU for the interface and the MTU for the bridge are both set to 1500.</p>
<p>To work around this issue, run <code>ifdown</code> on the interface, then run the <code>sudo ip link set dev &lt;interface&gt; mtu &lt;mtu&gt;</code> command.</p>
<p>For example:</p>
<pre><code>sudo ifdown swp3
sudo ip link set dev swp3 mtu 9192</code></pre>
<p>As an alternative, in the <code>/etc/network/interfaces</code> file, add a <code>post-down</code> command to reset the MTU of the interface. For example:</p>
<pre><code>auto swp3
iface swp3
    alias BNBYLAB-PD01HV-01_Port3
    bridge-vids 106 109 119 141 150-151
    mtu 9192
    post-down /sbin/ip link set dev swp3 mtu 9192</code></pre></td>
</tr>
<tr class="even">
<td><span id="RN964"></span> <a href="#RN964"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-964 (CM-21319)</td>
<td>When upgrading to Cumulus Linux 3.6, static routes in the default VRF are associated with other VRFs</td>
<td><p>When you upgrade to Cumulus Linux 3.6.x, static routes configured in the <code>frr.conf</code> file become associated with the VRF configured above them.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="RN965"></span> <a href="#RN965"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-965 (CM-21313, CM-15657)</td>
<td>Errors occur if comma-separated globs exist in the /etc/network/interfaces file</td>
<td><p>If you edit the <code>/etc/network/interfaces</code> file manually and add bridge VIDs to an interface using the NCLU syntax (comma separated globs), you see an error similar to the following:</p>
<pre><code>ERROR: numbers_to_glob() could not extract any IDs from [&#39;1,4,1000,1002,1006&#39;]</code></pre>
<p>To work around this issue, separate globs with spaces when manually editing the <code>/etc/network/interfaces</code> file.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="RN966"></span> <a href="#RN966"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-966 (CM-21297)</td>
<td>TACACS authenticated users in 'netshow' or 'netedit' groups cannot issue 'net' commands after upgrade to Cumulus Linux 3.6</td>
<td><p>When upgrading from a previous release to Cumulus Linux 3.6, TACACS-authenticated users mapped to tacacs0 thru tacacs15 users with the netshow or netedit user groups cannot run <code>net</code> commands and they see the following error:</p>
<pre><code>ERROR: You do not have permission to execute that command</code></pre>
<p>This behavior is seen when upgrading with simple authentication only and occurs without a restricted shell for command authorization being enabled.</p>
<p>This problem is not present on a binary install of 3.6.0 or 3.6.1 and only happens when upgrading from previous releases.</p>
<p>To work around this issue, edit the <code>/etc/netd.conf</code> file, add the <code>tacacs</code> user group to the <code>groups_with_show</code> list, and add the <code>tacacs15</code> user to the <code>users_with_edit</code> list as below:</p>
<pre><code># Control which users/groups are allowed to run &quot;add&quot;, &quot;del&quot;,
# &quot;clear&quot;, &quot;abort&quot;, and &quot;commit&quot; commands.
users_with_edit = root, cumulus, vagrant, tacacs15
groups_with_edit = netedit

\# Control which users/groups are allowed to run &quot;show&quot; commands.
users_with_show = root, cumulus, vagrant
groups_with_show = netshow, netedit, tacacs</code></pre>
<p>After making this change, restart <code>netd</code> with the <code>sudo systemctl restart netd</code> command.</p></td>
</tr>
<tr class="odd">
<td><span id="RN969"></span> <a href="#RN969"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-969 (CM-21278)</td>
<td>NCLU 'net show lldp' output has PortDescr as Remote Port</td>
<td><p>When you run the <code>net show lldp</code> command, the command output incorrectly displays the remote port as the port description.</p>
<p>To work around this issue, run the <code>net show interface</code> command when connected to Cisco equipment.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="RN970"></span> <a href="#RN970"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-970 (CM-21203)</td>
<td>VXLAN and tcam_resource_profile set to acl-heavy, causes the switch to crash</td>
<td><p>Changing <code>tcam_resource_profile</code> to <code>acl-heavy</code> on a switch with VXLAN enabled and attempting to apply the configuration with a <code>switchd</code> restart, causes <code>switchd</code> to fail to restart, <code>netd</code> to crash, the switch to become temporarily unresponsive, and a cl-support to be generated.</p>
<p>To work around this issue, remove the <code>acl-heavy</code> profile or the VXLAN configuration.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="RN971"></span> <a href="#RN971"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-971 (CM-20501)</td>
<td>cl-ecmpcalc is not supported on Maverick (Broadcom 5676x) ASICs</td>
<td><p>The <code>cl-ecmpcalc</code> tool is not supported on platforms based on ASICs in the Broadcom 5676x (Maverick) family.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
</tbody>
</table>

## Issues Fixed in Cumulus Linux 3.6.0

The following is a list of issues fixed in Cumulus Linux 3.6.0 from earlier versions of Cumulus Linux.

<table>

<tbody>
<tr class="odd">
<th>Release Note ID</th>
<th>Summary</th>
<th>Description</th>
</tr>
<tr class="even">
<td><span id="rn406"></span> <a href="#rn406"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-406 (CM-9895)</td>
<td>Mellanox SN2700 power off issues</td>
<td><p>The Mellanox SN2700 or SN2700B switch appears to be unresponsive for at least three minutes after a PDU power cycle is issued, if any of the following occur:</p>
<ul>
<li>A <code>shutdown</code> or <code>poweroff</code> command is executed</li>
<li>A temperature sensor hits a critical value and shuts down the box</li>
</ul>
<p>To fix this, update the system CPLD to version CPLD000085. Contact Mellanox support for assistance.</p></td>
</tr>
<tr class="odd">
<td><span id="rn545"></span> <a href="#rn545"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-545 (CM-13800)</td>
<td>OSPFv3 redistribute connected with route-map broken at reboot (or ospf6d start)</td>
<td><p>This issue only affects OSPFv3 (IPv6).</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn608"></span> <a href="#rn608"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-608 (CM-16145)</td>
<td>Buffer monitoring default port group discards_pg only accepts packet collection type</td>
<td><p>The default port group <code>discards_pg</code> does not accept <code>packet_extended</code> or <code>packet_all</code> collection types.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn704"></span> <a href="#rn704"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-704 (CM-18886, CM-20027)</td>
<td>ifreload causes MTU to drop on bridge SVIs </td>
<td><p>When you run the <code>ifreload</code> command on a bridge SVI with an MTU higher than 1500, the MTU resets to 1500 after the initial <code>ifreload -a</code>, then resets to its original value when running <code>ifreload -a</code> for the second time.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn738"></span> <a href="#rn738"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-738 (CM-18709)</td>
<td>On Dell S4148<strong>T</strong>-ON switches with Maverick ASICs, configuring 1G or 100M speeds on 10G fixed copper ports requires a ports.conf workaround</td>
<td><p>1G and 100M speeds on SFP ports are not working on the Dell S4148<strong>T</strong>-ON.</p>
<p>To enable a speed lower than 10G on a port on the S4148T platform, you must dedicate an entire port group (four interfaces) to a lower speed setting. Within a port group, you can mix 1G and 100M speeds, if needed. You cannot mix 10G and lower speeds.</p>
<p>To work around this issue:</p>
<ol>
<li><p>In the <code>/etc/cumulus/ports.conf</code> file, add each of the four ports in the port group as 1G interfaces. You must set each of the ports in the port group to be 1G. Port groups are swp1-4, swp5-8, swp9-12, and so on, and starting with swp31-35 on the right half of the switch. For example, to enable ports swp5-swp8 to autonegotiate to 100M or 1G speeds, add the following to the ports.conf file:<br />
</p>
<pre><code>5=1G
6=1G
7=1G
8=1G</code></pre></li>
<li><p>Restart <code>switchd</code>:<br />
</p>
<pre><code>cumulus@switch:~$ sudo systemctl reset-failed switchd; sudo systemctl restart switchd</code></pre>
<p>After this is done ports swp5-8 will be enabled to autonegotiate with the neighbor devices to 1G or 100M speeds.</p></li>
</ol>
<p>As of 3.5.1, 1G interfaces are supported when using the <code>ports.conf</code> file workaround as described above. As of 3.6.0, editing the <code>ports.conf</code> file is no longer required.</p></td>
</tr>
<tr class="odd">
<td><span id="rn743"></span> <a href="#rn743"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-743 (CM-18612)</td>
<td>Routes learned through BGP unnumbered become unusable</td>
<td><p>In certain scenarios, the routes learned through BGP unnumbered become unusable. The BGP neighbor relationships remain but the routes cannot be forwarded due to a failure in layer 2 and layer 3 next hop/MAC address resolution.</p>
<p>To work around this issue, restart FRR.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn759"></span> <a href="#rn759"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-759 (CM-18401)</td>
<td>The output for the NCLU net show config command is incorrect</td>
<td><p>The output for the NCLU <code>net show config</code> command is incorrect.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn766"></span> <a href="#rn766"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-766 (CM-19006)</td>
<td>On the Broadcom Trident II+ and Maverick platform, in an external VXLAN routing environment, the switch does not rewrite MAC addresses and TTL, so packets are dropped by the next hop</td>
<td><p>On the Broadcom Trident II+ and Maverick based switch, in an external VXLAN routing environment, when a lookup is done on the external-facing switch (exit/border leaf) after VXLAN decapsulation, the switch does not rewrite the MAC addresses and TTL; for through traffic, packets are dropped by the next hop instead of correctly routing from a VXLAN overlay network into a non-VXLAN external network (for example, to the Internet).</p>
<p>This issue affects all traffic from VXLAN overlay hosts that need to be routed after VXLAN decapsulation on an exit/border leaf, including:</p>
<ul>
<li>Traffic destined to external networks (through traffic)</li>
<li>Traffic destined to the exit leaf SVI address</li>
</ul>
<p>This issue should be fixed in the Trident 3 ASIC.</p>
<p>To work around this issue, modify the external-facing interface for each VLAN sub-interface by creating a temporary VNI and associating it with the existing VLAN ID.</p>
<p>For example, if the expected interface configuration is:</p>
<pre><code>auto swp3.2001
iface swp3.2001
    vrf vrf1
    address 45.0.0.2/24
# where swp3 is the external facing port and swp3.2001 is the VLAN sub-interface

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge ports vx-4001
    bridge-vids 4001

auto vx-4001
iface vx-4001
    vxlan-id 4001
    &lt;... usual vxlan config ...&gt;
    bridge-access 4001
\# where vnid 4001 represents the L3 VNI

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1</code></pre>
<p>Modify the configuration as follows:</p>
<pre><code>auto swp3
iface swp3
    bridge-access 2001
# associate the port (swp3) with bridge 2001

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge ports swp3 vx-4001 vx-16000000
    bridge-vids 4001 2001
\# where vx-4001 is the existing VNI and vx-16000000 is a new temporary VNI
\# this is now bridging the port (swp3), the VNI (vx-4001),
\# and the new temporary VNI (vx-16000000)
\# the bridge VLAN IDs are now 4001 and 2001

auto vlan2001
iface vlan2001
    vlan-id 2001
    vrf vrf1
    address 45.0.0.2/24
    vlan-raw-device bridge
\# create a VLAN 2001 with the associated VRF and IP address

auto vx-16000000
iface vx-16000000
    vxlan-id 16000000
    bridge-access 2001
    &lt;... usual vxlan config ...&gt;
\# associate the temporary VNI (vx-16000000) with bridge 2001

auto vx-4001
iface vx-4001
    vxlan-id 4001
    &lt;... usual vxlan config ...&gt;
    bridge-access 4001
\# where vnid 4001 represents the L3 VNI

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1</code></pre></td>
</tr>
<tr class="even">
<td><span id="rn778"></span> <a href="#rn778"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-778 (CM-19203)</td>
<td>On Dell 4148<strong>F</strong>-ON and 4128<strong>F</strong>-ON switches with Maverick ASICs, configuring 1G or 100M speeds requires a ports.conf workaround</td>
<td><p>1G and 100M speeds on SFP ports do not work automatically on Dell S4148<strong>F</strong>-ON and S4128<strong>F</strong>-ON switches.</p>
<p>To enable a speed lower than 10G on a port on the S4148F and S4128F platforms, you must dedicate an entire port group (four interfaces) to a lower speed setting. Within a port group, you can mix 1G and 100M speeds, if needed. You cannot mix 10G and lower speeds.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn785"></span> <a href="#rn785"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-785 (CM-19422)</td>
<td>NCLU 'net show interface detail' command does not display detailed output</td>
<td><p>The <code>net show interface swp#</code> command returns the same output as <code>net show interface swp# detail</code>.</p>
<p>To view the additional information typically presented, use alternative commands. For example, to view the module information and statistics, use <code>ethtool swp#</code> and <code>ethtool -S swp#</code>.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn787"></span> <a href="#rn787"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-787 (CM-19418)</td>
<td>NCLU 'net add hostname' creates an inconsistency between /etc/hostname and /etc/hosts files</td>
<td><p>Running the <code>net add hostname &lt;hostname&gt;</code> command updates both the <code>/etc/hostname</code> file and the<code>/etc/hosts</code> file. However, NCLU modifies the hostname value passed to the <code>/etc/hostname</code> file, removing certain characters and converting the hostname to lowercase, whereas the hostname passed to the <code>/etc/hosts</code> file is passed through as is, creating an inconsistency between the two files.</p>
<p>To work around this issue, manually set the hostname in both the <code>/etc/hostname</code> file and the <code>/etc/hosts</code> file using a text editor such as <code>vi</code> or <code>nano</code>.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn793"></span> <a href="#rn793"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-793 (CM-19321)</td>
<td>FRR does not detect the bandwidth for 100G interfaces correctly</td>
<td><p>FRR correctly detects the bandwidth for both 10G interfaces and 40G interfaces. However, it does not do so for 100G interfaces. Setting link speed manually does not fix this issue.</p>
<p>To work around this issue, restart the FRR service:</p>
<p><code>cumulus@switch:~$ sudo systemctl restart frr.service</code></p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn801"></span> <a href="#rn801"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-801 (CM-19195)</td>
<td>In VXLAN routing, border leafs in MLAG use anycast IP address after FRR restart</td>
<td><p>For type-5 routes, when an MLAG pair is used as border leaf nodes, the MLAG primary and secondary nodes use their respective loopback IP addresses as the originator IP address to start, but switch to using the MLAG anycast IP address after an FRR restart.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn803"></span> <a href="#rn803"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-803 (CM-19456)</td>
<td>EVPN and IPv4 routes change origin after redistribution</td>
<td><p>EVPN routes are re-injected into EVPN as type-5 routes when a type-5 advertisement is enabled. This issue occurs when advertising different subnets from different VTEPs into a type-5 EVPN symmetric mode environment.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn806"></span> <a href="#rn806"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-806 (CM-19241)</td>
<td>FRR removes all static routes when the service is stopped, including those created by ifupdown2</td>
<td><p>Whenever FRR is restarted, it deletes all routes in the kernel with a protocol type of BGP, ISIS, OSPF, and static. When you upgrade FRR and the service is stopped, the static routes defined in the <code>/etc/network/interfaces</code> file and installed using <code>ifupdown2</code> are also removed.</p>
<p>To work around this issue, configure static routes in the <code>/etc/network/interfaces</code> file as follows:</p>
<pre><code>post-up ip route add  via  proto kernel</code></pre>
<p>For example:</p>
<pre><code>auto swp2
iface swp2
  post-up ip route add 0.0.0.0/0 via 192.0.2.249 proto kernel</code></pre>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn807"></span> <a href="#rn807"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-807 (CM-17159)</td>
<td>NCLU 'net show interface &lt;bond&gt;' command shows interface counters that are not populated</td>
<td><p>The output of the NCLU <code>net show interface &lt;bond&gt;</code> command shows misleading and incorrect interface counters.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn809"></span> <a href="#rn809"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-809 (CM-19120)</td>
<td>The 'netshow lldp' command displays an error</td>
<td><p>When running the <code>netshow lldp</code> command, the output displays the following error:</p>
<pre><code>cumulus@switch:~# netshow lldp
ERROR: The lldpd service is running, but &#39;/usr/sbin/lldpctl -f xml&#39; failed.</code></pre>
<p>However, the NCLU <code>net show lldp</code> command works correctly.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn815"></span> <a href="#rn815"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-815 (CM-19630)</td>
<td>Bridge MAC address clashing when eth0 is part of the same broadcast domain</td>
<td><p>Cumulus Linux uses the eth0 MAC address as the MAC address for bridges. If eth0 is part of the same broadcast domain, you experience outages when upgrading.</p>
<p>To work around this issue, manually change the bridge MAC address in the <code>/etc/network/interfaces</code> file.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn820"></span> <a href="#rn820"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-820 (CM-19908)</td>
<td>RADIUS and TACACS Plus should use pam_syslog not openlog/syslog/closelog</td>
<td><p>The pam_syslog() interface is now being used to send messages to the system logger, which changes the message format. For example, with an incorrect password, the old message format for TACACS Plus is:</p>
<pre><code>Feb 27 21:06:02 switch3 PAM-tacplus[17368]: auth failed 2</code></pre>
<p>The new message format for TACACS Plus is:</p>
<pre><code>Feb 27 21:04:08 switch3 sshd[16676]: pam_tacplus(sshd:auth): auth failed 2</code></pre>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn821"></span> <a href="#rn821"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-821 (CM-19898)</td>
<td>The 'net show interface' command output missing information</td>
<td><p>The <code>net show interface</code> command output is missing LACP, CLAG, VLAN, LLDP, and physical link failure information.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn824"></span> <a href="#rn824"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-824 (CM-19667)</td>
<td>The show ipv6 route ospf command results in an unknown route type</td>
<td><p>When you run the <code>vtysh -c 'show ipv6 route ospf json'</code> command to show IPv6 routes through OSPF, you see the error <code>Unknown route type</code>. To work around this issue, you must specify <code>ospf6</code> in the command:</p>
<pre><code>cumulus@switch:~$  vtysh -c &#39;show ipv6 route ospf6 json&#39;</code></pre>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn826"></span> <a href="#rn826"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-826 (CM-16865)</td>
<td>The compute unique hash seed default value is the same for each switch</td>
<td><p>The algorithm that calculates hashing is the same on every switch instead of being unique.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn828"></span> <a href="#rn828"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-828 (CM-19748)</td>
<td>Security: Debian Security Advisory DSA-4110-1 for exim4 issue CVE-2018-6789</td>
<td><p>The following CVE was announced in Debian Security Advisory DSA-4110-1, and affects the exim4 package. While this package is no longer in the Cumulus Linux installation image, it is still in the repo3 repository. Cumulus Linux is built on Debian Jessie.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>-------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4110-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
February 10, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a><br />
-------------------------------------------------------------------------<br />
Package : exim4<br />
CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2018-6789" class="external-link" title="Follow link">CVE-2018-6789</a><br />
Debian Bug : 890000<br />
Meh Chang discovered a buffer overflow flaw in a utility function used in the SMTP listener of Exim, a mail transport agent. A remote attacker can take advantage of this flaw to cause a denial of service, or potentially the execution of arbitrary code via a specially crafted message.<br />
For the oldstable distribution (jessie), this problem has been fixed in version 4.84.2-2+deb8u5.<br />
For the stable distribution (stretch), this problem has been fixed in version 4.89-2+deb9u3.</p></td>
</tr>
<tr class="odd">
<td><span id="rn829"></span> <a href="#rn829"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-829 (CM-19660)</td>
<td>Security: Debian Security Advisory DSA-4052-1 for Bazaar issue CVE-2017-14176</td>
<td><p>The following CVE was announced in Debian Security Advisory DSA-4052-1, and affects the Bazaar version control system.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>-------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4052-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
November 29, 2017 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a><br />
-------------------------------------------------------------------------<br />
Package : bzr<br />
CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2017-14176" class="external-link" title="Follow link">CVE-2017-14176</a><br />
Debian Bug : 874429</p>
<p>Adam Collard discovered that Bazaar, an easy to use distributed version control system, did not correctly handle maliciously constructed bzr+ssh URLs, allowing a remote attackers to run an arbitrary shell command.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 2.6.0+bzr6595-6+deb8u1.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 2.7.0+bzr6619-7+deb9u1.</p></td>
</tr>
<tr class="even">
<td><span id="rn830"></span> <a href="#rn830"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-830 (CM-19595)</td>
<td>Security: Debian Security Advisory DSA-4098-1 for curl issues CVE-2018-1000005 CVE-2018-1000007</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4098-1, and affect the curl package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>-------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4098-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Alessandro Ghedini<br />
January 26, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a><br />
-------------------------------------------------------------------------<br />
Package : curl<br />
CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2018-1000005" class="external-link" title="Follow link">CVE-2018-1000005</a><a href="https://security-tracker.debian.org/tracker/CVE-2018-1000007" class="external-link" title="Follow link">CVE-2018-1000007</a><br />
Two vulnerabilities were discovered in cURL, an URL transfer library.</p>
<p>CVE-2018-1000005<br />
Zhouyihai Ding discovered an out-of-bounds read in the code handling HTTP/2 trailers. This issue doesn't affect the oldstable distribution (jessie).</p>
<p>CVE-2018-1000007<br />
Craig de Stigter discovered that authentication data might be leaked to third parties when following HTTP redirects.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 7.38.0-4+deb8u9.</p></td>
</tr>
<tr class="odd">
<td><span id="rn831"></span> <a href="#rn831"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-831 (CM-19507)</td>
<td>Security: Debian Security Advisory DSA-4091-1 for mysql issues CVE-2018-2562 CVE-2018-2622 CVE-2018-2640 CVE-2018-2665 CVE-2018-2668</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4091-1, and affect all mysql packages, including mysql-* and libmysql-*.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>-------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4091-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
January 18, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a><br />
-------------------------------------------------------------------------<br />
Package : mysql-5.5<br />
CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2018-2562" class="external-link" title="Follow link">CVE-2018-2562</a><a href="https://security-tracker.debian.org/tracker/CVE-2018-2622" class="external-link" title="Follow link">CVE-2018-2622</a><a href="https://security-tracker.debian.org/tracker/CVE-2018-2640" class="external-link" title="Follow link">CVE-2018-2640</a><a href="https://security-tracker.debian.org/tracker/CVE-2018-2665" class="external-link" title="Follow link">CVE-2018-2665</a><a href="https://security-tracker.debian.org/tracker/CVE-2018-2668" class="external-link" title="Follow link">CVE-2018-2668</a></p>
<p>Several issues have been discovered in the MySQL database server. The vulnerabilities are addressed by upgrading MySQL to the new upstream version 5.5.59, which includes additional changes. Please see the MySQL 5.5 Release Notes and Oracle's Critical Patch Update advisory for further details:</p>
<p><a href="https://dev.mysql.com/doc/relnotes/mysql/5.5/en/news-5-5-59.html" class="external-link" title="Follow link">https://dev.mysql.com/doc/relnotes/mysql/5.5/en/news-5-5-59.html</a><br />
<a href="http://www.oracle.com/technetwork/security-advisory/cpujan2018-3236628.html" class="external-link" title="Follow link">http://www.oracle.com/technetwork/security-advisory/cpujan2018-3236628.html</a></p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 5.5.59-0+deb8u1.</p></td>
</tr>
<tr class="even">
<td><span id="rn832"></span> <a href="#rn832"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-832 (CM-19458)</td>
<td>Security: Debian Security Advisory DSA-4089-1 for bind9 issue CVE-2017-3145</td>
<td><p>The following CVE was announced in Debian Security Advisory DSA-4089-1, and affects the bind9 package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>-------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4089-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
January 16, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a><br />
-------------------------------------------------------------------------<br />
Package : bind9</p>
<p>CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2017-3145" class="external-link" title="Follow link">CVE-2017-3145</a><br />
Jayachandran Palanisamy of Cygate AB reported that BIND, a DNS server implementation, was improperly sequencing cleanup operations, leading in some cases to a use-after-free error, triggering an assertion failure and crash in named.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed in version 1:9.9.5.dfsg-9+deb8u15.</p>
<p>For the stable distribution (stretch), this problem has been fixed in version 1:9.10.3.dfsg.P4-12.3+deb9u4.</p>
<p>We recommend that you upgrade your bind9 packages.</p></td>
</tr>
<tr class="odd">
<td><span id="rn833"></span> <a href="#rn833"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-833 (CM-19446)</td>
<td>Security: Debian Security Advisory DSA-4086 for libxml2 issue CVE-2017-15412</td>
<td><p>The following CVE was announced in Debian Security Advisory DSA-4086-1, and affects the libxml2 package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>--------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4086-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
January 13, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a><br />
--------------------------------------------------------------------------</p>
<p>Package : libxml2<br />
CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2017-15412" class="external-link" title="Follow link">CVE-2017-15412</a><br />
Debian Bug : 883790</p>
<p>Nick Wellnhofer discovered that certain function calls inside XPath<br />
predicates can lead to use-after-free and double-free errors when<br />
executed by libxml2's XPath engine via an XSLT transformation.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed<br />
in version 2.9.1+dfsg1-5+deb8u6.</p></td>
</tr>
<tr class="even">
<td><span id="rn834"></span> <a href="#rn834"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-834 (CM-19385)</td>
<td>Security: Debian Security Advisories DSA-4082 for kernel issues CVE-2017-8824 CVE-2017-15868 CVE-2017-16538 CVE-2017-16939 CVE-2017-17448 CVE-2017-17449 CVE-2017-17450 CVE-2017-17558 CVE-2017-17558 CVE-2017-17741 CVE-2017-17805 and more</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4086-1, and affect the Linux kernel.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>--------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4082-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
January 09, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a><br />
--------------------------------------------------------------------------</p>
<p>Package : linux<br />
CVE ID : CVE-2017-8824 CVE-2017-15868 CVE-2017-16538<br />
CVE-2017-16939 CVE-2017-17448 CVE-2017-17449 CVE-2017-17450<br />
CVE-2017-17558 CVE-2017-17741 CVE-2017-17805 CVE-2017-17806<br />
CVE-2017-17807 CVE-2017-1000407 CVE-2017-1000410</p>
<p>Several vulnerabilities have been discovered in the Linux kernel that may lead to a privilege escalation, denial of service or information leaks.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-8824" class="external-link" title="Follow link">CVE-2017-8824</a></p>
<p>Mohamed Ghannam discovered that the DCCP implementation did not correctly manage resources when a socket is disconnected and reconnected, potentially leading to a use-after-free. A local user could use this for denial of service (crash or data corruption) or possibly for privilege escalation. On systems that do not already have the dccp module loaded, this can be mitigated by disabling it:</p>
<p><code>echo &gt;&gt; /etc/modprobe.d/disable-dccp.conf install dccp false</code></p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-15868" class="external-link" title="Follow link">CVE-2017-15868</a></p>
<p>Al Viro found that the Bluebooth Network Encapsulation Protocol (BNEP) implementation did not validate the type of the second socket passed to the BNEPCONNADD ioctl(), which could lead to memory corruption. A local user with the CAP_NET_ADMIN capability can use this for denial of service (crash or data corruption) or possibly for privilege escalation.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-16538" class="external-link" title="Follow link">CVE-2017-16538</a></p>
<p>Andrey Konovalov reported that the dvb-usb-lmedm04 media driver did not correctly handle some error conditions during initialisation. A physically present user with a specially designed USB device can use this to cause a denial of service (crash).</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-16939" class="external-link" title="Follow link">CVE-2017-16939</a></p>
<p>Mohamed Ghannam reported (through Beyond Security's SecuriTeam Secure Disclosure program) that the IPsec (xfrm) implementation did not correctly handle some failure cases when dumping policy information through netlink. A local user with the CAP_NET_ADMIN capability can use this for denial of service (crash or data corruption) or possibly for privilege escalation.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17448" class="external-link" title="Follow link">CVE-2017-17448</a></p>
<p>Kevin Cernekee discovered that the netfilter subsystem allowed users with the CAP_NET_ADMIN capability in any user namespace, not just the root namespace, to enable and disable connection tracking helpers. This could lead to denial of service, violation of network security policy, or have other impact.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17449" class="external-link" title="Follow link">CVE-2017-17449</a></p>
<p>Kevin Cernekee discovered that the netlink subsystem allowed users with the CAP_NET_ADMIN capability in any user namespace to monitor netlink traffic in all net namespaces, not just those owned by that user namespace. This could lead to exposure of sensitive information.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17450" class="external-link" title="Follow link">CVE-2017-17450</a></p>
<p>Kevin Cernekee discovered that the xt_osf module allowed users with the CAP_NET_ADMIN capability in any user namespace to modify the global OS fingerprint list.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17558" class="external-link" title="Follow link">CVE-2017-17558</a></p>
<p>Andrey Konovalov reported that that USB core did not correctly handle some error conditions during initialisation. A physically present user with a specially designed USB device can use this to cause a denial of service (crash or memory corruption), or possibly for privilege escalation.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17741" class="external-link" title="Follow link">CVE-2017-17741</a></p>
<p>Dmitry Vyukov reported that the KVM implementation for x86 would over-read data from memory when emulating an MMIO write if the kvm_mmio tracepoint was enabled. A guest virtual machine might be able to use this to cause a denial of service (crash).</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17805" class="external-link" title="Follow link">CVE-2017-17805</a></p>
<p>Dmitry Vyukov reported that the KVM implementation for x86 would over-read data from memory when emulating an MMIO write if the kvm_mmio tracepoint was enabled. A guest virtual machine might be able to use this to cause a denial of service (crash).</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17806" class="external-link" title="Follow link">CVE-2017-17806</a></p>
<p>It was discovered that the HMAC implementation could be used with an underlying hash algorithm that requires a key, which was not intended. A local user could use this to cause a denial of service (crash or memory corruption), or possibly for privilege escalation.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17807" class="external-link" title="Follow link">CVE-2017-17807</a></p>
<p>Eric Biggers discovered that the KEYS subsystem lacked a check for write permission when adding keys to a process's default keyring. A local user could use this to cause a denial of service or to obtain sensitive information.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-1000407" class="external-link" title="Follow link">CVE-2017-1000407</a></p>
<p>Andrew Honig reported that the KVM implementation for Intel processors allowed direct access to host I/O port 0x80, which is not generally safe. On some systems this allows a guest VM to cause a denial of service (crash) of the host.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-1000410" class="external-link" title="Follow link">CVE-2017-1000410</a></p>
<p>Ben Seri reported that the Bluetooth subsystem did not correctly handle short EFS information elements in L2CAP messages. An attacker able to communicate over Bluetooth could use this to obtain sensitive information from the kernel.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed in version 3.16.51-3+deb8u1.</p></td>
</tr>
<tr class="odd">
<td><span id="rn836"></span> <a href="#rn836"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-836 (CM-19353)</td>
<td>NCLU 'net del' and 'net add bridge' commands do not work in the same 'net commit'</td>
<td><p>If a bridge is previously configured and you run the <code>net del all</code> and the <code>net add bridge</code> commands in the same net commit, all bridge and VLAN commands fail and no bridge or VLAN configuration is added to the switch.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn837"></span> <a href="#rn837"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-837 (CM-19919)</td>
<td>PCIe bus error (Malformed TLP) on the Dell Z9100 switch</td>
<td><p>Certain Dell Z9100 switches running Cumulus Linux have a different string coded in the Manufacturer field of the SMBIOS/DMI information. This discrepancy sometimes causes a problem with timing during the boot sequence that leaves <code>switchd</code> in a failed state.</p>
<p>To work around this issue, perform either a single cold reboot (power cycle the switch) or two warm reboots (run the reboot command twice).</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn861"></span> <a href="#rn861"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-861 (CM-20694)</td>
<td>NCLU 'net show lldp' command traceback on 'descr'</td>
<td><p>When you run the <code>net show lldp</code> command, the <code>netd</code> process crashes and does not recover. This occurs because the LLDP peer does not send the <code>description</code> field in the TLV (which is optional), so NCLU cannot parse the information.</p>
<p>To work around the issue, make sure that the LLDP peer device is configured to send the LLDP description in the TLV.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn862"></span> <a href="#rn862"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-862 (CM-20416)</td>
<td>The error message 'snmpd[xxx]: truncating integer value &gt; 32 bits' repeating in syslog</td>
<td><p>When the switch or snmpd is running for more than 497 days, the following error message repeats in syslog:</p>
<pre><code>snmpd[xxxx]: truncating integer value &gt; 32 bits</code></pre>
<p>This issue is resolved by limiting the number of log messages to 10 occurrences.</p></td>
</tr>
<tr class="odd">
<td><span id="rn863"></span> <a href="#rn863"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-863 (CM-20372)</td>
<td>The IPv6 default gateway GUA is not reachable through ICMP in a VXLAN configuration</td>
<td><p>When a server tries to reach the IPv6 default gateway global unique address (GUA) over a VXLAN enabled fabric, the communication fails if the gateway resides on a platform with the Broadcom Trident II + ASIC, as incorrect hardware programming fails to forward the packet to the control plane for termination.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn864"></span> <a href="#rn864"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-864 (CM-20272)</td>
<td><p>Security: Debian Security Advisory DSA-4154-1 for net-snmp issue<br />
CVE-2015-5621<br />
CVE-2018-1000116</p></td>
<td><p>The following CVE was announced in Debian Security Advisory DSA-4154-1, and affects the net-snmp package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>Debian Security Advisory DSA-4154-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
March 28, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : net-snmp<br />
CVE ID : <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-5621">CVE-2015-5621</a><a href="https://security-tracker.debian.org/tracker/CVE-2018-1000116">CVE-2018-1000116</a><br />
Debian Bug : 788964 894110</p>
<p>A heap corruption vulnerability was discovered in net-snmp, a suite of<br />
Simple Network Management Protocol applications, triggered when parsing<br />
the PDU prior to the authentication process. A remote, unauthenticated<br />
attacker can take advantage of this flaw to crash the snmpd process<br />
(causing a denial of service) or, potentially, execute arbitrary code<br />
with the privileges of the user running snmpd.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed<br />
in version 5.7.2.1+dfsg-1+deb8u1.</p>
<p>For the stable distribution (stretch), these problems have been fixed<br />
before the initial release.</p>
<p>We recommend that you upgrade your net-snmp packages.</p>
<p>For the detailed security status of net-snmp please refer to its<br />
<a href="https://security-tracker.debian.org/tracker/net-snmp" class="external-link" title="Follow link">https://security-tracker.debian.org/tracker/net-snmp</a></p>
<p>Further information about Debian Security Advisories, how to apply<br />
these updates to your system and frequently asked questions can be<br />
found at: <a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a></p></td>
</tr>
<tr class="odd">
<td><span id="rn865"></span> <a href="#rn865"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-865 (CM-20344)</td>
<td>On the Broadcom Trident II + ASIC, traceroute to an external host skips the anycast gateway address</td>
<td><p>When using traceroute from a server over a routed VXLAN overlay, the overlay router is not correctly accounted for in the path list. You might see the overlay router as an unknown hop or a repetition of the preceding hop. This applies for both IPv4 and IPv6.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn866"></span> <a href="#rn866"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-866 (CM-20182)</td>
<td>On Mellanox switches, ACL rules that match a TCP port do not work for encapsulated VXLAN packets</td>
<td><p>For an incoming VXLAN encapsulated packet, the inner packet does not match on the TCP port successfully after decapsulation.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn867"></span> <a href="#rn867"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-867 (CM-20126)</td>
<td>Implement forwarding table profiles for Maverick</td>
<td><p>Maverick switches should have layer 2 and layer 3 table sizes when using <code>cl-resource-query</code>.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn868"></span> <a href="#rn868"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-868 (CM-20069)</td>
<td>Link-down does not work on SVIs configured in a VRF</td>
<td><p>The <code>link-down yes</code> configuration in the <code>/etc/network/interfaces</code> file has no effect on shutting down SVI interfaces configured in a VRF. SVIs configured without a VRF are not affected.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn869"></span> <a href="#rn869"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-869 (CM-20002)</td>
<td>Kernel route uses the bridge VRR interface instead of the bridge interface</td>
<td><p>In the kernel routing table, the bridge VRR interface is used instead of the bridge interface. This causes ARP packets to be sourced from the VRR interface instead of the physical interface.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn870"></span> <a href="#rn870"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-870 (CM-19959)</td>
<td>Internal loopback ports on Tomahawk switches set to 40G cause traffic to throttle</td>
<td><p>The internal loopback ports on a Tomahawk switch should be set to the highest speed of which the port is capable. However, due to a software defect, the ports can be set to 40G, which throttles traffic. When configuring Tomahawk internal loopback ports, make sure the port is not configured to a speed other than 100G. If it is, first remove the configuration on that port, reboot the system, then reconfigure the loopback port in the <code>/etc/cumulus/ports.conf file</code>.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn871"></span> <a href="#rn871"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-871 (CM-19906)</td>
<td>Security: Debian Security Advisory DSA-4120-1 for Linux kernel issues CVE-2018-5750</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4120-1, and affect the Linux kernel.</p>
<p>The issue is fixed in Cumulus Linux 3.6.0.</p>
<p>-------------------------------------------------------------------------</p>
<p>Debian Security Advisory DSA-4120-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a><br />
January 19, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a><br />
-------------------------------------------------------------------------<br />
Package : linux<br />
CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2018-5750" class="external-link" title="Follow link">CVE-2018-5750</a></p>
<p>It was found that the acpi_smbus_hc_add function in drivers/acpi/sbshc.c in the Linux kernel through 4.14.15 allows local users to obtain sensitive address information by reading dmesg data from an SBS HC printk call.</p>
<p>See <a href="https://patchwork.kernel.org/patch/10174835/" class="external-link" title="Follow link">https://patchwork.kernel.org/patch/10174835/</a> for further details.</p></td>
</tr>
<tr class="even">
<td><span id="rn872"></span> <a href="#rn872"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-872 (CM-19753)</td>
<td>On Mellanox Spectum platforms configured with BGP unnumbered and multipath, cl-ecmpcalc fails on two links</td>
<td><p>On Mellanox Spectrum platforms, <code>cl-ecmpcalc</code> reports that the nexthop does not have multiple paths. For example:</p>
<pre><code>Error: traffic to IP Address:31.0.0.31 will not ECMP</code></pre>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn873"></span> <a href="#rn873"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-873 (CM-18076)</td>
<td>Platform-aware validation checker for ports.conf</td>
<td><p>Cumulus Linux provides a new <code>/etc/cumulus/ports.conf</code> file validator that finds both syntax and platform-specific errors, and provides a reason for each invalid line. Errors are shown when you run the <code>net commit</code> command or the <code>validate-ports</code> script. Previously, the <code>net commit</code> command failed silently, with no error message.</p>
<p>The following example shows a <code>ports.conf</code> file snippet that has a problem with split ports:</p>
<pre><code>...
# QSFP28 ports
#
# &lt;port label&gt; = [40G|50G|100G]
#   or when split = [2x50G|4x10G|4x25G|disabled
1=4x10G
2=100G
3=4x10G
4=disabled
...</code></pre>
<p>The above snippet in the <code>ports.conf</code> file produces in the following error message when you run the <code>net commit</code> command:</p>
<pre><code>cumulus@switch:~# net commit 
Error: 1 invalid lines found in /etc/cumulus/ports.conf:
[Line 57]:&#39;2=100G&#39;
  Invalid because: 2 is blocked by port 1 but is marked &#39;100G&#39; rather than disable[d]</code></pre>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn874"></span> <a href="#rn874"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-874 (CM-16293)</td>
<td>NCLU 'net show interface' output should be fewer than 80 characters</td>
<td><p>The output for the <code>net show interface</code> command can be more than 130 characters wide without line wrapping, which can be difficult to read on a 80 character wide terminal.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0. The <code>net show interface</code> output is now fewer than 80 characters long for 80 character wide terminals.</p></td>
</tr>
<tr class="odd">
<td><span id="rn905"></span> <a href="#rn905"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-905 (CM-19649)</td>
<td>LLDP-MED network policy not working after port flaps</td>
<td><p>LLDP-MED includes voice VLAN and DSCP values. When you configure LLDP, the service works when the port is first brought up, but the switch stops sending LLDP-MED TLVs after a link state transition.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn909"></span> <a href="#rn909"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-909 (CM-20543)</td>
<td>NCLU 'net del time ntp server *' command crashes netd</td>
<td><p>Removing all NTP servers from the configuration with the <code>net del ntp server *</code> command (using * as a wildcard to match all servers) causes <code>netd</code> to crash.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn910"></span> <a href="#rn910"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-910 (CM-20483)</td>
<td>On the Dell 4148F-ON switch, portwd tries to make 10G ports into 40G</td>
<td><p>On the Dell 4148F-ON switch, ports swp53 and swp54 do not link up with installed 10G DACs.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn911"></span> <a href="#rn911"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-911 (CM-20411)</td>
<td>OSPF is up after BFD fails in a point-to-point network</td>
<td><p>When a BFD session fails in a point-to-point network, the OSPF adjacency with the neighbor is not brought down.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn912"></span> <a href="#rn912"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-912 (CM-19801)</td>
<td>QinQ not working without a restart in traditional mode bridge</td>
<td><p>When changing the inner and outer VLANs of a double-tagged bridge interface using <code>ifreload</code>, the port's VLAN translation key is not updated correctly, causing an incorrect VLAN translation.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn913"></span> <a href="#rn913"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-913 (CM-19728)</td>
<td>NCLU 'ip forward' command has incorrect syntax and does not show in configuration</td>
<td><p>When you disable IP forwarding on an interface with the NCLU <code>ip forward off</code> command and commit the change, the command shows as unsupported when you run <code>net show configuration</code> commands.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn914"></span> <a href="#rn914"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-914 (CM-19727)</td>
<td>VRF not generated when used in BGP configuration</td>
<td><p>When you run the NCLU <code>net add bgp vrf</code> command, the VRF is not created in the <code>/etc/network/interfaces</code> file.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn915"></span> <a href="#rn915"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-915 (CM-19689)</td>
<td>The default syslog level for DHCP Relay results in too many messages</td>
<td><p>The default syslog severity level for DHCP Relay is 6, which causes too many syslog messages.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn916"></span> <a href="#rn916"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-916 (CM-19666)</td>
<td>netd crashes when you add unicode characters in SNMP commands</td>
<td><p>Unicode characters in SNMP commands cause <code>netd</code> to crash.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn917"></span> <a href="#rn917"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-917 (CM-19629)</td>
<td>FRR package code dependency causes FRR reload failure</td>
<td><p>Reloading a running FRR instance without a restart fails and generates errors in the log due to code failing dependencies.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn918"></span> <a href="#rn918"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-918 (CM-19615)</td>
<td>On the Tomahawk ASIC, the nexthop of a route in a VRF points to an incorrect interface</td>
<td><p>The nexthop of a route common to two VRFs points to an incorrect interface.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn919"></span> <a href="#rn919"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-919 (CM-19452)</td>
<td>NCLU 'net show lldp' command causes netd to crash</td>
<td><p>The <code>netd</code> process crashes when you run the <code>net show lldp</code> command and does not recover.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn920"></span> <a href="#rn920"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-920 (CM-19374)</td>
<td>sFlow sampling causes RX-DRP in kernel</td>
<td><p>sFlow sampling is causing the RX-DRP counter in the <code>net show counters</code> command output to increment.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn921"></span> <a href="#rn921"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-921 (CM-19370)</td>
<td>Link Local IPv6 address is not associated with a VRF</td>
<td><p>Link Local IPv6 addresses cannot be used to source SSH traffic inside a VRF such as the management VRF.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn922"></span> <a href="#rn922"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-922 (CM-20237)</td>
<td>Security: Debian Security Advisory DSA-4151-1 for librelp issue CVE-2018-1000140</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4151-1, and affect the librelp package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0</p>
<p>Debian Security Advisory DSA-4151-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
March 26, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : librelp<br />
CVE ID : <a href="https://nvd.nist.gov/vuln/detail/CVE-2018-1000140">CVE-2018-1000140</a></p>
<p>Bas van Schaik and Kevin Backhouse discovered a stack-based buffer<br />
overflow vulnerability in librelp, a library providing reliable event<br />
logging over the network, triggered while checking x509 certificates<br />
from a peer. A remote attacker able to connect to rsyslog can take<br />
advantage of this flaw for remote code execution by sending a specially<br />
crafted x509 certificate.</p>
<p>Details can be found in the upstream advisory:<br />
<a href="http://www.rsyslog.com/cve-2018-1000140/" class="external-link" title="Follow link">http://www.rsyslog.com/cve-2018-1000140/</a></p>
<p>For the oldstable distribution (jessie), this problem has been fixed<br />
in version 1.2.7-2+deb8u1.</p>
<p>For the stable distribution (stretch), this problem has been fixed in<br />
version 1.2.12-1+deb9u1.</p>
<p>We recommend that you upgrade your librelp packages.</p>
<p>For the detailed security status of librelp, please refer to its security<br />
tracker page at:<br />
<a href="https://security-tracker.debian.org/tracker/librelp" class="external-link" title="Follow link">https://security-tracker.debian.org/tracker/librelp</a></p></td>
</tr>
<tr class="even">
<td><span id="rn923"></span> <a href="#rn923"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-923 (CM-20093)</td>
<td>Security: Debian Security Advisory DSA-4140-1 for libvorbis issue CVE-2018-5146</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4140-1, and affect the libvorbis package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0</p>
<div class="user-content-block">
<p>--------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4140-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
March 16, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : libvorbis<br />
CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2018-5146">CVE-2018-5146</a><br />
Debian Bug : 893130</p>
<p>Richard Zhu discovered that an out-of-bounds memory write in the<br />
codeboook parsing code of the Libvorbis multimedia library could result<br />
in the execution of arbitrary code.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed<br />
in version 1.3.4-2+deb8u1.</p>
<p>For the stable distribution (stretch), this problem has been fixed in<br />
version 1.3.5-4+deb9u2.</p>
</div></td>
</tr>
<tr class="odd">
<td><span id="rn924"></span> <a href="#rn924"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-924 (CM-20066)</td>
<td>Security: Debian Security Advisory DSA-4136-1 for curl issues CVE-2018-1000120 CVE-2018-1000121 CVE-2018-1000122</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4136-1, and affect the curl package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>Debian Security Advisory DSA-4136-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Alessandro Ghedini<br />
March 14, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : curl<br />
CVE ID : CVE-2018-1000120 CVE-2018-1000121 CVE-2018-1000122</p>
<p>Multiple vulnerabilities were discovered in cURL, an URL transfer library.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2018-1000120">CVE-2018-1000120</a></p>
<p>Duy Phan Thanh discovered that curl could be fooled into writing a<br />
zero byte out of bounds when curl is told to work on an FTP URL with<br />
the setting to only issue a single CWD command, if the directory part<br />
of the URL contains a "%00" sequence.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2018-1000121">CVE-2018-1000121</a><br />
Dario Weisser discovered that curl might dereference a near-NULL<br />
address when getting an LDAP URL due to the ldap_get_attribute_ber()<br />
fuction returning LDAP_SUCCESS and a NULL pointer. A malicious server<br />
might cause libcurl-using applications that allow LDAP URLs, or that<br />
allow redirects to LDAP URLs to crash.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2018-1000122">CVE-2018-1000122</a></p>
<p>OSS-fuzz, assisted by Max Dymond, discovered that curl could be<br />
tricked into copying data beyond the end of its heap based buffer<br />
when asked to transfer an RTSP URL.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed<br />
in version 7.38.0-4+deb8u10.</p>
<p>For the stable distribution (stretch), these problems have been fixed in<br />
version 7.52.1-5+deb9u5.</p>
<p>We recommend that you upgrade your curl packages.</p>
<p>For the detailed security status of curl, please refer to<br />
its security tracker page at:<br />
<a href="https://security-tracker.debian.org/tracker/curl" class="external-link" title="Follow link">https://security-tracker.debian.org/tracker/curl</a></p></td>
</tr>
<tr class="even">
<td><span id="rn925"></span> <a href="#rn925"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-925 (CM-20030)</td>
<td>Security: Debian Security Advisory DSA-4100-1 for tiff (libtiff) issues CVE-2017-9935 CVE-2017-11335 CVE-2017-12944 CVE-2017-13726 CVE-2017-13727 CVE-2017-18013</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4100-1, and affect the tiff package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>Debian Security Advisory DSA-4100-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Moritz Muehlenhoff<br />
January 27, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : tiff<br />
CVE ID : <a href="https://nvd.nist.gov/vuln/detail/CVE-2017-9935">CVE-2017-9935</a><a href="https://nvd.nist.gov/vuln/detail/CVE-2017-11335">CVE-2017-11335</a><a href="https://nvd.nist.gov/vuln/detail/CVE-2017-12944">CVE-2017-12944</a><a href="https://security-tracker.debian.org/tracker/CVE-2017-13726">CVE-2017-13726</a><br />
<a href="https://security-tracker.debian.org/tracker/CVE-2017-13727">CVE-2017-13727</a><a href="https://nvd.nist.gov/vuln/detail/CVE-2017-18013">CVE-2017-18013</a></p>
<p>Multiple vulnerabilities have been discovered in the libtiff library and<br />
the included tools, which may result in denial of service or the<br />
execution of arbitrary code.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed<br />
in version 4.0.3-12.3+deb8u5.</p>
<p>For the stable distribution (stretch), these problems have been fixed in<br />
version 4.0.8-2+deb9u2.<br />
We recommend that you upgrade your tiff packages.</p>
<p>For the detailed security status of tiff, please refer to<br />
its security tracker page at:<br />
<a href="https://security-tracker.debian.org/tracker/tiff" class="external-link" title="Follow link">https://security-tracker.debian.org/tracker/tiff</a></p></td>
</tr>
<tr class="odd">
<td><span id="rn926"></span> <a href="#rn926"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-926 (CM-19996)</td>
<td>Security: Debian Security Advisory DSA-4133-1 for isc-dhcp issues CVE-2017-3144 CVE-2018-5732 CVE-2018-5733</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4133-1, and affect the isc-dhcp package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>Debian Security Advisory DSA-4133-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
March 07, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : isc-dhcp<br />
CVE ID : CVE-2017-3144 CVE-2018-5732 CVE-2018-5733<br />
Debian Bug : 887413 891785 891786</p>
<p>Several vulnerabilities have been discovered in the ISC DHCP client,<br />
relay and server. The Common Vulnerabilities and Exposures project<br />
identifies the following issues:</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-3144" class="external-link" title="Follow link">CVE-2017-3144</a></p>
<p>It was discovered that the DHCP server does not properly clean up<br />
closed OMAPI connections, which can lead to exhaustion of the pool<br />
of socket descriptors available to the DHCP server, resulting in<br />
denial of service.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2018-5732" class="external-link" title="Follow link">CVE-2018-5732</a></p>
<p>Felix Wilhelm of the Google Security Team discovered that the DHCP<br />
client is prone to an out-of-bound memory access vulnerability when<br />
processing specially constructed DHCP options responses, resulting<br />
in potential execution of arbitrary code by a malicious DHCP server.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2018-5733" class="external-link" title="Follow link">CVE-2018-5733</a></p>
<p>Felix Wilhelm of the Google Security Team discovered that the DHCP<br />
server does not properly handle reference counting when processing<br />
client requests. A malicious client can take advantage of this flaw<br />
to cause a denial of service (dhcpd crash) by sending large amounts<br />
of traffic.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed<br />
in version 4.3.1-6+deb8u3.</p>
<p>For the stable distribution (stretch), these problems have been fixed in<br />
version 4.3.5-3+deb9u1.</p>
<p>We recommend that you upgrade your isc-dhcp packages.</p>
<p>For the detailed security status of isc-dhcp, please refer to its<br />
security tracker page at:<br />
<a href="https://security-tracker.debian.org/tracker/isc-dhcp" class="external-link" title="Follow link">https://security-tracker.debian.org/tracker/isc-dhcp</a></p></td>
</tr>
<tr class="even">
<td><span id="rn927"></span> <a href="#rn927"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-927 (CM-19961)</td>
<td>Security: Debian Security Advisory DSA-4132 for libvpx issue CVE-2017-13194</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4132-1, and affect the libvpx package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>-------------------------------------------------------------------------<br />
Debian Security Advisory DSA-4132-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Moritz Muehlenhoff<br />
March 04, 2018 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : libvpx<br />
CVE ID : <a href="https://security-tracker.debian.org/tracker/CVE-2017-13194">CVE-2017-13194</a></p>
<p>It was discovered that incorrect validation of frame widths in the libvpx<br />
multimedia library may result in denial of service and potentially the<br />
execution of arbitrary code.</p>
<p>For the oldstable distribution (jessie), this problem has been fixed<br />
in version 1.3.0-3+deb8u1.</p>
<p>For the stable distribution (stretch), this problem has been fixed in<br />
version 1.6.1-3+deb9u1.</p>
<p>We recommend that you upgrade your libvpx packages.</p>
<p>For the detailed security status of libvpx please refer to<br />
its security tracker page at:<br />
<a href="https://security-tracker.debian.org/tracker/libvpx" class="external-link" title="Follow link">https://security-tracker.debian.org/tracker/libvpx</a></p></td>
</tr>
<tr class="odd">
<td><span id="rn928"></span> <a href="#rn928"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-928 (CM-19253)</td>
<td>Security: Debian Security Advisory DSA-4068-1 for rsync issues CVE-2017-16548 CVE-2017-17433 CVE-2017-17434</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4068-1, and affect the rsync package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>Debian Security Advisory DSA-4068-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a> Salvatore Bonaccorso<br />
December 17, 2017 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : rsync<br />
CVE ID: <a href="https://security-tracker.debian.org/tracker/CVE-2017-16548" class="external-link" title="Follow link">CVE-2017-16548  </a><a href="https://security-tracker.debian.org/tracker/CVE-2017-17433" class="external-link" title="Follow link">CVE-2017-17433</a><a href="https://security-tracker.debian.org/tracker/CVE-2017-17434" class="external-link" title="Follow link">CVE-2017-17434</a><br />
Debian Bug : 880954 883665 883667</p>
<p>Several vulnerabilities were discovered in rsync, a fast, versatile,<br />
remote (and local) file-copying tool, allowing a remote attacker to<br />
bypass intended access restrictions or cause a denial of service.</p>
<p>For the oldstable distribution (jessie), these problems have been fixed<br />
in version 3.1.1-3+deb8u1.</p>
<p>For the stable distribution (stretch), these problems have been fixed in<br />
version 3.1.2-1+deb9u1.</p></td>
</tr>
<tr class="even">
<td><span id="rn929"></span> <a href="#rn929"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-929 (CM-19303)</td>
<td>Security: Debian Security Advisory DSA-4073-1 for linux kernel issues CVE-2017-8824 CVE-2017-16995 CVE-2017-17448 CVE-2017-17449 CVE-2017-17450 CVE-2017-17558 CVE-2017-17712 CVE-2017-17741 CVE-2017-17805 CVE-2017(17806,17807,1000407,1000410)</td>
<td><p>The following CVEs were announced in Debian Security Advisory DSA-4073-1, and affect the linux package.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p>
<p>Debian Security Advisory DSA-4073-1 security@debian.org<br />
<a href="https://www.debian.org/security/" class="external-link" title="Follow link">https://www.debian.org/security/</a><br />
December 23, 2017 <a href="https://www.debian.org/security/faq" class="external-link" title="Follow link">https://www.debian.org/security/faq</a></p>
<p>-------------------------------------------------------------------------</p>
<p>Package : linux<br />
CVE ID : CVE-2017-8824 CVE-2017-16995 CVE-2017-17448<br />
CVE-2017-17449 CVE-2017-17450 CVE-2017-17558<br />
CVE-2017-17712 CVE-2017-17741 CVE-2017-17805 CVE-2017-17806<br />
CVE-2017-17807 CVE-2017-1000407 CVE-2017-1000410</p>
<p>Several vulnerabilities have been discovered in the Linux kernel that<br />
may lead to a privilege escalation, denial of service or information<br />
leaks.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-8824">CVE-2017-8824</a></p>
<p>Mohamed Ghannam discovered that the DCCP implementation did not<br />
correctly manage resources when a socket is disconnected and<br />
reconnected, potentially leading to a use-after-free. A local<br />
user could use this for denial of service (crash or data<br />
corruption) or possibly for privilege escalation. On systems that<br />
do not already have the dccp module loaded, this can be mitigated<br />
by disabling it:<br />
echo &gt;&gt; /etc/modprobe.d/disable-dccp.conf install dccp false</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-16995">CVE-2017-16995</a></p>
<p>Jann Horn discovered that the Extended BPF verifier did not<br />
correctly model the behaviour of 32-bit load instructions. A<br />
local user can use this for privilege escalation.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17448">CVE-2017-17448</a></p>
<p>Kevin Cernekee discovered that the netfilter subsystem allowed<br />
users with the CAP_NET_ADMIN capability in any user namespace, not<br />
just the root namespace, to enable and disable connection tracking<br />
helpers. This could lead to denial of service, violation of<br />
network security policy, or have other impact.</p>
<p><a href="https://nvd.nist.gov/vuln/detail/CVE-2017-17449">CVE-2017-17449</a></p>
<p>Kevin Cernekee discovered that the netlink subsystem allowed<br />
users with the CAP_NET_ADMIN capability in any user namespace<br />
to monitor netlink traffic in all net namespaces, not just<br />
those owned by that user namespace. This could lead to<br />
exposure of sensitive information.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17450">CVE-2017-17450</a></p>
<p>Kevin Cernekee discovered that the xt_osf module allowed users<br />
with the CAP_NET_ADMIN capability in any user namespace to modify<br />
the global OS fingerprint list.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17558">CVE-2017-17558</a></p>
<p>Andrey Konovalov reported that that USB core did not correctly<br />
handle some error conditions during initialisation. A physically<br />
present user with a specially designed USB device can use this to<br />
cause a denial of service (crash or memory corruption), or<br />
possibly for privilege escalation.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17712">CVE-2017-17712</a></p>
<p>Mohamed Ghannam discovered a race condition in the IPv4 raw socket<br />
implementation. A local user could use this to obtain sensitive<br />
information from the kernel.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17741">CVE-2017-17741</a></p>
<p>Dmitry Vyukov reported that the KVM implementation for x86 would<br />
over-read data from memory when emulating an MMIO write if the<br />
kvm_mmio tracepoint was enabled. A guest virtual machine might be<br />
able to use this to cause a denial of service (crash).</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17805">CVE-2017-17805</a></p>
<p>It was discovered that some implementations of the Salsa20 block<br />
cipher did not correctly handle zero-length input. A local user<br />
could use this to cause a denial of service (crash) or possibly<br />
have other security impact.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17806">CVE-2017-17806</a></p>
<p>It was discovered that the HMAC implementation could be used with<br />
an underlying hash algorithm that requires a key, which was not<br />
intended. A local user could use this to cause a denial of<br />
service (crash or memory corruption), or possibly for privilege<br />
escalation.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-17807">CVE-2017-17807</a></p>
<p>Eric Biggers discovered that the KEYS subsystem lacked a check for<br />
write permission when adding keys to a process's default keyring.<br />
A local user could use this to cause a denial of service or to<br />
obtain sensitive information.</p>
<p><a href="https://security-tracker.debian.org/tracker/CVE-2017-1000407">CVE-2017-1000407</a></p>
<p>Andrew Honig reported that the KVM implementation for Intel<br />
processors allowed direct access to host I/O port 0x80, which<br />
is not generally safe. On some systems this allows a guest<br />
VM to cause a denial of service (crash) of the host.</p>
<p><a href="https://nvd.nist.gov/vuln/detail/CVE-2017-1000410">CVE-2017-1000410</a></p>
<p>Ben Seri reported that the Bluetooth subsystem did not correctly<br />
handle short EFS information elements in L2CAP messages. An<br />
attacker able to communicate over Bluetooth could use this to<br />
obtain sensitive information from the kernel.</p>
<p>Debian disables unprivileged user namespaces by default, but if they<br />
are enabled (via the kernel.unprivileged_userns_clone sysctl) then<br />
CVE-2017-17448 can be exploited by any local user.</p></td>
</tr>
<tr class="odd">
<td><span id="rn930"></span> <a href="#rn930"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-930 (CM-19367)</td>
<td>Adding MTU to bonded interfaces creates an incorrect interface</td>
<td><p>When adding the MTU to bonded interfaces, NCLU creates an incorrect interface in the <code>/etc/network/interfaces</code> file.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="even">
<td><span id="rn931"></span> <a href="#rn931"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-931 (CM-19675)</td>
<td>Static route remains inactive following link flap</td>
<td><p>When a static route is removed from the zebra routing table because an interface is transitioning to down state, the static route remains inactive when the interface comes back up if an alternate route still exists.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
<tr class="odd">
<td><span id="rn934"></span> <a href="#rn934"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-934 (CM-19605)</td>
<td>The kernel reports incorrect link state for 10G BASE-LR on Broadcom switches</td>
<td><p>On Broadcom switches, the link status for the 10G BASE-LR and 10G BASE-SR might incorrectly display as up after you disconnect the cable.</p>
<p>This issue is fixed in Cumulus Linux 3.6.0.</p></td>
</tr>
</tbody>
</table>

## Known Issues in Cumulus Linux 3.6.0

The following issues are new to Cumulus Linux and affect the current release.

<table>

<tbody>
<tr class="odd">
<th>Release Note ID</th>
<th>Summary</th>
<th>Description</th>
</tr>
<tr class="even">
<td><span id="rn382"></span> <a href="#rn382"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-382 (CM-6692)</td>
<td>FRR: Removing a bridge using  ifupdown2 does not remove it from the configuration files</td>
<td><p>Removing a bridge using ifupdown2 does not remove it from the FRR configuration files. However, restarting FRR successfully removes the bridge.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="rn389"></span> <a href="#rn389"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-389 (CM-8410)</td>
<td>switchd supports only port 4789 as the UDP port for VXLAN packets</td>
<td><p><code>switchd</code> currently allows only the standard port 4789 as the UDP port for VXLAN packets. If a hypervisor uses a non-standard UDP port, VXLAN exchanges with the hardware VTEP do not work; packets are not terminated and encapsulated packets are sent out on UDP port 4789.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="rn537"></span> <a href="#rn537"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-537 (CM-12967)</td>
<td>Pause frames sent by a Tomahawk switch are not honored by the upstream switch</td>
<td><p>When link pause or priority flow control (PFC) is enabled on a Broadcom Tomahawk-based switch and there is over-subscription on a link, where the ASIC sends pause frames aggressively, the upstream switch does not throttle enough.</p>
<p>If you need link pause or PFC functionality, use a switch that does not use the Tomahawk ASIC.</p></td>
</tr>
<tr class="odd">
<td><span id="rn602"></span> <a href="#rn602"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-602 (CM-15094)</td>
<td>sFlow interface speed incorrect in counter samples</td>
<td><p>Counter samples exported from the switch show an incorrect interface speed.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="rn604"></span> <a href="#rn604"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-604 (CM-15959)</td>
<td>ARP suppression does not work well with VXLAN active-active mode</td>
<td><p>In some instances, ARP requests are not suppressed in a VXLAN active-active scenario, but instead get flooded over VXLAN tunnels. This issue is caused because there is no control plane syncing the snooped local neighbor entries between the MLAG pair; MLAG does not perform this sync, and neither does EVPN.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="rn640"></span> <a href="#rn640"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-640 (CM-16461)</td>
<td>Cumulus VX OVA image for VMware reboots due to critical readings from sensors</td>
<td><p>After booting a Cumulus VX virtual machine running the VMware OVA image, sometimes messages from sensors appear, indicating that the "Avg state" is critical, with all values displayed as 100.0. A cl-support is generated.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="rn656"></span> <a href="#rn656"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-656 (CM-17617)</td>
<td>The switchd heartbeat fails on Tomahawk switches with VXLAN scale configuration (512 VXLAN interfaces)</td>
<td><p>When a Tomahawk switch has 512 VXLAN interfaces configured, the switchd heartbeat fails. This can cause switchd to dump core.</p>
<p>To work around this issue, disable VXLAN statistics in <code>switchd</code>. Edit <code>/etc/cumulus/switchd.conf</code> and comment out the following line:</p>
<pre><code>cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf

...

#stats.vxlan.member = BRIEF

...</code></pre>
<p>Then restart <code>switchd</code> for the change to take effect. This causes all network ports to reset in addition to resetting the switch hardware configuration.</p>
<pre><code>cumulus@switch:~$ sudo systemctl restart switchd.service</code></pre></td>
</tr>
<tr class="odd">
<td><span id="rn744"></span> <a href="#rn744"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-744 (CM-18986)</td>
<td>Unable to modify BGP ASN for a VRF associated with layer 3 VNI</td>
<td><p>After editing the <code>frr.conf file</code> to modify BGP ASN for a VRF associated with a layer 3 VNI, the change is not applied.</p>
<p>To work around this issue, first delete the layer 3 VNI, then try to modify the BGP VRF instance.</p></td>
</tr>
<tr class="even">
<td><span id="rn750"></span> <a href="#rn750"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-750 (CM-17457)</td>
<td>On Maverick switches, multicast traffic limited by lowest speed port in the group</td>
<td><p>The Maverick switch limits multicast traffic by the lowest speed port that has joined a particular group.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="rn751"></span> <a href="#rn751"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-751 (CM-17157)</td>
<td>Pull source-node replication schema patch from upstream</td>
<td><p>The upstream OVSDB VTEP schema has been updated multiple times and now contains a patch to support source-node replication. This patch is not included with the latest version of Cumulus Linux.</p>
<p>Cumulus Networks is currently working to fix this issue.</p></td>
</tr>
<tr class="even">
<td><span id="rn753"></span> <a href="#rn753"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-753 (CM-18170)</td>
<td>MLAG neighbor entries deleted on link down, but ARP table out of sync when bond comes back up and system MAC address changed</td>
<td><p>The MLAG neighbor entries are deleted when the switch goes down; however, the ARP table is out of sync when the bond comes back up and the system MAC address is changed.</p>
<p>To work around this issue, ping the SVI address of the MLAG switch or issue an <code>arping</code> command to the host from the broken switch.</p></td>
</tr>
<tr class="odd">
<td><span id="rn754"></span> <a href="#rn754"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-754 (CM-15812)</td>
<td>Multicast forwarding fails for IP addresses whose DMAC overlaps with reserved DIPs</td>
<td><p>Multicast forwarding fails for IP addresses whose DMAC overlaps with reserved DIPs.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="rn755"></span> <a href="#rn755"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-755 (CM-16855)</td>
<td>Auto-negotiation ON sometimes results in NO-CARRIER</td>
<td><p>If a two nodes on both sides of a link change from auto-negotiation off to auto-negotiation on for both sides during a short interval (around one second), the link might start flapping or stay down.</p>
<p>To work around this issue and stop the flapping, turn the link down on the switch with the command <code>ifdown swpX</code>, wait a few seconds, then bring the link back up with the command <code>ifup swpX</code>. Repeat this on the other side if necessary.</p></td>
</tr>
<tr class="odd">
<td><span id="rn757"></span> <a href="#rn757"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-757 (CM-18537)</td>
<td>On Mellanox switches, congestion drops not counted</td>
<td><p>On the Mellanox switch, packet drops due to congestion are not counted.</p>
<p>To work around this issue, run the command <code>sudo ethtool -S swp1</code> to collect interface traffic statistics.</p></td>
</tr>
<tr class="even">
<td><span id="rn758"></span> <a href="#rn758"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-758 (CM-17557)</td>
<td>If sFlow is enabled, some sampled packets (such as multicast) are forwarded twice</td>
<td><p>When sFlow is enabled, some sampled packets, such as IPMC, are forwarded twice (in the ASIC and then again through the kernel networking stack).</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="rn760"></span> <a href="#rn760"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-760 (CM-18682)</td>
<td>smonctl utility JSON parsing error</td>
<td><p>There is a parsing error with the <code>smonctl</code> utility. In some cases when JSON output is chosen, the <code>smonctl</code> utility crashes. The JSON output is necessary to make the information available through SNMP.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn762"></span> <a href="#rn762"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-762 (CM-15677)</td>
<td>SBUS error warnings on Tomahawk switches</td>
<td><p>SBUS error warnings display on Tomahawk switches.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="rn763"></span> <a href="#rn763"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-763 (CM-16139)</td>
<td>OSPFv3 does not handle ECMP properly</td>
<td><p>IPv6 ECMP is not working as expected in OSPFv3.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="rn764"></span> <a href="#rn764"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-764 (CM-17434)</td>
<td>On Broadcom switches, all IP multicast traffic uses only queue 0</td>
<td><p>On Broadcom switches, IPv4 and IPv6 multicast traffic always maps into queue 0.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="rn788"></span> <a href="#rn788"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-788 (CM-19381)</td>
<td>dhcrelay does not bind to interfaces that have names longer than 14 characters</td>
<td><p>The <code>dhcrelay</code> command does not bind to an interface if the interface's name is longer than 14 characters.</p>
<p>To work around this issue, change the interface name to be 14 or fewer characters if <code>dhcrelay</code> is required to bind to it.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="rn790"></span> <a href="#rn790"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-790 (CM-19014)</td>
<td>Configuring DHCP relay with VRR breaks ifreload</td>
<td><p>When you configure DHCP relay with VRR, the <code>ifreload</code> command does not work as expected; for example, the IP address might be removed from an SVI.</p>
<p>This issue is currently being investigated. </p></td>
</tr>
<tr class="odd">
<td><span id="rn799"></span> <a href="#rn799"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-799 (CM-16493)</td>
<td>No way to configure IPv6 link-local addrgenmode using ifupdown2 or NCLU</td>
<td><p>You cannot use NCLU or <code>ifupdown2</code> to enable or disable of the IPv6 link-local eui-64 format.</p>
<p>To work around this limitation, you can use the following <code>iproute2</code> command:</p>
<pre><code>cumulus@switch:~$ sudo ip link set swp# addrgenmode {eui-64|none}</code></pre>
<p>Note that this command does not persist across a reboot of the switch.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="rn808"></span> <a href="#rn808"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-808 (CM-15902)</td>
<td>In EVPN, sticky MAC addresses move from one bridge port to another</td>
<td><p>In EVPN environments, sticky MAC addresses move from one bridge port to another on soft nodes.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="rn822"></span> <a href="#rn822"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-822 (CM-19788)</td>
<td>Using the same VLAN ID on a subinterface and bridge VIDs for a given port is not easily corrected</td>
<td><p>If you configure a VLAN under a VLAN-aware bridge and create a subinterface of the same VLAN on one of the bridge ports, the bridge and interface compete for the same VLAN and if the interface is flapped, it stops working. Correcting the configuration and running the <code>ifreload</code> command does not resolve the conflict. To work around this issue, correct the bridge VIDs and restart <code>switchd</code> or delete the subinterface.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn823"></span> <a href="#rn823"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-823 (CM-19724)</td>
<td>Multicast control protocols are classified to the bulk queue by default</td>
<td><p>PIM and MSDP entries are set to the internal COS value of 6 so they are grouped together with the bulk traffic priority group in the default <code>traffic.conf</code> file. However, PIM, IGMP, and MSDP are considered control-plane and should be set to the internal COS value of 7.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn825"></span> <a href="#rn825"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-825 (CM-19633)</td>
<td>cl-netstat counters count twice for VXLAN traffic in TX direction</td>
<td><p>This is expected behavior that stems from the chipset itself. When the decision is made in the ASIC not to flood BUM (Broadcast, Unknown Unicast, and Multicast) traffic back out the same interface it came in on (known as a split-horizon correction), these hardware counters get incremented.</p>
<p>This behavior is not seen on a bridge filled with typical switch port interfaces. However, when VNIs are configured as <code>bridge-ports</code>, switch ports in that bridge are no longer treated as regular ports in this regard. These switch ports are susceptible to this behavior, and the hardware counters increment as split-horizon decisions occur.</p></td>
</tr>
<tr class="even">
<td><span id="rn827"></span> <a href="#rn827"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-827 (CM-14300)</td>
<td>cl-acltool counters for implicit accept do not work for IPv4 on management (ethX) interfaces</td>
<td><p>The iptables are not counting against the default INPUT chain rule for packets ingressing ethernet interfaces.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn860"></span> <a href="#rn860"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-860 (CM-20695)</td>
<td>Tab completion with the  'net add vxlan' command produces a traceback in the log</td>
<td><p>When using tab completion with the <code>net add vxlan</code> command, the following traceback appears in the log:</p>
<pre><code>ERROR: &#39;name&#39; 
Traceback (most recent call last): 
File &quot;/usr/lib/python2.7/dist-packages/nclu/__init__.py&quot;, line 789, in get_lldp 
lldp[value[&#39;name&#39;]] = value[&#39;chassis&#39;][0][&#39;name&#39;][0][&#39;value&#39;] 
KeyError: &#39;name&#39;</code></pre>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn875"></span> <a href="#rn875"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-875 (CM-20779)</td>
<td>On Mellanox switches, withdrawal of one ECMP next-hop results in the neighbor entry for that next hop missing from hardware</td>
<td><p>On a Mellanox switch, when you withdraw one ECMP next hop, the neighbor entry for that next hop is missing from the hardware.</p>
<p>To work around this issue, manually delete the ARP entry from kernel with the <code>arp -d</code> command to repopulate it in the hardware.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn876"></span> <a href="#rn876"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-876 (CM-20776)</td>
<td>EVPN symmetric IRB with numbered neighbors omits the NEXTHOP attribute when advertising to an external router</td>
<td><p>With EVPN symmetric routing (including type-5 routes) you can only advertise host routes or prefix routes learned through EVPN to a VRF peer if EVPN peering uses BGP unnumbered. If the BGP peering is numbered, the <code>NEXTHOP of MP_REACH</code> attribute is not included, which causes the neighbor to reply with a BGP notification.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn877"></span> <a href="#rn877"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-877 (CM-20745, CM-20678)</td>
<td>NCLU 'net show interface' commands report wrong mode in output for trunk ports</td>
<td><p>The <code>net show interface</code> command output displays the mode as Access/L2 instead of Trunk/L2, or vice versa (Trunk/L2 mode is displayed instead of Access/L2).</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn878"></span> <a href="#rn878"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-878 (CM-20741)</td>
<td>NCLU 'net pending' command does not show 'net add vxlan vni bridge access '</td>
<td><p>When you issue the <code>net pending</code> command, the resulting output is missing the VXLAN VNI and bridge access additions.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn879"></span> <a href="#rn879"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-879 (CM-20724)</td>
<td>NCLU treats interface names with a hyphen as a range</td>
<td><p>If you create an interface name that includes a hyphen (-), Cumulus Linux treats the interface as a range of interfaces.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn881"></span> <a href="#rn881"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-881 (CM-20665)</td>
<td>On Tomahawk+ switches, 100G DAC cables don’t link up on 3 out of the 6 ports when auto-negotiation is on</td>
<td><p>100G Copper Direct Attach Cables (DAC) might not link up on ports 49, 51, and 52 when auto-negotiation is set to on.</p>
<p>To work around this issue, disable auto-negotiation on both sides of the cables plugged into these ports or move the 100G DACs to ports 50, 53, or 54.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn882"></span> <a href="#rn882"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-882 (CM-20648)</td>
<td>When using VRF route leaking on a Mellanox switch, forwarded packets are copied to the CPU several times</td>
<td><p>When using VRF Route leaking on Mellanox switches in a VLAN-unaware bridge configuration, the packets for a locally attached leaked host are software forwarded.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn883"></span> <a href="#rn883"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-883 (CM-20644)</td>
<td>If the PTP services are running when switchd is restarted, the PTP services need to be restarted</td>
<td><p>When using PTP and <code>switchd.service</code> is restarted, the PTP services need to be restarted after <code>switchd.service</code> with the following commands:</p>
<pre><code>systemctl reset-failed ptp4l.service phc2sys.service
systemctl restart ptp4l.service phc2sys.service</code></pre>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn884"></span> <a href="#rn884"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-884 (CM-20534)</td>
<td>Dynamic leaking of routes between VRFs occurs through the default BGP instance</td>
<td><p>The default BGP instance must be provisioned and always exist for proper operation of dynamic leaking of routes between VRFs.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="rn885"></span> <a href="#rn885"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-885 (CM-20530)</td>
<td>NCLU 'net show interface' command shows 'NotConfigured' for unnumbered interfaces</td>
<td><p>When an interface is configured for OSPF/BGP unnumbered, the <code>net show interface</code> command shows <code>NotConfigured</code> instead of showing that it is unnumbered.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="rn886"></span> <a href="#rn886"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-886 (CM-20508)</td>
<td>On Mellanox and Broadcom switches, the Cumulus-Resource-Query-MIB defines buffer utilization objects but returns nothing</td>
<td><p>The Cumulus-Resource-Query-MIB defines the ability to gather buffer utilization status but when these objects are polled, they return nothing.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="rn887"></span> <a href="#rn887"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-887 (CM-20474)</td>
<td>VXLAN Encapsulation drops ARP QinQ tunneled packets</td>
<td><p>When an ARP request or response (or IPv6 NS/NA) packet with double VLAN tags (such as 802.1Q over 802.1Q), is sent to a VXLAN overlay, the outer VLAN tag is stripped during VXLAN encapsulation. If the receiving VTEP is a Broadcom Trident II + platform, the post VXLAN decapsulated packet is incorrectly directed to the control plane. As the packet traverses the linux kernel VXLAN interface into the VLAN-aware bridge device, the exposed inner VLAN tag is incorrectly used for VLAN filtering against the outer VLAN set, causing the packet to be discarded.</p>
<p>To work around this issue, disable VXLAN routing on the Trident II + switch by editing the <code>/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf</code> file, then restart <code>switchd</code>.</p>
<pre><code>vxlan_routing_overlay.profile = disable
sudo systemctl restart switchd.service</code></pre>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="rn888"></span> <a href="#rn888"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-888 (CM-20468, CM-20357)</td>
<td>Routes in a VRF learned through iBGP or multi-hop eBGP get leaked even if their next hops are unresolved</td>
<td><p>Routes in a VRF learned through iBGP or multi-hop eBGP are marked as installed even when they are not installed in the source VRF.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="rn889"></span> <a href="#rn889"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-889 (CM-20415)</td>
<td>NCLU 'net add routing import-table' command results in an FRR service crash</td>
<td><p>The FRR service crashes when you run the <code>net add routing import-table</code> command. To work around this issue, do not use the NCLU command.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn891"></span> <a href="#rn891"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-891 (CM-20684)</td>
<td>On Mellanox switches, attempts to configure a VRF with a nexthop from another VRF results in an sx_sdk daemon crash and loss of forwarding functionality</td>
<td><p>VRF Route Leaking is not supported on Mellanox platforms in 3.6.0. Attempts to configure a VRF with a nexthop from another VRF can result in an <code>sx_sdk</code> daemon crash and loss of forwarding functionality. Do not configure VRF import to leak routes between VRFs.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn892"></span> <a href="#rn892"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-892 (CM-20370)</td>
<td>In VXLAN active-active mode, the IPv6 default gateway LLA is not reachable through ICMP</td>
<td><p>In a VXLAN active-active mode configuration, a ping from a host within the VXLAN fabric towards the gateway (LLA) fails.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn893"></span> <a href="#rn893"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-893 (CM-20363)</td>
<td>IPv6 RA should include all on-link prefixes as prefix information</td>
<td><p>IPv6 RAs from a router can be used to do some host auto-configuration. The main aspects that can be auto-configured are the prefixes which are on-link (which can be used by the host to autoconfigure its addresses) and the default router. Some other information can also be indicated. FRR does have support to "advertise" some of these parameters. To work around this issue, configure the prefixes explicitly for announcement through RA using the IPv6 <code>nd</code> prefix command.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn894"></span> <a href="#rn894"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-894 (CM-20177)</td>
<td>Inter-subnet routing intermittently stops working in a central VXLAN routing configuration</td>
<td><p>In a VXLAN centralized routing configuration, IPv6 hosts (auto-configured using SLAAC) might experience intermittent connectivity loss between VXLAN segments (inter-subnet routing) within the data center fabric (EVPN type-5 external routes are not affected). The NA message has the wrong flag set (the router flag is not set, which is incorrect behavior based on RFC 4861, Section 4.4).</p>
<p>To work around this issue, configure <code>bridge-arp-nd-suppress off</code> under VNI interfaces for all VTEP devices.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn895"></span> <a href="#rn895"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-895 (CM-20160)</td>
<td>I2C bus hangs after setting speed to 40G on 100G/40G DAC on a Maverick 4148T switch</td>
<td><p>On Maverick 4148T switches, the l2C bus can hang, causing the fans and temperature sensors to be unreadable and the log file to fill with the error message:</p>
<pre><code>ismt_smbus 0000:00:13.0 completion wait timed out</code></pre>
<p>To work around this issue, reboot the switch.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn896"></span> <a href="#rn896"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-896 (CM-20139)</td>
<td>On Mellanox switches, egress ACL (destination port matching) on bonds is not allowed</td>
<td><p>An ACL rule that matches on an outbound bond interface fails to install. For example, a rule like this fails.</p>
<pre><code>[iptables]
-A FORWARD --out-interface  -j DROP</code></pre>
<p>To work around this issue, duplicate the ACL rule on each physical port of the bond. For example:</p>
<pre><code>[iptables]
-A FORWARD --out-interface  -j DROP
-A FORWARD --out-interface  -j DROP</code></pre>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn897"></span> <a href="#rn897"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-897 (CM-20086)</td>
<td> </td>
<td><p>NCLU reports an error when attempting to configure FRR when the configured hostname begins with a digit:</p>
<pre><code>unknown: buffer_flush_available: write error on fd -1: Bad file descriptor</code></pre>
<p>To work around this issue, change the hostname of the switch to begin with an alphabetic character; not a digit.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn898"></span> <a href="#rn898"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-898 (CM-20034)</td>
<td>Fiberstore SFP1G-LX-31 optic causes i2c bus to hang and switch to reboot</td>
<td><p>Using the Fiberstore SFP1G-LX-31 SFP module can cause the system to reboot.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="rn899"></span> <a href="#rn899"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-899 (CM-20028)</td>
<td>On the Dell-S4148 switch, you can't configure ports on the second pipeline into a gang</td>
<td><p>On the Dell S4148 switch, when you try to configure any of the ports on the second pipeline (port 31-54) into a gang (40G/4) through the <code>ports.conf</code> file, <code>switchd</code> fails.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="odd">
<td><span id="rn900"></span> <a href="#rn900"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-900 (CM-20026)</td>
<td>OSPF default-information originate stops working if removed and added in quick succession</td>
<td><p>When OSPF is originating a default route, and the command is removed from the process, then re-added, the router stops advertising the default route. Configuring the default-information originate command a second time causes it to start working.</p>
<p>This issue is currently being investigated.</p></td>
</tr>
<tr class="even">
<td><span id="rn901"></span> <a href="#rn901"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-901 (CM-19936)</td>
<td>'rdnbrd' should not be enabled with EVPN</td>
<td><p>If you start <code>rdnbrd</code> in an EVPN configuration, local and remote neighbor entries are deleted. Enabling <code>rdnbrd</code> in an EVPN configuration is not supported.</p></td>
</tr>
<tr class="odd">
<td><span id="rn902"></span> <a href="#rn902"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-902 (CM-19699)</td>
<td>BGP scaling not hashing southbound traffic from Infra switches</td>
<td><p>When routing traffic from Infra switches back through VXLAN, the switches choose one spine through which to send all flows.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn903"></span> <a href="#rn903"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-903 (CM-19643)</td>
<td>Disabling 'bgp bestpath as-path multipath relax' still leaves multipath across AS for EVPN</td>
<td><p>When BGP multipath is enabled, EVPN prefix (type-5) routes imported into a VRF always form multipath across paths that originate even from a different neighbor AS. This happens even if the <code>as-path-relax</code> configuration is disabled or not applied.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn904"></span> <a href="#rn904"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-904 (CM-20800)</td>
<td>NCLU 'net add' and 'net del' commands missing for EVPN type-5 default originate</td>
<td><p>The NCLU <code>net add</code> and <code>net del</code> commands are missing for the default originate EVPN type-5 route feature.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn907"></span> <a href="#rn907"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-907 (CM-20829)</td>
<td>'netd' fails on a reboot after upgrade to 3.6.0 with the error ImportError: No module named time</td>
<td><p>When you use the <code>apt-get upgrade</code> command to upgrade to Cumulus Linux 3.6.0 and you select to keep the currently-installed version of <code>netd.conf</code> (by typing N at the prompt), <code>netd</code> fails to start after reboot and you see errors in the logs when you try to restart it.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="odd">
<td><span id="rn908"></span> <a href="#rn908"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-908 (CM-20789)</td>
<td>In symmetric VXLAN/EVPN, FRR crashes when flapping the peer link</td>
<td><p>In a symmetric VXLAN/EVPN environment, flapping the peer link causes FRR to crash on the peer switch. The issue is not seen if the <code>clagd-vxlan-anycast-ip</code> is not configured.</p>
<p>This issue is being investigated at this time.</p></td>
</tr>
<tr class="even">
<td><span id="rn932"></span> <a href="#rn932"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-932 (CM-20869)</td>
<td>Bridge loop causes BGP EVPN to install remote MAC as a local MAC and does not recover automatically</td>
<td><p>A bridge loop causes frames that arrive through EVPN to be forwarded back to the EVPN bridge. After resolving the forwarding loop, the bridge FDB table recovers, but BGP does not recover automatically. Because the MAC appears to move rapidly, BGP installs the remote MAC as a local entry and advertises it out. Even though the bridge FDB table appears to be correct, bridged traffic destined to the misprogrammed MAC fails.</p>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="odd">
<td><span id="rn933"></span> <a href="#rn933"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-933 (CM-20781)</td>
<td>NCLU 'net add bgp neighbor' command with swp1, swp2, or swp1-2 causes TB NameError</td>
<td><p>Issuing the <code>net add bgp neighbor</code> command with swp1, swp2 or swp1-2 causes the following error:</p>
<pre><code>TB NameError: global name &#39;ifname_expand_glob&#39; is not defined.</code></pre>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
<tr class="even">
<td><span id="rn972"></span> <a href="#rn972"><img src="/images/knowledge-base/RT-mono.svg" width="32" /></a><br />
RN-972 (CM-21003)</td>
<td>Cumulus Linux does not forward PTP traffic by default</td>
<td><p>Cumulus Linux 3.6.0 or later does not forward transit precision time protocol (PTP) packets as PTP is not enabled by default in Cumulus Linux.</p>
<p>To work around this issue, do one of the following:</p>
<ul>
<li>Downgrade the switch to Cumulus Linux 3.5.3.</li>
<li>Enable PTP on the Cumulus Linux switch. Edit <code>/etc/cumulus/switchd.conf</code> and set <code>ptp.timestamping</code> to <em>TRUE</em>.</li>
</ul>
<p>This issue should be fixed in an upcoming release of Cumulus Linux.</p></td>
</tr>
</tbody>
</table>
