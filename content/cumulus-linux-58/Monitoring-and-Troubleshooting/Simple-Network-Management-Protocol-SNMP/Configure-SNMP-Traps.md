---
title: Configure SNMP Traps
author: NVIDIA
weight: 1160
toc: 4
---

SNMP *traps* are alert notification messages from SNMP agents to the SNMP manager. These messages generate whenever any failure or fault occurs in a monitored device or service. An SNMPv3 inform is an acknowledged SNMPv3 trap.

You configure the following for SNMPv3 trap and inform messages:

- The trap destination IP address; the VRF name is optional.
- The authentication type and password. The encryption type and password are optional.
- The engine ID and username pair for the Cumulus Linux switch sending the traps. The *inform* keyword specifies an inform message where the SNMP agent waits for an acknowledgement. You can find this at the end of the `/var/lib/snmp/snmpd.conf` file labeled *oldEngineID*. Configure this same engine ID/username (with authentication and encryption passwords) for the trap daemon receiving the trap to validate the received trap.

## Generate Event Notification Traps

The Net-SNMP agent provides a method to generate SNMP trap events using the Distributed Management (DisMan) Event MIB for various system events, including:

- Link up/down.
- Exceeding the temperature sensor threshold, CPU load, or memory threshold.
- Other SNMP MIBs.

To enable specific types of traps, create the following configurations in `/etc/snmp/snmpd.conf`.

### Define Access Credentials
<!-- vale off -->
Although the traps are sent to an SNMPv2c receiver, the SNMPv3 username is still required to authorize the DisMan service. Starting with Net-SNMP 5.3, `snmptrapd` no longer accepts all traps by default. You must configure `snmptrapd` with authorized SNMPv1 and v2c community strings and, or SNMPv3 users. Non-authorized traps and informs are dropped.
<!-- vale on -->
Follow the steps in {{<link url="Configure-SNMP/#configure-the-snmpv3-username">}} to define the username. You can refer to the {{<exlink url="http://www.net-snmp.org/docs/man/snmptrapd.conf.html" text="snmptrapd.conf(5) manual page">}} for more information.

{{%notice note%}}
If not already on the system, install the `snmptrapd` Debian package with the `sudo apt-get install snmptrapd` command before you configure the username.
{{%/notice%}}

### Define Trap Receivers

The following configuration defines the trap receiver IP address for SNMPv1 and SNMPv2c traps. For SNMP versions 1 and 2c, you must set at least one SNMP trap destination IP address; multiple destinations can exist. Removing all settings disables SNMP traps. The default version is 2c. You must include a VRF name with the IP address to force traps to send in a non-default VRF table.

{{< tabs "trap-destination" >}}
{{< tab "NVUE Commands" >}}

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf rocket community-password mymanagementvrfpassword version 1
cumulus@switch:~$ nv set service snmp-server trap-destination localhost-v6 community-password mynotsosecretpassword version 2c
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands" >}}

To define the IP address of the notification (or trap) receiver for either SNMPv1 traps or SNMPv2 traps, use the `trapsink` (SNMPv1) `trap2sink` (SNMPv2c). Specifying more than one sink directive generates multiple copies of each notification (in the appropriate formats). You must configure a trap server to receive and decode these trap messages (for example, `snmptrapd`). You can configure the address of the trap receiver with a different protocol and port but this is most often left out. The defaults are to use the well-known UDP packets and port 162.

Edit the `/etc/snmp/snmpd.conf` file and configure the trap settings.

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
trap2sink [::1] mynotsosecretpassword
trapsink 127.0.0.1@rocket mymanagementvrfpassword
...
```

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

{{< /tab >}}
{{< /tabs >}}

### SNMPv3 Trap and Inform Messages

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

{{< tabs "traps-informs" >}}
{{< tab "NVUE Commands" >}}

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-md5 md5password1 encrypt-aes myaessecret engine-id  0x80001f888070939b14a514da5a00000000 inform
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf mgmt username mymgmtvrfusername auth-md5 md5password2 encrypt-aes myaessecret2 engine-id  0x80001f888070939b14a514da5a00000000 inform
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands" >}}

You can configure SNMPv3 trap and inform messages with the `trapsess` configuration command. Inform messages are traps that the receiving trap daemon acknowledges. You configure inform messages with the `-Ci` parameter. You must specify the EngineID of the receiving trap server with the `-e` field.

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
trapsess -Ci -e 0x80001f888070939b14a514da5a00000000 -v3 -l authPriv -u mymgmtvrfusername -a MD5 -A md5password2 -x AES -X myaessecret2 127.0.0.1@mgmt
trapsess -Ci -e 0x80001f888070939b14a514da5a00000000 -v3 -l authPriv -u myv3user -a MD5 -A md5password1 -x AES -X myaessecret 127.0.0.1
...
```

