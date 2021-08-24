---
title: Linux for Networking Quick Start Cheat Sheet
author: NVIDIA
weight: 20
toc: 4
---
Using Linux for networking completely unifies the network stack. The switch from traditional networking operating systems is easy and can be done with existing skill sets.</br> This handy cheat sheet is a quick reference as you learn and use NVIDIA® Cumulus® Linux. It features the most common native Linux, as well as Cumulus NVUE, commands with explanations on how to use them.

## Common Linux Commands

<table>
    <tr>
        <td>
        <b>sudo</b>
        <code><i>command</i></br></code>
        <i>Run a command in root</i>
        </td>
        <td>
        <b>man</b>
        <code><i>program</i></br></code>
        <i>Display help menu for program</i>
        </td>
        <td>
        <b>kill</b>
        <code><i>PID</i></br></code>
        <i>Halt process by process-id</i>
        </td>
        <td>
        <b>killall</b>
        <code><i>proccess_name</i></br></code>
        <i>Halt any processes based on a name</i>
        </td>       
    </tr>
    <tr>
        <td>
        <b>history</br></b>
        <i>Display recently entered commands</i>
        </td>    
        <td>
        <b>sudo reboot</br></b>
        <i>Reboot the switch immediately</i>
        </td>   
        <td>
        <code><i>command</i></code>
        <b>-h</br></b>
        <i>Display commands help menu</i>
        </td>
        <td>
        <code><i>command</i></code>
        <b>&</br></b>
        <i>Send command execution to the background </br>(use “fg” to send command to the foreground)</i>
        </td>
    </tr>
</table>

## Linux User Administration Commands

<table>
    <tr>
        <td>
        <b>sudo adduser</b>
        <code><i>username</i></br></code>
        <i>Add a user</i>
        </td>
        <td>
        <b>sudo userdel -r</b>
        <code><i>username</i></br></code>
        <i>Delete a user</i>
        </td>
        <td>
        <b>sudo passwd</b>
        <code><i>username</i></br></code>
        <i>Change a user password</i>
        </td>
        <td>
        <b>sudo passwd -l</b>
        <code><i>username</i></br></code>
        <i>Disable a user</i>
        </td>   
        <td>
        <b>id</b>
        <code><i>username</i></br></code>
        <i>Display user information</i>
        </td>    
    </tr>
    <tr>
        <td>
        <b>who</br></b>
        <i>Display all logged-in users and their activity</i>
        </td>     
        <td>
        <b>whoami</br></b>
        <i>Display the current logged-in user</i>
        </td>   
        <td>
        <b>su</b>
        <code><i>username</i></br></code>
        <i>Switch user</i>
        </td>
        <td>
        <b>last</br></b>
        <i>Display last login of a user(s)</i>
        </td>   
        <td>
        <b>exit</br></b>
        <i>Logout of the current session</i>
        </td>   
    </tr>
</table>

## Linux Monitoring and Troubleshooting Commands

<table>
    <tr>
        <td>
        <b>top</br></b>
        <i>View real-time CPU/memory info</i>
        </td>
        <td>
        <b>free -m</br></b>
        <i>Show free memory in MB</i>
        </td>
        <td>
        <b>ps aux</br></b>
        <i>Show all running processes</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>uptime</br></b>
        <i>Display uptime info</i>
        </td>   
        <td>
        <b>nslookup</b>
        <code><i>hostname</i></br></code>
        <i>Perform DNS lookup</i>
        </td>
        <td>
        <b>ntpq -pn</br></b>
        <i>Perform ntp query</i>
        </td>    
    </tr>
    <tr>
        <td>
        <b>date</br></b>
        <i>Print the current date and time</i>
        </td>     
        <td>
        <b>tcpdump -i</b>
        <code><i>interface</i></br></code>
        <i>Collect control plane traffic from an interface</i>
        </td> 
        <td>
        <b>clear</br></b>
        <i>Clear a command-line screen</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>smonctl -v</br></b>
        <i>Show PSU/FAN/Temp information</i>
        </td>   
        <td>
        <b>ping</b>
        <code><i>ip_address</i></br></code>
        <i>Check connectivity status to remote IP</i>
        </td>
        <td>
        <b>sudo cl-support</br></b>
        <i>Create an archive file for troubleshooting. </br>A tar file will be created in the /var/support/ directory.</i>
        </td>  
    </tr>
</table>

## Working with Files and Folders

