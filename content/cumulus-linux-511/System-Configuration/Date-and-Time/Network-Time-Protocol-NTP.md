---
title: Network Time Protocol - NTP
author: NVIDIA
weight: 124
toc: 3
---
The `ntpd` daemon running on the switch implements the NTP protocol. It synchronizes the system time with time servers in the `/etc/ntpsec/ntp.conf` file. The `ntpd` daemon starts at boot by default.

{{%notice note%}}
If you intend to run this service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF#run-services-within-the-management-vrf" text="these steps">}} to configure the service.
{{%/notice%}}

## Configure NTP Servers

The default NTP configuration includes the following servers, which are in the `/etc/ntpsec/ntp.conf` file:

- server 0.cumulusnetworks.pool.ntp.org iburst
- server 1.cumulusnetworks.pool.ntp.org iburst
- server 2.cumulusnetworks.pool.ntp.org iburst
- server 3.cumulusnetworks.pool.ntp.org iburst

To add the NTP servers you want to use, run the following commands. Include the `iburst` option to increase the sync speed.

{{< tabs "TabID106 ">}}
{{< tab "NVUE Commands ">}}

The NVUE command requires a VRF. The following command adds the NTP servers in the default VRF.

```
cumulus@switch:~$ nv set service ntp default server 4.cumulusnetworks.pool.ntp.org iburst on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ntpsec/ntp.conf` file to add or update NTP server information:

```
cumulus@switch:~$ sudo nano /etc/ntpsec/ntp.conf
# pool.ntp.org maps to about 1000 low-stratum NTP servers.  Your server will
# pick a different set every time it starts up.  Please consider joining the
# pool: <http://www.pool.ntp.org/join.html>
server 0.cumulusnetworks.pool.ntp.org iburst
server 1.cumulusnetworks.pool.ntp.org iburst
server 2.cumulusnetworks.pool.ntp.org iburst
server 3.cumulusnetworks.pool.ntp.org iburst
server 4.cumulusnetworks.pool.ntp.org iburst
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
To set the initial date and time with NTP before starting the `ntpd` daemon, run the `ntpd -q` command. Be aware that `ntpd -q` can hang if the time servers are not reachable.
{{%/notice%}}

To verify that `ntpd` is running on the system:

```
cumulus@switch:~$ ps -ef | grep ntp
ntp       4074     1  0 Jun20 ?        00:00:33 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -u 101:102
```

To check the NTP peer status:

{{< tabs "TabID166 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show service ntp mgmt server
                 delay    iburst  jitter  offset   peer-state  poll  reach  refid         stratum  type  when
---------------  -------  ------  ------  -------  ----------  ----  -----  ------------  -------  ----  ----
23.157.160.168   67.4257          2.3843  -3.9378  -           128   377    129.6.15.28   2        u     41  
50.205.57.38     72.6007          1.0799  -1.8208  *           128   377    .GPS.         1        u     63  
h134-215-155-17  59.4988          2.3081  -2.6286  +           128   377    216.239.35.0  2        u     15  
li1150-42.membe  40.9645          0.4877  -1.9565  +           64    376    129.7.1.66    2        u     162
```

{{%notice note%}}
The `nv show service ntp <vrf-id> pool` command shows information about the configured NTP pools. However, this command does not show an accurate representation of the connectivity state to the NTP reference clocks on the network. To show the actual state of the NTP reference servers discovered by the switch, run the `nv show service ntp <vrf-id> server` command.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ ntpq -p
      remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
+ec2-34-225-6-20 129.6.15.30      2 u   73 1024  377   70.414   -2.414   4.110
+lax1.m-d.net    132.163.96.1     2 u   69 1024  377   11.676    0.155   2.736
*69.195.159.158  199.102.46.72    2 u  133 1024  377   48.047   -0.457   1.856
-2.time.dbsinet. 198.60.22.240    2 u 1057 1024  377   63.973    2.182   2.692
```

{{< /tab >}}
{{< /tabs >}}

The following example commands remove default NTP servers:

{{< tabs "TabID204 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv unset service ntp default server 0.cumulusnetworks.pool.ntp.org
cumulus@switch:~$ nv unset service ntp default server 1.cumulusnetworks.pool.ntp.org
cumulus@switch:~$ nv unset service ntp default server 2.cumulusnetworks.pool.ntp.org
cumulus@switch:~$ nv unset service ntp default server 3.cumulusnetworks.pool.ntp.org
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ntpsec/ntp.conf` file to delete NTP servers.

```
cumulus@switch:~$ sudo nano /etc/ntpsec/ntp.conf
...
# pool.ntp.org maps to about 1000 low-stratum NTP servers.  Your server will
# pick a different set every time it starts up.  Please consider joining the
# pool: <http://www.pool.ntp.org/join.html>
server 4.cumulusnetworks.pool.ntp.org iburst
...
```

{{< /tab >}}
{{< /tabs >}}

## Specify the NTP Source Interface

By default, the source interface that NTP uses is eth0. The following example command configures the NTP source interface to be swp10.

