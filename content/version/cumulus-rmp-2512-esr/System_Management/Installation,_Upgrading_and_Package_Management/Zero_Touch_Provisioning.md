---
title: Zero Touch Provisioning
author: Cumulus Networks
weight: 135
aliases:
 - /display/RMP25ESR/Zero+Touch+Provisioning
 - /pages/viewpage.action?pageId=5116322
pageID: 5116322
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
*Zero *touch provisioning** allows devices to be quickly deployed in
large-scale environments. Data center engineers only need to rack and
stack the switch, connect it to the management network, then install
Cumulus RMP via ONIE; the initial configuration gets invoked via ZTP.
Alternatively, you can insert a USB stick with the configuration so the
provisioning process can start automatically.

The provisioning framework allows for a one-time, user-provided script
to be executed. This script can be used to add the switch to a
configuration management (CM) platform such as
[puppet](http://puppetlabs.com/puppet/what-is-puppet),
[Chef](http://www.opscode.com), [CFEngine](https://cfengine.com), or
even a custom, home-grown tool.

In addition, you can use the `autoprovision` command in Cumulus RMP to
invoke your provisioning script.

Provisioning initially takes place over the management network and is
initiated via a DHCP hook. A DHCP option is used to specify a
configuration script. This script is then requested from the Web server
and executed locally on the switch.

(Click to expand)

## <span>Commands</span>

  - autoprovision

## <span>Zero Touch Provisioning Process</span>

The zero touch provisioning process involves these steps:

1.  The first time you boot Cumulus RMP, eth0 is configured for DHCP and
    makes a DHCP request.

2.  The DHCP server offers a lease to the switch.

3.  If option 239 is present in the response, the zero touch
    provisioning process itself will start.

4.  The zero touch provisioning process requests the contents of the
    script from the URL, sending additional [HTTP
    headers](#src-5116322_ZeroTouchProvisioning-http_headers) containing
    details about the switch.

5.  The script’s contents are parsed to ensure it contains the
    ` CUMULUS-AUTOPROVISIONING  `flag.

6.  If the ` CUMULUS-AUTOPROVISIONING  `flag is present, then the script
    executes locally on the switch.

7.  The return code of the script gets examined. If it is 0, then the
    provisioning state is marked as complete.

## <span>Specifying DHCP Option 239</span>

During the DHCP process over `eth0`, Cumulus RMP will request DHCP
option 239. This option is used to specify the custom provisioning
script.

For example, the ` dhcpd.conf  `file for an ISC DHCP server could look
like:

    option cumulus-provision-url code 239 = text;
    
    subnet 192.168.0.0 netmask 255.255.255.0 {
     range 192.168.0.100 192.168.0.200;
     option cumulus-provision-url "http://192.168.0.2/demo.sh";
    }

Additionally, the hostname of the switch can be specified via the
` host-name  `option:

    subnet 192.168.0.0 netmask 255.255.255.0 {
     range 192.168.0.100 192.168.0.200;
     option cumulus-provision-url "http://192.168.0.2/demo.sh";
     host dc1-tor-sw1 { hardware ethernet 44:38:39:00:1a:6b; fixed-address 192.168.0.101; option host-name "dc1-tor-sw1"; }
    }

<span id="src-5116322_ZeroTouchProvisioning-http_headers"></span>

## <span>HTTP Headers</span>

The following HTTP headers are sent in the request to the Web server to
retrieve the provisioning script:

    Header                        Value                 Example
    ------                        -----                 -------
    User-Agent                                          CumulusRMP-AutoProvision/0.4
    CUMULUS-ARCH                  CPU architecture      powerpc
    CUMULUS-BUILD                                       2.5.3-5c6829a-201309251712-final
    CUMULUS-LICENSE-INSTALLED     Either 0 or 1         1
    CUMULUS-MANUFACTURER                                dni
    CUMULUS-PRODUCTNAME                                 et-7448bf
    CUMULUS-SERIAL                                      XYZ123004
    CUMULUS-VERSION                                     2.5.3
    CUMULUS-PROV-COUNT                                  0
    CUMULUS-PROV-MAX                                    32

## <span>Script Requirements</span>

The script contents must contain the ` CUMULUS-AUTOPROVISIONING  `flag.
This can be in a comment or remark and does not needed to be echoed or
written to ` stdout  `.

The script can be written in any language currently supported by Cumulus
RMP, such as:

  - Perl

  - Python

  - Ruby

  - Shell

The script must return an exit code of 0 upon success, as this triggers
the provisioning process to be marked as complete.

## <span>Example Scripts</span>

Here is a simple script to install ` puppet  `:

    #!/bin/bash
    function error() {
      echo -e "\e[0;33mERROR: The Zero Touch Provisioning script failed while running the command $BASH_COMMAND at line $BASH_LINENO.\e[0m" >&2
      exit 1
    }
    trap error ERR
    apt-get update -y
    apt-get upgrade -y
    apt-get install puppet -y
    sed -i /etc/default/puppet -e 's/START=no/START=yes/'
    sed -i /etc/puppet/puppet.conf -e 's/\[main\]/\[main\]\npluginsync=true/'
    service puppet restart
    # CUMULUS-AUTOPROVISIONING
    exit 0

This script illustrates how to specify an internal APT mirror and
` puppet  `master:

    #!/bin/bash
    function error() {
      echo -e "\e[0;33mERROR: The Zero Touch Provisioning script failed while running the command $BASH_COMMAND at line $BASH_LINENO.\e[0m" >&2
      exit 1
    }
    trap error ERR
    sed -i /etc/apt/sources.list -e 's/repo.cumulusnetworks.com/labrepo.mycompany.com/'
    apt-get update -y
    apt-get upgrade -y
    apt-get install puppet -y
    sed -i /etc/default/puppet -e 's/START=no/START=yes/'
    sed -i /etc/puppet/puppet.conf -e 's/\[main\]/\[main\]\npluginsync=true/'
    sed -i /etc/puppet/puppet.conf -e 's/\[main\]/\[main\]\nserver=labpuppet.mycompany.com/'
    service puppet restart
    # CUMULUS-AUTOPROVISIONING
    exit 0

Now ` puppet  `can take over management of the switch, configuration
authentication, changing the default root password, and setting up
interfaces and routing protocols.

## <span>Using the autoprovision Command</span>

You can directly invoke an your provisioning script by running the
` autoprovision  `command. You can use this command to enable and
disable zero touch provisioning on the switch. Be sure to specify the
full path to the command, as in the examples below.

To enable zero touch provisioning, use the ` -e  `option:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -e

To run the provisioning script, use the ` -u  `option and include the
URL to the script:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -u http://192.168.0.1/ztp.sh

To disable zero touch provisioning, use the ` -x  `option:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -x

To enable startup discovery mode, without relying on DHCP when you boot
the switch, use the ` -s  `option:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -s

## <span>Notes</span>

  - During the development of a provisioning script, the switch may need
    to be reset.

  - You can use the Cumulus RMP ` cl-img-select  `-`i` command to cause
    the switch to reprovision itself and install a network operating
    system again using ONIE.

  - You can trigger the zero touch provisioning process when eth0 is set
    to use DHCP and one of the following events occur:
    
      - Booting the switch
    
      - Plugging a cable into or unplugging it from the eth0 port
    
      - Disconnecting then reconnecting the switch’s power cord

## <span>Configuration Files</span>

  - /var/lib/cumulus/autoprovision.conf
