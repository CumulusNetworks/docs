---
title: Configure SNMP Traps without NCLU
author: Cumulus Networks
weight: 1084
toc: 4
---

This topic describes how to configure SNMP traps manually; that is, without NCLU.

## Generate Event Notification Traps

The Net-SNMP agent provides a method to generate SNMP trap events using the Distributed Management (DisMan) Event MIB for various system events, including:

- Link up/down.
- Exceeding the temperature sensor threshold, CPU load, or memory threshold.
- Other SNMP MIBs.

To enable specific types of traps, you need to create the following configurations in `/etc/snmp/snmpd.conf`.

### Define Access Credentials

An SNMPv3 username is required to authorize the DisMan service even though you are not configuring SNMPv3 here. The example `snmpd.conf` configuration shown below creates *trapusername* as the username using the `createUser` command. `iquerySecName` defines the default SNMPv3 username to be used when making internal queries to retrieve monitored expressions. `rouser` specifies which username to use for these SNMPv3 queries. All three are required for `snmpd` to retrieve information and send traps (even with the `monitor` command shown below in the examples). Add the following lines to your `/etc/snmp/snmpd.conf` configuration file:

```
createuser trapusername
iquerysecname trapusername
rouser trapusername
```

{{%notice note%}}

`iquerysecname` specifies the default SNMPv3 username to be used when making internal queries to retrieve any necessary information - either for evaluating the monitored expression or building a notification payload. These internal queries always use SNMPv3, even if normal querying of the agent is done using SNMPv1 or SNMPv2c. Note that this user must also be explicitly created via `createUser` and given appropriate access rights, for `rouser`, for example. The `iquerysecname` directive is purely concerned with defining which user should be used, not with actually setting this user up.

{{%/notice%}}

### Define Trap Receivers

The following configuration defines the trap receiver IP address where SNMPv2 traps are sent:

```
trap2sink 192.168.1.1 public
# For SNMPv1 Traps, use
# trapsink  192.168.1.1  public 
```

{{%notice note%}}

Although the traps are sent to an SNMPV2 receiver, the SNMPv3 user is still required. Starting with Net-SNMP 5.3, `snmptrapd` no longer accepts all traps by default. `snmptrapd` must be configured with authorized SNMPv1/v2c community strings and/or SNMPv3 users. Non-authorized traps/informs are dropped. Refer to the {{<exlink url="http://www.net-snmp.org/docs/man/snmptrapd.conf.html" text="snmptrapd.conf(5) manual page">}} for details.

{{%/notice%}}

{{%notice note%}}

It is possible to define multiple trap receivers and to use the domain name instead of an IP address in the `trap2sink` directive.

{{%/notice%}}

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

### SNMP Version 3 Trap and Inform Messages

You can configure SNMPv3 trap and inform messages with the `trapsess` configuration command. Inform messages are traps that are acknowledged by the receiving trap daemon. You configure inform messages with the `-Ci` parameter. You must specify the EngineID of the receiving trap server with the `-e` field.

```
trapsess -Ci -e 0x80ccff112233445566778899 -v3 -l authPriv  -u trapuser1 -a MD5 -A trapuser1password -x DES -X trapuser1encryption 192.168.1.1
```

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages. You specify the level of authentication and encryption for SNMPv3 trap and inform messages with `-l` (`NoauthNoPriv, authNoPriv,` or `authPriv`).

{{%notice note%}}

You can define multiple trap receivers and use the domain name instead of an IP address in the `trap2sink` directive.

{{%/notice%}}

After you complete the configuration, restart the `snmpd` service to apply the changes:

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

### Source Traps from a Different Source IP Address

When client SNMP programs (such as `snmpget`, `snmpwalk`, or `snmptrap`) are run from the command line, or when `snmpd` is configured to send a trap (based on `snmpd.conf`), you can configure a *clientaddr* in `snmp.conf` that allows the SNMP client programs or `snmpd` (for traps) to source requests from a different source IP address.

