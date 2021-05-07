---
title: Early Access Features Defined
author: NVIDIA
weight: 709
toc: 4
---

Cumulus Linux is Linux; as an operating system, it enables a vast number of applications. A set of core networking functions is integrated into the main Cumulus Linux distribution or validated as add-on applications. In addition, Cumulus Networks provides a set of early-access features with the goal to ensure faster feature velocity, solve customer-specific challenges and collect feedback.  
  
Early access features are provided on an "as is" basis. The early access packages are intended for validation only and are not supported in a production environment. Customers are encouraged to work closely with their sales engineer and our product and development teams assessing the feature. In general, early access features are located in the {{<link url="Cumulus-Networks-Repositories-Organization-and-Support-Levels" text="early-access repository">}}, although this might not always be the case. If in doubt, refer to the Cumulus Linux {{<kb_link url="cumulus-linux-43/Whats-New/rn/" text="release notes">}} for the status of a feature.

You should make sure you fully update your switch to the version of Cumulus Linux that contains the early access package you want to install; Cumulus Networks only tests early access features against the version in which an early access feature is released.  
  
Cumulus Networks intends to incorporate early access features into the main Cumulus Linux distribution. Cumulus Networks reserves the right to re-prioritize or withdraw an early access feature wherever appropriate.

## Installing an Early Access Feature Package

To install the package for an early access feature on a Cumulus Linux switch (version 3.y.z only):

1. Open the `/etc/apt/sources.list` file in a text editor.

2. Uncomment the early access repo lines and save the file:

        #deb http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus
        #deb-src http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus

3. Run the following commands to install the package in Cumulus Linux:

        cumulus@switch:~$ sudo -E apt-get update
        cumulus@switch:~$ sudo -E apt-get install EA_PACKAGENAME
        cumulus@switch:~$ sudo -E apt-get upgrade

## Removing an Early Access Feature Package

To remove an early access feature from a Cumulus Linux switch, run the following commands:

    cumulus@switch:~$ sudo -E apt-get remove EA_PACKAGENAME
    cumulus@switch:~$ sudo -E apt-get autoremove
