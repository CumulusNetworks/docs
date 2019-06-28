---
title: Using sudo to Delegate Privileges
author: Cumulus Networks
weight: 131
aliases:
 - /display/RMP31/Using+sudo+to+Delegate+Privileges
 - /pages/viewpage.action?pageId=5122736
pageID: 5122736
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
By default, Cumulus RMP has two user accounts: *root* and *cumulus*. The
*cumulus* account is a normal user and is in the group *sudo*.

You can add more user accounts as needed. Like the *cumulus* account,
these accounts must use `sudo` to execute privileged commands.

## <span>Commands</span>

  - sudo

  - visudo

## <span>Using sudo</span>

`sudo` allows you to execute a command as superuser or another user as
specified by the security policy. See `man sudo(8)` for details.

The default security policy is *sudoers*, which is configured using
`/etc/sudoers`. Use `/etc/sudoers.d/` to add to the default sudoers
policy. See `man sudoers(5)` for details.

{{%notice warning%}}

Use `visudo` only to edit the `sudoers` file; do not use another editor
like `vi` or `emacs`. See `man` `visudo(8)` for details.

Errors in the `sudoers` file can result in losing the ability to elevate
privileges to root. You can fix this issue only by power cycling the
switch and booting into single user mode. Before modifying `sudoers`,
enable the root user by setting a password for the root user.

{{%/notice%}}

By default, users in the *sudo* group can use `sudo` to execute
privileged commands. To add users to the sudo group, use the
`useradd(8)` or `usermod(8)` command. To see which users belong to the
sudo group, see `/etc/group` (`man group(5)`).

Any command can be run as `sudo`, including `su`. A password is
required.

The example below shows how to use `sudo` as a non-privileged user
*cumulus* to bring up an interface:

    cumulus@switch:~$ ip link show dev swp1
    3: swp1: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master br0 state DOWN mode DEFAULT qlen 500
    link/ether 44:38:39:00:27:9f brd ff:ff:ff:ff:ff:ff
     
    cumulus@switch:~$ ip link set dev swp1 up
    RTNETLINK answers: Operation not permitted
     
    cumulus@switch:~$ sudo ip link set dev swp1 up
    Password:
     
    cumulus@switch:~$ ip link show dev swp1
    3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master br0 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:27:9f brd ff:ff:ff:ff:ff:ff

## <span>sudoers Examples</span>

The following examples show how you grant as few privileges as necessary
to a user or group of users to allow them to perform the required task.
For each example, the system group *noc* is used; groups are prefixed
with an %.

When executed by an unprivileged user, the example commands below must
be prefixed with `sudo.`