{{%notice note%}}

`snmptrap`, `snmpget`, `snmpwalk` and `snmpd` itself must be able to bind to this address.

{{%/notice%}}

For more information, read `snmp.conf` man page:

```
clientaddr [<transport-specifier>:]<transport-address>
            specifies the source address to be used by command-line applica-
            tions when sending SNMP requests. See snmpcmd(1) for more infor-
            mation about the format of addresses.
            This value is also used by snmpd when generating notifications.
```

### Monitor Fans, Power Supplies, and Transformers

An SNMP agent (`snmpd`) waits for incoming SNMP requests and responds to them. If no requests are received, an agent does not initiate any actions. However, various commands can configure `snmpd` to send traps based on preconfigured settings (`load`, `file`, `proc`, `disk`, or `swap` commands), or customized `monitor` commands.

From the `snmpd.conf` man page, the `monitor` command is defined this way:

```
monitor [OPTIONS] NAME EXPRESSION

            defines  a  MIB  object to monitor.  If the EXPRESSION condition holds then 
            this will trigger the corresponding event, and either send a notification or
            apply a SET assignment (or both).  Note that the event will only be triggered once,
            when the expression first matches.  This monitor entry will not fire again until the
            monitored condition first becomes false, and then matches again.  NAME is an administrative
            name for this expression, and is used for indexing the mteTriggerTable (and related tables).
            Note also that such monitors use an internal SNMPv3 request to retrieve the values
            being monitored (even  if  normal  agent  queries  typically  use SNMPv1 or SNMPv2c).
            See the iquerySecName token described above.

      EXPRESSION
            There are three types of monitor expression supported by the Event MIB - existence, boolean and threshold tests.

            OID | ! OID | != OID

                    defines  an  existence(0)  monitor  test.  A bare OID specifies a present(0) test,
                    which will fire when (an instance of) the monitored OID is created.  An expression
                    of the form ! OID specifies an absent(1) test, which will fire when the monitored
                    OID is delected.  An expression of the form != OID specifies a changed(2) test,
                    which will fire whenever the monitored value(s) change.  Note that there must be
                    whitespace before the OID token.

            OID OP VALUE

                    defines a boolean(1) monitor test.  OP should be one of the defined comparison operators
                    (!=, ==, <, <=, >, >=) and VALUE should be an integer value to compare against.  Note that
                    there must be whitespace around the OP token.  A comparison such as OID !=0 will not be
                    handled correctly.

            OID MIN MAX [DMIN DMAX]

                    defines a threshold(2) monitor test.  MIN and MAX are integer values, specifying
                    lower and upper thresholds.  If the value of the monitored OID falls below the lower
                    threshold (MIN) or rises above the upper threshold (MAX), then the monitor entry will
                    trigger the corresponding event.

                    Note that the rising threshold event will only be re-armed when the monitored value
                    falls below the lower threshold (MIN).  Similarly, the falling threshold event will
                    be re-armed by the upper threshold (MAX).

                    The optional parameters DMIN and DMAX configure a pair of similar threshold tests,
                    but working with the delta differences between successive sample values.

    OPTIONS

            There are various options to control the behaviour of the monitored expression.  These include:
            -D     indicates that the expression should be evaluated using delta differences between sample
                    values (rather than the values themselves).
            -d OID  or  -di OID
                    specifies a discontinuity marker for validating delta differences.  A -di object instance
                    will be used exactly as given.  A -d object will have the instance subidentifiers from
                    the corresponding (wildcarded) expression object appended.  If the -I flag is specified,
                    then there is no difference between these two options. This option also implies -D.
            -e EVENT
                    specifies the event to be invoked when this monitor entry is triggered.  If this option
                    is not given, the monitor entry will generate one of the standard notifications defined
                    in the DISMAN-EVENT-MIB.
            -I     indicates that the monitored expression should be applied to the specified OID as a
                    single instance.  By default, the OID will be treated as a wildcarded object, and the
                    monitor expanded to cover all matching instances.
            -i OID or -o OID
                    define additional varbinds to be added to the notification payload when this monitor
                    trigger fires.  For a wildcarded expression, the suffix of the matched instance will be
                    added to any OIDs specified using -o, while OIDs specified using -i will be treated
                    as exact instances.  If the -I flag is specified,  then  there  is  no difference between
                    these two options.
                    See strictDisman for details of the ordering of notification payloads.
            -r FREQUENCY
                    monitors the given expression every FREQUENCY, where FREQUENCY is in seconds or optionally
                    suffixed by one of s (for seconds), m (for minutes), h (for hours), d (for days),
                    or w (for weeks).  By default, the expression will be evaluated every 600s (10 minutes).
            -S     indicates that the monitor expression should not be evaluated when the agent first starts up.
                    The first evaluation will be done once the first repeat interval has expired.
            -s      indicates that the monitor expression should be evaluated when the agent first starts up.
                    This is the default behaviour.
                    Note:  Notifications triggered by this initial evaluation will be sent before the coldStart trap.
             -u SECNAME
                     specifies a security name to use for scanning the local host, instead of the default
                     iquerySecName.  Once again, this user must be explicitly created and given suitable access rights.
```