{{%notice note%}}
You can define multiple trap receivers and use the domain name instead of an IP address in the `trap2sink` directive.
{{%/notice%}}

Restart the `snmpd` service to apply the changes:

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

{{< /tab >}}
{{< /tabs >}}

### Source Traps from a Different Source IP Address

When you run client SNMP programs (such as `snmpget`, `snmpwalk`, or `snmptrap`) from the command line, or when you configure `snmpd` to send a trap (based on `snmpd.conf`), you can configure a `clientaddr` in `snmpd.conf` that allows the SNMP client programs or `snmpd` (for traps) to source requests from a different source IP address.

For more information about `clientaddr`, see the `snmpd.conf` {{<exlink url="http://www.net-snmp.org/docs/man/snmpd.conf.html" text="man page">}}.

{{%notice note%}}
`snmptrap`, `snmpget`, `snmpwalk` and `snmpd` itself must be able to bind to this address.
{{%/notice%}}

Edit the `/etc/snmp/snmpd.conf` file and add the `clientaddr` option. In the following example, spine01 is the client (IP address 192.168.200.21).

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
trapsess -Ci --clientaddr=192.168.200.21 -v 2c
...
```

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

{{%notice note%}}
NVUE does not provide commands for this configuration.
{{%/notice%}}

### Monitor Fans, Power Supplies, Temperature and Transformers

An SNMP agent (`snmpd`) waits for incoming SNMP requests and responds to them. If the agent does not receive any requests, it does not start any actions. However, various commands can configure `snmpd` to send traps according to preconfigured settings (`load`, `file`, `proc`, `disk`, or `swap` commands), or customized `monitor` directives.

See the `snmpd.conf` {{<exlink url="http://www.net-snmp.org/docs/man/snmpd.conf.html" text="man page">}} for details on the `monitor` directive.

You can configure `snmpd` to monitor the operational status of either the Entity MIB or Entity-Sensor MIB by adding the `monitor` directive to the `snmpd.conf` file. After you know the OID, you can determine the operational status, which can be a value of *ok(1)*, *unavailable(2)* or *nonoperational(3)*. Add a configuration like the following example to `/etc/snmp/snmpd.conf` and adjust the values:

- Use the `entPhySensorOperStatus` integer:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
# without installing extra MIBS we can check the check Fan1 status
# if the Fan1 index is 100011001, monitor this specific OID (-I) every 10 seconds (-r), and defines additional information to be included in the trap (-o).
monitor -I -r 10  -o 1.3.6.1.2.1.47.1.1.1.1.7.100011001 "Fan1 Not OK"  1.3.6.1.2.1.99.1.1.1.5.100011001 > 1
# Any Entity Status non OK (greater than 1)
monitor  -r 10  -o 1.3.6.1.2.1.47.1.1.1.1.7  "Sensor Status Failure"  1.3.6.1.2.1.99.1.1.1.5 > 1
```

- Use the OID name. You can use the OID name if the `snmp-mibs-downloader` package is on the system (see {{<link url="#enable-mib-to-oid-translation" text="below">}}).

```  
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
# for a specific fan called Fan1 with an index 100011001
monitor -I -r 10  -o entPhysicalName.100011001 "Fan1 Not OK"  entPhySensorOperStatus.100011001 > 1
# for any Entity Status not OK ( greater than 1)
monitor  -r 10  -o entPhysicalName  "Sensor Status Failure"  entPhySensorOperStatus > 1
```

   {{%notice note%}}
You can find the `entPhySensorOperStatus` integer by walking the `entPhysicalName` table.
{{%/notice%}}

To get all sensor information, run `snmpwalk` on the `entPhysicalName` table. For example:

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

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