<table>
<thead>
<tr class="header">
<th><p>Category</p></th>
<th><p>Privilege</p></th>
<th><p>Example Command</p></th>
<th><p>sudoers Entry</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Monitoring</p></td>
<td><p>Switch port info</p></td>
<td><pre><code>ethtool -m swp1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/ethtool</code></pre></td>
</tr>
<tr class="even">
<td><p>Monitoring</p></td>
<td><p>System diagnostics</p></td>
<td><pre><code>cl-support</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/cumulus/bin/cl-support</code></pre></td>
</tr>
<tr class="odd">
<td><p>Monitoring</p></td>
<td><p>Routing diagnostics</p></td>
<td><pre><code>cl-resource-query</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/cumulus/bin/cl-resource-query</code></pre></td>
</tr>
<tr class="even">
<td><p>Image management</p></td>
<td><p>Install images</p></td>
<td><pre><code>onie-select http://lab/install.bin</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/cumulus/bin/cl-img-install</code></pre></td>
</tr>
<tr class="odd">
<td><p>Package management</p></td>
<td><p>Any apt-get command</p></td>
<td><pre><code>apt-get update or apt-get install</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/bin/apt-get</code></pre></td>
</tr>
<tr class="even">
<td><p>Package management</p></td>
<td><p>Just apt-get update</p></td>
<td><pre><code>apt-get update</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/bin/apt-get update</code></pre></td>
</tr>
<tr class="odd">
<td><p>Package management</p></td>
<td><p>Install packages</p></td>
<td><pre><code>apt-get install vim </code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/bin/apt-get install *</code></pre></td>
</tr>
<tr class="even">
<td><p>Package management</p></td>
<td><p>Upgrading</p></td>
<td><pre><code>apt-get upgrade</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/bin/apt-get upgrade</code></pre></td>
</tr>
<tr class="odd">
<td><p>L1 + 2 features</p></td>
<td><p>Any LLDP command</p></td>
<td><pre><code>lldpcli show neighbors / configure</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/sbin/lldpcli</code></pre></td>
</tr>
<tr class="even">
<td><p>L1 + 2 features</p></td>
<td><p>Just show neighbors</p></td>
<td><pre><code>lldpcli show neighbors</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/sbin/lldpcli show neighbours*</code></pre></td>
</tr>
<tr class="odd">
<td><p>Interfaces</p></td>
<td><p>Modify any interface</p></td>
<td><pre><code>ip link set dev swp1 {up|down}</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/ip link set *</code></pre></td>
</tr>
<tr class="even">
<td><p>Interfaces</p></td>
<td><p>Up any interface</p></td>
<td><pre><code>ifup swp1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/ifup</code></pre></td>
</tr>
<tr class="odd">
<td><p>Interfaces</p></td>
<td><p>Down any interface</p></td>
<td><pre><code>ifdown swp1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/ifdown</code></pre></td>
</tr>
<tr class="even">
<td><p>Interfaces</p></td>
<td><p>Up/down only swp2</p></td>
<td><pre><code>ifup swp2 / ifdown swp2</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/ifup swp2,/sbin/ifdown swp2</code></pre></td>
</tr>
<tr class="odd">
<td><p>Interfaces</p></td>
<td><p>Any IP address chg</p></td>
<td><pre><code>ip addr {add|del} 192.0.2.1/30 dev swp1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/ip addr *</code></pre></td>
</tr>
<tr class="even">
<td><p>Interfaces</p></td>
<td><p>Only set IP address</p></td>
<td><pre><code>ip addr add 192.0.2.1/30 dev swp1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/ip addr add *</code></pre></td>
</tr>
<tr class="odd">
<td><p>Ethernet bridging</p></td>
<td><p>Any bridge command</p></td>
<td><pre><code>brctl addbr br0 / brctl delif br0 swp1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/brctl</code></pre></td>
</tr>
<tr class="even">
<td><p>Ethernet bridging</p></td>
<td><p>Add bridges and ints</p></td>
<td><pre><code>brctl addbr br0 / brctl addif br0 swp1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/brctl addbr *,/sbin/brctl addif *</code></pre></td>
</tr>
<tr class="odd">
<td><p>Spanning tree</p></td>
<td><p>Set STP properties</p></td>
<td><pre><code>mstpctl setmaxage br2 20</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/sbin/mstpctl</code></pre></td>
</tr>
<tr class="even">
<td><p>Troubleshooting</p></td>
<td><p>Restart switchd</p></td>
<td><pre><code>systemctl restart switchd.service</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/sbin/service switchd *</code></pre></td>
</tr>
<tr class="odd">
<td><p>Troubleshooting</p></td>
<td><p>Restart any service</p></td>
<td><pre><code>systemctl cron switchd.service</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/sbin/service</code></pre></td>
</tr>
<tr class="even">
<td><p>Troubleshooting</p></td>
<td><p>Packet capture</p></td>
<td><pre><code>tcpdump</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/usr/sbin/tcpdump</code></pre></td>
</tr>
<tr class="odd">
<td><p>L3</p></td>
<td><p>Add static routes</p></td>
<td><pre><code>ip route add 10.2.0.0/16 via 10.0.0.1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/bin/ip route add *</code></pre></td>
</tr>
<tr class="even">
<td><p>L3</p></td>
<td><p>Delete static routes</p></td>
<td><pre><code>ip route del 10.2.0.0/16 via 10.0.0.1</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/bin/ip route del *</code></pre></td>
</tr>
<tr class="odd">
<td><p>L3</p></td>
<td><p>Any static route chg</p></td>
<td><pre><code>ip route *</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/bin/ip route *</code></pre></td>
</tr>
<tr class="even">
<td><p>L3</p></td>
<td><p>Any iproute command</p></td>
<td><pre><code>ip *</code></pre></td>
<td><pre><code>%noc ALL=(ALL) NOPASSWD:/bin/ip</code></pre></td>
</tr>
</tbody>
</table>

## <span>Configuration Files</span>

  - /etc/sudoers - default security policy

  - /etc/sudoers.d/ - default security policy

## <span>Useful Links</span>

  - [sudo](https://wiki.debian.org/sudo)

  - [Adding Yourself to
    sudoers](http://rubypond.com/blog/adding-yourself-to-the-sudoers-file)
