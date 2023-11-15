---
title: Early Access Features Defined
author: NVIDIA
weight: 709
toc: 4
---
{{%notice note%}}
The term early access (EA) is used in Cumulus Linux 5.3 and earlier. In Cumulus Linux 5.4 and later, early access is called Beta.
{{%/notice%}}

Cumulus Linux is Linux; as an operating system, it enables a vast number of applications. A set of core networking functions integrates with the main Cumulus Linux distribution or validated as add-on applications. In addition, NVIDIA provides a set of early access features with the goal to ensure faster feature velocity, solve customer-specific challenges and collect feedback.  
  
NVIDIA provides early access features on an "as is" basis. The intent for early access packages is for validation only; NVIDIA does not support them in a production environment. NVIDIA encourage customers to work closely with their sales engineer and the NVIDIA product and development teams while assessing the feature. NVIDIA publishes early access features in the {{<link url="Cumulus-Networks-Repositories-Organization-and-Support-Levels" text="early-access repository">}}, although this might not always be the case. If in doubt, refer to the Cumulus Linux [release notes]({{<ref "/cumulus-linux-51/Whats-New/rn" >}}) for the status of a feature.

You should make sure you fully update your switch to the version of Cumulus Linux that contains the early access package you want to install; NVIDIA only tests early access features against the version in which it releases an early access feature.  
  
NVIDIA intends to incorporate early access features into the main Cumulus Linux distribution. NVIDIA reserves the right to re-prioritize or withdraw an early access feature wherever appropriate.

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
