---
title: Update Expired GPG Keys
author: Cumulus Networks
weight: 292
toc: 4
---

## Issue

When updating a switch running Cumulus Linux via `apt`, the OS reports errors for expired GPG keys, and prevent package upgrades:

    W: GPG error: http://repo3.cumulusnetworks.com CumulusLinux-3 InRelease: The following signatures were invalid: KEYEXPIRED 1522652605 KEYEXPIRED 1522652605 KEYEXPIRED 1522652605
    W: GPG error: http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates InRelease: The following signatures were invalid: KEYEXPIRED 1522652605 KEYEXPIRED 1522652605 KEYEXPIRED 1522652605
    W: GPG error: http://repo3.cumulusnetworks.com CumulusLinux-3-updates InRelease: The following signatures were invalid: KEYEXPIRED 1522652605 KEYEXPIRED 1522652605 KEYEXPIRED 1522652605

## Resolution

You can resolve this issue in one of three ways.
<!-- vale off -->
### Option 1: Use the allow-unauthenticated Flag
<!-- vale on -->
1. Run `apt` update using the `--allow-unathenticated` flag:

       sudo apt-get update --allow-unauthenticated

1. Install the new `cumulus-archive-keyring` package:

       sudo apt-get install --allow-unauthenticated cumulus-archive-keyring

1. Proceed with the update/upgrade procedure via `apt`:

       sudo apt-get update && sudo apt-get upgrade
<!-- vale off -->
### Option 2: Download the Updated cumulus-archive-keyring Package
<!-- vale on -->
1. Download the updated `cumulus-archive-keyring` package:

       wget http://repo3.cumulusnetworks.com/repo/pool/cumulus/c/cumulus-archive-keyring/cumulus-archive-keyring_4-cl3u5_all.deb

1. Install the new package:

       sudo dpkg -i cumulus-archive-keyring_4-cl3u5_all.deb

1. Proceed with the update/upgrade procedure via `apt`:

       sudo apt-get update && sudo apt-get upgrade

### Option 3: Update the GPG Key on the Switch

Update the GPG key on the switch with the following procedure.

1. Download the new key:

       sudo apt-key adv --keyserver keys.gnupg.net --recv-keys A88BBC95

1. Update the packages on the switch:

       sudo apt-get update

If you still see the messages when running an update, do the following:

1. Remove the old key:

       sudo rm /etc/apt/trusted.gpg.d/cumulus-stage-keyring.gpg

1. Update the packages on the switch:

       sudo apt-get update

1. Upgrade the packages on the switch:

       sudo apt-get upgrade

1. If prompted to replace `/etc/pat/trusted.gpg.d/cumulus-stage-keyring.gpg` or `/etc/apt/trusted.gpg.d/cumulus-external-keyring.gpg`, press _Y_ to install the package maintainers version:

       Configuration file '/etc/apt/trusted.gpg.d/cumulus-external-keyring.gpg'
       ==> Modified (by you or by a script) since installation.
       ==> Package distributor has shipped an updated version.
       What would you like to do about it ? Your options are:
       Y or I : install the package maintainer's version
       N or O : keep your currently-installed version
       D : show the differences between the versions
       Z : start a shell to examine the situation
       The default action is to keep your current version.
       *** cumulus-external-keyring.gpg (Y/I/N/O/D/Z) [default=N] ? Y
       Installing new version of config file /etc/apt/trusted.gpg.d/cumulus-external-keyring.gpg ...

       Configuration file '/etc/apt/trusted.gpg.d/cumulus-stage-keyring.gpg'
       ==> Deleted (by you or by a script) since installation.
       ==> Package distributor has shipped an updated version.
       What would you like to do about it ? Your options are:
       Y or I : install the package maintainer's version
       N or O : keep your currently-installed version
       D : show the differences between the versions
       Z : start a shell to examine the situation
       The default action is to keep your current version.
       *** cumulus-stage-keyring.gpg (Y/I/N/O/D/Z) [default=N] ? Y
       Installing new version of config file /etc/apt/trusted.gpg.d/cumulus-stage-keyring.gpg ...