You can configurec`snmpd` to monitor the operational status of an Entity MIB or Entity-Sensor MIB. You can determine the operational status, given as a value of *ok(1)*, *unavailable(2)* or
*nonoperational(3)*, by adding the following example configuration to `/etc/snmp/snmpd.conf` and adjusting the values:

- Using the `entPhySensorOperStatus` integer:

```
# without installing extra MIBS we can check the check Fan1 status
# if the Fan1 index is 100011001, monitor this specific OID (-I) every 10 seconds (-r), and defines additional information to be included in the trap (-o).
monitor -I -r 10  -o 1.3.6.1.2.1.47.1.1.1.1.7.100011001 "Fan1 Not OK"  1.3.6.1.2.1.99.1.1.1.5.100011001 > 1
# Any Entity Status non OK (greater than 1)
 monitor  -r 10  -o 1.3.6.1.2.1.47.1.1.1.1.7  "Sensor Status Failure"  1.3.6.1.2.1.99.1.1.1.5 > 1
```

- Using the OID name:

```  
# for a specific fan called Fan1 with an index 100011001
monitor -I -r 10  -o entPhysicalName.100011001 "Fan1 Not OK"  entPhySensorOperStatus.100011001 > 1
# for any Entity Status not OK ( greater than 1)
 monitor  -r 10  -o entPhysicalName  "Sensor Status Failure"  entPhySensorOperStatus > 1
```

   {{%notice note%}}

You can use the OID name if the `snmp-mibs-downloader` package is installed.

   {{%/notice%}}

   {{%notice note%}}

The `entPhySensorOperStatus` integer can be found by walking the `entPhysicalName` table.

   {{%/notice%}}

- To get all sensor information, run `snmpwalk` on the `entPhysicalName` table. For example:

   ```
   cumulus@leaf01:~$ snmpwalk -v 2c -cpublic localhost .1.3.6.1.2.1.47.1.1.1.1.7
   iso.3.6.1.2.1.47.1.1.1.1.7.100000001 = STRING: "PSU1Temp1"
   iso.3.6.1.2.1.47.1.1.1.1.7.100000002 = STRING: "PSU2Temp1"
   iso.3.6.1.2.1.47.1.1.1.1.7.100000003 = STRING: "Temp1"
   iso.3.6.1.2.1.47.1.1.1.1.7.100000004 = STRING: "Temp2"
   iso.3.6.1.2.1.47.1.1.1.1.7.100000005 = STRING: "Temp3"
   iso.3.6.1.2.1.47.1.1.1.1.7.100000006 = STRING: "Temp4"
   iso.3.6.1.2.1.47.1.1.1.1.7.100000007 = STRING: "Temp5"
   iso.3.6.1.2.1.47.1.1.1.1.7.100011001 = STRING: "Fan1"
   iso.3.6.1.2.1.47.1.1.1.1.7.100011002 = STRING: "Fan2"
   iso.3.6.1.2.1.47.1.1.1.1.7.100011003 = STRING: "Fan3"
   iso.3.6.1.2.1.47.1.1.1.1.7.100011004 = STRING: "Fan4"
   iso.3.6.1.2.1.47.1.1.1.1.7.100011005 = STRING: "Fan5"
   iso.3.6.1.2.1.47.1.1.1.1.7.100011006 = STRING: "Fan6"
   iso.3.6.1.2.1.47.1.1.1.1.7.100011007 = STRING: "PSU1Fan1"
   iso.3.6.1.2.1.47.1.1.1.1.7.100011008 = STRING: "PSU2Fan1"
   iso.3.6.1.2.1.47.1.1.1.1.7.110000001 = STRING: "PSU1"
   iso.3.6.1.2.1.47.1.1.1.1.7.110000002 = STRING: "PSU2"
   ```

