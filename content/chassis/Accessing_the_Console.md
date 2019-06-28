---
title: Accessing the Console
author: Cumulus Networks
weight: 11
aliases:
 - /display/CHASSIS/Accessing+the+Console
 - /pages/viewpage.action?pageId=7766291
pageID: 7766291
product: Cumulus Chassis
version: '1.0'
imgData: chassis
siteSlug: chassis
---
You access the console slightly differently, depending upon whether your
chassis is a Backpack or the CX-10256-S/OMP-800.

## <span>Accessing the Console on a Backpack Chassis</span>

Every CPU in the chassis has its own console. However, for design
simplicity, console access is multiplexed, so the only console ports are
on the chassis management modules (CMMs) and system controller modules
(SCMs).

### <span>Accessing a Console through a CMM</span>

Each CMM has an RJ45 port for console access. If you connect to either
CMM's console port, you can access every other console port in the
chassis. By default, the CMM console port connects to that CMM's local
baseboard management controller (BMC) ARM processor. The default
parameters are 9600 8N1, and the default login credentials for OpenBMC
are *root/0penBmc* (the first character of the password is the number
zero, not a capital letter O).

    OpenBMC Release wedge100-v10-1023-g6f113cb
     
    bmc login: root
    Password:  0penBmc
    Last login: Mon Apr 24 18:39:35 -0700 2017 on pts/0 from 10.40.10.230.
    root@bmc:~#

In order to connect to a line card, fabric card or the other CMM's
console port, use the OpenBMC `sol.sh` command. When you execute this
command on a CMM, it takes just one parameter: the name of the card to
connect to, which is one of the following:

  - *lc101*, for the left side ASIC (when viewed from the front) on line
    card 1.

  - *lc102*, for the right side ASIC on line card 1.

  - *lc201*, for the left side ASIC on line card 2.

  - *lc202*, for the right side ASIC on line card 2.

  - *lc301*, for the left side ASIC on line card 3.

  - *lc302*, for the right side ASIC on line card 3.

  - *lc401*, for the left side ASIC on line card 4.

  - *lc402*, for the right side ASIC on line card 4.

  - *fc1*, for fabric card 1.

  - *fc2*, for fabric card 2.

  - *fc3*, for fabric card 3.

  - *fc4*, for fabric card 4.

  - *cmm*, for the other CMM.

For example, to connect to the console on the right side of line card 3,
run `sol.sh lc302`. By default, this connects to the console port of the
BMC.

    root@bmc:~# sol.sh lc302
    You are in SOL session.
    Use ctrl-x to quit.
    -----------------------
      
    OpenBMC Release
    bmc login:

{{%notice tip%}}

The prompts in the console can be somewhat confusing, because there is
no indication that the console is now connected to the BMC for the right
of line card 3 instead of the console of the CMM’s BMC to which you were
previously connected. Since this BMC is running OpenBMC, just like the
BMC on the CMM module, they appear identical. The default login
credentials for OpenBMC are the same — *root/0penBmc*.

    bmc login: root
    Password:  0penBmc
    root@bmc:~#

{{%/notice%}}

You can switch the console back to the CMM by pressing *ctrl-x*. As
mentioned earlier, since both the line card and CMM are running OpenBMC
and there is no indication to which instance you are currently
connected, it can be confusing as to which BMC you are accessing.

    root@bmc:~#  ctrl+x
    -----------------------
    Exit from SOL session.
    root@bmc:~#

In addition to returning to the CMM console, when connected to a line
card or fabric card BMC, the connection can also be switched to the
Intel Atom E3845's console port by running the `sol.sh` command. The
`sol.sh` command on a line card's or fabric card's BMC does not take any
parameters; it can only switch the connection to the Intel Atom E3845's
console port for that same line card or fabric card.

    root@bmc:~# sol.sh lc302
    You are in SOL session.
    Use ctrl-x to quit.
    -----------------------
      
    root@bmc:~# sol.sh
    You are in SOL session.
    Use ctrl-x to quit.
    -----------------------
      
    Debian GNU/Linux 8 backpack-lc302 ttyS0
    backpack-lc302 login:

Once connected to the line card or fabric card's Intel Atom E3845
console port, you see one of the following:

  - The ONIE prompt, if no operating system is installed.

  - The Cumulus Linux prompt, if Cumulus Linux has been installed.

{{%notice tip%}}

The `sol.sh` command on the CMM, the line card and the fabric card BMC
all use the same escape sequence (*ctrl-x*) to cancel the `sol.sh`
command and return to the BMC console connection. When connected to a
line card or fabric card's Intel Atom E3845 console port, typing
*ctrl-x* cancels the CMM’s `sol.sh` command, returning the connection
back to the CMM's BMC.

