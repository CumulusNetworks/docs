---
title: Zero Touch Provisioning - ZTP
author: NVIDIA
weight: 90
toc: 3
---
Use <span class="a-tooltip">[ZTP](## "Zero Touch Provisioning")</span> to deploy network devices in large-scale environments. On first boot, Cumulus Linux runs ZTP, which executes the provisioning automation that deploys the device for its intended role in the network.

The provisioning framework allows you to execute a one-time, user-provided script. You can develop this script using a variety of automation tools and scripting languages. You can also use it to add the switch to a configuration management (CM) platform such as {{<exlink url="http://puppet.com/" text="Puppet">}}, {{<exlink url="https://www.chef.io" text="Chef">}}, {{<exlink url="https://cfengine.com" text="CFEngine">}} or a custom, proprietary tool.

While developing and testing the provisioning logic, you can use the `ztp` command in Cumulus Linux to run your provisioning script manually on a device.

ZTP in Cumulus Linux can run automatically in one of the following ways, in this order:

1. Through a local file
2. Using a USB drive inserted into the switch (ZTP-USB)
3. Through DHCP

## Use a Local File

ZTP only looks one time for a ZTP script on the local file system when the switch boots. ZTP searches for an install script that matches an {{<exlink url="https://opencomputeproject.github.io/onie/" text="ONIE">}}-style waterfall in `/var/lib/cumulus/ztp`, looking for the most specific name first, and ending at the most generic:

- `'cumulus-ztp-' + architecture + '-' + vendor + '_' + model + '-r' + revision`
- `'cumulus-ztp-' + architecture + '-' + vendor + '_' + model`
- `'cumulus-ztp-' + vendor + '_' + model`
- `'cumulus-ztp-' + architecture`
- `'cumulus-ztp'`

You can also trigger the ZTP process manually by running the `ztp --run <URL>` command, where the URL is the path to the ZTP script.

## Use a USB Drive

{{%notice note%}}
NVIDIA tests this feature only with *thumb* drives, not an external large USB hard drive.
{{%/notice%}}
If the `ztp` process does not discover a local script, it tries one time to locate an inserted but unmounted USB drive. If it discovers one, it begins the ZTP process.
Cumulus Linux supports the use of a FAT32, FAT16, or VFAT-formatted USB drive as an installation source for ZTP scripts. You must plug in the USB drive **before** you power up the switch.

At minimum, the script must:
- Install the Cumulus Linux operating system.
- Copy over a basic configuration to the switch.
- Restart the switch or the relevant services to get `switchd` up and running with that configuration.

Follow these steps to perform ZTP using a USB drive:

1. Copy the installation image to the USB drive.
2. The `ztp` process searches the root filesystem of the newly mounted drive for filenames matching an {{<exlink url="https://opencomputeproject.github.io/onie/user-guide/index.html#directly-connected-scenario" text="ONIE-style waterfall">}} (see the patterns and examples above), looking for the most specific name first, and ending at the most generic.
3. ZTP parses the contents of the script to ensure it contains the `CUMULUS-AUTOPROVISIONING` flag (see {{<link url="#write-ztp-scripts" text="example scripts">}}).

{{%notice note%}}
The USB drive mounts to a temporary directory under `/tmp` (for example, `/tmp/tmpigGgjf/`). To reference files on the USB drive, use the environment variable `ZTP_USB_MOUNTPOINT` to refer to the USB root partition.
{{%/notice%}}

## ZTP Over DHCP

If the `ztp` process does not discover a local <span class="a-tooltip">[ONIE](## "Open Network Install Environment")</span> script or applicable USB drive, it checks DHCP every ten seconds for up to five minutes for the presence of a ZTP URL specified in `/var/run/ztp.dhcp`. The URL can be any of HTTP, HTTPS, FTP, or TFTP.

For ZTP using DHCP, provisioning initially takes place over the management network and initiates through a DHCP hook. A DHCP option specifies a configuration script. The ZTP process requests this script from the Web server and the script executes locally.

The ZTP process over DHCP follows these steps:

1. The first time you boot Cumulus Linux, eth0 makes a DHCP request.
2. The DHCP server offers a lease to the switch.
3. If option 239 is in the response, the ZTP process starts.
4. The ZTP process requests the contents of the script from the URL, sending additional {{<link url="#inspect-http-headers" text="HTTP headers">}} containing details about the switch.
5. ZTP parses the contents of the script to ensure it contains the `CUMULUS-AUTOPROVISIONING` flag (see {{<link url="#write-ztp-scripts" text="example scripts">}}).
6. If provisioning is necessary, the script executes locally on the switch with root privileges.
7. ZTP examines the return code of the script. If the return code is 0, ZTP marks the provisioning state as complete in the autoprovisioning configuration file.

Cumulus Linux always sends DHCP option 60 (the vendor class identifier) with value `cumulus-linux  x86_64`.

### Trigger ZTP Over DHCP

If you have not yet provisioned the switch, you can trigger the ZTP process over DHCP when eth0 uses DHCP and one of the following events occur:

- The switch boots.
- You plug a cable into or unplug a cable from the eth0 port.
- You disconnect, then reconnect the switch power cord.

You can also run the `ztp --run <URL>` command, where the `URL` is the path to the ZTP script.

### Configure the DHCP Server

During the DHCP process over eth0, Cumulus Linux requests DHCP option 239. This option specifies the custom provisioning script.

For example, the `/etc/dhcp/dhcpd.conf` file for an ISC DHCP server looks like:

```
option cumulus-provision-url code 239 = text;

  subnet 192.0.2.0 netmask 255.255.255.0 {
  range 192.0.2.100 192.168.0.200;
  option cumulus-provision-url "http://192.0.2.1/demo.sh";
}
```

In addition, you can specify the hostname of the switch with the `host-name` option:

```
subnet 192.168.0.0 netmask 255.255.255.0 {
  range 192.168.0.100 192.168.0.200;
  option cumulus-provision-url "http://192.0.2.1/demo.sh";
  host dc1-tor-sw1 { hardware ethernet 44:38:39:00:1a:6b; fixed-address 192.168.0.101; option host-name "dc1-tor-sw1"; }
}
```

{{%notice note%}}
Do not use an underscore (_) in the hostname; underscores are not permitted in hostnames.
{{%/notice%}}

### DHCP on Front Panel Ports

ZTP runs DHCP on all the front panel switch ports and on any active interface. ZTP assesses the list of active ports on every retry cycle. When it receives the DHCP lease and option 239 is present in the response, ZTP starts to execute the script.

### Inspect HTTP Headers

The following HTTP headers in the request to the web server retrieve the provisioning script:

```
Header                        Value                 Example
------                        -----                 -------
User-Agent                                          CumulusLinux-AutoProvision/0.4
CUMULUS-ARCH                  CPU architecture      x86_64
CUMULUS-BUILD                                       5.1.0
CUMULUS-MANUFACTURER                                odm
CUMULUS-PRODUCTNAME                                 switch_model
CUMULUS-SERIAL                                      XYZ123004
CUMULUS-BASE-MAC                                    44:38:39:FF:40:94
CUMULUS-MGMT-MAC                                    44:38:39:FF:00:00
CUMULUS-VERSION                                     5.1.0
CUMULUS-PROV-COUNT                                  0
CUMULUS-PROV-MAX                                    32
```

## Write ZTP Scripts

{{%notice note%}}
You must include the following line in any of the supported scripts that you expect to run using the autoprovisioning framework.

```
# CUMULUS-AUTOPROVISIONING
```

{{%/notice%}}

The script must contain the `CUMULUS-AUTOPROVISIONING` flag. You can include this flag in a comment or remark; you do not need to echo or write the flag to `stdout`.

You can write the script in any language that Cumulus Linux supports, such as:

- Perl
- Python
- Ruby
- Shell

The script must return an exit code of 0 upon success to mark the process as complete in the autoprovisioning configuration file.

The following script installs Cumulus Linux from a USB drive and applies a configuration:

```
#!/bin/bash
function error() {
  echo -e "\e[0;33mERROR: The ZTP script failed while running the command $BASH_COMMAND at line $BASH_LINENO.\e[0m" >&2
  exit 1
}

# Log all output from this script
exec >> /var/log/autoprovision 2>&1
date "+%FT%T ztp starting script $0"

trap error ERR

#Add Debian Repositories
echo "deb http://http.us.debian.org/debian buster main" >> /etc/apt/sources.list
echo "deb http://security.debian.org/ buster/updates main" >> /etc/apt/sources.list

#Update Package Cache
apt-get update -y

#Load interface config from usb
cp ${ZTP_USB_MOUNTPOINT}/interfaces /etc/network/interfaces

#Load port config from usb
#   (if breakout cables are used for certain interfaces)
cp ${ZTP_USB_MOUNTPOINT}/ports.conf /etc/cumulus/ports.conf

#Reload interfaces to apply loaded config
ifreload -a

# CUMULUS-AUTOPROVISIONING
exit 0
```

## Continue Provisioning

Typically ZTP exits after executing the script locally and does not continue. To continue with provisioning so that you do not have to intervene manually or embed an Ansible callback into the script, you can add the `CUMULUS-AUTOPROVISION-CASCADE` directive.

## Best Practices

ZTP scripts come in different forms and frequently perform the same tasks. As BASH is the most common language for ZTP scripts, use the following BASH snippets to perform common tasks with robust error checking.

### Set the Default Cumulus User Password

The default *cumulus* user account password is `cumulus`. When you log into Cumulus Linux for the first time, you must provide a new password for the *cumulus* account, then log back into the system.

Add the following function to your ZTP script to change the default *cumulus* user account password to a clear-text password. The example changes the password `cumulus` to `MyP4$$word`.

```
function set_password(){
     # Unexpire the cumulus account
     passwd -x 99999 cumulus
     # Set the password
     echo 'cumulus:MyP4$$word' | chpasswd
}
set_password
```

If you have an insecure management network, set the password with an encrypted hash instead of a clear-text password.

- First, generate a sha-512 password hash with the following python commands. The example commands generate a sha-512 password hash for the password `MyP4$$word`.

   ```
   user@host:~$ python3 -c "import crypt; print(crypt.crypt('MyP4$$word',salt=crypt.mksalt()))"
   $6$hs7OPmnrfvLNKfoZ$iB3hy5N6Vv6koqDmxixpTO6lej6VaoKGvs5E8p5zNo4tPec0KKqyQnrFMII3jGxVEYWntG9e7Z7DORdylG5aR/
   ```

- Then, add the following function to the ZTP script to change the default *cumulus* user account password:

   ```
   function set_password(){
        # Unexpire the cumulus account
        passwd -x 99999 cumulus
        # Set the password
        usermod -p '$6$hs7OPmnrfvLNKfoZ$iB3hy5N6Vv6koqDmxixpTO6lej6VaoKGvs5E8p5zNo4tPec0KKqyQnrFMII3jGxVEYWntG9e7Z7DORdylG5aR/' cumulus
   }
   set_password
   ```

### Test DNS Name Resolution

DNS names are frequently used in ZTP scripts. The `ping_until_reachable` function tests that each DNS name resolves into a reachable IP address. Call this function with each DNS target used in your script before you use the DNS name elsewhere in your script.

The following example shows how to call the `ping_until_reachable` function in the context of a larger task.

```
function ping_until_reachable(){
    last_code=1
    max_tries=30
    tries=0
    while [ "0" != "$last_code" ] && [ "$tries" -lt "$max_tries" ]; do
        tries=$((tries+1))
        echo "$(date) INFO: ( Attempt $tries of $max_tries ) Pinging $1 Target Until Reachable."
        ping $1 -c2 &> /dev/null
        last_code=$?
            sleep 1
    done
    if [ "$tries" -eq "$max_tries" ] && [ "$last_code" -ne "0" ]; then
        echo "$(date) ERROR: Reached maximum number of attempts to ping the target $1 ."
        exit 1
    fi
}
```

### Check the Cumulus Linux Release

The following script segment demonstrates how to check which Cumulus Linux release is running and upgrades the node if the release is not the *target release*. If the release *is* the target release, normal ZTP tasks execute. This script calls the `ping_until_reachable` script (described above) to make sure the server holding the image server and the ZTP script is reachable.

```
function init_ztp(){
    #do normal ZTP tasks
}

CUMULUS_TARGET_RELEASE=5.1.0
CUMULUS_CURRENT_RELEASE=$(cat /etc/lsb-release  | grep RELEASE | cut -d "=" -f2)
IMAGE_SERVER_HOSTNAME=webserver.example.com
IMAGE_SERVER= "http:// "$IMAGE_SERVER_HOSTNAME "/ "$CUMULUS_TARGET_RELEASE ".bin "
ZTP_URL= "http:// "$IMAGE_SERVER_HOSTNAME "/ztp.sh "

if [ "$CUMULUS_TARGET_RELEASE" != "$CUMULUS_CURRENT_RELEASE" ]; then
    ping_until_reachable $IMAGE_SERVER_HOSTNAME
    /usr/cumulus/bin/onie-install -fa -i $IMAGE_SERVER -z $ZTP_URL && reboot
else
    init_ztp && reboot
fi
exit 0
```

### Apply Management VRF Configuration

If you apply a management VRF in your script, either apply it last or reboot instead. If you do *not* apply a management VRF last, you need to prepend any commands that require `eth0` to communicate out with `/usr/bin/ip vrf exec mgmt`; for example, `/usr/bin/ip vrf exec mgmt apt-get update -y`.

### Perform Ansible Provisioning Callbacks

After initially configuring a node with ZTP, use {{<exlink url="http://docs.ansible.com/ansible-tower/latest/html/userguide/job_templates.html#provisioning-callbacks" text="Provisioning Callbacks">}} to inform Ansible Tower or AWX that the node is ready for more detailed provisioning. The following example demonstrates how to use a provisioning callback:

```
/usr/bin/curl -H "Content-Type:application/json" -k -X POST --data '{"host_config_key":"'somekey'"}' -u username:password http://ansible.example.com/api/v2/job_templates/1111/callback/
```

### Disable the DHCP Hostname Override Setting

Make sure to disable the DHCP hostname override setting in your script.

```
function set_hostname(){
    # Remove DHCP Setting of Hostname
    sed s/'SETHOSTNAME="yes"'/'SETHOSTNAME="no"'/g -i /etc/dhcp/dhclient-exit-hooks.d/dhcp-sethostname
    hostnamectl set-hostname $1
}
```

## Test ZTP Scripts

Use these commands to test and debug your ZTP scripts.

You can use verbose mode to debug your script and see where your script fails. Include the `-v` option when you run ZTP:

```
cumulus@switch:~$ sudo ztp -v -r http://192.0.2.1/demo.sh
Attempting to provision via ZTP Manual from http://192.0.2.1/demo.sh

Broadcast message from root@dell-s6010-01 (ttyS0) (Tue May 10 22:44:17 2016):  

ZTP: Attempting to provision via ZTP Manual from http://192.0.2.1/demo.sh
ZTP Manual: URL response code 200
ZTP Manual: Found Marker CUMULUS-AUTOPROVISIONING
ZTP Manual: Executing http://192.0.2.1/demo.sh
error: ZTP Manual: Payload returned code 1
error: Script returned failure
```

To see results of the most recent ZTP execution, you can run the `ztp -s` command.

```
cumulus@switch:~$ ztp -s
ZTP INFO:

State              enabled
Version            1.0
Result             Script Failure
Date               Mon 20 May 2019 09:31:27 PM UTC
Method             ZTP DHCP
URL                http://192.0.2.1/demo.sh
```

If ZTP runs when the switch boots and not manually, you can run the `systemctl -l status ztp.service` then `journalctl -l -u ztp.service` to see if any failures occur:

```
cumulus@switch:~$ sudo systemctl -l status ztp.service
● ztp.service - Cumulus Linux ZTP
    Loaded: loaded (/lib/systemd/system/ztp.service; enabled)
    Active: failed (Result: exit-code) since Wed 2016-05-11 16:38:45 UTC; 1min 47s ago
        Docs: man:ztp(8)
    Process: 400 ExecStart=/usr/sbin/ztp -b (code=exited, status=1/FAILURE)
    Main PID: 400 (code=exited, status=1/FAILURE)

May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP USB: Device not found
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: Looking for ZTP Script provided by DHCP
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: Attempting to provision via ZTP DHCP from http://192.0.2.1/demo.sh
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: URL response code 200
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: Found Marker CUMULUS-AUTOPROVISIONING
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: Executing http://192.0.2.1/demo.sh
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: Payload returned code 1
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: Script returned failure
May 11 16:38:45 dell-s6010-01 systemd[1]: ztp.service: main process exited, code=exited, status=1/FAILURE
May 11 16:38:45 dell-s6010-01 systemd[1]: Unit ztp.service entered failed state.
cumulus@switch:~$
cumulus@switch:~$ sudo journalctl -l -u ztp.service --no-pager
-- Logs begin at Wed 2016-05-11 16:37:42 UTC, end at Wed 2016-05-11 16:40:39 UTC. --
May 11 16:37:45 cumulus ztp[400]: ztp [400]: /var/lib/cumulus/ztp: Sate Directory does not exist. Creating it...
May 11 16:37:45 cumulus ztp[400]: ztp [400]: /var/run/ztp.lock: Lock File does not exist. Creating it...
May 11 16:37:45 cumulus ztp[400]: ztp [400]: /var/lib/cumulus/ztp/ztp_state.log: State File does not exist. Creating it...
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Looking for ZTP local Script
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell_s6010_s1220-rUNKNOWN
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell_s6010_s1220
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP USB: Looking for unmounted USB devices
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP USB: Parsing partitions
May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP USB: Device not found
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: Looking for ZTP Script provided by DHCP
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: Attempting to provision via ZTP DHCP from http://192.0.2.1/demo.sh
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: URL response code 200
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: Found Marker CUMULUS-AUTOPROVISIONING
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: Executing http://192.0.2.1/demo.sh
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: ZTP DHCP: Payload returned code 1
May 11 16:38:45 dell-s6010-01 ztp[400]: ztp [400]: Script returned failure
May 11 16:38:45 dell-s6010-01 systemd[1]: ztp.service: main process exited, code=exited, status=1/FAILURE
May 11 16:38:45 dell-s6010-01 systemd[1]: Unit ztp.service entered failed state.
```

Instead of running `journalctl`, you can see the log history by running:

```
cumulus@switch:~$ cat /var/log/syslog | grep ztp
2016-05-11T16:37:45.132583+00:00 cumulus ztp [400]: /var/lib/cumulus/ztp: State Directory does not exist. Creating it...
2016-05-11T16:37:45.134081+00:00 cumulus ztp [400]: /var/run/ztp.lock: Lock File does not exist. Creating it...
2016-05-11T16:37:45.135360+00:00 cumulus ztp [400]: /var/lib/cumulus/ztp/ztp_state.log: State File does not exist. Creating it...
2016-05-11T16:37:45.185598+00:00 cumulus ztp [400]: ZTP LOCAL: Looking for ZTP local Script
2016-05-11T16:37:45.485084+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell_s6010_s1220-rUNKNOWN
2016-05-11T16:37:45.486394+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell_s6010_s1220
2016-05-11T16:37:45.488385+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell
2016-05-11T16:37:45.489665+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64
2016-05-11T16:37:45.490854+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp
2016-05-11T16:37:45.492296+00:00 cumulus ztp [400]: ZTP USB: Looking for unmounted USB devices
2016-05-11T16:37:45.493525+00:00 cumulus ztp [400]: ZTP USB: Parsing partitions
2016-05-11T16:37:45.636422+00:00 cumulus ztp [400]: ZTP USB: Device not found
2016-05-11T16:38:43.372857+00:00 cumulus ztp [1805]: Found ZTP DHCP Request
2016-05-11T16:38:45.696562+00:00 cumulus ztp [400]: ZTP DHCP: Looking for ZTP Script provided by DHCP
2016-05-11T16:38:45.698598+00:00 cumulus ztp [400]: Attempting to provision via ZTP DHCP from http://192.0.2.1/demo.sh
2016-05-11T16:38:45.816275+00:00 cumulus ztp [400]: ZTP DHCP: URL response code 200
2016-05-11T16:38:45.817446+00:00 cumulus ztp [400]: ZTP DHCP: Found Marker CUMULUS-AUTOPROVISIONING
2016-05-11T16:38:45.818402+00:00 cumulus ztp [400]: ZTP DHCP: Executing http://192.0.2.1/demo.sh
2016-05-11T16:38:45.834240+00:00 cumulus ztp [400]: ZTP DHCP: Payload returned code 1
2016-05-11T16:38:45.835488+00:00 cumulus ztp [400]: Script returned failure
2016-05-11T16:38:45.876334+00:00 cumulus systemd[1]: ztp.service: main process exited, code=exited, status=1/FAILURE
2016-05-11T16:38:45.879410+00:00 cumulus systemd[1]: Unit ztp.service entered failed state.
```

If you see that the issue is a script failure, you can modify the script and then run ZTP manually using `ztp -v -r <URL/path to that script>`, as above.

```
cumulus@switch:~$ sudo ztp -v -r http://192.0.2.1/demo.sh
Attempting to provision via ZTP Manual from http://192.0.2.1/demo.sh

Broadcast message from root@dell-s6010-01 (ttyS0) (Tue May 10 22:44:17 2019):  

ZTP: Attempting to provision via ZTP Manual from http://192.0.2.1/demo.sh
ZTP Manual: URL response code 200
ZTP Manual: Found Marker CUMULUS-AUTOPROVISIONING
ZTP Manual: Executing http://192.0.2.1/demo.sh
error: ZTP Manual: Payload returned code 1
error: Script returned failure
cumulus@switch:~$ sudo ztp -s
State         enabled
Version       1.0
Result        Script Failure
Date          Mon 20 May 2019 09:31:27 PM UTC
Method        ZTP Manual
URL           http://192.0.2.1/demo.sh
```

Use the following command to check `syslog` for information about ZTP:

```
cumulus@switch:~$ sudo grep -i ztp /var/log/syslog
```

## Common ZTP Script Errors

<!-- vale off -->
**Could not find referenced script/interpreter in downloaded payload**
<!-- vale on -->
```
cumulus@leaf01:~$ sudo cat /var/log/syslog | grep ztp
2018-04-24T15:06:08.887041+00:00 leaf01 ztp [13404]: Attempting to provision via ZTP Manual from http://192.168.0.254/ztp_oob_windows.sh
2018-04-24T15:06:09.106633+00:00 leaf01 ztp [13404]: ZTP Manual: URL response code 200
2018-04-24T15:06:09.107327+00:00 leaf01 ztp [13404]: ZTP Manual: Found Marker CUMULUS-AUTOPROVISIONING
2018-04-24T15:06:09.107635+00:00 leaf01 ztp [13404]: ZTP Manual: Executing http://192.168.0.254/ztp_oob_windows.sh
2018-04-24T15:06:09.132651+00:00 leaf01 ztp [13404]: ZTP Manual: Could not find referenced script/interpreter in downloaded payload.
2018-04-24T15:06:14.135521+00:00 leaf01 ztp [13404]: ZTP Manual: Retrying
2018-04-24T15:06:14.138915+00:00 leaf01 ztp [13404]: ZTP Manual: URL response code 200
2018-04-24T15:06:14.139162+00:00 leaf01 ztp [13404]: ZTP Manual: Found Marker CUMULUS-AUTOPROVISIONING
2018-04-24T15:06:14.139448+00:00 leaf01 ztp [13404]: ZTP Manual: Executing http://192.168.0.254/ztp_oob_windows.sh
2018-04-24T15:06:14.143261+00:00 leaf01 ztp [13404]: ZTP Manual: Could not find referenced script/interpreter in downloaded payload.
2018-04-24T15:06:24.147580+00:00 leaf01 ztp [13404]: ZTP Manual: Retrying
2018-04-24T15:06:24.150945+00:00 leaf01 ztp [13404]: ZTP Manual: URL response code 200
2018-04-24T15:06:24.151177+00:00 leaf01 ztp [13404]: ZTP Manual: Found Marker CUMULUS-AUTOPROVISIONING
2018-04-24T15:06:24.151374+00:00 leaf01 ztp [13404]: ZTP Manual: Executing http://192.168.0.254/ztp_oob_windows.sh
2018-04-24T15:06:24.155026+00:00 leaf01 ztp [13404]: ZTP Manual: Could not find referenced script/interpreter in downloaded payload.
2018-04-24T15:06:39.164957+00:00 leaf01 ztp [13404]: ZTP Manual: Retrying
2018-04-24T15:06:39.165425+00:00 leaf01 ztp [13404]: Script returned failure
2018-04-24T15:06:39.175959+00:00 leaf01 ztp [13404]: ZTP script failed. Exiting...
```

Errors in syslog for ZTP like those shown above often occur if you create or edit the script on a Windows machine. Check to make sure that the `\r\n` characters are *not* present in the end-of-line encodings.

Use the `cat -v ztp.sh` command to view the contents of the script and search for any hidden characters.

```
root@oob-mgmt-server:/var/www/html# cat -v ./ztp_oob_windows.sh 
#!/bin/bash^M
^M
###################^M
#   ZTP Script^M
###################^M
^M
/usr/cumulus/bin/cl-license -i http://192.168.0.254/license.txt^M
^M
# Clean method of performing a Reboot^M
nohup bash -c 'sleep 2; shutdown now -r "Rebooting to Complete ZTP"' &^M
^M
exit 0^M
^M
# The line below is required to be a valid ZTP script^M
#CUMULUS-AUTOPROVISIONING^M
root@oob-mgmt-server:/var/www/html#
```

The `^M` characters in the output of your ZTP script, as shown above, indicate the presence of Windows end-of-line encodings that you need to remove.

Use the translate (`tr`) command on any Linux system to remove the `'\r'` characters from the file.

```
root@oob-mgmt-server:/var/www/html# tr -d '\r' < ztp_oob_windows.sh > ztp_oob_unix.sh
root@oob-mgmt-server:/var/www/html# cat -v ./ztp_oob_unix.sh 
#!/bin/bash
###################
#   ZTP Script
###################
/usr/cumulus/bin/cl-license -i http://192.168.0.254/license.txt
# Clean method of performing a Reboot
nohup bash -c 'sleep 2; shutdown now -r "Rebooting to Complete ZTP"' &
exit 0
# The line below is required to be a valid ZTP script
#CUMULUS-AUTOPROVISIONING
root@oob-mgmt-server:/var/www/html#
```

## Manually Use the ztp Command
To enable ZTP, use the `-e` option:

```
cumulus@switch:~$ sudo ztp -e
```

{{%notice note%}}
When you enable ZTP, it tries to run the next time the switch boots. However, if ZTP already ran on a previous boot up or if there is a manual configuration, ZTP exits without trying to look for a script.

ZTP checks for these manual configurations when the switch boots:
- Password changes
- Users and groups changes
- Packages changes
- Interfaces changes

When the switch boots for the first time, ZTP records the state of important files that can update after you configure the switch. After a reboot, ZTP compares the recorded state to the current state of these files. If they do not match, ZTP considers the switch as already provisioned and exits. ZTP only deletes these files after a reset.
{{%/notice%}}

To reset ZTP to its original state, use the `-R` option. This removes the `ztp` directory and ZTP runs the next time the switch reboots.

```
cumulus@switch:~$ sudo ztp -R
```

To disable ZTP, use the `-d` option:

```
cumulus@switch:~$ sudo ztp -d
```

To force provisioning to occur and ignore the status listed in the configuration file, use the `-r` option:

```
cumulus@switch:~$ sudo ztp -r cumulus-ztp.sh
```

To see the current ZTP state, use the `-s` option:

```
cumulus@switch:~$ sudo ztp -s
ZTP INFO:
State          disabled
Version        1.0
Result         success
Date           Mon May 20 21:51:04 2019 UTC
Method         Switch manually configured  
URL            None
```

## Considerations

- While you are writing a provisioning script, you sometimes need to reboot the switch.
- You can use the Cumulus Linux `onie-select -i` command to reprovision the switch and install a network operating system again using ONIE.