### Enable MIB to OID Translation

MIB names can be used instead of OIDs, by installing the `snmp-mibs-downloader`, to download SNMP MIBs to the switch prior to enabling traps. This greatly improves the readability of the `snmpd.conf` file.

1. Open `/etc/apt/sources.list` in a text editor.

2. Add the `non-free` repository, then save the file:

   ```
   cumulus@switch:~$ sudo deb http://ftp.us.debian.org/debian/ buster main non-free
   ```

3. Update the switch:

   ```
   cumulus@switch:~$ sudo -E apt-get update
   ```

4. Install the `snmp-mibs-downloader`:

   ```
   cumulus@switch:~$ sudo -E apt-get install snmp-mibs-downloader
   ```

5. Open the `/etc/snmp/snmp.conf` file to verify that the `mibs :` line is commented out:

   ```
   #
   # As the snmp packages come without MIB files due to license reasons, loading
   # of MIBs is disabled by default. If you added the MIBs you can reenable
   # loading them by commenting out the following line.
   #mibs :
   ```

6. Open the `/etc/default/snmpd` file to verify that the `export MIBS=` line is commented out:

   ``` 
   # This file controls the activity of snmpd and snmptrapd

   # Don't load any MIBs by default.
   # You might comment this lines once you have the MIBs Downloaded.
   #export MIBS=
   ```

7. After you confirm the configuration, remove or comment out the `non-free` repository in `/etc/apt/sources.list`.

   ```
   #deb http://ftp.us.debian.org/debian/ buster main non-free
   ```

### Configure Link Up/Down Notifications

The `linkUpDownNotifications` directive is used to configure link up/down notifications when the operational status of the link changes.

```
    linkUpDownNotifications yes
```

{{%notice note%}}

The default frequency for checking link up/down is 60 seconds. You can change the default frequency using the `monitor` directive directly instead of the `linkUpDownNotifications` directive. See `man snmpd.conf` for details.

{{%/notice%}}

### Configure Temperature Notifications

Temperature sensor information for each available sensor is maintained in lmSensors MIB. Each platform can contain a different number of temperature sensors. The example below generates a trap event when any temperature sensor exceeds a threshold of 68 degrees (centigrade). It monitors each `lmTempSensorsValue`. When the threshold value is checked and exceeds the `lmTempSensorsValue`, a trap is generated. The `-o lmTempSenesorsDevice` option is used to instruct SNMP to also include the lmTempSensorsDevice MIB in the generated trap. The default frequency for the `monitor` directive is 600 seconds. You can change the default frequency with the `-r` option:

```
monitor lmTemSensor -o lmTempSensorsDevice lmTempSensorsValue > 68000
```

To monitor the sensors individually, first use the `sensors` command to determine which sensors are available to be monitored on the platform.