{{%notice note%}}
Cumulus Linux no longer uses the LM-SENSORS MIB to monitor temperature.
{{%/notice%}}

### Configure Link Up and Link Down Notifications

You can configure the switch to trigger link up and link down notifications when the operational status of the link changes.

{{< tabs "traps-linkupdown" >}}
{{< tab "NVUE Commands" >}}

The following example commands enable the Disman Event MIB (.1.3.6.1.2.1.88.2.0.1) to monitor the ifTable for network interfaces that come up every 15 seconds or go down every 10 seconds, and trigger a `CumulusLinkUp` and `CumulusLinkDown` named notification.

The default check frequency is 60 seconds, with a minimum of 5 and a maximum of 300 seconds.

These notifications include the following information.
- `ifName`
- `ifIndex`
- `ifAdminStatus`
- `ifOperStatus`

```
cumulus@switch:~$ nv set service snmp-server trap-link-down check-frequency 10
cumulus@switch:~$ nv set service snmp-server trap-link-up check-frequency 15
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands" >}}

Edit the `/etc/snmp/snmpd.conf` file and configure the trap settings.

The following example commands enable the Disman Event MIB (.1.3.6.1.2.1.88.2.0.1) to monitor the ifTable for network interfaces that come up every 15 seconds or go down every 10 seconds, and trigger a `CumulusLinkUp` and `CumulusLinkDown` named notification.

These notifications include the following information.
- `ifName`
- `ifIndex`
- `ifAdminStatus`
- `ifOperStatus`

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
monitor CumulusLinkDOWN -S -r 10 -o ifName -o ifIndex -o ifAdminStatus -o ifOperStatus ifOperStatus == 2
monitor CumulusLinkUP -S -r 15 -o ifName -o ifIndex -o ifAdminStatus -o ifOperStatus ifOperStatus != 2
```

The following example adds `linkUpTrap` and `linkDownTrap` traps as defined in {{<exlink url="https://www.rfc-editor.org/rfc/rfc3418" text="RFC 3418">}}:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
linkUpDownNotifications yes

notificationEvent  linkUpTrap    linkUp   ifIndex ifAdminStatus ifOperStatus
notificationEvent  linkDownTrap  linkDown ifIndex ifAdminStatus ifOperStatus
monitor  -r 15 -e linkUpTrap   "Generate linkUp" ifOperStatus != 2
monitor  -r 10 -e linkDownTrap "Generate linkDown" ifOperStatus == 2
...
```

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

For more information or additional options, refer to the `snmpd.conf` man page.

{{< /tab >}}
{{< /tabs >}}

### Configure Free Memory Notifications

You can monitor free memory and configure the switch to generate a trap when free memory drops below a certain size.

The following example generates a trap when free memory drops below 1,000,000KB. The free memory trap also includes the amount of total real memory:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
monitor MemFreeTotal -o memTotalReal memTotalFree <  1000000
...
```

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

{{%notice note%}}
NVUE does not provide commands to configure free memory notifications.
{{%/notice%}}

### Configure Processor Load Notifications

To generate a trap when the CPU load average exceeds a certain threshold, run the following commands. You can only use integers or floating point numbers.

The following example generates a trap when the 1 minute interval reaches 12%, the 5 minute interval reaches 10%, or the 15 minute interval reaches 5%.

{{< tabs "traps-cpuload" >}}
{{< tab "NVUE Commands" >}}

```
cumulus@switch:~$ nv set service snmp-server trap-cpu-load-average one-minute 12 five-minute 10 fifteen-minute 5
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands" >}}

Edit the `/etc/snmp/snmpd.conf` file and configure the CPU load settings. To monitor CPU load for 1, 5, or 15 minute intervals, use the `load` directive with the `monitor` directive.

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
load 12 10 5
...

```
Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

{{< /tab >}}
{{< /tabs >}}

### Configure Disk Utilization Notifications

To monitor disk utilization for all disks, use the `includeAllDisks` directive together with the `monitor` directive. The example code below generates a trap when a disk is 99% full:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
includeAllDisks 1%
monitor -r 60 -o dskPath -o DiskErrMsg "dskTable" diskErrorFlag !=0
...
```

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

{{%notice note%}}
NVUE does not provide commands to configure disk utilization notifications.
{{%/notice%}}

### Configure Authentication Notifications

To generate SNMP trap notifications for every SNMP authentication failure, run the following commands.

{{< tabs "traps-authfailurre" >}}
{{< tab "NVUE Commands" >}}

```
cumulus@switch:~$ nv set service snmp-server trap-snmp-auth-failures
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands" >}}

