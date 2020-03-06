---
title: Cumulus Linux 4.0 Release Notes
author: Cumulus Networks
weight: -30
cascade:
    product: Cumulus Linux
    version: "4.0"
toc: 1
---
## Issues fixed in 4.0

<table>
 <thead>
     <tr>
     <th>Bug ID</th>
     <th>Description</th>
     <th>Affects</th>
     <th>Fixed in release</th>
     </tr>
  <thead>
  <tbody>
     <tr>
         <td>CM-28372 </td>
         <td><p>On the EdgeCore AS7326-56X switch, the default fan speed, which is defined in the thermal specification, results in excessive fan noise.</p> </td>
         <td>['3.7.11-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28313 </td>
         <td><p>On the EdgeCore Wedge100 and Facebook Wedge-100S switch, certain physical ports are not correctly mapped to the logical ones. For example:<br/>
Logical swp39 controls physical swp41<br/>
Logical swp40 controls physical swp42<br/>
Logical swp43 controls physical swp45<br/>
Logical swp44 controls physical swp46<br/>
This might causes incorrect forwarding behavior.</p> </td>
         <td>['3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-28276 </td>
         <td><p>When a Trident3 switch receives packets containing an IP checksum value that is not compliant with RFC 1624, the TTL is decremented after a routing operation but the checksum is not recalculated. This results in the IP checksum value being invalid as the packet leaves the switch. </p> </td>
         <td>['3.7.10-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-28226 </td>
         <td><p>When you restart the <tt>hsflowd</tt> service, you see a <tt>systemd</tt> warning message similar to the following:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>Warning: The unit file, source configuration file or drop-ins of hsflowd@mgmt.service changed on disk. Run 'systemctl daemon-reload'.
</pre>
</div></div> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28200 </td>
         <td><p>The Mellanox SN3700C switch encounters a memory leak after you apply an EVPN and PIM configuration.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28189 </td>
         <td><p>When host-resources and ucd-snmp-mib are polled, you see permission denied messages similar to the following:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>Jan 30 19:22:53 switch123 snmpd[23172]: Cannot statfs /sys/kernel/debug/tracing: Permission denied
</pre>
</div></div> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28184 </td>
         <td><p>TACACS users are unable to execute sudo commands.<br/>
To work around this issue, add the tacacs0 user to the sudo group; for example:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>cumulus@switch:~$  usermod -a -G sudo tacacs0
</pre>
</div></div>
<p>Alternatively, run the following command:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>ip vrf exec default sudo -i
</pre>
</div></div> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28169 </td>
         <td><p>On the Dell Z9264F-ON switch, the CPU core temperature sensors report ABSENT.</p> </td>
         <td>['3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-28160 </td>
         <td><p>On Broadcom Trident3 switches with DHCP relay, where the DHCP server is reachable through the EVPN overlay, DHCP discover packets forwarded to the CPU might appear corrupt and might not get forwarded.</p> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28156 </td>
         <td><p>NCLU crashes when you run the <tt>net add interface storage-optimized pfc</tt> command because non-ascii quotes exist in the <tt>datapath.conf</tt> file.<br/>
To work around this issue, manually edit the <tt>/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf</tt> file and replace the non-ascii single quotes  with ascii single quotes (standard single quote on the keyboard).</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28150 </td>
         <td><p>On Broadcom switches with the Trident3 ASICs, the ECN-CE bit is set by default on transit traffic. This might result in hosts adjusting traffic behavior if they are configured for the ECN feature.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28136 </td>
         <td><p>The MLAG switch pair has VLANs defined that are not used on MLAG bonds, these VLANs still synchronize MAC addresses across to the peer switch. This results in log messages that indicate a MAC address is installed and the VLAN is not defined; for example:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>RTM_NEWNEIGH with unconfigured vlan XXXX on port peerlink
</pre>
</div></div> </td>
         <td>['3.7.10-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28119 </td>
         <td><p>On the Delta AG6248C switch, the NCLU <tt>net show system sensors</tt> command shows an error:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>Could not collect output from command: ['/usr/sbin/smonctl']
</pre>
</div></div>
<p>To work around this issue, run the <tt>net show system sensors json</tt> command instead.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28087 </td>
         <td><p>The last eight ports of the EdgeCore AS4610-54P switch (swp41 through swp48) do not power UPOE access points.</p> </td>
         <td>['3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-28086 </td>
         <td><p>The <tt>ospfd</tt> daemon might crash with the following kernel trace: </p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>2019-11-06T23:00:08.261749+09:00 cumulus ospfd[5339]: Assertion `node' failed in file ospfd/ospf_packet.c, line 671, function ospf_write
</pre>
</div></div> </td>
         <td>['3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-28080 </td>
         <td><p>TACACS+ through ClearPass is not currently supported. Cumulus Linux sends authorization before authentication, but ClearPass does not accept an authorization before the user is authenticated.</p> </td>
         <td>['3.7.11-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28077 </td>
         <td><p>An unhandled exception might occur after you run the <tt>sudo poectl -i</tt> command. In addition, random <tt>poed</tt> daemon restarts can occur without any unhandled exceptions but with an invalid response length error. Both issues can occur due to a SerialException.<br/>
To work around this issue, power cycle the switch. A software reboot does not resolve the issue.</p> </td>
         <td>['3.7.10-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-28076 </td>
         <td><p>After you hot swap a PSU, the <tt>decode-syseeprom -t psuX</tt> command shows the old PSU information (such as the serial number), until you run the <tt>decode-syseeprom --init</tt> command.</p> </td>
         <td>['3.6.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28061 </td>
         <td><p>On Trident3 switches, PFC is not working as expected. If you set the PFC for only one CoS,  pause frames are sent for all CoS traffic.</p> </td>
         <td>['3.7.11-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-28048 </td>
         <td><p>The fan speeds on the Lenovo NE2580  switch are higher than expected within normal operating conditions.</p> </td>
         <td>['3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-28038 </td>
         <td><p>After you convert a bond back to a layer 2 access port, ifupdown2 changes all SVI MTUs to 1500. <br/>
To work around this issue, run <tt>ifreload -a</tt> a second time.</p> </td>
         <td>['3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-28016 </td>
         <td><p>On Mellanox Spectrum switches, <tt>switchd</tt> can sometimes fail when PBR rules are installed or removed from hardware if the rule is setting a next hop learned via a routing protocol.</p> </td>
         <td>['3.7.7-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27957 </td>
         <td><p>If you have configured a higher number of ports and VLANs (ports x VLANs) or the switch is a lower-powered (CPU) platform, the <tt>switchd</tt> service might fail to send a <tt>systemd keepalive</tt> within the watchdog timeout value (2 minutes by default) and you see an error similar to the following:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>bq. systemd[1]: switchd.service watchdog timeout (limit 2min)!
</pre>
</div></div>
<p>To workaround this issue, either reduce the number of configured interfaces and/or VLANs or increase the <tt>systemd</tt> timeout for <tt>switchd.service</tt>.<br/>
To increase the <tt>systemd</tt> timeout:</p>
<ol>
	<li>Edit the <tt>/etc/systemd/system/switchd.service.d/override.conf</tt> file and increase the <tt>WatchdogSec</tt> parameter.</li>
	<li>Restart the <tt>switchd</tt> service with the <tt>sudo systemctl restart switchd.service</tt> command.<br/>
<tt>systemd</tt> will attempt to restart the <tt>switchd</tt> service automatically (after the watchdog timeout). If the restart fails multiple times in a short time period, run the <tt>sudo systemctl reset-failed</tt> command followed by the <tt>sudo systemctl restart switchd</tt> command.</li>
</ol>
 </td>
         <td>['3.7.11-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27950 </td>
         <td><p>On the Dell S5232F, S5248F, S5296F, and S3048 switches, using the <tt>poweroff</tt> or <tt>halt</tt> commands does not fully power off the switch.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27947 </td>
         <td><p>Broadcom Field Alert - SID - MMU 2B Errors<br/>
A few of the MMU memories on Broadcom switches are grouped together with single parity control. During SER correction when a parity error occurs on one of those groups, other memories in that group might also report a SER error. This occurs when the memory is accessed either by a packet hit or through a schan operation.This issue can cause SER errors in other memory and cause traffic mis-forwarding or a packet drop.</p> </td>
         <td>['3.7.0-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27855 </td>
         <td><p>The FRR cl-support module times out on switches on the ARM platform even when the switch is not under heavy load.<br/>
To work around this issue, run the <tt>cl-support -M</tt> command to disable timeouts.</p> </td>
         <td>['3.7.0-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27801 </td>
         <td><p>On the Mellanox SN3700C switch, if you try to break out 100G switch ports into 2x50G, the configuration fails and <tt>switchd</tt> does not restart. Breaking out the ports into 4x25G works without issue.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27793 </td>
         <td><p>A security vulnerability has been announced in the cyrus-sasl2 (libsasl2-2 and libsasl2-modules) package. The libraries are installed by default on Cumulus Linux.<br/>
CVE-2019-19906: Stephan Zeisberg reported an out-of-bounds write vulnerability in the _sasl_add_string() function in cyrus-sasl2, a library implementing the Simple Authentication and Security Layer. A remote attacker can take advantage of this issue to cause denial-of-service conditions for applications using the library.<br/>
Vulnerable: 2.1.27+dfsg-1<br/>
Fixed: 2.1.27+dfsg-1+deb10u1</p> </td>
         <td>['3.0.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27764 </td>
         <td><p>On the EdgeCore AS7326-56X, eth0 and swp1 use the same MAC address.</p> </td>
         <td>['3.7.9-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27753 </td>
         <td><p>The EdgeCore Minipack-AS8000 supports FEC RS by default; you cannot disable this setting. However, the <tt>ethtool --show-fec</tt> command output indicates that FEC is disabled. Also, if you try to change the FEC setting, Cumulus Linux reports an error. For example:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>cumulus@switch:~$  net add interface swp23 link speed 100000
cumulus@switch:~$  net add interface swp23 link autoneg off
cumulus@switch:~$  net add interface swp23 link fec rs
"/sbin/ifreload -a" failed:
error: swp23: cmd '/sbin/ethtool --set-fec swp23 encoding rs' failed: returned 255 (Cannot set FEC settings: Operation not supported)
Command '['/sbin/ifreload', '-a']' returned non-zero exit status 1
</pre>
</div></div> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27740 </td>
         <td><p>On a Mellanox SN3700C switch, when you run the NCLU <tt>net del all</tt> command to delete all configuration on the switch, you see an error similar to the following:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>ERROR: [Errno 2] No such file or directory: '/cumulus/switchd/config/interface/&lt;swp&gt;/port_security/enable'#012Traceback
</pre>
</div></div> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27719 </td>
         <td><p>Several vulnerabilities have been discovered in the interpreter for the Ruby language, which could result in unauthorized access by bypassing intended path matchings, denial of service, or the execution of arbitrary code.<br/>
These vulnerabilities affect the ruby2.5 package that is available for optional installation in Cumulus Linux 4.x, but is not installed by default.<br/>
CVE-2019-15845: Ruby through 2.4.7, 2.5.x through 2.5.6, and 2.6.x through 2.6.4 mishandles path checking within File.fnmatch functions.<br/>
CVE-2019-16201: WEBrick::HTTPAuth::DigestAuth in Ruby through 2.4.7, 2.5.x through 2.5.6, and 2.6.x through 2.6.4 has a regular expression Denial of Service cause by looping/backtracking. A victim must expose a WEBrick server that uses DigestAuth to the Internet or a untrusted network.<br/>
CVE-2019-16254: Ruby through 2.4.7, 2.5.x through 2.5.6, and 2.6.x through 2.6.4 allows HTTP Response Splitting. If a program using WEBrick inserts untrusted input into the response header, an attacker can exploit it to insert a newline character to split a header, and inject malicious content to deceive clients.<br/>
CVE-2019-16255: Ruby through 2.4.7, 2.5.x through 2.5.6, and 2.6.x through 2.6.4 allows code injection if the first argument (aka the "command" argument) to Shell#[] or Shell#test in lib/shell.rb is untrusted data. An attacker can exploit this to call an arbitrary Ruby method.<br/>
Vulnerable: 2.5.5-3</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27699 </td>
         <td><p>In a default VX instance, a ping to a device's hostname fails.<br/>
To work around this issue, edit the <tt>/etc/gai.conf</tt> file and uncomment <tt>precedence ::ffff:0:0/96  10</tt>.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27678 </td>
         <td><p>The <tt>net show bridge macs</tt> command returns an empty interface column.<br/>
To work around this issue, run the <tt>bridge fdb show</tt> command to show the interface.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27670 </td>
         <td><p>A memory leak in <tt>switchd</tt> might occur, which causes <tt>switchd</tt> to restart.</p> </td>
         <td>['3.7.10-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27645 </td>
         <td><p>Several vulnerabilities have been discovered in git, a fast, scalable,<br/>
distributed revision control system, which is installed by default on Cumulus Linux 4.x.<br/>
CVE-2019-1348: export-marks is insecure, fix is to disable by default.<br/>
CVE-2019-1349: .git / git~1 filename vulnerability on NTFS<br/>
CVE-2019-1352: .git vulnerability with NTFS Alternate Streams Accesses<br/>
CVE-2019-1353: NTFS filesystem protection should be on by default<br/>
CVE-2019-1387: dubiously-nested submodule git directories should be disallowed<br/>
CVE-2019-19604: submodule update repository code execution vulnerability<br/>
Vulnerable: &lt;= 2.20.1-2<br/>
Fixed: 2.20.1-2+deb10u1</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27644 </td>
         <td><p>Ifupdown2 does not set up the front panel interface for the <tt>dhclient</tt> to accept the DHCP OFFER.<br/>
To work around this issue, restart the networking service after <tt>ifreload -a</tt> with the <tt>systemctl restart networking</tt> command.</p> </td>
         <td>['3.7.10-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27642 </td>
         <td><p>The following CVEs were announced that affect the libssh package:<br/>
CVE-2019-14889 has been announced in the libssh library, where unsanitized user-provided scp command lines could allow an attacker to execute arbitrary commands on the server.<br/>
The libssh library is not installed on Cumulus Linux by default, but is available in the Cumulus Linux 4 repository for optional installation. Note that libssh is distinct from libssh2 and openssh, which are present on the switches and in the repositories.<br/>
See the following for more information:<br/>
<a href="https://www.libssh.org/security/advisories/CVE-2019-14889.txt" class="external-link" rel="nofollow">https://www.libssh.org/security/advisories/CVE-2019-14889.txt</a><br/>
<a href="https://security-tracker.debian.org/tracker/CVE-2019-14889" class="external-link" rel="nofollow">https://security-tracker.debian.org/tracker/CVE-2019-14889</a></p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27637 </td>
         <td><p>On the EdgeCore Minipack-AS8000 switch, a 100G DAC link does not come up when auto-negotiation is enabled on the neighbor. This switch does not support 100G DAC auto-negotiation at this time.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27619 </td>
         <td><p>The following security vulnerabilities have been announced in the nss / libnss3 library, which is not installed by default but is available in the repository:<br/>
CVE-2019-11745: Out-of-bounds write when passing an output buffer smaller than the block size to NSC_EncryptUpdate<br/>
CVE-2019-17007: nss: Handling of Netscape Certificate Sequences in CERT_DecodeCertPackage() may crash with a NULL deref leading to DoS<br/>
See <a href="https://security-tracker.debian.org/tracker/source-package/nss" class="external-link" rel="nofollow">https://security-tracker.debian.org/tracker/source-package/nss</a> for more information.<br/>
Vulnerable: &lt;= 3.42.1-1+deb10u1</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27496 </td>
         <td><p>All Broadcom Trident3 X7 switches contain PCIE firmware, which is programmed by the vendor when the switch is manufactured. The latest version of this firmware (2.6) is incompatible with Cumulus Linux 3.7.11 and earlier, and Cumulus Linux 4.0. <br/>
To work around this issue, downgrade the Broadcom ASIC firmware to an earlier version.<br/>
A fix for this issue will be provided in a future Cumulus Linux release.</p> </td>
         <td>['3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27457 </td>
         <td><p>If you delete, then re-add a PBR policy on an interface, the configured PBR policy is not programmed in the kernel or <tt>switchd</tt>.</p> </td>
         <td>['3.7.9-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27456 </td>
         <td><p>After making a series of PBR configuration changes using NCLU commands, the stale PBR entry is still present in the kernel.</p> </td>
         <td>['3.7.9-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27444 </td>
         <td><p>If you use the NCLU commands to configure NTP and run the <tt>net add time ntp source &lt;interface&gt;</tt> command before you run the <tt>net add time ntp server &lt;server&gt; iburst</tt> command, the <tt>/etc/ntp.conf</tt> file is misconfigured.<br/>
To work around this issue, run the <tt>net add time ntp server &lt;server&gt; iburst</tt> command before you run the <tt>net add time ntp source &lt;interface&gt;</tt> command.</p> </td>
         <td>['3.7.10-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27367 </td>
         <td><p>Under certain circumstances, <tt>switchd</tt> might crash, then restart, on Mellanox switches with the Spectrum or Spectrum-2 ASIC.  </p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27299 </td>
         <td><p>The protocol daemon <tt>bgpd</tt> crashes when a link/neighbor flaps if static routes pointing to Null0 are advertising through BGP.<br/>
To work around this issue, reboot the switch, then remove the static routes or stop advertising these routes.</p> </td>
         <td>['3.7.9-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27295 </td>
         <td><p>IPv6 table rules might affect forwarding. For example, if you create the following rule in the <tt>/etc/cumulus/acl/policy.d/03-sshd.rules</tt> file, the rule counter increments but IPv4 SSH traffic might be dropped.</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>[ip6tables]
-A INPUT -p tcp --dport 22 -j DROP
</pre>
</div></div> </td>
         <td>['3.7.2-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27275 </td>
         <td><p>CVE-2018-12207: Improper invalidation for page table updates by a virtual guest operating system for multiple Intel(R) Processors may allow an authenticated user to potentially enable denial of service of the host system via local access.<br/>
Running hypervisors for virtual guest operating systems is not supported on Cumulus Linux.  Additionally, an affected package qemu is not included in the image, although it is available on upstream repo mirrors.  </p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27254 </td>
         <td><p>On Mellanox switches with the Spectrum and Spectrum-2 ASIC, IPv6 egress ACLs are not supported on subinterfaces.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27243 </td>
         <td><p>The length of the netlink message is not set properly for non-bridge family type messages. The same length is used for both bridge and non-bridge family type messages even though the bridge family type message has an extra attribute. This causes extra bytes to be left over in non-bridge family type netlink messages.</p> </td>
         <td>['3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27229 </td>
         <td><p>On a traditional bridge, VLAN tagged traffic is not discarded when it exceeds the port security MAC limit.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27193 </td>
         <td><p>The <tt>l1-show</tt> command prints a traceback for switch ports that have sub-interfaces configured. There is no functional impact to traffic but the <tt>l1-show</tt> troubleshooting and validation command does not execute on switch ports that have VLAN sub-interfaces.</p> </td>
         <td>['3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27184 </td>
         <td><p>With the port security feature, if you change the number of MAC addresses allowed to access a port with the NCLU <tt>net add interface &lt;port&gt; port-security mac-limit &lt;number&gt;</tt> command, the <tt>net show configuration commands</tt> command might fail.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27173 </td>
         <td><p>On Trident3 switches, unicast ARP packets received on a VNI and forwarded to the CPU are not policed.</p> </td>
         <td>['3.7.10-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27143 </td>
         <td><p>The CPU core temperature sensors are absent on the Dell S5248F-ON switch.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27136 </td>
         <td><p>With a high number of active routes (20K or more), when you perform a networking restart, the FRR log files might become flooded with error messages associated with the restart. These logs are normal and are not directly a problem. However, the large number of messages can cause the logs to <em>rotate away</em> any previous history, which prevents you from tracing back events leading up to the restart. In a troubleshooting environment, this can be problematic.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27131 </td>
         <td><p>On switches with the Broadcom Tomahawk3 ASIC, such as the EdgeCore Minipack AS8000, SPAN and ERSPAN functionality is not supported.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27118 </td>
         <td><p>Switches with the Broadcom Tomahawk3 ASIC, such as the EdgeCore Minipack AS8000, might not learn all MAC address on a port configured for bridging when the hardware MAC table is near the maximum capacity.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27099 </td>
         <td><p>Precision Time Protocol (PTP) is not currently supported on Mellanox switches with the Spectrum-2 ASIC. </p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27096 </td>
         <td><p>Rare I2C errors seen on Edgecore AS6812 switch.</p> </td>
         <td>['3.7.2-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-27094 </td>
         <td><p>On the Delta AG9032v1 switch, smonctl and sensors report inaccurate PSU current and power.</p> </td>
         <td>['3.5.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27081 </td>
         <td><p>On the switches with the Broadcom Tomahawk3 ASIC, such as the EdgeCore Minipack AS8000, if you configure more than 96 ports in a layer 2 bridge, <tt>switchd</tt> might hit a timeout error and restart.  </p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-27018 </td>
         <td><p>When more than one VRR interface is configured on an SVI interface, deleting one of the VRR addresses does not remove the interface/address. </p> </td>
         <td>['3.7.10-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26996 </td>
         <td><p>On Mellanox switches with the Spectrum ASIC, the <tt>--set-burst</tt> parameter in an iptables rule does not take effect.</p> </td>
         <td>['3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26968 </td>
         <td><p>When networking fails to start properly, an MLAG memory leak occurs, which might cause memory issues.</p> </td>
         <td>['3.7.9-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26961 </td>
         <td><p>On Mellanox switches, error messages with <tt>hw-management-thermal-events.sh</tt> are displayed on shutdown.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26942 </td>
         <td><p>Port security is not currently supported on VX. The NCLU commands produce errors.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26921 </td>
         <td><p>If you delete an undefined bond, then add a bond slave, the <tt>net commit</tt> command fails.</p> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26913 </td>
         <td><p>FRR configuration commands for an SVI interface might have the \n misplaced in the output.  For example:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>sudo sh -c "printf 'interface 50\nvrf TEST description L3 routing interface\n' &gt;&gt; /etc/frr/frr.conf"
</pre>
</div></div>
<p>should be:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>sudo sh -c "printf 'interface 50 vrf TEST\ndescription L3 routing interface\n' &gt;&gt; /etc/frr/frr.conf"
</pre>
</div></div>
<p>To work around this issue, configure the interface manually in the <tt>/etc/frr/frr.conf</tt> file.</p> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26907 </td>
         <td><p>NCLU incorrectly allows you to apply port security configuration on layer 2 and layer 3 ports that are not part of a bridge.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26905 </td>
         <td><p>When you update the hostname of a switch with the NCLU <tt>net add hostname &lt;hostname&gt;</tt> command, then run <tt>net commit</tt>, the <tt>lldpd</tt> service is not restarted and other devices still see the old name.<br/>
To work around this issue, run the <tt>sudo systemctl restart lldpd.service</tt> command.</p> </td>
         <td>['3.7.10-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26875 </td>
         <td><p>After deleting an IPv6 numbered BGP peer group neighbor, Cumulus Linux may continue to send RAs.  To address this, restart frr after removing IPv6 numbered configuration.</p> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26860 </td>
         <td><p>When you run the NCLU <tt>net show commit last</tt> command, there is no output.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26839 </td>
         <td><p>On the Dell S5248F-ON switch, CPU core temp sensors may show as ABSENT.</p> </td>
         <td>['4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26838 </td>
         <td><p>You might experience a <tt>bgpd</tt> memory usage increase and significant update exchanges due to host moves between VTEPs.</p> </td>
         <td>['3.7.7-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26769 </td>
         <td><p>Setting ProtoDown on ports populated with SFP modules providing RJ-45 1000BASE-T interfaces does not cause the carrier to be dropped. The kernel shows carrier down; however, the remote device still shows a link.</p> </td>
         <td>['3.7.6-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26702 </td>
         <td><p>On Mellanox switches with the Spectrum-2 ASIC, policy-based routing (PBR) is not currently supported.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26655 </td>
         <td><p>Reconfiguring an NTP server via NCLU with different trailing options (such as iburst) after the IP address causes an invalid configuration to be added to the <tt>/etc/ntp.conf</tt> file.  As an example</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>net add time ntp server 1.2.3.4 iburst
net commit
net add time ntp server 1.2.3.4
net commit
</pre>
</div></div>
<p>If you need to alter existing server configurations, first remove the server, commit, then re-add the server with any trailing options.</p> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26599 </td>
         <td><p>Auto-negotiation does not work with the QSFP28 cables and a remote system opreating at 10G. Attempting to enable auto-negotiation via <tt>ethtool -s swp&lt;#&gt; autoneg on</tt> returns <tt>Operation not supported</tt>.</p>

<p>As a workaround, do not use auto-negotiation and set the local port speed to 10G.</p> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26595 </td>
         <td><p>The NCLU <tt>net show lldp</tt> command displays the speed of a ganged port group as the speed of one of the individual links, rather than the sum of their speeds.</p> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26525 </td>
         <td><p>When an MLAG peerlink frequently alternates states between learning and blocking, an excessive number of TCP sessions might be created, which results in the following error display:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>OSError: [Errno 24] Too many open files
</pre>
</div></div> </td>
         <td>['3.6.2-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26516 </td>
         <td><p>Applying a policy-based routing (PBR) rule for all traffic from a host might disrupt ARP refresh for that connected host.</p> </td>
         <td>['3.7.5-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26450 </td>
         <td><p>Cumulus Linux poed generates excessive debug log entries.  These will be reduced in a future release.</p> </td>
         <td>['3.7.3-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26423 </td>
         <td><p>NCLU requires you to specify an interface with multiple address-virtual statements in ascending MAC address order. </p>
 </td>
         <td>['3.7.5-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26412 </td>
         <td><p>Mac learning is not disabled by default on a double tagged peer link interface resulting in the MAC address flipping between the MLAG bond and the peer link.<br/>
To work around this issue, disable MAC learning on QinQ VLANs by adding <tt>bridge-learning off</tt> to the VLAN stanza in the <tt>etc/network/interfaces</tt> file.</p> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26308 </td>
         <td><p>An interface alias configured outside FRR using <tt>iproute2</tt> is imported into the FRR running configuration and overrides the internal description. After an FRR reload, this causes FRR to delete the interface alias in an inefficient way. Depending on how many interfaces with aliases you have configured, this can cause a FRR reload to time out.<br/>
To work around this issue, remove the interface alias description from <tt>iproute2</tt>.</p> </td>
         <td>['3.7.8-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26288 </td>
         <td><p>On Mellanox switches, static VXLAN tunnels incorrectly allow traffic from any remote tunnel IP address.</p> </td>
         <td>['3.7.8-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26256 </td>
         <td><p>The <tt>net show evpn vni detail json</tt> command includes an extra empty dictionary at the end of the output. </p>
 </td>
         <td>['3.7.8-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26241 </td>
         <td><p>On the Dell S5248F-ON switch, <tt>smond</tt> may generate syslog messages indicating that the fan input RPM is lower than the normal low speed of 2500 RPM.  Speeds as low as 1700 RPM are acceptable in normal thermal environments and so these messages can be disregarded.</p> </td>
         <td>['3.7.6-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26225 </td>
         <td><p>On the EdgeCore AS5712, AS6712, AS5812 and AS6812 switch, support for multiple PSU types results in log messages similar to the following:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>2019-09-05T05:15:17.246597+00:00 hp-6712-03 decode-syseeprom: Unable to find eeprom at /sys/bus/i2c/devices/11-0050/eeprom for psu2
2019-09-05T05:15:17.274521+00:00 hp-6712-03 decode-syseeprom: Unable to find eeprom at /sys/bus/i2c/devices/12-0053/eeprom for psu2
2019-09-05T05:15:17.469556+00:00 hp-6712-03 decode-syseeprom: Unable to find eeprom at /sys/bus/i2c/devices/11-0050/eeprom for psu2
2019-09-05T05:15:17.497514+00:00 hp-6712-03 decode-syseeprom: Unable to find eeprom at /sys/bus/i2c/devices/12-0053/eeprom for psu2
</pre>
</div></div> </td>
         <td>['3.7.9-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26217 </td>
         <td><p>NCLU does not allow you to configure OSPF NSSAs. For example: </p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>cumulus@switch:~$ net add ospf area 0.0.0.1 nssa 
ERROR: Command not found. 
net add ospf area 0.0.0.1 nssa
</pre>
</div></div>
<p>To work around this issue, use FRR instead. For example: </p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>switch# configure terminal 
switch(config)# router ospf 
switch(config-router)# area 0.0.0.1 nssa 
</pre>
</div></div> </td>
         <td>['3.7.7-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26200 </td>
         <td><p>The following CVEs were announced that affect the systemd-resolved package. <br/>
Cumulus Linux does not enable <tt>systemd-resolved</tt> by default, so Cumulus Linux is not vulnerable as shipped. <br/>
CVE-2019-15718 <br/>
Missing access controls on systemd-resolved's D-Bus interface <br/>
Source Package Release Version Status: buster 241-7 vulnerable<br/>
For the detailed security status, refer to the security tracker page at:<br/>
<a href="https://security-tracker.debian.org/tracker/CVE-2019-15718" class="external-link" rel="nofollow">https://security-tracker.debian.org/tracker/CVE-2019-15718</a></p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26179 </td>
         <td><p>If a hostname contains utf-8 characters, the NCLU <tt>net show lldp</tt> command outputs the following error: </p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>ERROR: 'ascii' codec can't encode character u'\xe9' in position 3: ordinal not in range(128) 
See /var/log/netd.log for more details.  
</pre>
</div></div> </td>
         <td>['3.7.7-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26158 </td>
         <td><p>On Mellanox switches, UFT profiles are unable to support the documented capacity for routes to addresses that are more than 64 bits in length. The listed capacities assume 64-bit destination IP addresses.</p> </td>
         <td>['3.7.8-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-26139 </td>
         <td><p>Selective ERSPAN does not work when you specify a bridge port.</p> </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26138 </td>
         <td><p>You cannot specify a source and destination MAC address in an ERSPAN ebtables rule. For example, the following rule does not work:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>-A FORWARD -i swp5 -s 00:25:90:b2:bd:9d -d 50:6b:4b:96:c4:04 -j erspan --src-ip 100.1.1.2 --dst-ip 100.1.1.1 --ttl 64
</pre>
</div></div> </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26137 </td>
         <td><p>ERSPAN in ebtables does not work for VNIs. For example, the following rule does not work:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>-A FORWARD -i vni10 -j erspan --src-ip 100.1.1.2 --dst-ip 100.1.1.1 --ttl 64
</pre>
</div></div> </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26136 </td>
         <td><p>In an ebtables rule, ERSPAN (upper case) does not work. You need to specify erspan (lower case).</p> </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-26024 </td>
         <td><p>On switches with the Spectrum ASIC, the underlay hashes VXLAN packets for a given overlay flow randomly.<br/>
To work around this issue, configure the ECMP hash seed to the same value on the EVPN egress leaf switches.</p> </td>
         <td>['3.7.7-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25986 </td>
         <td><p>On the Mellanox SN3700C switch, the time required to establish a link (from the time a link is set to <tt>admin up</tt> until the link becomes operationally up) can take between 5 and 10 seconds. </p>
 </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25890 </td>
         <td><p>In some cases, the <tt>switchd</tt> service might warn of excessive MAC moves from one switch port to itself (for example, from swp18 to swp18).</p> </td>
         <td>['3.7.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25859 </td>
         <td><p>The MTU of an SVI cannot be higher than the MTU on the bridge. Changing the MTU on the SVI with NCLU does not update the bridge MTU. The <tt>net commit</tt> commands succeeds even though the MTU is not changed as expected.<br/>
To work around this issue, change the MTU on all SVIs and the bridge manually in the <tt>/etc/network/interfaces</tt> file, then apply the change with the <tt>ifreload -a</tt> command.</p> </td>
         <td>['3.7.7-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25815 </td>
         <td><p>When an SVI with a virtual MAC is configured with a layer 2 VNI in an EVPN environment , if the <tt>/etc/network/interfaces</tt> file is replaced with a different file that does not have the SVI and layer 2 VNI configuration anymore, the original virtual MAC does not get populated through the EVPN route until FRR is restarted. </p>
 </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25766 </td>
         <td><p>When you run the <tt>apt upgrade</tt> command on the Dell-N3048EP switch, the upgrade does not work. </p>
 </td>
         <td>['3.7.7-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25740 </td>
         <td><p>On Broadcom Maverick switches with a QinQ configuration, the packets coming into the CPU might be tagged incorrectly; for example, 802.1ad + 802.1q tags are expected in the packets but the packets have 802.1q + 802.1q tags. <br/>
 To work around this issue, configure the bridge with <tt>bridge-vlan-protocol 802.1ad</tt>: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 cumulus@switch:~$ net add bridge mybridge vlan-protocol 802.1ad 
 </pre>
</div></div> 
 </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25694 </td>
         <td><p>If a packet is policed by ebtables, it does not increment an ACL drop on the ingress interface. Instead, it increments the TDBGC3/6 drop counter to the CPU.</p> </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25693 </td>
         <td><p>After you issue the NCLU <tt>net del bgp vrf &lt;vrf&gt; autonomous-system &lt;AS&gt;</tt> command and commit the change, Cumulus Linux does not remove the configuration from the <tt>/etc/frr/frr.conf</tt> file or the <tt>net show config commands</tt>. </p>
 </td>
         <td>['3.7.3-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-25665 </td>
         <td><p>On Broadcom Trident 3 switches, VXLAN encapsulated packets are dropped on the ingress port (tagged layer 2 port) during transit forwarding (the local switch does not terminate the VXLAN tunnel). An example of where this two-layer VXLAN inside VXLAN encapsulation might occur:</p>
<ul class="alternate" type="square">
	<li>VXLAN tunnel (#1) between two servers (different racks) to provide layer 2 extension for containers or VM hosts.</li>
	<li>VXLAN tunnel (#2) between the TOR switch in rack 1 to the TOR switch located in the remote rack.</li>
</ul>


<p>To work around this issue, either:</p>
<ul class="alternate" type="square">
	<li>Configure the edge port (facing the servers) to be an access port (instead of a trunk/tagged port)</li>
	<li>Change the destination port from 4789 to something else (VXLAN tunnel terminated by the servers)</li>
</ul>
 </td>
         <td>['3.7.5-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-25641 </td>
         <td><p>If the BMC operating system fails to respond to IPMI, you see a traceback in <tt>bmcd</tt>, and all the sensors might report ABSENT devices in <tt>smonctl</tt>. <br/>
 To work around this issue, power cycle the switch. </p>
 </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25505 </td>
         <td><p>During the bring-up sequence following a reboot, VXLAN routed packets (tenant traffic flows) transiting an MLAG peer are dropped until the <tt>clagd</tt> <tt>init-delay</tt> timer expires. <br/>
The problem is caused by a race condition when programming the anycast IP address (used to terminate VXLAN tunnels), where the hardware is programmed before the software by <tt>clagd</tt>. To route the tenant traffic flows, the kernel must perform address resolution but has to wait for the <tt>clagd</tt> <tt>init-delay</tt> timer to expire before the bonds can forward traffic. During the time when the ARP entry is unresolved, packets might be dropped. <br/>
During the <tt>init-delay</tt> period, the ARP cache is not yet populated so the problem exists until either the <tt>init-delay</tt> timer expires or <tt>clagd</tt> neighbor synchronization is complete. By default the <tt>clagd</tt> <tt>init-delay</tt> timer is set to 10 seconds and <tt>clagd</tt> neighbor synchronization occurs halfway through the <tt>init-delay</tt> period. Traffic resumes forwarding after one of the two criteria described above are met. <br/>
You might see this issue in EVPN symmetric or centralized configurations with BGP peering over a peer link. <br/>
To work around this issue, configure the BGP path across the peer link to be less preferred. The example below uses AS path prepending and the MLAG switches are iBGP neighbors. However, other BGP configurations achieve the same result. <br/>
In the <tt>/etc/frr/frr.conf</tt> file, make a new AS path access list and route map to apply BGP pre-pending of the local ASN one or more times. For example: </p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
ip as-path access-list MY_ASN permit ^$ 

route-map peerlink-add-asn permit 10 
match as-path MY_ASN 
set as-path prepend 4200000101 
route-map peerlink-add-asn permit 20 
</pre>
</div></div>  </td>
         <td>['3.7.6-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-25400 </td>
         <td><p>If an SVI exists in the configuration before you assign it an IP address, when you do assign the IP address with the NCLU command, the vlan-id and the raw-device bridge stanzas are not added automatically. </p>
 </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-25397 </td>
         <td><p>When first creating a bond and enslaving an interface, NCLU hides some of the bridge command suggestions, although they are still accepted. </p>
 </td>
         <td>['3.7.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24993 </td>
         <td><p>When you try to change the NTP time zone with the NCLU <tt>net add time zone &lt;timezone&gt;</tt> command or by editing the <tt>/etc/timezone</tt> file manually, the configuration does not take effect.<br/>
To work around this issue, change the time zone with the <tt>sudo timedatectl set-timezone &lt;timezone&gt;</tt> command. For example:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>cumulus@switch:~$ sudo timedatectl set-timezone US/Eastern
</pre>
</div></div> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24894 </td>
         <td><p>The <tt>maximum-prefix</tt> configuration under the IPv4 address family has an optional restart value which you can configure. This configuration is ignored and, instead of restarting the sessions every x minutes, the peer constantly changes between established and idle due to the prefix count being exceeded. </p>
 </td>
         <td>['3.7.5-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24803 </td>
         <td><p>When you execute the following command on the Dell N3048EP-ON or the Delta AG6248C, the switch reboots and then comes right back into Cumulus Linux without installing the new image. The install image is still in <tt>/var/lib/cumulus/installer</tt>, which causes issues with cl-support. </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 cumulus@switch:~$ sudo onie-install -fai http://&lt;path to image&gt; 
 cumulus@switch:~$ sudo reboot 
 </pre>
</div></div> 
<p>To work around this issue, use the <tt>onie-select</tt> command to access ONIE, and then use the <tt>nos-install</tt> command in ONIE to install a new binary image. <br/>
The workaround only works when an out-of-band network is present.</p> </td>
         <td>['3.7.6-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24799 </td>
         <td><p>On switches using the Trident2 ASIC, 802.1Q-encapsulated control plane traffic received on an interface with 802.1AD configured subinterfaces might be dropped. <br/>
This issue only affects QinQ configurations. </p>
 </td>
         <td>['3.7.5-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24762 </td>
         <td><p>On the EdgeCore AS7326 switch, the 1000BASE-T SFP RJ-45 on a 25G port does not work at 1G. </p>
 </td>
         <td>['3.7.3-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-24751 </td>
         <td><p>On the QuantaMesh T4048-IX8 or EdgeCore AS7326-56X switches, when using a 1000BASE-T SFP module, the module LEDs do not light to reflect link status.</p>
 </td>
         <td>['3.7.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24652 </td>
         <td><p>In an EVPN environment, the centralized MAC address is not getting installed on the MLAG pair because Cumulus Linux does not perform an SVI MAC check per VLAN. <br/>
 This issue does not manifest itself in a pure distributed routing (symmetric or asymmetric) environment or in a pure centralized routing environment. </p>
 </td>
         <td>['3.7.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24618 </td>
         <td><p>If the interface alias contains a single or double quotation mark, or an apostrophe, the <tt>net show configuration</tt> commands fail with the following error: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 ERROR: No closing quotation 
 See /var/log/netd.log for more details. 
 </pre>
</div></div> 
 </td>
         <td>['3.6.1-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24473 </td>
         <td><p>SNMP incorrectly requires engine ID specification. </p>
 </td>
         <td>['3.7.4-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24435 </td>
         <td><p>When you use NCLU to configure a route map, the parser allows for glob matching of interfaces for a <em>match interface</em> condition when there can only be a single interface matched. The proper syntax is to use multiple route map clauses, each matching a single interface, instead of a single clause matching multiple interfaces. <br/>
 For example, this command is incorrect: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 net add routing route-map Proxy-ARP permit 25 match interface swp9-10 
 </pre>
</div></div> 
<p> These commands are correct: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 net add routing route-map Proxy-ARP permit 25 match interface swp9 
 net add routing route-map Proxy-ARP permit 30 match interface swp10 
 </pre>
</div></div> 
 </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24426 </td>
         <td><p>NCLU allows for the configuration of addresses on VRF interfaces, but tab completion for the <tt>net add vrf &lt;name&gt;</tt> command just displays &lt;ENTER&gt;. For example: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 cumulus@switch:~$ net add vrf mgmt 
 &lt;ENTER&gt; 
 </pre>
</div></div> 
<p> Tab completion for the <tt>net add vrf &lt;name&gt; ip address &lt;address&gt;</tt> command works correctly. </p>
 </td>
         <td>['3.7.4-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24379 </td>
         <td><p>On Maverick switches, CPU forwarded packets might be dropped when there is no route to a leaked host route.</p> </td>
         <td>['3.7.5-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24343 </td>
         <td><p>The <tt>net del bridge bridge mcsnoop yes</tt> command does not return the value to the default of disabled. <br/>
To work around this issue, use the <tt>net add bridge bridge mcsnoop no</tt> command to delete the <tt>mcsnoop attribute</tt> and return to the default value.</p> </td>
         <td>['3.7.4-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24332 </td>
         <td><p>On Broadcom switches, when moving configuration from bridged to routed (or toggling from routed to bridged to routed), some traffic is not seen by the kernel. This can cause BGP to not establish on a transit node. </p>
 </td>
         <td>['3.7.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24272 </td>
         <td><p>When you try to configure the VRRP priority and advertisement-interval with NCLU on a traditional mode bridge, the <tt>net commit</tt> command fails. <br/>
 To work around this issue, use the vtysh command (inside FRR) to change the VRRP priority or advertisement-interval on traditional bridges. For example: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 cumulus@switch:~$ sudo vtysh 
 switch# configure terminal 
 switch(config)# interface br0.100 
 switch(config-if)# vrrp 1 priority 110 
 switch(config-if)# vrrp 1 advertisement-interval 
 switch(config-if)# end 
 switch# write memory 
 switch# exit 
 cumulus@switch:~ 
 </pre>
</div></div> 
 </td>
         <td>['3.7.4-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24271 </td>
         <td><p>On SVIs in a VLAN-aware bridge, you cannot change the VRRP priority with NCLU. <br/>
 To work around this issue, run the vtysh command inside FRR to change the default priority. For example: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 cumulus@switch:~$ sudo vtysh 
 switch# configure terminal 
 switch(config)# interface vlan100 
 switch(config-if)# vrrp 1 priority 110 
 switch(config-if)# end 
 switch# write memory 
 switch# exit 
 cumulus@switch:~ 
 </pre>
</div></div> 
 </td>
         <td>['3.7.4-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24270 </td>
         <td><p>Cumulus Linux uses VRRPv3 as the default version, and enables both preempt and accept mode by default. You cannot change these default values with NCLU. <br/>
To work around this issue, run the vtysh commands (inside FRR) to change the default values. For example: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 cumulus@switch:~$ sudo vtysh 
 switch# configure terminal 
 switch(config)# interface swp4 
 switch(config-if)# vrrp 1 version 2 
 switch(config-if)# no vrrp 1 preempt 
 switch(config-if)# end 
 switch# write memory 
 switch# exit 
 cumulus@switch:~ 
 </pre>
</div></div> 
 </td>
         <td>['3.7.4-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24262 </td>
         <td><p>NCLU does not honor "auto all" in the <tt>/etc/network/interfaces</tt> file and removes the existing configuration if no individual <tt>auto &lt;iface&gt;</tt> lines exist. </p>
 </td>
         <td>['3.7.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24241 </td>
         <td><p>When you try to remove a BGP peer group configuration with NCLU, the command fails but no warning message is shown. For example: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 cumulus@switch:~$ net del bgp neighbor fabric peer-group 
 'router bgp 65001' configuration does not have 'neighbor fabric peer-group' 
 </pre>
</div></div> 
 </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24222 </td>
         <td><p>When an LDAP user that does not have NCLU privileges (either in the <tt>netshow</tt> or <tt>netedit</tt> group, or in the <tt>/etc/netd.conf</tt> file) runs an NCLU command, a traceback occurs instead of a permissions error. </p>
 </td>
         <td>['3.7.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-24035 </td>
         <td><p>On the Edgecore 4610-54P switch, automatic medium-dependent interface crossover (auto-MDIX) stops working on a 100M full duplex interface and does not detect the required cable connection type. </p>
 </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23825 </td>
         <td><p>The <tt>net add interface &lt;interface&gt; ptm-enable</tt> command adds <tt>no ptm-enable</tt> for that interface in the <tt>frr.conf</tt> file. <br/>
 Running the <tt>net add</tt> or the <tt>net del</tt> command does not remove <tt>no ptm-enable</tt> from the <tt>frr.conf</tt> file. You have to remove it manually using vtysh. </p>
 </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23665 </td>
         <td><p>NCLU automatically adds the VLAN ID (for the layer 3 VNI/SVI) to the bridge when using <tt>net add vxlan <span class="error">&#91;L3VNI&#93;</span> bridge access <span class="error">&#91;VLAN&#93;</span></tt> <br/>
This configuration breaks network connectivity in an MLAG system in an EVPN symmetric routing configuration. <br/>
To restore connectivity, you need to remove the VLAN ID from the bridge. </p>
 </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23661 </td>
         <td><p>When you configure a GRE tunnel on a Mellanox switch, the traffic behind the local tunnel endpoint destined through the GRE tunnel is software-forwarded. </p>
 </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23651 </td>
         <td><p>In an EVPN symmetric routing configuration, when an IP address is frozen, kernel neighbor table information and kernel VRF routing table information about the frozen IP address might be out-of-sync. </p>
 </td>
         <td>['3.7.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23584 </td>
         <td><p>When you configure a control plane ACL to define permit and deny rules destined to the local switch, NCLU programs the control plane ACL rules into the FORWARD chain. </p>
 </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23570 </td>
         <td><p>On an RMP/1G-T switch, when you remove <tt>link-speed 100</tt> with the NCLU command or by editing the <tt>etc/network/interfaces</tt> file to revert the 100M interface to the default (1G auto), the interface fails to recover and does not come back up.<br/>
After you remove the link-speed, <tt>ethtool</tt> shows the advertised link modes as not reported and Speed/Duplex as unknown.<br/>
To work around this issue and bring the interface back up, either restart <tt>switchd</tt> or use ethtool to configure the speed, advertised, duplex or MDI-X settings. <br/>
Note: The advertised link mode gets set incorrectly if you include 1000baseT/Half. The port will come up successfully at 1G.</p> </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23418 </td>
         <td><p>For QSFP modules, the <tt>sudo ifdown</tt> command does not disable the Tx laser. </p>
 </td>
         <td>['3.7.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23417 </td>
         <td><p>When using NCLU to create an ibgp peering across the peerlink, the addition of the <tt>net add bgp l2vpn evpn neighbor peerlink.4094 activate</tt> command creates a new EBGP neighborship when one has already been configured for IBGP. This is unexpected, the existing IBGP configuration is valid. </p>
 </td>
         <td>['3.7.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23397 </td>
         <td><p>On Broadcom switches, when a link-local multicast frame is received on an access port with a VNI in the bridge, two copies of the packet are sent across the VNI to remote VTEPs and the receiving hosts observe duplicate packets. </p>
 </td>
         <td>['3.6.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23311 </td>
         <td><p>In an EVPN centralized routing configuration, where the layer 2 network extends beyond VTEPs, (for example, host with bridges), the gateway MAC address does not get refreshed in the network when ARP suppression is enabled on the gateway.<br/>
To work around this issue, disable ARP suppression on the centralized gateway.</p> </td>
         <td>['4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23075 </td>
         <td><p>There is a limitation on the number of SVI interfaces you can specify as DHCP relay interfaces in the <tt>/etc/default/isc-dhcp-relay</tt> file. For example, 1500 SVI interfaces causes the <tt>dhcrelay</tt> service to exit without a core file and logs similar to the following are generated for the interfaces: </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 2018-11-10T23:35:30.992370-08:00 Dev dhcrelay: Listening on LPF/vlan.101/a0:00:00:00:00:51 
 2018-11-10T23:35:30.993472-08:00 Dev dhcrelay: Sending on LPF/vlan.101/a0:00:00:00:00:51 
 </pre>
</div></div> 
<p> Eventually the <tt>dhcrelay</tt> service stops. </p>
 </td>
         <td>['3.7.1-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-23021 </td>
         <td><p>When you run the <tt>mstpctl</tt> command, you might see the bridge-port state as blocking when it is actually disabled. You might see the same incorrect bridge-port state when other programs or tools use the output of <tt>mstpctl</tt>; for example, SNMP output from the BRIDGE-MIB.</p> </td>
         <td>['3.7.1-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-22794 </td>
         <td><p>The Dell S5048F-ON switch (with reverse airflow, rear to front), shows the Temp-3 sensor as absent. </p>
 </td>
         <td>['3.6.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-22591 </td>
         <td><p>CVE-2018-5391 (FragmentSmack) is a network vulnerability where an attacker can trigger time and calculation expensive fragment reassembly with specially crafted packets, leading to a denial of service. On a Cumulus Linux switch, the impact is limited to control plane and management plane traffic. Any control plane traffic coming in the front panel ports will be limited by existing policer ACLs.<br/>
To work around this issue, create a file called <tt>/etc/sysctl.d/ip.conf</tt> and add these settings:</p>
<div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre>net.ipv4.ipfrag_low_thresh = 196608
net.ipv6.ip6frag_low_thresh = 196608
net.ipv4.ipfrag_high_thresh = 262144
net.ipv6.ip6frag_high_thresh = 262144
</pre>
</div></div> </td>
         <td>['3.7.0-3.7.11', '4.0.0'] </td>
         <td>['3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-22554 </td>
         <td><p>If you try to bring down several members of a bond remotely at the same time, the link state of one of the interfaces might not transition correctly to the down state; however, all links show down in hardware. </p>
 </td>
         <td>['3.6.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-22386 </td>
         <td><p>The BFD packet redirection logic used by OVSDB server high availability mode redirects BUM packets across the peerlink. The iptables rule for redirection does differentiate between BFD and non-BFD VXLAN inner packets because the service node sends all frames with its own IP address as the tunnel source IP address. The VXLAN encapsulated BUM packets do not get forwarded to the CPU and do not go through the iptable redirection rule; only VXLAN encapsulated BFD packets get forwarded to the CPU due to the inner MAC DA lookup in hardware. </p>
 </td>
         <td>['3.7.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-22301 </td>
         <td><p>For an unresolved address, the IPROUTER default policer rule has been modified to <em>not</em> match on packets exiting a TUNNEL and headed to the CPU to resolve the address via ARP. As a result, the following default rule no longer matches TUNNEL ingress packets. </p>
 <div class="preformatted" style="border-width: 1px;"><div class="preformattedContent panelContent">
<pre> 
 A $INGRESS_CHAIN --in-interface $INGRESS_INTF -m addrtype --dst-type 
 IPROUTER -j POLICE --set-mode pkt --set-rate 400 --set-burst 100 
 </pre>
</div></div> 
<p> These packets are now policed by catch all rules. <br/>
 To work around this issue, the VPORT value on a TRIDENT switch must be changed from binary 011 to 100. </p>
 </td>
         <td>['3.6.1-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-22287 </td>
         <td><p>When a layer 3 ECMP path is brought down on the EdgeCore AS7712 (Tomahawk) switch running in atomic mode, traffic traversing the path stops working for about four seconds. When the switch is changed to non-atomic mode, the delay is less than one second. This issue is seen across OSPF and static ECMP routes. </p> </td>
         <td>['3.6.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-22228 </td>
         <td><p>Counters associated with VLANs and VRFs are not working on Trident 2+ switches. </p>
 </td>
         <td>['3.7.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-22041 </td>
         <td><p>At a high CPU transmit traffic rate (for example, if there is unexpected CPU generated flooding or replication in software), when the ASIC packet driver cannot keep up with the transmit rate because there are no free DMA buffers, it can back pressure by suspending the switch port transmit queues. This can fill up the application socket buffers resulting in <tt>No buffer space available</tt> error messages on protocol sockets.<br/>
When the driver recovers, it automatically resumes the transmit queues. In most cases these error messages are transient. In rare cases, the hardware queues might get stuck, which you can recover with a <tt>switchd</tt> restart.</p> </td>
         <td>['3.4.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-22020 </td>
         <td><p>On the Trident3 platform, static PIM with IIF based on a layer 2 bridge does not work reliably. PIM Join via signaling is required for IPMC to work properly.<br/>
To work around this issue, use dynamic signaling (joins) to manage IP multicast traffic.</p> </td>
         <td>['3.7.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-21927 </td>
         <td><p>When running <tt>ifreload</tt> after updating an interface configuration, sometimes VLANs are not programmed into the hardware data plane. The Linux control plane looks normal but the VLAN has not been programmed into the hardware and packets that arrive for the VLAN might be dropped. <br/>
To work around this issue, remove and re-add the affected VLANs from the port. </p>
 </td>
         <td>['3.5.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-21898 </td>
         <td><p>On a Trident 3 switch, IGMP packets are not getting policed by the police rule in the 00control ACL file. The packets are policed by the catchall policer in the 99control ACL file instead. <br/>
 <tt>-A $INGRESS_CHAIN -p ipv4 -d 01:00:5e:00:00:00/ff:ff:ff:80:00:00 -j police --set-mode pkt --set-rate 100 --set-burst 100</tt> <br/>
 To work around this issue, let the CPU bound IGMP packet hit the following rule and change the policer rate to a desired value for IGMP packets: <br/>
 <tt>-A $INGRESS_CHAIN -p ipv4 -d 01:00:5e:00:00:00/ff:ff:ff:80:00:00 -j police --set-mode pkt --set-rate 100 --set-burst 100</tt> <br/>
 Typically, the destination MAC address 01:00:5e:xx:xx:xx is used only for PIM/IGMP control and data stream packets. However, this workaround cannot handle data stream multicast packets that are not TCP/UDP; this is not typically done. </p>
 </td>
         <td>['3.6.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-21785 </td>
         <td><p>The source address of the ICMPv6 time exceeded message (traceroute hop) is sourced from the wrong VRF when the traceroute target resides on the same switch but in a different VRF.</p> </td>
         <td>['3.6.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-21769 </td>
         <td><p>On a Mellanox switch, GRE tunneling does not work if the tunnel source is configured on an SVI interface. If  the tunnel source is configured on a physical switch port, then tunneling works as expected.</p> </td>
         <td>['3.6.1-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-21678 </td>
         <td><p>On a Dell switch with a Maverick ASIC, NetQ might receive false alerts like the following via PagerDuty: </p>
 <div class="code panel" style="border-width: 1px;"><div class="codeContent panelContent">
<pre class="code-java"> 
 cumulus@<span class="code-keyword">switch</span>:~$ netq show sensors temp changes | grep absent | grep -v psu 
 P2Leaf01 temp9 networking asic die temp sensor absent 43 105 100 5 Unable to find driver path: /cumulu Add 7d:22h:1m:41s 
 P2Leaf01 temp6 networking asic die temp sensor absent 45 105 100 5 Unable to find driver path: /cumulu Add 7d:22h:1m:41s 
 P2Leaf01 temp6 networking asic die temp sensor absent 47 105 100 5 Unable to read temp4_highest Add 9d:23h:26m:6s 
 P2Leaf01 temp6 networking asic die temp sensor absent 45 105 100 5 Unable to read temp4_highest Add 14d:22h:46m:45s 
 </pre>
</div></div> 
<p> This message might occur as a result of a timeout at the hardware level, or the switch might be reporting a failure to get a response. </p>
 </td>
         <td>['3.5.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-21667 </td>
         <td><p>FRR does not add BGP <tt>ttl-security</tt> to either the running configuration or to the <tt>/etc/frr/frr.conf</tt> file when configured on a peer group instead of a specific neighbor. <br/>
To work around this issue, add <tt>ttl-security</tt> to individual neighbors instead of the peer group.</p> </td>
         <td>['3.6.1-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-21278 </td>
         <td><p>The <tt>net show lldp</tt> command sometimes shows the port description in the <tt>Remote Port</tt> field. The <tt>net show interface</tt> command shows the correct value in the <tt>Remote Host</tt> field.<br/>
To work around this issue, use <tt>net show interface</tt> command for LLDP output when connected to Cisco equipment.</p> </td>
         <td>['3.5.3-3.7.10', '4.0.0'] </td>
         <td>['3.7.11-3.7.12'] </td>
     </tr>
     <tr>
         <td>CM-21055 </td>
         <td><p>On Mellanox switches, the destination MAC address of ERSPAN GRE packets is set to all zeros; therefore, the packets might be dropped by the first transit switch.</p> </td>
         <td>['3.6.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-20813 </td>
         <td><p>Span rules matching the out-interface as a bond do not mirror packets.</p> </td>
         <td>['3.6.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-20508 </td>
         <td><p>The Cumulus-Resource-Query-MIB defines the ability to gather buffer utilization status but when these objects are polled, they return nothing. </p> </td>
         <td>['3.5.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-20033 </td>
         <td><p>The VLAN interface stays up even though the physical link carrying the VLAN is admin or carrier down.</p>
 </td>
         <td>['3.5.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-19788 </td>
         <td><p>If you configure a VLAN under a VLAN-aware bridge and create a subinterface of the same VLAN on one of the bridge ports, the bridge and interface compete for the same VLAN and if the interface is flapped, it stops working. Correcting the configuration and running the ifreload command does not resolve the conflict. <br/>
To work around this issue, correct the bridge VIDs and restart switchd or delete the subinterface. </p> </td>
         <td>['3.5.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-19724 </td>
         <td><p>PIM and MSDP entries are set to the internal COS value of 6 so they are grouped together with the bulk traffic priority group in the default <tt>traffic.conf</tt> file. However, PIM, IGMP, and MSDP are considered control-plane and should be set to the internal COS value of 7. </p> </td>
         <td>['3.5.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-19454 </td>
         <td><p>When you use NCLU to bring a bond admin down (<tt>net add bond &lt;bond&gt; link down</tt>), the bond interface goes into admin down state but the switch ports enslaved to the bond remain UP. If you are using bond-lacp-bypass-allow or balance-xor mode, the host might continue to send traffic. This traffic will be dropped because although the bond slaves are UP, they are not members of the bridge.<br/>
To work around this issue, use the <tt>sudo ifdown &lt;bondname&gt;</tt> command.</p> </td>
         <td>['3.5.0-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-17494 </td>
         <td><p>In certain cases, a peer device sends an ARP request from a source IP address that is not on the connected subnet and the switch creates a STALE neighbor entry. Eventually, the switch attempts to keep the entry fresh and sends ARP requests to the host. If the host responds, the switch has REACHABLE neighbor entries for hosts that are not on the connected subnet. <br/>
To work around this issue, change the value of <tt>arp_ignore</tt> to 2. See <a href="https://support.cumulusnetworks.com/hc/en-us/articles/203859616-Default-ARP-Settings-in-Cumulus-Linux" class="external-link" rel="nofollow">Default ARP Settings in Cumulus Linux</a> for more information.</p> </td>
         <td>['3.3.2-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-16571 </td>
         <td><p>NCLU cannot manage <tt>rsyslog</tt> to addresses routed via a VRF.  In Cumulus Linux 4.0.0 and later, management VRF is enabled by default.   To work around this issue, update the <tt>/etc/network/interfaces</tt> file to disable management VRF.</p> </td>
         <td>['3.4.3-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
     <tr>
         <td>CM-15812 </td>
         <td><p>Multicast forwarding fails for IP addresses whose DMAC overlaps with reserved DIPs.</p> </td>
         <td>['3.2.1-3.7.12', '4.0.0'] </td>
         <td>[] </td>
     </tr>
  </tbody>
</table>