```
cumulus@switch:~$ sudo sensors
]
CY8C3245-i2c-4-2e
Adapter: i2c-0-mux (chan_id 2)
fan5: 7006 RPM (min = 2500 RPM, max = 23000 RPM)
fan6: 6955 RPM (min = 2500 RPM, max = 23000 RPM)
fan7: 6799 RPM (min = 2500 RPM, max = 23000 RPM)
fan8: 6750 RPM (min = 2500 RPM, max = 23000 RPM)
temp1: +34.0 C (high = +68.0 C)
temp2: +28.0 C (high = +68.0 C)
temp3: +33.0 C (high = +68.0 C)
temp4: +31.0 C (high = +68.0 C)
temp5: +23.0 C (high = +68.0 C)
```

Configure a `monitor` command for the specific sensor using the `-I` option. The `-I` option indicates that the monitored expression is applied to a single instance. In this example, there are five temperature sensors available. Use the following directive to monitor only temperature sensor 3 at 5 minute intervals.

```
monitor -I -r 300 lmTemSensor3 -o lmTempSensorsDevice.3 lmTempSensorsValue.3 > 68000
```

### Configure Free Memory Notifications

You can monitor free memory using the following directives. The example below generates a trap when free memory drops below 1,000,000KB. The free memory trap also includes the amount of total real memory:

```
monitor MemFreeTotal -o memTotalReal memTotalFree <  1000000
```

### Configure Processor Load Notifications

To monitor CPU load for 1, 5, or 15 minute intervals, use the `load` directive with the `monitor` directive. The following example generates a trap when the 1 minute interval reaches 12%, the 5 minute interval reaches 10%, or the 15 minute interval reaches 5%.

```
load 12 10 5
```

### Configure Disk Utilization Notifications

To monitor disk utilization for all disks, use the `includeAllDisks` directive together with the `monitor` directive. The example code below generates a trap when a disk is 99% full:

```
includeAllDisks 1%
monitor -r 60 -o dskPath -o DiskErrMsg "dskTable" diskErrorFlag !=0
```

### Configure Authentication Notifications

To generate authentication failure traps, use the `authtrapenable` directive:

```
authtrapenable 1
```

## snmptrapd.conf

Use the Net-SNMP trap daemon to **receive** SNMP traps. The `/etc/snmp/snmptrapd.conf` file is used to configure how **incoming** traps are processed. Starting with Net-SNMP release 5.3, you must specify who is authorized to send traps and informs to the notification receiver (and what types of processing these are allowed to trigger). You can specify three processing types:

- *log* logs the details of the notification in a specified file to standard output (or stderr), or through syslog (or similar).
- *execute* passes the details of the trap to a specified handler program, including embedded Perl.
- *net* forwards the trap to another notification receiver.

Typically, this configuration is *log,execute,net* to cover any style of processing for a particular category of notification. But it is possible (even desirable) to limit certain notification sources to selected processing only.

`authCommunity TYPES COMMUNITY [SOURCE [OID | -v VIEW ]]` authorizes traps and SNMPv2c INFORM requests with the specified community to trigger the types of processing listed. By default, this allows any notification using this community to be processed. You can use the SOURCE field to specify that the configuration only applies to notifications received from particular sources. For more information about specific configuration options within the file, look at the `snmpd.conf(5)` man page with the following command:

```
cumulus@switch:~$ man 5 snmptrapd.conf

###############################################################################
#
# EXAMPLE-trap.conf:
#   An example configuration file for configuring the Net-SNMP snmptrapd agent.
#
###############################################################################
#
# This file is intended to only be an example.  If, however, you want
# to use it, it should be placed in /etc/snmp/snmptrapd.conf.
# When the snmptrapd agent starts up, this is where it will look for it.
#
# All lines beginning with a '#' are comments and are intended for you
# to read.  All other lines are configuration commands for the agent.

#
# PLEASE: read the snmptrapd.conf(5) manual page as well!
#
# this is the default (port 162) and defines the listening
# protocol and address  (e.g.  udp:10.10.10.10)
snmpTrapdAddr localhost
#
# defines the actions and the community string
authCommunity log,execute,net public
```
