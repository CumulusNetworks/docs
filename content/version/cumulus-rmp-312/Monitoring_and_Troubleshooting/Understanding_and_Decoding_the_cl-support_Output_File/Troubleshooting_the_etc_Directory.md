---
title: Troubleshooting the etc Directory
author: Cumulus Networks
weight: 177
aliases:
 - /display/RMP31/Troubleshooting+the+etc+Directory
 - /pages/viewpage.action?pageId=5122757
pageID: 5122757
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
The
[`cl-support`](/version/cumulus-rmp-312/Monitoring_and_Troubleshooting/Understanding_and_Decoding_the_cl-support_Output_File/)
script replicates the /`etc` directory.

Files that `cl-support` deliberately excludes are:

| File              | Description                                                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| /etc/nologin      | `nologin` prevents unprivileged users from logging into the system.                                                                            |
| /etc/alternatives | `update-alternatives` creates, removes, maintains and displays information about the symbolic links comprising the Debian alternatives system. |

This is the alphabetical of the output from running `ls -l` on the
`/etc` directory structure created by `cl-support`. The green
highlighted rows are the ones Cumulus Networks finds most important when
troubleshooting problems.

| **File**                  |
| ------------------------- |
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
| cumulus                   |
| debconf.conf              |
| debian\_version           |
| debsums-ignore            |
| default                   |
| deluser.conf              |
| dhcp                      |
| dpkg                      |
| e2fsck.conf               |
| environment               |
| ethertypes                |
| fstab                     |
| fstab.d                   |
| fw\_env.config            |
| gai.conf                  |
| groff                     |
| group                     |
| group-                    |
| gshadow                   |
| gshadow-                  |
| host.conf                 |
| hostname                  |
| hosts                     |
| hosts.allow               |
| hosts.deny                |
| init                      |
| init.d                    |
| inittab                   |
| inputrc                   |
| insserv                   |
| insserv.conf              |
| insserv.conf.d            |
| iproute2                  |
| issue                     |
| issue.net                 |
| ld.so.cache               |
| ld.so.conf                |
| ld.so.conf.d              |
| ldap                      |
| libaudit.conf             |
| libnl-3                   |
| lldpd.d                   |
| localtime                 |
| logcheck                  |
| login.defs                |
| logrotate.conf            |
| logrotate.d               |
| lsb-release               |
| magic                     |
| magic.mime                |
| mailcap                   |
| mailcap.order             |
| manpath.config            |
| mime.types                |
| mke2fs.conf               |
| modprobe.d                |
| modules                   |
| monit                     |
| motd                      |
| mtab                      |
| nanorc                    |
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
| passwd                    |
| passwd-                   |
| perl                      |
| profile                   |
| profile.d                 |
| protocols                 |
| ptm.d                     |
| python                    |
| python2.6                 |
| python2.7                 |
| rc.local                  |
| rc0.d                     |
| rc1.d                     |
| rc2.d                     |
| rc3.d                     |
| rc4.d                     |
| rc5.d                     |
| rc6.d                     |
| rcS.d                     |
| resolv.conf               |
| rmt                       |
| rpc                       |
| rsyslog.conf              |
| rsyslog.d                 |
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
| sudoers                   |
| sudoers.d                 |
| sysctl.conf               |
| sysctl.d                  |
| systemd                   |
| terminfo                  |
| timezone                  |
| ucf.conf                  |
| udev                      |
| ufw                       |
| vim                       |
| wgetrc                    |