In the `/etc/snmp/snmpd.conf` file, add the `authtrapenable` directive:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
authtrapenable 1
...
```

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
### Monitor UCD-SNMP-MIB Tables
<!-- vale on -->
To configure the Event MIB tables to monitor the various UCD-SNMP-MIB tables for problems (xxErrFlag column objects) and send a trap, add `defaultMonitors yes` to the `snmpd.conf` file and provide a configuration. You must first download the `snmp-mibs-downloader` Debian package and comment out the `mibs` line from the `/etc/snmp/snmpd.conf` file (see {{<link url="#enable-mib-to-oid-translation" text="below">}}). Then add a configuration like the following example:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
defaultMonitors yes

monitor   -o prNames -o prErrMessage "process table" prErrorFlag != 0
monitor   -o memErrorName -o memSwapErrorMsg "memory" memSwapError != 0
monitor   -o extNames -o extOutput "extTable" extResult != 0<br>monitor   -o dskPath -o dskErrorMsg "dskTable" dskErrorFlag != 0
monitor   -o laNames -o laErrMessage  "laTable" laErrorFlag != 0<br>monitor   -o fileName -o fileErrorMsg  "fileTable" fileErrorFlag != 0
...
```

Restart the `snmpd` service to apply the changes.

```
cumulus@switch:~$ sudo systemctl restart snmpd.service
```

## Enable MIB to OID Translation

You can use MIB names instead of OIDs, which greatly improves the readability of the `snmpd.conf` file. You enable this by installing the `snmp-mibs-downloader`, which downloads SNMP MIBs to the switch before enabling traps.

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

5. Open the `/etc/snmp/snmp.conf` file to verify that the `mibs :` line is in comments:

   ```
   #
   # As the snmp packages come without MIB files due to license reasons, loading
   # of MIBs is disabled by default. If you added the MIBs you can reenable
   # loading them by commenting out the following line.
   #mibs :
   ```

6. Open the `/etc/default/snmpd` file to verify that the `export MIBS=` line is in comments:

   ``` 
   # This file controls the activity of snmpd and snmptrapd

   # Don't load any MIBs by default.
   # You might comment this lines after you have the MIBs Downloaded.
   #export MIBS=
   ```

7. After you confirm the configuration, remove or comment out the `non-free` repository in `/etc/apt/sources.list`.

   ```
   #deb http://ftp.us.debian.org/debian/ buster main non-free
   ```

## Configure Incoming SNMP Traps
<!-- vale off -->
The Net-SNMP trap daemon in `/etc/snmp/snmpd.conf` *receives* SNMP traps. You configure how *incoming* traps process in the `/etc/snmp/snmptrapd.conf` file. With Net-SNMP release 5.3 and later, you must specify who is authorized to send traps and informs to the notification receiver (and what types of processing these are allowed to trigger). You can specify three processing types:
<!-- vale on -->
- *log* logs the details of the notification in a specified file to standard output (or `stderr`), or through syslog (or similar).
- *execute* passes the details of the trap to a specified handler program, including embedded Perl.
- *net* forwards the trap to another notification receiver.

Typically, you configure all three &mdash; *log,execute,net* &mdash; to cover any style of processing for a particular category of notification. You can limit certain notification sources to certain processing only.

`authCommunity TYPES COMMUNITY [SOURCE [OID | -v VIEW ]]` authorizes traps and SNMPv2c INFORM requests with the community you specify to trigger the types of processing you list. By default, this allows any notification using this community to process. You can use the SOURCE field to specify that the configuration only applies to notifications from particular sources. For more information about specific configuration options within the file, see {{<exlink url="http://www.net-snmp.org/docs/man/snmptrapd.conf.html" text="snmptrapd.conf(5) man page">}} with the `man 5 snmptrapd.conf` command.

{{%notice note%}}
If not already on the system, install the `snmptrapd` Debian package before you configure incoming traps:

```
cumulus@switch:~$ sudo apt-get install snmptrapd
```

{{%/notice%}}