<table>
    <tr>
        <td>
        <b>nano</b>
        <code><i>file_name</i></br></code>
        <i>Edit a text file</i>
        </td>
        <td>
        <b>tree</br></b>
        <i>Show filesystem hierarchy</i>
        </td>
        <td>
        <b>pwd</br></b>
        <i>Print current folder name</i>
        </td>
        <td>
        <b>head -n 5</b>
        <code><i>file_name</i></br></code>
        <i>Display top 5 lines of a file</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>tail -n 5</b>
        <code><i>file_name</i></br></code>
        <i>Display last 5 lines of a file</i>
        </td>
        <td>
        <b>tail -f</b>
        <code><i>file_name</i></br></code>
        <i>Follow file and disaplay new lines</i>
        </td>
        <td>
        <b>mkdir</b>
        <code><i>folder</i></br></code>
        <i>Make new folder</i>
        </td>
        <td>
        <b>cd</b>
        <code><i>folder</i></br></code>
        <i>Change into different folder</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>ls -lha</br></b>
        <i>List the files in the current folder</i>
        </td>
        <td>
        <b>find / -name</b>
        <code><i>file_name</i></br></code>
        <i>Find file named <code>file_name</code></i>
        </td>
        <td>
        <b>find / -name</b>
        <code><i>"string"</i></br></code>
        <i>Find file_name containing <code>string</code></i>
        </td>
        <td>
        <b>chmod 777</b>
        <code><i>file_name</i></br></code>
        <i>Change file permissions to all</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>mv</b>
        <code><i>old_file</i></code>
        <code><i>new_file</i></br></code>
        <i>Move/rename a file</i>
        </td>
        <td>
        <b>cp</b>
        <code><i>old_file</i></code>
        <code><i>new_file</i></br></code>
        <i>Copy a file</i>
        </td>
        <td>
        <b>rm</b>
        <code><i>file_name</i></br></code>
        <i>Delete a file</i>
        </td>
        <td>
        <b>chown</b>
        <code><i>username</i></code>
        <code><i>file_name</i></br></code>
        <i>Change file ownership</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>grep</b>
        <code><i>"string"</i></code>
        <code><i>file_name</i></br></code>
        <i>Search file for a text <code>string</code></i>
        </td>
        <td>
        <b>touch</b>
        <code><i>file_name</i></br></code>
        <i>Create a new file</i>
        </td>
        <td>
        <b>cat</b>
        <code><i>file_name</i></br></code>
        <i>Display a text file</i>
        </td>
        <td>
        <code><i>command</i></code>
        <b>></b>
        <code><i>new_file</i></br></code>
        <i>Redirect stadndard command output to a file.</br> e.g. <code>ip link show > ip_addr_output</code></i>
        </td>
    </tr>
    <tr>
        <td colspan="2">
        <b>cat</b>
        <code><i>/path/file_name</i></code>
        <b>| grep</b>        
        <code><i>"string"</i></code>
        <b>></b>
        <code><i>new_file</br></i></code>
        <i>Filter one program’s/files output to a file.</br> e.g. <code>cat /var/log/syslog | grep kernel > syslog_kernel_output</code></i>
        </td>
        <td colspan="2">
        <code><i>command</i></code>
        <b>& ></b>
        <code><i>new_file</i></br></code>
        <i>Redirect stadndard command output and Standard error to a file.</br> e.g. <code>ifreload -a & > ifreload_output</code></i>
        </td>
    </tr>
    </tr>
</table>

## NVUE (NVIDIA User Experience) General Commands

<table>
    <tr>
        <td>
        <b>nv list-commands</br></b>
        <i>List all NVUE commands</i>
        </td>
        <td>
        <b>nv show</b>
        <i><code>[options]</code> <code>attribute</br></code></i>
        <i>Show system configuration</i>
        </td>
        <td>
        <b>nv set</b>
        <code><i>attribute</i></br></code>
        <i>Modify system configurations</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>nv unset</b>
        <code><i>attribute</i></br></code>
        <i>Remove system configurations attribute</i>
        </td>
        <td>
        <b>nv config</b>
        <code><i>command</i></br></code>
        <i>Manage/Apply system configurations</i>
        </td>
        <td>
        <b>nv</b>
        <code><i>command</i></code>
        <b>-h</br></b>
        <i>Show command usage with all its options and attributes </i>
        </td>
    </tr>
</table>

## System Software and Hardware Commands

