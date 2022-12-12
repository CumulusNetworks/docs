---
title: Setting the Date and Time 
author: NVIDIA
weight: 124
toc: 3
---

This section discusses how to set the time zone, and how to set the date and time on the software clock on the switch. To configure NTP, see {{<link url="Network-Time-Protocol-NTP">}}. To configure PTP, see {{<link url="Precision-Time-Protocol-PTP">}}.

Setting the time zone, and the date and time on the software clock requires root privileges; use `sudo`.

## Set the Time Zone

You can use one of these methods to set the time zone on the switch:
- Run NVUE commands.
- Use the guided wizard.
- Edit the `/etc/timezone` file.

{{< tabs "TabID19 ">}}
{{< tab "NVUE Commands ">}}
<!-- vale off -->
Run the `nv set system timezone <timezone>` command. To see all the available time zones, run `nv set system timezone` and press the Tab key. The following example sets the time zone to US/Eastern:

```
cumulus@switch:~$ nv set system timezone US/Eastern
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Follow the Guided Wizard ">}}

1. In a terminal, run the following command:

    ```
    cumulus@switch:~$ sudo dpkg-reconfigure tzdata
    ```

2. Follow the on screen menu options to select the geographic area and region.

   {{< img src = "/images/cumulus-linux/date-time-wizard.png" >}}

For more information, see the Debian {{<exlink url="http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html" text="System Administrator's Manual - Time">}}.

{{< /tab >}}
{{< tab "Edit the /etc/timezone File ">}}
<!-- vale on -->
1. Edit the `/etc/timezone` file to add your desired time zone. You can see a list of valid time zones {{<exlink url="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" text="here">}}.

   ```
   cumulus@switch:~$ sudo vi /etc/timezone
   US/Eastern
   ```

2. Apply the new time zone:

   ```
   cumulus@switch:~$ sudo dpkg-reconfigure --frontend noninteractive tzdata
   ```

3. Change `/etc/localtime` to reflect your current time zone:

   ```
   sudo ln -sf /usr/share/zoneinfo/US/Eastern /etc/localtime
   ```

{{< /tab >}}
{{< /tabs >}}

## Set the Date and Time

The switch contains a battery backed hardware clock that maintains the time while the switch powers off and between reboots. When the switch is running, the Cumulus Linux operating system maintains its own software clock.

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
