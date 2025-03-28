---
title: NVIDIA Cumulus NetQ 4.0 Release Notes
author: NVIDIA
weight: 30
product: Cumulus NetQ
version: "4.0"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-40" >}}
## 4.0.1 Release Notes
### Open Issues in 4.0.1

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="2893000"></a> [2893000](#2893000) <a name="2893000"></a> <br /> | CVE-2021-44228: Apache Log4j2 <=2.14.1 JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. | 2.4.0-4.0.1 | 4.1.0-4.13.0|
| <a name="2843640"></a> [2843640](#2843640) <a name="2843640"></a> <br /> | In NetQ clustered environments, the network snapshot feature may fail. | 4.0.0-4.1.1 | 4.2.0-4.13.0|
| <a name="2817749"></a> [2817749](#2817749) <a name="2817749"></a> <br /> | If you configure an event suppression rule with <code>is_active false</code>, the event will no longer be displayed with the <code>netq show events-config</code> command. | 4.0.1-4.2.0 | 4.3.0-4.13.0|
| <a name="2815596"></a> [2815596](#2815596) <a name="2815596"></a> <br /> | The NetQ Cloud VM for KVM hypervisors installer and opta-check fail because the minimum disk requirements do not meet the default image settings. To work around this issue, increase the disk space from 32GB to 64GB before you run the <code>netq bootstrap</code> command<br />1. Check the size of the existing hard disk in the VM to confirm it is 32 GB. In this example, the number of 1 MB blocks is 31583, or 32 GB<br />	<pre>cumulus&#64;netq-401-cloud:~$ df -hm /	Filesystem     1M-blocks  Used Available Use% Mounted on	/dev/vda1          31583  1192     30375   4% /</pre>2. Shutdown the VM<br /><br>3. Check the size of the existing disk on the server hosting the VM to confirm it is 32 GB. In this example, the size appears in the virtual size field:	<pre>root&#64;server:/var/lib/libvirt/images# qemu-img info netq-4.0.1-ubuntu-18.04-tscloud-qemu.qcow2	image: netq-4.0.1-ubuntu-18.04-tscloud-qemu.qcow2	file format: qcow2	virtual size: 32G (34359738368 bytes)	disk size: 1.3G	cluster_size: 65536	Format specific information:	    compat: 1.1	    lazy refcounts: false	    refcount bits: 16	    corrupt: false</pre>4. Add 32 GB to the image:	<pre>root&#64;server:/var/lib/libvirt/images# qemu-img resize netq-4.0.1-ubuntu-18.04-tscloud-qemu.qcow2 +32G	Image resized.</pre>5. Verify the change<br />	<pre>root&#64;server:/var/lib/libvirt/images# qemu-img info netq-4.0.1-ubuntu-18.04-tscloud-qemu.qcow2	image: netq-3.1.0-ubuntu-18.04-tscloud-qemu.qcow2	file format: qcow2	virtual size: 64G (68719476736 bytes)	disk size: 1.3G	cluster_size: 65536	Format specific information:	    compat: 1.1	    lazy refcounts: false	    refcount bits: 16	    corrupt: false</pre>6. Start the VM and log back in<br />7. Run the following commands on the partition, referencing the filesystem /dev/vda1 obtained in step 1:	<pre>cumulus&#64;netq-401-cloud:~$ sudo growpart /dev/vda 1	CHANGED: partition=1 start=227328 old: size=66881503 end=67108831 new: size=133990367,end=134217695	cumulus&#64;netq-401-cloud:~$ sudo resize2fs /dev/vda1	resize2fs 1.44.1 (24-Mar-2018)	Filesystem at /dev/vda1 is mounted on /; on-line resizing required	old_desc_blocks = 4, new_desc_blocks = 8	The filesystem on /dev/vda1 is now 16748795 (4k) blocks long.</pre>8. Verify the disk is now configured with 64 GB. In this example, the number of 1 MB blocks is now 63341, or 64 GB:	<pre>cumulus&#64;netq-401-cloud:~$ df -hm /	Filesystem     1M-blocks  Used Available Use% Mounted on	/dev/vda1          63341  1193     62132   2% /</pre> | 4.0.1-4.1.1 | 4.2.0-4.13.0|
| <a name="2711101"></a> [2711101](#2711101) <a name="2711101"></a> <br /> | When RoCE (RDMA over Converged Ethernet) data collection is enabled in Cumulus Linux 4.3.z and 4.4.z, you can experience high dual uplink convergence times<br />To work around this issue, disable RoCE monitoring:1. Edit '/etc/netq/commands/cl4-netq-commands.yml' and comment out the following lines:<br />       #- period: "60"<br />       #  key: "roce"<br />       #  isactive: true<br />       #  command: "/usr/lib/cumulus/mlxcmd --json roce counters"<br />       #  parser: "local"2. Delete the '/var/run/netq/netq_commands.yml' file:<br />       $ sudo rm /var/run/netq/netq_commands.yml3. Restart the NetQ agent:<br />      $ netq config agent restart | 4.0.0-4.1.1 | 4.2.0-4.13.0|
| <a name="2690469"></a> [2690469](#2690469) <a name="2690469"></a> <br /> | While upgrading an on-premises deployment from version 2.4.x to 3.x.y then to 4.x, the upgrade fails during the NetQ application stage<br />To work around this issue, run the following command on the NetQ telemetry server, then start the upgrade again:'netq install opta activate-job config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIiw3T2sweW9kR3Y4Wk9sTHU3MkwrQTRjNkhhQkU3bVpBNVlZVjEvWWgyZGJBPQ==' | 3.2.1-4.0.1 | 4.1.0-4.13.0|

### Fixed Issues in 4.0.1
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |

## 4.0.0 Release Notes
### Open Issues in 4.0.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="2893000"></a> [2893000](#2893000) <a name="2893000"></a> <br /> | CVE-2021-44228: Apache Log4j2 <=2.14.1 JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. | 2.4.0-4.0.1 | 4.1.0-4.13.0|
| <a name="2843640"></a> [2843640](#2843640) <a name="2843640"></a> <br /> | In NetQ clustered environments, the network snapshot feature may fail. | 4.0.0-4.1.1 | 4.2.0-4.13.0|
| <a name="2711101"></a> [2711101](#2711101) <a name="2711101"></a> <br /> | When RoCE (RDMA over Converged Ethernet) data collection is enabled in Cumulus Linux 4.3.z and 4.4.z, you can experience high dual uplink convergence times<br />To work around this issue, disable RoCE monitoring:1. Edit '/etc/netq/commands/cl4-netq-commands.yml' and comment out the following lines:<br />       #- period: "60"<br />       #  key: "roce"<br />       #  isactive: true<br />       #  command: "/usr/lib/cumulus/mlxcmd --json roce counters"<br />       #  parser: "local"2. Delete the '/var/run/netq/netq_commands.yml' file:<br />       $ sudo rm /var/run/netq/netq_commands.yml3. Restart the NetQ agent:<br />      $ netq config agent restart | 4.0.0-4.1.1 | 4.2.0-4.13.0|
| <a name="2690469"></a> [2690469](#2690469) <a name="2690469"></a> <br /> | While upgrading an on-premises deployment from version 2.4.x to 3.x.y then to 4.x, the upgrade fails during the NetQ application stage<br />To work around this issue, run the following command on the NetQ telemetry server, then start the upgrade again:'netq install opta activate-job config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIiw3T2sweW9kR3Y4Wk9sTHU3MkwrQTRjNkhhQkU3bVpBNVlZVjEvWWgyZGJBPQ==' | 3.2.1-4.0.1 | 4.1.0-4.13.0|

### Fixed Issues in 4.0.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="2611898"></a> [2611898](#2611898) <a name="2611898"></a> <br /> | Fixed an issue where deleting a snapshot does not remove the snapshot card from the workbench. However, the workbench might refresh before the deleted snapshot’s card is removed. During the refresh, you may notice a brief flashing. This is expected behavior and you can safely ignore the flashing. |  | |
| <a name="2556754"></a> [2556754](#2556754) <a name="2556754"></a> <br /> | netq-agent installed on Cumulus Linux might slowly leak memory during sustained layer two network events at high scale. | 3.3.0-3.3.1 | |
| <a name="2555197"></a> [2555197](#2555197) <a name="2555197"></a> <br /> | NetQ CLI: Occasionally, when a command response contains a large number of objects to be displayed the NetQ CLI does not display all results in the console. When this occurs, view all results using the <code>json</code> format option. | 3.3.0-3.3.1 | |
| <a name="2553453"></a> [2553453](#2553453) <a name="2553453"></a> <br /> | The <code>netqd</code> daemon logs a traceback to _/var/log/netqd.log_ when the OPTA server is unreachable and <code>netq show</code> commands are run. | 3.1.0-3.3.1 | |
| <a name="2549319"></a> [2549319](#2549319) <a name="2549319"></a> <br /> | NetQ UI: The legend and segment colors on Switches and Upgrade History card graphs sometimes do not match. These cards appear on the lifecycle management dashboard (Manage Switch Assets view). Hover over graph to view the correct values. | 3.0.0-3.3.1 | |