<table>
    <tr>
        <td>
        <b>sudo -E apt list</b>
        <code><i>package_name</i></br></code>
        <i>Show the list of packages based on package name</br> (all if <code>package_name</code> not specified)</i>
        </td>
        <td>
        <b>sudo -E apt-get install</b>
        <code><i>package_name</i></br></code>
        <i>Install a package from the repository</i>
        </td>
        <td>
        <b>sudo -E apt-get update</br></b>
        <i>Update software packages to latest versions</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>sudo apt-cache search</b>
        <code><i>string</i></br></code>
        <i>Look for packages containing <code>string</code></i>
        </td>
        <td>
        <b>sudo systemctl</b>
        <code><i>[start|stop|restart|reload]</code> <code>program</code><b>.service</b></br></i>
        <i>Control current execution of a service</i>
        </td>
        <td>
        <b>sudo systemctl</b>
        <code><i>[enable|disable]</code> <code>program</code><b>.service</b></br></i>
        <i>Set/unset a service to start on system boot</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>cat /etc/image-release</br></b>
        <i>Show precise software version</i>
        </td>
        <td>
        <b>nv show system global</br></b>
        <i>Show switch global configuration</i>
        </td>
        <td>
        <b>nv show platform software installed</b>
        <code><i>package_name</code></br></i>
        <i>Show a specific installed software package on the switch</br> (all if <code>package_name</code> not specified)</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>nv show platform capabilities</br></b>
        <i>Show switch hardware information</i>
        </td>
        <td>
        <b>nv show platform hardware</b>
        <code><i>component_device</code></br></i>
        <i>Show switch hardware information</i>
        </td>
        <td>
        <b>nv show platform hardware component device fan</br></b>
        <i>Show switch PSU/FAN/Temp information</i>
        </td> 
    </tr>
</table>

## Working with Interfaces 

### Using Linux Commands

<table>
    <tr>
        <td>
        <b>ip addr show</b>
        <code><i>interface</i></br></code>
        <i>Layer 2 and 3 interface status</i>
        </td>
        <td>
        <b>cl-netstat</br></b>
        <i>Display interfaces counters</i>
        </td>
        <td>
        <b>ifup</b>
        <code><i>interface</i></br></code>
        <i>Set port admin UP</i>
        </td>
        <td>
        <b>ifdown</b>
        <code><i>interface</i></br></code>
        <i>Set port admin DOWN</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>ifreload -a</br></b>
        <i>Apply interface configuration changes</i>
        </td>
        <td>
        <b>ip addr set</b>
        <code><i>ip_address/mask</i></code>
        <b>dev</b>
        <code><i>interface</br></i></code>
        <i>Set IP address and mask to an interface</i>
        </td>
        <td>
        <b>ifquery -s</br></b>
        <i>Show ALL interface keywords</i>
        </td>
        <td>
        <b>ifquery -a</br></b>
        <i>Show interfaces config (to be applied)</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>ethtool</b>
        <code><i>interface</i></br></code>
        <i>Show transceiver information</i>
        </td>
        <td>
        <b>ethtool -S</b>
        <code><i>interface</i></br></code>
        <i>Show port statistics</i>
        </td>
        <td>
        <b>ethtool -s</b>
        <code><i>interface</i></code>
        <b>speed</b>
        <code><i>speed</i></br></code>
        <i>Set physical interface's speed</i>
        </td>
        <td>
        <b>ip monitor link</br></b>
        <i>Monitor changes to link state in real time</i>
        </td>
    </tr>
    </tr>
</table>

### Using NVUE Commands

