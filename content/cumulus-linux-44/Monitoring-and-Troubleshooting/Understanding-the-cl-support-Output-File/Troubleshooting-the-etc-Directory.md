---
title: Troubleshooting the etc Directory
author: NVIDIA
weight: 1070
toc: 4
---
The `{{<link url="Understanding-the-cl-support-Output-File" text="cl-support">}}` script replicates the /`etc` directory, however, it excludes certain files, such as `/etc/nologin`, which prevents unprivileged users from logging into the system.

The following list shows the output from `ls -l` on the `/etc` directory structure, which `cl-support` creates.
<!-- vale off -->
## etc Directory Contents

| **File**                  |
| ------------------------- |
| acpi |
| adduser.conf |
| alternatives |
| apm |
| apparmor |
| apparmor.d |
| apt |
| audisp |
| audit |
| bash.bashrc |
| bash_completion |
| bash_completion.d |
| bindresvport.blacklist |
| binfmt.d |
| ca-certificates |
| ca-certificates.conf |
| calendar |
| console-setup |
| containerd |
| cron.d |
| cron.daily |
| cron.hourly |
| cron.monthly |
| crontab |
| cron.weekly |
| cruft |
| cumulus |
| dbus-1 |
| debconf.conf |
| debian_version |
| debsums-ignore |
| default |
| deluser.conf |
| depmod.d |
| dhcp |
| dhcpsnoop |
| discover.conf.d |
| discover-modprobe.conf |
| dnsmasq.conf |
| dnsmasq.d |
| docker |
| dpkg |
| e2fsck.conf |
| emacs |
| environment |
| .etckeeper |
| etckeeper |
| ethertypes |
| fonts |
| freeipmi |
| frr |
| fstab |
| gai.conf |
| .git |
| .gitignore |
| groff |
| group |
| group- |
| grub.d |
| gshadow |
| gshadow- |
| gss |
| gunicorn.conf.py |
| hdparm.conf |
| host.conf |
| hostname |
| hosts |
| hosts.allow |
| hosts.deny |
| hsflowd |
| hsflowd.conf |
| hw_init.d |
| image-release |
| init |
| init.d |
| initramfs-tools |
| inputrc |
| insserv |
| insserv.conf |
| insserv.conf.d |
| iproute2 |
| issue |
| issue.net |
| kernel |
| ldap |
| ld.so.cache |
| ld.so.conf |
| ld.so.conf.d |
| libaudit.conf |
| libnl |
| linuxptp |
| lldpd.d |
| locale.alias |
| locale.gen |
| localtime |
| logcheck |
| login.defs |
| login.defs.cumulus |
| login.defs.cumulus-orig |
| logrotate.conf |
| logrotate.conf.cumulus |
| logrotate.conf.cumulus-orig |
| logrotate.d |
| lsb-release |
| lttng |
| lvm |
| machine-id |
| magic |
| magic.mime |
| mailcap |
| mailcap.order |
| manpath.config |
| mime.types |
| mke2fs.conf |
| mlx |
| modprobe.d |
| modules |
| modules-load.d |
| motd |
| motd.distrib |
| mtab |
| mysql |
| nanorc |
| netd.conf |
| netq |
| network |
| NetworkManager |
| networks |
| nginx |
| nsswitch.conf |
| ntp.conf |
| nvue-auth.yaml |
| nvue.d |
| openvswitch |
| opt |
| os-release |
| pam.conf |
| pam.d |
| passwd|
| passwd-|
| perl |
| profile |
| profile.cumulus |
| profile.cumulus-orig |
| profile.d |
| protocols |
| ptm.d |
| ptp4l.conf|
| .pwd.lock |
| python |
| python2.7 |
| python3 |
| python3.7 |
| ras |
| rc0.d |
| rc1.d |
| rc2.d |
| rc3.d |
| rc4.d |
| rc5.d |
| rc6.d |
| rcS.d |
| rdnbrd.conf |
| resolv.conf |
| resolvconf |
| resolv.conf.bak |
| restapi.conf |
| rmt |
| rpc |
| rsyslog.conf |
| rsyslog.conf.cumulus |
| rsyslog.conf.cumulus-orig |
| rsyslog.d |
| runit |
| screenrc |
| securetty |
| security |
| selinux |
| sensors3.conf |
| sensors.d |
| services |
| sgml |
| shadow |
| shadow- |
| shells |
| skel |
| smartd.conf |
| smartmontools |
| snmp |
| ssh |
| ssl |
| subgid |
| subgid- |
| subuid |
| subuid- |
| sudoers |
| sudoers.d |
| sv |
| sysctl.conf |
| sysctl.d |
| systemd |
| terminfo |
| timezone |
| tmpfiles.d |
| ucf.conf |
| udev |
| ufw |
| update-motd.d |
| vim |
| vrf |
| watchdog.conf |
| wgetrc |
| what-just-happened |
| X11 |
| xattr.conf |
| xdg |
| xml |

<!-- vale on -->