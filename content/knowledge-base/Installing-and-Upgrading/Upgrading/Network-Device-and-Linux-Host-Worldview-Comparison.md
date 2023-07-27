---
title: Upgrades - Network Device and Linux Host Worldview Comparison
author: NVIDIA
weight: 291
toc: 4
---

## Manual and Automated Configuration

Historically, people configured *network devices* in place and most network devices required customized configurations, which led predominantly to configuring the hardware manually. A lack of standardization between vendors, device types, and device roles hampered the development of APIs and automation tools. However, for very large data centers, configurations became uniform and repeatable, and therefore scriptable. Some larger enterprises had to develop their own custom scripts to roll out data center network configurations. Virtually no industry-standard provisioning tools existed.

In contrast to data center network devices, *Linux hosts* in the data center number in the thousands and tend to have similar configurations. This increased scale led Linux system administrators long ago to move to common tools to automate installation and configuration, because manually installing and configuring hosts did not work at the scale of a data center. You can perform nearly every task using commonly available provisioning and orchestration tools.
<!-- vale off -->
## Pre-deployment Testing of Production Environments
<!-- vale on -->
Historically, the cost of a *single network device* hindered the cost of *network device testing*. Setting up an appropriately sized lab topology can be very expensive. As a result, it is difficult to do comprehensive topology-based testing of a release before deploying it. Therefore, many network administrators cannot do comprehensive system testing of a new release before deploying it.

Otherwise, the cost of a *Linux host* is cheap (or nearly free when using virtualization), so budgeting is not a concern when it comes to rigorous testing of a release before deploying it. Most system administrators extensively test new releases in the complete application environment.

## Locations of Configuration Data Versus Executables

*Network devices* generally separate configuration data from the executable code. On bootup, the executable code looks into a different file system and retrieves the configuration file or files, parses the text and uses that data to configure the software options for each software subsystem. The model is very centralized, with all the executables packaged together, and the configuration data following a set of rules that a centralized parser can read. Each vendor controls the configuration format for the entire switch, as each vendor generally supports only their own software. This made sense because they designed their platforms as application-specific appliances.

Because a *Linux host* is a general purpose platform, with applications running on top of it, the locations of the files are much more distributed. Applications install and read their configuration data from text files usually stored in the `/etc` directory tree. Executables are generally stored in one of several *bin* directories, but the `bin` and `etc` directories are often on the same physical device. Because a different organization often developed each *module* (application or executable) and shared it with the world, each module was responsible for its own configuration data format. The community supports most applications, and while there are some generally accepted guiding principles on how to format their configuration data, no central authority exists to control or ensure compliance.

## Upgrade Procedure

Both network administrators and system administrators generally plan upgrades only to gain new functionality or to get bug fixes when the workarounds become too onerous. The goal is to reduce the number of upgrades as much as possible.

The *network device* upgrade paradigm is to leave the configuration data in place, and *replace the executable files* either all at one time from a single binary image or in large chunks (subsystems). A full release upgrade comes with risk due to unexpected behavior changes in subsystems where the administrator did not expect or need changes.

The *Linux host* upgrade paradigm is to independently *upgrade a small list of packages* while leaving most of the OS untouched. Changing a small list of packages reduces the risk of unintended consequences. Usually upgrades are a *forward only* paradigm, where the system administrators generally plan to move to the latest code within the same major release when needed. Every few years, when the developers release a new kernel train, they plan for a major upgrade. A major upgrade involves wiping and replacing the entire OS and migrating configuration data.

## Rollback Procedure

Even the most well planned and tested upgrades can result in unforeseen problems, and sometimes the best solution to new problems is to roll back to the previous state.

Because *network devices* clearly separate data and executables, generally the process is to *overwrite the new release executable* with the previously running executable. If the newer release changed the configuration, then you either have to manually back out or repair the changes, or restore from an already backed up configuration.

The *Linux host* scenario can have more complications. There are three main approaches:

- Back out individual packages: If you can identify the problematic package, the system administrator can downgrade the affected package directly. In rare cases you might have to restore the configuration files from backup, or edit them to back out any changes that were automatically made by the upgrade package.
- Flatten and rebuild: If the OS becomes unusable, you can use orchestration tools to reinstall the previous OS release from scratch and then automatically rebuild the configuration.
- Backup and restore: Another common strategy is to restore to a previous state via a backup captured before the upgrade.

## Third Party Packages

Third party packages are rare in the *network device* world. Because the network OS is usually proprietary, third party packages are usually packaged by the network device vendor and the network device upgrade system handles upgrading those packages.

Third party packages in the *Linux host* world often use the same package system as the distribution into which you are installing it (for example, Debian uses `apt-get`). Or the system administrator might compile and install the package. Configuration and executable files generally follow the same filesystem hierarchy standards as other applications.

## Cumulus Linux Device Upgrade: Strategies and Processes

Because Cumulus Linux is both Linux *and* a network device, it has characteristics of both paradigms. The following describes the Cumulus Linux paradigm regarding upgrade planning and execution.
<!-- vale off -->
### Automated Configuration Is Preferred over Manual Configuration
<!-- vale on -->
Because Cumulus Linux *is* Linux, NVIDIA recommends that even with small networks or test labs, network administrators should make the jump to deploy, provision, configure, and upgrade switches using automation from the very beginning. The small up front investment of time spent learning an orchestration tool, even to provision a small number of Cumulus Linux devices, pays back dividends for a long time. You realize the biggest gain during the upgrade process, where the network administrator can quickly upgrade dozens of devices in a repeatable manner.

You should treat switches &mdash; and servers &mdash; like {{<exlink url="https://www.google.com/search?q=cattle+not+pets" text="cattle, not pets">}}.
<!-- vale off -->
### Out-of-Band Management Is Worth the Investment
<!-- vale on -->
Because network devices are reachable via the IP addresses on the front panel ports, many network administrators of small-to-medium sized networks use *in-band* networks to manage their switches. In this design, management traffic like SSH, SNMP, and console server connections use the same networks that regular network traffic traverses &mdash; there is no separation between the *management plane* and the *data plane*. Larger data centers create a separate *out-of-band* network with a completely separate subnet and reachability path to attach to the management ports &mdash; that is accessible via eth0 and the serial console.

This is a situation where smaller companies should learn from the big companies. A separate management network is not free, but it is inexpensive. With an inexpensive Cumulus RMP management switch, an inexpensive console server, and a separate cable path, you can completely control up to 48 devices via the out-of-band network if you have a network emergency.

Many scenarios exist where in-band networking can fail and leave the network administrator waiting for someone to drive to the data center or remote site to connect directly to the console of a misconfigured or failing device. The cost of one outage would usually more than pay for the investment in a separate network. For even more security, attach remote-controllable power distribution units (PDUs) in each rack to the management network, so you can have complete control to remote power cycle every device in that rack.

{{%notice tip%}}

However, if an out-of-band network is not available for you to upgrade, you can use {{<link url="Using-dtach-for-In-band-apt-get-Upgrades" text="the dtach tool">}} instead to upgrade in band.

{{%/notice%}}
<!-- vale off -->
### Pre-deployment Testing of New Releases Is Advised and Enabled

White box switches and virtualization (Cumulus VX) bring the cost of networking devices down, so the ability for network administrators to test their own procedures, configurations, applications, and network topology in an appropriately sized lab topology becomes extremely affordable.
<!-- vale on -->
