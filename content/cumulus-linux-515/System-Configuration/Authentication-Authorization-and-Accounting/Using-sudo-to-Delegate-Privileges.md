---
title: Using sudo to Delegate Privileges
author: NVIDIA
weight: 160
toc: 4
---
By default, Cumulus Linux has two user accounts: *root* and *cumulus*. The *cumulus* account is a normal user and is in the group *sudo*.

You can add more user accounts as needed. Like the *cumulus* account, these accounts must use `sudo` to execute privileged commands.

## sudo Basics

`sudo` allows you to execute a command as superuser or another user as specified by the security policy.

The default security policy is *sudoers*, which you configure in the `/etc/sudoers` file. Use `/etc/sudoers.d/` to add to the default sudoers policy.

{{%notice warning%}}
Use `visudo` only to edit the `sudoers` file; do not use another editor like `vi` or `emacs`.

When creating a new file in `/etc/sudoers.d`, use `visudo -f`. This option performs sanity checks before writing the file to avoid errors that prevent sudo from working.

Errors in the `sudoers` file can result in losing the ability to elevate privileges to root. You can fix this issue only by power cycling the switch and booting into single user mode. Before modifying `sudoers`, enable the root user by setting a password for the root user.
{{%/notice%}}

By default, users in the *sudo* group can use `sudo` to execute privileged commands. To add users to the sudo group, use the `useradd(8)` or `usermod(8)` command. To see which users belong to the sudo group, see `/etc/group` (`man group(5)`).

You can run any command as `sudo`, including `su`. You must enter a password.

The example below shows how to use `sudo` as a non-privileged user *cumulus* to bring up an interface:

```
cumulus@switch:~$ ip link show dev swp1
3: swp1: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master br0 state DOWN mode DEFAULT qlen 500
link/ether 44:38:39:00:27:9f brd ff:ff:ff:ff:ff:ff

cumulus@switch:~$ ip link set dev swp1 up
RTNETLINK answers: Operation not permitted

cumulus@switch:~$ sudo ip link set dev swp1 up
Password:

umulus@switch:~$ ip link show dev swp1
3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master br0 state UP mode DEFAULT qlen 500
link/ether 44:38:39:00:27:9f brd ff:ff:ff:ff:ff:ff
```

## sudoers Examples

The following examples show how you grant as few privileges as necessary to a user or group of users to allow them to perform the required task. Each example uses the system group *noc*; groups include the prefix %.

When an unprivileged user runs a command, the command must include the `sudo` prefix.
<!-- vale off -->
| Category | Privilege | Example Command | sudoers Entry |
|--------- |---------- |---------------- |-------------- |
| Monitoring | Switch port information|ethtool -m swp1|%noc ALL=(ALL) NOPASSWD:/sbin/ethtool |
| Monitoring | System diagnostics|cl-support|%noc ALL=(ALL) NOPASSWD:/usr/cumulus/bin/cl-support |
| Monitoring | Routing diagnostics|cl-resource-query|%noc ALL=(ALL) NOPASSWD:/usr/cumulus/bin/cl-resource-query |
| Image management | Install images|onie-select http://lab/install.bin|%noc ALL=(ALL) NOPASSWD:/usr/cumulus/bin/onie-select |
| Package management | Any apt-get command|apt-get update or apt-get install|%noc ALL=(ALL) NOPASSWD:/usr/bin/apt-get |
| Package management | Just apt-get update | apt-get update | %noc ALL=(ALL) NOPASSWD:/usr/bin/apt-get update |
| Package management | Install packages | apt-get install vim | %noc ALL=(ALL) NOPASSWD:/usr/bin/apt-get install * |
| Package management | Upgrading | apt-get upgrade | %noc ALL=(ALL) NOPASSWD:/usr/bin/apt-get upgrade |
| Netfilter | Install ACL policies | cl-acltool -i | %noc ALL=(ALL) NOPASSWD:/usr/cumulus/bin/cl-acltool |
| Netfilter | List iptables rules | iptables -L | %noc ALL=(ALL) NOPASSWD:/sbin/iptables |
| Layer 1 and 2 |Any LLDP command | lldpcli show neighbors / configure | %noc ALL=(ALL) NOPASSWD:/usr/sbin/lldpcli |
| Layer 1 and 2 | Just show neighbors | lldpcli show neighbors | %noc ALL=(ALL) NOPASSWD:/usr/sbin/lldpcli show neighbors* |
| Interfaces | Modify any interface | ip link set dev swp1 {up\|down} | %noc ALL=(ALL) NOPASSWD:/sbin/ip link set * |
| Interfaces | Up any interface | ifup swp1 | %noc ALL=(ALL) NOPASSWD:/sbin/ifup |
| Interfaces | Down any interface | ifdown swp1 | %noc ALL=(ALL) NOPASSWD:/sbin/ifdown |
| Interfaces | Up/down only swp2 | ifup swp2 / ifdown swp2 | %noc ALL=(ALL) NOPASSWD:/sbin/ifup swp2,/sbin/ifdown swp2 |
| Interfaces | Any IP address change | ip addr {add\|del} 192.0.2.1/30 dev swp1 | %noc ALL=(ALL) NOPASSWD:/sbin/ip addr * |
| Interfaces | Only set IP address | ip addr add 192.0.2.1/30 dev swp1 | %noc ALL=(ALL) NOPASSWD:/sbin/ip addr add * |
| Ethernet bridging | Any bridge command | brctl addbr br0 / brctl delif br0 swp1 | %noc ALL=(ALL) NOPASSWD:/sbin/brctl |
| Ethernet bridging | Add bridges and interfaces | brctl addbr br0 / brctl addif br0 swp1 | %noc ALL=(ALL) NOPASSWD:/sbin/brctl addbr *,/sbin/brctl addif * |
| Spanning tree | Set STP properties | mstpctl setmaxage br2 20 | %noc ALL=(ALL) NOPASSWD:/sbin/mstpctl|
| Troubleshooting | Restart switchd | systemctl restart switchd.service | %noc ALL=(ALL) NOPASSWD:/usr/sbin/service switchd * |
| Troubleshooting | Restart any service | systemctl cron switchd.service | %noc ALL=(ALL) NOPASSWD:/usr/sbin/service |
| Troubleshooting | Packet capture | tcpdump | %noc ALL=(ALL) NOPASSWD:/usr/sbin/tcpdump |
| Layer 3| Add static routes | ip route add 10.2.0.0/16 via 10.0.0.1 | %noc ALL=(ALL) NOPASSWD:/bin/ip route add * |
| Layer 3| Delete static routes | ip route del 10.2.0.0/16 via 10.0.0.1 | %noc ALL=(ALL) NOPASSWD:/bin/ip route del * |
| Layer 3| Any static route change | ip route *|%noc ALL=(ALL) NOPASSWD:/bin/ip route * |
| Layer 3| Any iproute command | ip * | %noc ALL=(ALL) NOPASSWD:/bin/ip |
| Layer 3| Non-modal OSPF | cl-ospf area 0.0.0.1 range 10.0.0.0/24 | %noc ALL=(ALL) NOPASSWD:/usr/bin/cl-ospf |
<!-- vale on -->
## Related Information

- {{<exlink url="https://wiki.debian.org/sudo" text="Debian wiki - sudo">}}
