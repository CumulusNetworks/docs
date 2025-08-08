---
title: Adding and Updating Packages
author: NVIDIA
weight: 60
toc: 3
---

{{%notice warning%}}
Updating, upgrading, and installing packages causes disruptions to network services:
- Upgrading a package can cause services to restart or stop.
- Installing a package sometimes disrupts core services by changing core service dependency packages. In some cases, installing new packages also upgrades additional existing packages due to dependencies.
- If services stop, you need to reboot the switch to restart the services.
{{%/notice%}}

## List Packages Installed on the Switch

To show the packages installed on the switch, run the following command.

{{< tabs "TabID19 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv show system version packages installed
Installed packages
=====================
    Installed package                      Description                                                                                                                                                                                                                                              Package                                Version                                  
    -------------------------------------  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  -------------------------------------  -----------------------------------------
    acpi                                   displays information on ACPI devices                                                                                                                                                                                                                     acpi                                   1.7-1.2                                  
    acpi-support-base                      scripts for handling base ACPI events such as the power button                                                                                                                                                                                           acpi-support-base                      0.143-5.1                                
    acpid                                  Advanced Configuration and Power Interface event daemon                                                                                                                                                                                                  acpid                                  1:2.0.33-2+b1                            
    adduser                                add and remove users and groups                                                                                                                                                                                                                          adduser                                3.134                                    
    apt                                    commandline package manager                                                                                                                                                                                                                              apt                                    2.6.1                                    
    arping                                 sends IP and/or ARP pings (to the MAC address)                                                                                                                                                                                                           arping                                 2.23-1                                   
    arptables                              ARP table administration                                                                                                                                                                                                                                 arptables                              0.0.5-3.1                                
    atftp                                  advanced TFTP client                                                                                                                                                                                                                                     atftp                                  0.8.0-3                                  
    atftpd                                 advanced TFTP server                                                                                                                                                                                                                                     atftpd                                 0.8.0-3                                  
    auditd                                 User space tools for security auditing                                                                                                                                                                                                                   auditd                                 1:3.0.9-1                                
    babeltrace                             Trace conversion program                                                                                                                                                                                                                                 babeltrace                             1.5.11-1+b2                              
    base-files                             Debian base system miscellaneous files                                                                                                                                                                                                                   base-files                             12.4+deb12u10                            
    base-passwd                            Debian base system master password and group files                                                                                                                                                                                                       base-passwd                            3.6.1                                    
    bash                                   GNU Bourne Again SHell                                                                                                                                                                                                                                   bash                                   5.2.15-2+b7                              
    bash-completion                        programmable completion for the bash shell                                                                                                                                                                                                               bash-completion                        1:2.11-6                                 
    bind9-dnsutils                         Clients provided with BIND 9                                                                                                                                                                                                                             bind9-dnsutils                         1:9.18.33-1~deb12u2                      
    bind9-host                             DNS Lookup Utility                                                                                                                                                                                                                                       bind9-host                             1:9.18.33-1~deb12u2                      
    bind9-libs                             Shared Libraries used by BIND 9                                                                                                                                                                                                                          bind9-libs                             1:9.18.33-1~deb12u2                      
    binutils                               GNU assembler, linker and binary utilities                                                                                                                                                                                                               binutils                               2.40-2                                   
    binutils-common                        Common files for the GNU assembler, linker and binary utilities                                                                                                                                                                                          binutils-common                        2.40-2                                   
    binutils-x86-64-linux-gnu              GNU binary utilities, for x86-64-linux-gnu target                                                                                                                                                                                                        binutils-x86-64-linux-gnu              2.40-2                                   
    bridge-utils                           Utilities for configuring the Linux Ethernet bridge                                                                                                                                                                                                      bridge-utils                           1.7.1-cl5.9.0u1                          
    bsd-mailx                              simple mail user agent                                                                                                                                                                                                                                   bsd-mailx                              8.1.2-0.20220412cvs-1
...
```

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ dpkg -l
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                Version                   Architecture Description
+++-===================-=========================-============-=================================
ii  acpi                1.7-1.1                   amd64        displays information on ACPI devices
ii  acpi-support-base   0.142-8                   all          scripts for handling base ACPI events such as th
ii  acpid               1:2.0.31-1                amd64        Advanced Configuration and Power Interface event
ii  adduser             3.118                     all          add and remove users and groups
ii  apt                 1.8.2                     amd64        commandline package manager
ii  arping              2.19-6                    amd64        sends IP and/or ARP pings (to the MAC address)
ii  arptables           0.0.4+snapshot20181021-4  amd64        ARP table administration
...
```

{{< /tab >}}
{{< /tabs >}}

## Show the Package Version

To show the version of a package installed on the switch:

{{< tabs "TabID67 ">}}
{{< tab "NVUE Command ">}}

The following example command shows which version of the `vrf` package is on the switch:

```
cumulus@switch:~$ nv show system version packages installed vrf
             operational        
-----------  -------------------
package      vrf                
version      1.0-cl5.9.0u4      
description  Linux tools for VRF
```

{{< /tab >}}
{{< tab "Linux Command ">}}

The following example command shows which version of the `vrf` package is on the switch:

```
cumulus@switch:~$ dpkg -l vrf
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name       Version      Architecture Description
+++-==========-============-============-=================================
ii  vrf        1.0-cl5.9.0u4    amd64        Linux tools for VRF
```

{{< /tab >}}
{{< /tabs >}}

## Upgrade All Packages

To upgrade all the packages installed on the switch to their latest versions, run the following commands:

{{< tabs "TabID103 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ sudo nv action upgrade system packages to latest use-vrf default dry-run
```

By default, the NVUE `sudo nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf>` option.

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get upgrade
```

The system lists the packages for upgrade and prompts you to continue.

The above commands upgrade all installed versions with their latest versions but do not install any new packages. To add a new package, refer to {{<link url="#add-a-package" text="Add a Package">}} below.

{{%notice tip%}}
Use the `-E` option with `sudo` whenever you run any `apt-get` command. This option preserves your environment variables (such as HTTP proxies) before you install new packages or upgrade your distribution.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Add a Package

To add a new package, first ensure the package is not already on the system with the NVUE `nv show system version packages installed <package-name>` command or the Linux `dpkg -l | grep <package-name>` command.
- If the package is already on the system, you can update the package from the Cumulus Linux repository as part of the package upgrade process, which upgrades all packages on the system. See {{<link url="#upgrade-packages" text="Upgrade Packages">}} above.
- If the package is *not* already on the system, add it with the Linux `sudo -E apt-get install <name of package>` command. This command retrieves the package from the Cumulus Linux repository and installs it on your switch together with any dependent packages. The following example adds the `tcpreplay` package on the switch:

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get install tcpreplay
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
tcpreplay
0 upgraded, 1 newly installed, 0 to remove and 1 not upgraded.
Need to get 436 kB of archives.
After this operation, 1008 kB of additional disk space will be used
...
```

You can install several packages at the same time:

```
cumulus@switch:~$ sudo -E apt-get install <package1> <package2> <package3>
```

{{%notice tip%}}
In some cases, installing a new package also upgrades additional existing packages due to dependencies. To view these additional packages before you install, run the `apt-get install --dry-run` command.
{{%/notice%}}

## Configure Additional Repositories

As shipped, Cumulus Linux searches the Cumulus Linux repository for available packages. You can configure additional repositories to search by adding them to the list of sources that Cumulus Linux consults.

{{%notice note%}}
- NVIDIA adds features or makes bug fixes to certain packages; do not replace these packages with versions from other repositories.
- NVIDIA does not test and Cumulus Linux Technical Support does not support packages that are not part of the Cumulus Linux repository.
{{%/notice%}}

To configure an additional repository:
- Provide the repository location, distribution, and pool.
- Either set the repository to trusted or provide the secure key.
- Enable repository source to add source files from the repository (optional).
- Set the VRF to use when adding an additional repository (optional). The default VRF is `mgmt`.

The repository URL can be `https`or `http` format, or the directory and file name on the switch (`/etc/myrepo`).

{{< tabs "TabID176 ">}}
{{< tab "NVUE Commands ">}}

The following example configures the repository located at `http://test.myrepo.com` with distribution `mydist` and pool `mypool`, enables source files from the repository, and sets the repository to trusted. The example also sets the VRF to `default`.

```
cumulus@switch:~$ nv set system packages use-vrf default
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com distribution mydist pool mypool 
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com source enabled
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com insecure enabled
cumulus@switch:~$ nv config apply
```

The following example configures the repository located at `http://test.myrepo.com` with distribution `mydist` and pool `mypool`, enables source files from the repository, and provides the secure key `thekey.asc`.

```
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com distribution mydist pool mypool
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com source enabled
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com key thekey.asc
cumulus@switch:~$ nv config apply 
```

{{< /tab >}}
{{< tab "Linux Command ">}}

Edit the `/etc/apt/sources.list` file to configure the repository.

The following example configures the repository located at `http://test.myrepo.com` with distribution `mydist` and pool `mypool`, enables source files from the repository, and sets the repository to trusted.

```
deb [trusted=yes] http://test.myrepo.com mydist mypool
deb-src [trusted=yes] http://test.myrepo.com mydist mypool
```

The following example configures the repository located at `http://test.myrepo.com` with distribution `mydist` and pool `mypool`, enables source files from the repository, and provides the secure key `thekey.asc`.

```
deb [signed-by=/etc/apt/keyrings/thekey.asc] http://test.myrepo.com mydist mypool 
deb-src [signed-by=/etc/apt/keyrings/thekey.asc] http://test.myrepo.com mydist mypool 
```

{{< /tab >}}
{{< /tabs >}}

### Manage Repository Keys

Cumulus Linux provides commands to:
- Fetch a repository key and save it on the switch.
- Delete a repository key.

{{< tabs "TabID218 ">}}
{{< tab "NVUE Commands ">}}

- To fetch and save a key globally, run the `nv action fetch system packages key <key>` command. Cumulus Linux fetches the key and saves it globally in the `/etc/apt/trusted.gpg.d/` directory. This is the default setting.
- To fetch and save a key for a specific repository, run the `nv action fetch system packages key <key> scope repository` command. Cumulus Linux fetches the key and saves it in the `/etc/apt/keyrings/` directory.

The following example fetches the repository key `http://deb.opera.com/archive.key` and saves it in the `/etc/apt/trusted.gpg.d` directory:

```
cumulus@switch:~$ nv action fetch system packages key http://deb.opera.com/archive.key 
```

The following example fetches the repository key `http://deb.opera.com/archive.key` and saves it in the `/etc/apt/keyrings` directory by setting the scope to `repository`:

```
cumulus@switch:~$ nv action fetch system packages key http://deb.opera.com/archive.key scope repository
```

To delete a package key, run the `nv action delete system packages key <key>` command:

```
cumulus@switch:~$ nv action delete system packages key debian-archive-bookworm-automatic.asc
```

{{< /tab >}}
{{< tab "Linux Command ">}}

To fetch and save a repository key globally:
- If the key already exists on the filesystem, copy it to the `/etc/apt/trusted.gpg.d/` directory. 
- If the key is at a remote URL, fetch it with `wget` or another utility, then copy it to the `/etc/apt/trusted.gpg.d/` directory.

The following example fetches the key `http://your-url.com/name.key` from the remote URL and copies it to the `/etc/apt/trusted.gpg.d/` directory:

```
cumulus@switch:~$ wget -qO - http://your-url.com/name.key
cumulus@switch:~$ sudo cp name.key /etc/apt/trusted.gpg.d
```

To fetch and save a key for a specific repository:
- If your key already exists on the filesystem, copy it to the `/etc/apt/keyrings/` directory. 
- If the key is at a remote URL, fetch it with `wget` or another utility, then copy it to the `/etc/apt/keyrings/` directory.

The following example copies the key `name.key` located on the filesystem to the `/etc/apt/keyrings/` directory.

```
cumulus@switch:~$ sudo cp name.key /etc/apt/keyrings/
```

To delete a key, remove the key from the `/etc/apt/keyrings` or `/etc/apt/trusted.gpg.d` directory.

```
cumulus@switch:~$ sudo rm /etc/apt/keyrings/name.key
```

{{< /tab >}}
{{< /tabs >}}

### Show Repository Information

To show the list of repositories and their details:

```
cumulus@switch:~$ nv show system packages repository 
Repository                                    Insecure  Source   Distribution             Pool 
--------------------------------------------  --------  -------  -----------------------  ----------- 
https://apps3.cumulusnetworks.com/repos/deb/  enabled   enabled  CumulusLinux-d12         netq-latest 
                                                                 CumulusLinux-d12-latest  netq 
                                                                                          upstream 
https://apt.cumulusnetworks.com/repo                             CumulusLinux-d12-latest  cumulus 
                                                                                          netq 
                                                                                          upstream
```

To show the details for a specific repository:

```
cumulus@switch:~$ nv show system packages repository https://apt.cumulusnetworks.com/repo
                operational              applied 
--------------  -----------------------  ------- 
insecure        enabled                  enabled 
source          enabled                  enabled 
[distribution]  CumulusLinux-d12         CumulusLinux-d12 
[distribution]  CumulusLinux-d12-latest  CumulusLinux-d12-latest
```

To show the list of distributions for a repository:

```
cumulus@switch:~$ nv show system packages repository https://apt.cumulusnetworks.com/repo distribution
Distribution      Origin            Version  Codename          Pool         Priority 
----------------  ----------------  -------  ----------------  -----------  --------
CumulusLinux-d12  Cumulus Networks           CumulusLinux-d12  netq-latest  991
```

To show the details for a distribution for a repository:

```
cumulus@switch:~$ nv show system packages repository https://apps3.cumulusnetworks.com/repos/deb/ distribution CumulusLinux-d12 
          operational       applied 
--------  ----------------  ------- 
[pool]    netq-latest 
codename  CumulusLinux-d12 
origin    Cumulus Networks 
```

To show the list of distribution pools for a repository:

```
cumulus@switch:~$ nv show system packages repository https://apps3.cumulusnetworks.com/repos/deb/ distribution CumulusLinux-d12 pool 
Pool          priority 
--------      -------- 
netq-latest   100 
```

To show the list of repositories and keys:

```
cumulus@switch:~$ nv show system packages
         operational  applied
-------  -----------  -------
use-vrf               mgmt

repository
=============
    Repository                                       Insecure  Source    Key  Distribution               Pool
    -----------------------------------------------  --------  --------  ---  -------------------------  ----
    copy:/var/lib/cumulus/cumulus-local-apt-archive  enabled   disabled       cumulus-local-apt-archive  main

key
======
    Key ID                                          Path                                                                   Scope 
    ----------------------------------------------  ---------------------------------------------------------------------  ------
    debian-archive-bookworm-automatic.asc           /etc/apt/trusted.gpg.d/debian-archive-bookworm-automatic.asc           global
    debian-archive-bookworm-security-automatic.asc  /etc/apt/trusted.gpg.d/debian-archive-bookworm-security-automatic.asc  global
    debian-archive-bookworm-stable.asc              /etc/apt/trusted.gpg.d/debian-archive-bookworm-stable.asc              global
    debian-archive-bullseye-automatic.asc           /etc/apt/trusted.gpg.d/debian-archive-bullseye-automatic.asc           global
    debian-archive-bullseye-security-automatic.asc  /etc/apt/trusted.gpg.d/debian-archive-bullseye-security-automatic.asc  global
    debian-archive-bullseye-stable.asc              /etc/apt/trusted.gpg.d/debian-archive-bullseye-stable.asc              global
    debian-archive-buster-automatic.asc             /etc/apt/trusted.gpg.d/debian-archive-buster-automatic.asc             global
    debian-archive-buster-security-automatic.asc    /etc/apt/trusted.gpg.d/debian-archive-buster-security-automatic.asc    global
    debian-archive-buster-stable.asc                /etc/apt/trusted.gpg.d/debian-archive-buster-stable.asc                global
```

To show the list of keys:

```
cumulus@switch:~$ nv show system packages keys
Key ID                                          Path                                                                   Scope 
----------------------------------------------  ---------------------------------------------------------------------  ------ 
debian-archive-bookworm-automatic.asc           /etc/apt/trusted.gpg.d/debian-archive-bookworm-automatic.asc           global 
debian-archive-bookworm-security-automatic.asc  /etc/apt/trusted.gpg.d/debian-archive-bookworm-security-automatic.asc  global 
debian-archive-bookworm-stable.asc              /etc/apt/trusted.gpg.d/debian-archive-bookworm-stable.asc              global 
sample-test-key.asc                             /etc/apt/keyrings/sample-test-key.asc                                  repository
```

To show the details for a package key:

```
cumulus@switch:~$ nv show system packages key debian-archive-bookworm-automatic.asc
        operational 
 -----  --------------------------------------------------------------------- 
 scope  global 
 path   /etc/apt/trusted.gpg.d/debian-archive-bookworm-security-automatic.asc
```
