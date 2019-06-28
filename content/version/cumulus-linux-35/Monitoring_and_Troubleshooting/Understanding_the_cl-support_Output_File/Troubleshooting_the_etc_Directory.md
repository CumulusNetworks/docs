---
title: Troubleshooting the etc Directory
author: Cumulus Networks
weight: 437
aliases:
 - /display/CL35/Troubleshooting+the+etc+Directory
 - /pages/viewpage.action?pageId=8357383
pageID: 8357383
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
The
[`cl-support`](/version/cumulus-linux-35/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/)
script replicates the /`etc` directory.

Files that `cl-support` deliberately excludes are:

| File              | Description                                                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| /etc/nologin      | ` nologin  `prevents unprivileged users from logging into the system.                                                                          |
| /etc/alternatives | `update-alternatives` creates, removes, maintains and displays information about the symbolic links comprising the Debian alternatives system. |

This is the alphabetical of the output from running `ls -l` on the
`/etc` directory structure created by `cl-support`. The green
highlighted rows are the ones Cumulus Networks finds most important when
troubleshooting problems.

| **File**                  |
| ------------------------- |
| acpi                      |
| adduser.conf              |
| adjtime                   |
| apt                       |
| audisp                    |
| audit                     |
| bash.bashrc               |
| bash\_completion          |
| bash\_completion.d        |
| bcm.d                     |
| bindresvport.blacklist    |
| binfmt.d                  |
| ca-certificates           |
| ca-certificates.conf      |
| calendar                  |
| chef                      |
| cron.d                    |
| cron.daily                |
| cron.hourly               |
| cron.monthly              |
| cron.weekly               |
| crontab                   |
| cruft                     |
| cumulus                   |
| dbus-1                    |
| debconf.conf              |
| debian\_version           |
| debsums-ignore            |
| default                   |
| deluser.conf              |
| dhcp                      |
| discover.conf.d           |
| discover-modprobe.conf    |
| dnsmasq.conf              |
| dnsmasq.d                 |
| dpkg                      |
| e2fsck.conf               |
| environment               |
| etckeeper                 |
| ethertypes                |
| frr                       |
| fstab                     |
| fstab.d                   |
| fw\_env.config            |
| gai.conf                  |
| groff                     |
| group                     |
| group-                    |
| grub.d                    |
| gshadow                   |
| gshadow-                  |
| gss                       |
| hostapd                   |
| hostapd.conf              |
| host.conf                 |
| hostname                  |
| hosts                     |
| hosts.allow               |
| hosts.deny                |
| hsflowd.conf              |
| hw\_init.d                |
| image-release             |
| init                      |
| init.d                    |
| initramfs-tools           |
| inputrc                   |
| insserv                   |
| insserv.conf              |
| insserv.conf.d            |
| iproute2                  |
| issue                     |
| issue.net                 |
| kbd                       |
| kernel                    |
| ld.so.cache               |
| ld.so.conf                |
| ld.so.conf.d              |
| ldap                      |
| libaudit.conf             |
| libnl                     |
| lldpd.d                   |
| locale.alias              |
| locale.gen                |
| localtime                 |
| logcheck                  |
| login.defs                |
| logrotate.conf            |
| logrotate.d               |
| lsb-release               |
| lvm                       |
| machine-id                |
| magic                     |
| magic.mime                |
| mailcap                   |
| mailcap.order             |
| manpath.config            |
| mcelog                    |
| mime.types                |
| mke2fs.conf               |
| mlx                       |
| modprobe.d                |
| modules                   |
| modules-load.d            |
| motd                      |
| motd.distrib              |
| mtab                      |
| mysql                     |
| nanorc                    |
| netd.conf                 |
| network                   |
| networks                  |
| nsswitch.conf             |
| ntp.conf                  |
| openvswitch               |
| openvswitch-vtep          |
| opt                       |
| os-release                |
| pam.conf                  |
| pam.d                     |
| pam\_radius.conf          |
| passwd                    |
| passwd-                   |
| perl                      |
| popularity-contest.conf   |
| profile                   |
| profile.d                 |
| protocols                 |
| ptm.d                     |
| python                    |
| python2.6                 |
| python2.7                 |
| python3                   |
| python3.4                 |
| rc.local                  |
| rc0.d                     |
| rc1.d                     |
| rc2.d                     |
| rc3.d                     |
| rc4.d                     |
| rc5.d                     |
| rc6.d                     |
| rcS.d                     |
| rdnbrd.conf               |
| resolvconf                |
| resolv.conf               |
| rmt                       |
| rpc                       |
| rsyslog.conf              |
| rsyslog.d                 |
| screenrc                  |
| securetty                 |
| security                  |
| selinux                   |
| sensors.d                 |
| sensors3.conf             |
| services                  |
| shadow                    |
| shadow-                   |
| shells                    |
| skel                      |
| snmp                      |
| ssh                       |
| ssl                       |
| staff-group-for-usr-local |
| subgid                    |
| subgid-                   |
| subuid                    |
| subuid-                   |
| sudoers                   |
| sudoers.d                 |
| sysctl.conf               |
| sysctl.d                  |
| systemd                   |
| tacplus\_nss.conf         |
| tacplus\_servers          |
| terminfo                  |
| timezone                  |
| ucf.conf                  |
| udev                      |
| ufw                       |
| vim                       |
| vrf                       |
| vxrd.conf                 |
| vxsnd.conf                |
| watchdog.conf             |
| wgetrc                    |
| X11                       |
| xdg                       |
