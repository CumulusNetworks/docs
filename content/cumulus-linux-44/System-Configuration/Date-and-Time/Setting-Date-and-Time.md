---
title: Setting the Date and Time 
author: NVIDIA
weight: 124
toc: 3
---

This section discusses how to set the time zone, and how to set the date and time on the software clock on the switch. To configure NTP, see {{<link url="Network-Time-Protocol-NTP">}}. To configure PTP, see {{<link url="Precision-Time-Protocol-PTP">}}.

Setting the time zone, and the date and time on the software clock requires root privileges; use `sudo`.

## Set the Time Zone

You can use one of two methods to set the time zone on the switch:

- Edit the `/etc/timezone` file.
- Use the guided wizard.

<!-- vale off -->
### Edit the /etc/timezone File
<!-- vale on -->
To see the current time zone, list the contents of `/etc/timezone`:

```
cumulus@switch:~$ cat /etc/timezone
US/Eastern
```

Edit the file to add your desired time zone. You can see a list of valid time zones {{<exlink url="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" text="here">}}.

Use the following command to apply the new time zone:

```
cumulus@switch:~$ sudo dpkg-reconfigure --frontend noninteractive tzdata
```

Use the following command to change `/etc/localtime` to reflect your current time zone. Use the same value as the previous step.

```
sudo ln -sf /usr/share/zoneinfo/US/Eastern /etc/localtime
```

### Follow the Guided Wizard

To set the time zone using the guided wizard, run the following command:

```
cumulus@switch:~$ sudo dpkg-reconfigure tzdata
```

{{< img src = "/images/cumulus-linux/date-time-wizard.png" >}}

For more information, see the Debian {{<exlink url="http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html" text="System Administrator's Manual - Time">}}.

## Set the Date and Time

The switch contains a battery backed hardware clock that maintains the time while the switch is powered off and between reboots. When the switch is running, the Cumulus Linux operating system maintains its own software clock.

During boot up, the switch copies the time from the hardware clock to the operating system software clock. The software clock takes care of all the timekeeping. During system shutdown, the switch copies the software clock back to the battery backed hardware clock.

You can set the date and time on the software clock with the `date` command. First, determine your current time zone:

```
cumulus@switch:~$ date +%Z
```

{{%notice note%}}
If you need to reconfigure the current time zone, refer to the instructions above.
{{%/notice%}}

To set the software clock according to the configured time zone:

```
cumulus@switch:~$ sudo date -s "Tue Jan 26 00:37:13 2021"
```

You can write the current value of the software clock to the hardware clock using the `hwclock` command:

```
cumulus@switch:~$ sudo hwclock -w
```

See `man hwclock(8)` for more information.

## Related Information

- {{<exlink url="http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html" text="Debian System Administrator's Manual - Time">}}