<table>
    <tr>
        <td>
        <b>nv show interface</br></b>
        <i>High-level interfaces status</i>
        </td>
        <td>
        <b>nv show interface</b>
        <code><i>interface</i></br></code>
        <i>Detailed interface status and counters</i>
        </td>
        <td>
        <b>nv set interface</b>
        <code><i>interface</i></code>
        <b>link state down</br></b>
        <i>Administratively disable physical port</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>nv set interface</b>
        <code><i>interface</i></code>
        <b>link state up</br></b>
        <i>Administratively enable physical port </br> (by default all ethernet ports are disabled)</i>
        </td>
        <td>
        <b>nv set interface</b>
        <code><i>interface</i></code>
        <b>ip address</b>
        <code><i>ip_address/mask</br></i></code>
        <i>Set IP address to physical layer 3 port or loopback</i>
        </td>
        <td>
        <b>nv set</b>
        <code><i>interface</i></code>
        <b>bridge domain br_default</br></b>
        <i>Creates a default bridge and sets physical port/s as its member</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>nv unset interface</b>
        <code><i>interface</i></code>
        <b>ip address</br></b>
        <i>Unset IP address from an inteface (SVI/layer 3/Lo)</i>
        </td>
        <td>
        <b>nv set interface vlan</b>
        <code><i>vlan_id</i></code>
        <b>ip address</b>
        <code><i>ip_address/mask</br></i></code>
        <i>Create and set IP address to logical layer 3 port (SVI)</i>
        </td>
        <td>
        <b>nv set interface</b>
        <code><i>bond0</i></code>
        <b>bond member</b>
        <code><i>interface(s)</br></i></code>
        <i>Create bond(LAG) interface and set physical member(s) into it</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>nv set interface</b>
        <code><i>interface</i></code>
        <b>link speed</b>
        <code><i>speed</br></i></code>
        <i>Set physical interface's speed</i>
        </td>
        <td>
        <b>nv show interface</b>
        <code><i>interface</i></code>
        <code><i>[attribute]</br></i></code>
        <i>Show interface's configuration</i>
        </td>
        <td>
        <b>nv set interface</b>
        <code><i>interface</i></code>
        <b>link breakout</b>
        <code><i>breakout_options</br></i></code>
        <i>Breakout physical interfaces according to the supported options</i>
        </td>
    </tr>
    </tr>
</table>

## Important Log Files

<table>
    <tr>
        <td>
        <b>cat /var/log/apt</br></b>
        <i>Logs for apt utility</i>
        </td>
        <td>
        <b>cat /var/log/audit/*</br></b>
        <i>Logs for auditd service</i>
        </td>
        <td>
        <b>cat /var/log/syslog </br></b>
        <i>The main system log</i>
        </td>
        <td>
        <b>cat /var/log/clagd</br></b>
        <i>Logs status of the clagd service</i>
        </td>
    </tr>    
    <tr>
        <td>
        <b>cat /var/log/frr/frr.log</br></b>
        <i>Location of the FRRouting log (if enabled)</i>
        </td>
        <td>
        <b>cat /var/log/rdnbrd.log</br></b>
        <i>Logs for redistribute neighbor</i>
        </td>
        <td>
        <b>cat /var/log/netd.log</br></b>
        <i>Log file for NVUE</i>
        </td>
        <td>
        <b>cat /var/log/ptmd</br></b>
        <i>Logs file for ptmd service</i>
        </td>
    </tr>    
    <tr>
        <td>
        <b>cat /var/log/switchd.log </br></b>
        <i>The HAL log for NVIDIA Cumulus Linux</i>
        </td>
        <td colspan="2">
        <b>cat /var/log/autoprovision</br></b>
        <i>Logs output generated by running the ZTP script</i>
        </td>
        <td colspan="2">
        <b>cat /var/log/dpkg.log</br></b>
        <i>Log file for packages added or removed using dpkg command</i>
        </td>
    </tr>    
    <tr>
        <td colspan="2">
        <b>cat /var/log/installer/*</br></b>
        <i>Directory containing files related to the NVIDIA Cumulus Linux installation</i>
        </td>
        <td colspan="2">
        <b>dmesg</br></b>
        <i>(driver message) is a command that prints the message buff of the kernel </i>
        </td>
    </tr>
</table>

## Configuration Management with NVUE Commands

<table>
    <tr>
        <td>
        <b>nv config apply</br></b>
        <i>Applies the pending configuration</i>
        </td>
        <td>
        <b>nv config detach</br></b>
        <i>Detaches the configuration from the current pending</i>
        </td>
    </tr>
    <tr>
        <td colspan="2">
        <b>nv config save</br></b>
        <i>Overwrites startup configuration with the applied configuration (writes to <code>/etc/nvue.d/startup.yaml</code>). This configuration persists after reboot.</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>nv config diff</b>
        <code><i>revision_1</i></code>
        <code><i>revision_2</i></br></code>
        <i>Compares between two configuration types (e.g. <code>pending</code> vs. <code>applied</code>)</i>
        </td>
        <td>
        <b>nv config history</b>
        <code><i>nvue-file</code></br></i>
        <i>Shows applied configuration history for the revision</i>
        </td>
    </tr>
    <tr>
        <td>
        <b>nv config patch</b>
        <code><i>nvue-file</code></br></i>
        <i>Updates pending configuration with a YAML file</i>
        </td>
        <td>
        <b>nv config replace</b>
        <code><i>nvue-file</code></br></i>
        <i>Replaces pending configuration with a YAML file</i>
        </td>
    </tr>
</table>