---
title: Configure the interfaces File with a Bash Script
author: NVIDIA
weight: 412
toc: 4
---

While the long term strategy for many data centers is to automate the configuration of Cumulus Networks switches, this is often overkill for smaller environments.

However, manually adding all of the switch ports to the configuration file can be a painfully dreary task. So it's a good thing NCLU supports {{<kb_link url="cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/#use-globs-for-port-lists" text="globs">}} so you can use one to quickly define a range or ports.

But if you're old school and want to use the tools available through the native Bash shell, this article shows you how to quickly add the switch ports using a Bash script.

1.  Determine the switch port identifiers on your device using the `ip link show` command:

        cumulus@switch$ ip link show
        1:  lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN mode DEFAULT
            link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        2:  eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 1000
            link/ether 08:9e:01:f8:9b:ac brd ff:ff:ff:ff:ff:ff
        3:  swp1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT qlen 500
            link/ether 08:9e:01:f8:9b:af brd ff:ff:ff:ff:ff:ff
        ...
        53: swp51: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT qlen 500
            link/ether 08:9e:01:f8:9b:df brd ff:ff:ff:ff:ff:ff
        54: swp52: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT qlen 500
            link/ether 08:9e:01:f8:9b:e0 brd ff:ff:ff:ff:ff:ff

    For this device, you will have to configure swp1 through swp52.

2.  Back up the current `/etc/network/interfaces` file:

        cumulus@switch$ sudo cp /etc/network/interfaces /etc/network/interfaces.orig

    This step is an insurance policy in case you accidentally corrupt the file you are trying to update.

3.  Create the script in the *cumulus* user home directory. Substitute the highest-numbered swp on your switch for the number on the line starting with `while`.

        cumulus@switch$ vi populate.sh

        #!/bin/bash

        mycount=1

        while (( $mycount <= 52 ))
        do
        echo  >> /etc/network/interfaces
        echo auto swp$mycount >> /etc/network/interfaces
        echo iface swp$mycount >> /etc/network/interfaces
        ((mycount++))
        done

    {{%notice note%}}

The spacing and special characters must be followed exactly or the script could corrupt your `/etc/network/interfaces` file. (Aren't you glad you made a copy in step 2?)

{{%/notice%}}

4.  Run the script using `sudo`, then apply the changes:

        cumulus@switch$ chmod 744 populate.sh
        cumulus@switch$ sudo bash populate.sh
        cumulus@switch$ cat /etc/network/interfaces
        # This file describes the network interfaces available on your system
        # and how to activate them. For more information, see interfaces(5), ifup(8)
        #
        # Please see /usr/share/doc/python-ifupdown2/examples/ for examples
        #
        #

        # The loopback network interface
        auto lo
        iface lo inet loopback

        # The primary network interface
        auto eth0
        iface eth0 inet dhcp

        auto swp1
        iface swp1
        ...

        auto swp52
        iface swp52

        cumulus@switch$ sudo ifreload -a

5.  Verify that the ports are active using the `ip link show` command:

        cumulus@switch$ ip link show
        1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN mode DEFAULT
            link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 1000
            link/ether 08:9e:01:f8:9b:ac brd ff:ff:ff:ff:ff:ff
        3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
           link/ether 08:9e:01:f8:9b:af brd ff:ff:ff:ff:ff:ff
        ...
        53: swp51: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
           link/ether 08:9e:01:f8:9b:df brd ff:ff:ff:ff:ff:ff
        54: swp52: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
           link/ether 08:9e:01:f8:9b:e0 brd ff:ff:ff:ff:ff:ff

## Bonus Section: How this Script Works

The script in step 3 works as written &mdash; just copy it onto your switch (adjusting the number of the highest numbered swp) and it just works. But if you want to start learning Bash scripting, let's take a look at the script line by line.

{{%notice tip%}}

There are multiple ways to accomplish the tasks described in shell scripting. This example uses my preferred methods &mdash; consult other resources (for example, {{<exlink url="http://www.cyberciti.biz/faq/category/bash-shell/" text="nixCraft">}}) for a more complete discussion of scripting tools.

{{%/notice%}}

     #!/bin/bash

This statement tells the script which shell (command interpreter) should be used to run it. Typically the # character denotes a comment but here it actually passes information to the script.

     mycount=1

The script will use a counter to cycle through the swp interfaces. Here we set the variable named *mycount* with the initial value of 1.

    while (( $mycount <= 52 ))

The while statement indicates a loop which continues to run as long as the specified condition is true. All commands contained between the *do* and *done* statements are performed on each pass of the loop.

The double parentheses contain a conditional check. Using the $ character substitutes in the current value of the variable it precedes &mdash; in this case *mycount*. This line checks whether the counter is greater than or equal to the highest port ID on our switch.

{{%notice note%}}

The white space in this line is critical &mdash; the notation used does not work if the spacing is not correct.

{{%/notice%}}

    echo  >> /etc/network/interfaces
    echo auto swp$mycount >> /etc/network/interfaces
    echo iface swp$mycount >> /etc/network/interfaces

The `echo` command typically prints any arguments directly to the screen. The addition of the \>\> characters redirects that output and appends it to the end of the specified file. Be careful; a single \> character will **overwrite** the file rather than adding to the end of it.

This block of code adds a blank line, followed by the standard auto and iface statements while substituting in the current value of the *mycount* variable to generate the swp interface name.

    ((mycount++))

This is the most critical part of this while loop. If the counter is not incremented, the loop will not exit automatically because the conditional check will never change.