{{< tabs "TabID243 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ntp default listen swp10
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ntpsec/ntp.conf` file and modify the entry under the `Specify interfaces` comment.

```
cumulus@switch:~$ sudo nano /etc/ntpsec/ntp.conf
...
# Specify interfaces
interface listen swp10
...
```

{{< /tab >}}
{{< /tabs >}}

## Use NTP in a DHCP Environment

You can use DHCP to specify your NTP servers. Ensure that the DHCP-generated configuration file `/run/ntp.conf.dhcp` exists. The `/etc/dhcp/dhclient-exit-hooks.d/ntp` script generates this file, which is a copy of the default `/etc/ntpsec/ntp.conf` file with a modified server list from the DHCP server. If this file does not exist and you plan on using DHCP in the future, you can copy your current `/etc/ntpsec/ntp.conf` file to the location of the DHCP file.

To use DHCP to specify your NTP servers, run the `sudo -E systemctl edit ntpsec.service` command and add the `ExecStart=` line:

```
cumulus@switch:~$ sudo -E systemctl edit ntpsec.service
[Service]
ExecStart=
ExecStart=/usr/sbin/ntpd -n -u ntp:ntp -g -c /run/ntp.conf.dhcp
```

{{%notice note%}}
The `sudo -E systemctl edit ntpsec.service` command always updates the base `ntpsec.service` even if you use `ntp@mgmt.service`. The `ntpsec@mgmt.service` is re-generated automatically.
{{%/notice%}}

To validate that your configuration, run these commands:

```
cumulus@switch:~$ sudo systemctl restart ntp
cumulus@switch:~$ sudo systemctl status -n0 ntpsec.service
```

If the state is not *Active*, or the alternate configuration file does not appear in the `ntp` command line, it is likely that you made a configuration mistake. Correct the mistake and rerun the commands above to verify.

## Configure NTP with Authorization Keys

For added security, you can configure NTP to use authorization keys.

### Configure the NTP Server

1. Create a `.keys` file, such as `/etc/ntp.keys`. Specify a key identifier (a number between 1 and 65535), an encryption method (M for MD5), and the password. The following provides an example:
<!-- vale off -->
    ```
    #
    # PLEASE DO NOT USE THE DEFAULT VALUES HERE.
    #
    #65535  M  akey
    #1      M  pass

    1  M  CumulusLinux!
    ```
<!-- vale on -->
2. In the `/etc/ntpsec/ntp.conf` file, add a pointer to the `/etc/ntp.keys` file you created above and specify the key identifier. For example:

    ```
    keys /etc/ntp/ntp.keys
    trustedkey 1
    controlkey 1
    requestkey 1
    ```

3. Restart NTP with the `sudo systemctl restart ntp` command.

### Configure the NTP Client

The NTP client is the Cumulus Linux switch.

1. Create the same `.keys` file you created on the NTP server (`/etc/ntp.keys`). For example:
<!-- vale off -->
    ```
    cumulus@switch:~$  sudo nano /etc/ntp.keys
    #
    # DO NOT USE THE DEFAULT VALUES HERE.
    #
    #65535  M  akey
    #1      M  pass

    1  M  CumulusLinux!
    ```
<!-- vale on -->
2. Edit the `/etc/ntpsec/ntp.conf` file to specify the server you want to use, the key identifier, and a pointer to the `/etc/ntp.keys` file you created in step 1. For example:

    ```
    cumulus@switch:~$ sudo nano /etc/ntpsec/ntp.conf
    ...
    # You do need to talk to an NTP server or two (or three).
    #pool ntp.your-provider.example
    # OR
    #server ntp.your-provider.example

    # pool.ntp.org maps to about 1000 low-stratum NTP servers.  Your server will
    # pick a different set every time it starts up.  Please consider joining the
    # pool: <http://www.pool.ntp.org/join.html>
    #server 0.cumulusnetworks.pool.ntp.org iburst
    #server 1.cumulusnetworks.pool.ntp.org iburst
    #server 2.cumulusnetworks.pool.ntp.org iburst
    #server 3.cumulusnetworks.pool.ntp.org iburst
    server 10.50.23.121 key 1

    #keys
    keys /etc/ntp.keys
    trustedkey 1
    controlkey 1
    requestkey 1
    ...
    ```

3. Restart NTP in the active VRF (default or management). For example:

    ```
    cumulus@switch:~$ systemctl restart ntp@mgmt.service
    ```

4. Wait a few minutes, then run the `ntpq -c as` command to verify the configuration:

    ```
    cumulus@switch:~$ ntpq -c as

    ind assid status  conf reach auth condition  last_event cnt
    ===========================================================
      1 40828  f014   yes   yes   ok     reject   reachable  1
    ```

    After a successful authorization, you see the following command output:

    ```
    cumulus@switch:~$ ntpq -c as

    ind assid status  conf reach auth condition  last_event cnt
    ===========================================================
      1 40828  f61a   yes   yes   ok   sys.peer    sys_peer  1
    ```

## Considerations

NTP in Cumulus Linux uses the `/usr/share/zoneinfo/leap-seconds.list` file, which expires periodically and results in generated log messages about the expiration. When the file expires, update it from {{<exlink url="https://www.ietf.org/timezones/data/leap-seconds.list" text="https://www.ietf.org/timezones/data/leap-seconds.list">}} or upgrade the `tzdata` package to the newest version.

## Related Information

- {{<exlink url="http://www.ntp.org" text="NTP website">}}
- {{<exlink url="http://en.wikipedia.org/wiki/Network_Time_Protocol" text="Wikipedia - Network Time Protocol">}}
- {{<exlink url="http://wiki.debian.org/NTP" text="Debian wiki - NTP">}}