A subsequent `sol.sh` command issued from the CMM that connects to the
same card connects directly to the Intel Atom E3845's console port,
since the `sol.sh` command is still running on the line card or fabric
card BMC.

You cannot exit the `sol.sh` command on the line card or fabric card,
and thus cannot access the line card or fabric card BMC's console port
again using this method.

{{%/notice%}}

### <span>Accessing a Console through an SCM</span>

Each SCM module has an RJ45 console port which provides access to the
BMC and Intel Atom E3845 console ports associated with that SCM. Using
this method prevents you from accessing the console ports of other line
cards, fabric cards or the CMMs. The default parameters of this console
port are *115200 8N1*.

When you connect through an SCM's console port, access to the BMC and
Intel Atom E3845 consoles is determined by entering a special
four-character key sequence:

| Key Sequence           | Switch Connection to Console Port                               |
| ---------------------- | --------------------------------------------------------------- |
| ctrl+f ctrl+b ctrl+u 1 | Fabric card BMC or left line card BMC                           |
| ctrl+f ctrl+b ctrl+u 2 | Right line card BMC                                             |
| ctrl+f ctrl+b ctrl+u 3 | Fabric card Intel Atom E3845 or left line card Intel Atom E3845 |
| ctrl+f ctrl+b ctrl+u 4 | Right line card Intel Atom E3845                                |

Since fabric cards have only one BMC and Intel Atom E3845, only the
first and third key sequences are recognized. This key sequence can be
pressed at any time to switch between the console ports associated with
a line card or fabric card. The default power-on connection is the
fabric card BMC/left line card BMC.

    OpenBMC Release
     
    bmc login:  ctrl+f ctrl+b ctrl+u 2
    OpenBMC Release
     
    bmc login:  ctrl+f ctrl+b ctrl+u 3
    Debian GNU/Linux 8 backpack-lc301 ttyS0
     
    backpack-lc301 login:  ctrl+f ctrl+b ctrl+u 4
    Debian GNU/Linux 8 backpack-lc302 ttyS0
     
    backpack-lc302 login:  ctrl+f ctrl+b ctrl+u 1
    OpenBMC Release
     
    bmc login:

## <span>Accessing the Console on a CX-10256-S/OMP-800 Chassis</span>

Each fabric card has 2 RJ45 console ports, one for each of the CPUs.
Each line card also has 2 console ports, one for each CPU that connect
via a USB type A jack — this requires a special cable from Edgecore in
order to access the line card console ports. By default, the console
connects at 115200 baud 8N1.

Once connected to the line card or fabric card's console port, you see
one of the following:

  - The ONIE prompt, if no operating system is installed.

  - The Cumulus Linux prompt, if Cumulus Linux has been installed.

### <span>Line Card Naming Convention</span>

Each line card and fabric card has a default identifier, which is
displayed in the console. The name is one of the following:

  - *lc101*, for the A side ASIC (the left side in the image below) on
    line card 1.

  - *lc102*, for the B side ASIC on line card 1.

  - *lc201*, for the A side ASIC on line card 2.

  - *lc202*, for the B side ASIC on line card 2.

  - *lc301*, for the A side ASIC on line card 3.

  - *lc302*, for the B side ASIC on line card 3.

  - *lc401*, for the A side ASIC on line card 4.

  - *lc402*, for the B side ASIC on line card 4.

  - *lc501*, for the A side ASIC on line card 5.

  - *lc502*, for the B side ASIC on line card 5.

  - *lc601*, for the A side ASIC on line card 6.

  - *lc602*, for the B side ASIC on line card 6.

  - *lc701*, for the A side ASIC on line card 7.

  - *lc702*, for the B side ASIC on line card 7.

  - *lc801*, for the A side ASIC on line card 8.

  - *lc802*, for the B side ASIC on line card 8.

  - *fc101*, for the A side ASIC (the bottom half of the leftmost fabric
    card in the image below) on fabric card 1.

  - *fc102*, for the B side ASIC on fabric card 1.

  - *fc201*, for the A side ASIC on fabric card 2.

  - *fc202*, for the B side ASIC on fabric card 2.

  - *fc301*, for the A side ASIC on fabric card 3.

  - *fc302*, for the B side ASIC on fabric card 3.

  - *fc401*, for the A side ASIC (the top half of the rightmost fabric
    card in the image below) on fabric card 4.

  - *fc402*, for the B side ASIC on fabric card 4.

Note that fabric cards 3 and 4 are installed upside down relative to
fabric cards 1 and 2.

{{% imgOld 0 %}}
