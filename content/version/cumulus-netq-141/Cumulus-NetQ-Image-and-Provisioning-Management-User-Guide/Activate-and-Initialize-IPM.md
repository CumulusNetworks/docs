---
title: Activate and Initialize IPM
author: Cumulus Networks
weight: 31
aliases:
 - /display/NETQ141/Activate+and+Initialize+IPM
 - /pages/viewpage.action?pageId=10453539
pageID: 10453539
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
There is no need to install the IPM software as it comes pre-installed
on the NetQ Telemetry Server when NetQ is installed. However, there are
a few simple steps needed to activate and configure the application for
your environment. These are described in this topic.

## Activation and Initialization Task Flow

The following steps are required to fully activate and perform the
initial configuration needed to run the IPM application.

{{% imgOld 0 %}}

The IPM application comes configured with the minimum DHCP configuration
and a default ONIE and ZTP script mapping. If you want to expand on the
DHCP configuration (specify an IP address pool, reservations, and
leases) or add and map additional ONIE and ZTP scripts, you can do so.
Please refer to the corresponding topics for instructions for these
tasks.

## Open VM Network Ports

The primary IPM services are located in Docker containers. They are
configured to run in network *host mode*, meaning the internal ports
they expose are bound to the VM (virtual machine) network ports. This
provides a direct path, or pass through, for traffic from the
applications and services running within the VM to the external
ecosystem where the VM is running. To ensure proper operation of the IPM
services, you must open the following ports in the VM where the IPM
services are run:

  - Ports 67 and 68: DHCP (Dynamic Host Control Protocol)
  - Port 9300: ZTP (Zero-Touch Provisioning) and ONIE (Open Network
    Installation Environment)

{{%notice note%}}

It may also be necessary to configure external firewalls and
the substrate the image runs on, such as the QEMU, VirtualBox, or VMware
hypervisors.

{{%/notice%}}

How to configure these ports is outside
the scope of this document.

## Start the Image and Provisioning Management Application

The application is activated in a similar manner as most UNIX services,
using the `systemctrl` command to start the application service.

To start the IPM application and all of its services:

1.  Log in to the NetQ Telemetry Server.

2.  Start the application using the `start` option of the `systemctrl`
    command using root-level credentials or using the `sudo` command.

3.  Configure the application to start on subsequent boots using the
    `enable` option of the command.

4.  Verify the application is running using the `status` option of the
    command.

        <machine-name>:~<username>$ ssh cumulus@<telemetry-server-name-or-ip-address>   
        cumulus@ts:~$ sudo systemctl start tips-appliance
         
        cumulus@ts:~$ sudo systemctl enable tips-appliance  
        Created symlink from /etc/systemd/system/multi-user.target.wants/tips-appliance.service to /lib/systemd/system/tips-appliance.service.

        cumulus@oob-mgmt-server:~$ sudo systemctl status tips-appliance
        ● tips-appliance.service - tips Backend
           Loaded: loaded (/lib/systemd/system/tips-appliance.service; enabled)
           Active: active (running) since Wed 2018-09-12 20:06:45 UTC; 1min 59s ago
         Main PID: 16909 (docker-compose)
           CGroup: /system.slice/tips-appliance.service
                   └─16909 /opt/venvs/cl-docker-compose/bin/python /usr/sbin/docker-compose -p tips -f /etc/tips/docker/tips-compose.yml up --no-color

Once the IPM application is running, the IPM Command Line Interface,
*TIPCTL*, is available. TIPCTL is the key user interface used to
activate, configure, and monitor the IPM application and services.

## Perform Initial Configuration

The next step in setting up IPM is to use TIPCTL to configure key
application and service parameters. Configuration is performed using the
`tipctl config` command, which can be run in one of two modes:
traditional command line or prompt. Prompt mode provides the user with
the steps and choices needed to perform the configuration. The command
line mode requires the user to know what commands to execute and the
appropriate parameter values. Either mode effectively completes the
initial configuration of the IPM server.

Running the configuration setup sequence:

  - Configures the KEA service with the network interface to bind to and
    the IP address to use to serve up the default-url and the
    cumulus-provision-url
  - Causes the KEA service to create either one or two subnet pools
    based on the designated IP address of the server (if it is in the
    middle of the address range, two pools are created, each excluding
    the server IP address)

### Use Prompt Mode

To perform the initial configuration in prompt mode:

1.  Run configuration setup and follow the prompts.

2.  Accept the default eth0 address as the port for the DHCP to listen
    on (as shown in the example here) or select another interface using
    the Up and Down Arrows on your keyboard. The selected address is
    highlighted in blue. Press Return. The application completes the
    configuration and returns you to the command line prompt.

3.  Confirm the status of the IPM application.

        cumulus@ts:~$ tipctl config setup
        [?] Select local network configuration: eth0:10.255.0.92
         > eth0:10.255.0.92
           eth1:192.168.0.254
           Quit
         
        Using eth0 10.255.0.92 to finish the configuration
         
        cumulus@ts:~$ tipctl config verify
        The TIPS application is running as expected. 

    If the application is not running as expected, the output indicates
    the problem. For example:  

        cumulus@ts:~$ tipctl config verify
        Status      Service
        ----------  ---------
        restarting  DHCP missing     
         
        DB Status   Issue
        --------    --------------------------
        error       Cannot connect to backend.

### Use Command Line Mode

To perform the initial configuration in traditional command line mode:

1.  Specify the interface OR the IP address on which the server should
    listen.

2.  Confirm the status of the IPM application.

        cumulus@ts:~$ tipctl config setup --interface eth1
        Using eth1 192.168.0.254 to finish the configuration
         
        cumulus@ts:~$ tipctl config setup --ip 10.255.0.92
        Using eth0 10.255.0.92 to finish the configuration
         
        cumulus@ts:~$ tipscl config verify
        The TIPS application is running as expected.
