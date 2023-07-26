---
title: Cumulus Networks Repositories - Organization and Support Levels
author: NVIDIA
weight: 711
toc: 4
---

All packages included in the official Cumulus Linux distribution are available from NVIDIA repository servers. The organization of the repository differs depending upon the version of Cumulus Linux you are running.
<!-- vale off -->
## Cumulus Linux Repos for Versions 4.0.0 and Later
<!-- vale on -->
Cumulus Linux 4.0.0 and later distributions come in a single package source for each minor (4.y) release, with the most recent repo called *latest*.

<table>
<thead>
<tr class="header">
<th>Short Name</th>
<th>Contents</th>
<th>Codename</th>
<th>Cumulus Linux Update Version*</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>latest</strong></td>
<td>All packages in the Cumulus Linux image.<br />
Optional additional packages.<br />
New features and hardware platforms.<br />
All previous security and maintenance updates.</td>
<td>CumulusLinux-4-latest</td>
<td>Minor and maintenance updates to the most current version available (4.y.0 and 4.y.z)</td>
</tr>
<tr>
<td><strong>latest minor release</strong></td>
<td>All packages in the Cumulus Linux image for that minor release.<br />
Optional additional packages in that minor release.<br />
New features and hardware platforms for that minor release.<br />
All previous security and maintenance updates for that minor release.</td>
<td>CumulusLinux-4.y-latest</td>
<td>Maintenance updates to the most current version in the 4.y release branch (for example, 4.0.0, 4.0.1, 4.0.2)</td>
</tr>
<tr>
<td><strong>4.y.z</strong></td>
<td>All packages in the Cumulus Linux image for that specific version.<br />
Optional additional packages in that specific version.<br />
New features and hardware platforms for that specific version.<br />
All previous security and maintenance updates for that specific version.</td>
<td>CumulusLinux-4.y.z</td>
<td>Updates only to the specified version (for example, CumulusLinux-4.0.1 would update the switch only to version 4.0.1 and no later.</td>
</tr>
</tbody>
</table>

<!-- vale off -->
The *latest* source is enabled by default. In addition to packages in the Cumulus Linux image, the default configuration provides access to additional packages such as `iperf` or `git`, as well as Cumulus-provided updates for all these packages.
<!-- vale on -->
Security fixes and early access features also go into the latest source.

If you want to change to a more specific distribution (from latest to latest minor release or a specific version), you need to manually edit the `/etc/apt/sources.list`file for both the distribution and the source distribution (deb and deb-src).

You can install Debian packages and Debian source packages from upstream by uncommenting the corresponding lines in `/etc/apt/sources.list`:

    cumulus@switch:~$ cat /etc/apt/sources.list
    # Cumulus Linux package repository
    deb      http://apt.cumulusnetworks.com/repo CumulusLinux-4-latest cumulus upstream netq
    deb-src  http://apt.cumulusnetworks.com/repo CumulusLinux-4-latest cumulus upstream netq
    
    # Debian 10 Buster main package repositories
    # Uncomment these if you want to install upstream Debian packages
    # that are not mirrored in the Cumulus Linux repositories.
    # Packages installed this way may cause problems, and are not
    # officially supported by Cumulus Networks, Inc.
    #deb     http://deb.debian.org/debian buster main
    #deb     http://deb.debian.org/debian buster-updates main
    #deb     http://security.debian.org buster/updates main
    #deb     http://deb.debian.org/debian buster-backports main
    
    # Debian 10 Buster main package source repositories
    # Only need to uncomment these if you want to install
    # upstream Debian source packages
    #deb-src http://deb.debian.org/debian buster main
    #deb-src http://deb.debian.org/debian buster-updates main
    #deb-src http://security.debian.org buster/updates main
    #deb-src http://deb.debian.org/debian buster-backports main
<!-- vale off -->
## Cumulus Linux Versions 3.y.z Repos

Cumulus Linux 3 (including versions 3.0.0 through the latest 3.7.z release) distributions are organized into the following package sources:
<!-- vale on -->

<table>
<thead>
<tr>
<th>Short Name</th>
<th>Contents</th>
<th>Codename</th>
<th>Cumulus Linux Update Version*</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>mainline</strong></td>
<td>All packages in the Cumulus Linux image.<br />
Optional additional packages.<br />
New features and hardware platforms.<br />
All previous security and maintenance updates.</td>
<td>CumulusLinux-3</td>
<td>Minor update (3.y)</td>
</tr>
<tr>
<td><strong>security</strong></td>
<td>Security-related updates to any packages in mainline.</td>
<td>CumulusLinux-3-security-updates</td>
<td>Maintenance update (3.y.z)</td>
</tr>
<tr>
<td><strong>updates</strong></td>
<td>Bug fixes and updates to any packages in mainline that are not security related.</td>
<td>CumulusLinux-3-updates</td>
<td>Maintenance update (3.y.z)</td>
</tr>
<tr>
<td><strong>early access</strong></td>
<td>Packages that are still undergoing development; do not use them in a production environment.</td>
<td>CumulusLinux-3-early-access</td>
<td>Packages updated asynchronously from updates.</td>
</tr>
<tr>
<td><strong>marketplace</strong>**</td>
<td><p>Optional third party packages, (for example, Puppet from Puppet Labs).<br />
Community-contributed packages.</p>
<p><strong>Not affiliated with or related to the NVIDIA Solutions Marketplace.</strong> </p></td>
<td>CumulusLinux-3-marketplace</td>
<td>N/A</td>
</tr>
</tbody>
</table>

\* For more information on Cumulus Linux versioning, refer to {{<link url="Cumulus-Linux-Release-Versioning-and-Support-Policy">}}.

\*\* In development. Does not contain packages as of the Cumulus Linux 3.0 initial release.
<!-- vale off -->
The *mainline*, *security* and *updates* sources are enabled by default. In addition to packages in the Cumulus Linux image, the default configuration provides access to additional packages such as `iperf` or `git`, as well as Cumulus-provided updates for all these packages.
<!-- vale on -->
To maintain access to the latest Cumulus Linux updates, keep the *updates* source enabled.

If you're an early adopter or are testing out new features that are not yet in Cumulus Linux mainline, you can enable the `early-access` source.

You can enable non-default sources by uncommenting the corresponding lines in `/etc/apt/sources.list`:

    cumulus@switch:~$ cat /etc/apt/sources.list
    
    deb     http://repo3.cumulusnetworks.com/repo CumulusLinux-3 cumulus upstream
    deb-src http://repo3.cumulusnetworks.com/repo CumulusLinux-3 cumulus upstream
    
    deb     http://repo3.cumulusnetworks.com/repo CumulusLinux-3-security-updates cumulus upstream
    deb-src http://repo3.cumulusnetworks.com/repo CumulusLinux-3-security-updates cumulus upstream
    
    deb     http://repo3.cumulusnetworks.com/repo CumulusLinux-3-updates cumulus upstream
    deb-src http://repo3.cumulusnetworks.com/repo CumulusLinux-3-updates cumulus upstream
    
    #deb     http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus
    #deb-src http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus
    
    # Currently under construction
    #deb     http://community.cumulusnetworks.com/repo CumulusLinux-3-marketplace commercial community

The contents of each repository component in `sources.list` are as follows:

- **cumulus:** Contains packages maintained by NVIDIA.
- **upstream**: Contains unmodified packages from an upstream community.
- **commercial**: Contains packages from third party vendors.
- **community**: Contains community-contributed packages.
<!-- vale off -->
## Cumulus Linux Versions 1.5.z and 2.y.z Repos

Cumulus Linux distributions for versions 1.5.z and 2.y.z are organized into the following components:
<!-- vale on -->
- **main**: This contains all the packages that are in the Cumulus Linux image, including packages from Debian and other sources.
- **addons**: This contains additional packages that are not in the image (for example, Puppet from Puppet Labs).
- **updates**: This contains updates to any of the packages in main that are not security related.
- **security-updates**: This contains updates to any of the packages in main that are security related.
- **testing**: This contains packages that are still undergoing development.

You can select which repositories you want to draw from using apt by uncommenting the appropriate repos in `/etc/apt/sources.list`:

    cumulus@switch:~$ cat /etc/apt/sources.list
    #  The Cumulus Package Repository.
    #
    #  Only packages from this repository are supported
    #
    #
    
    deb http://repo.cumulusnetworks.com CumulusLinux-2.5 main addons updates
    deb http://repo.cumulusnetworks.com CumulusLinux-2.5 security-updates
    
    # Uncomment the next line to get access to the testing component
    # deb http://repo.cumulusnetworks.com CumulusLinux-2.5 testing
    
    # Uncomment the next line to get access to the Cumulus community repository
    # deb http://repo.cumulusnetworks.com/community/ CumulusLinux-Community-2.5  main addons updates

## Accessing the Repository

To access packages from the repository server, just follow Debian convention and use `apt-get`. You can find details in the [Cumulus Linux user guide]({{<ref "/cumulus-linux-43" >}}).

## Additional Reading

- [Cumulus Linux User Guide: How to install packages using apt-get]({{<ref "/cumulus-linux-43/Installation-Management/Adding-and-Updating-Packages#add-new-packages" >}})
- [Cumulus Linux User Guide: How to enable third party repositories]({{<ref "/cumulus-linux-43/Installation-Management/Adding-and-Updating-Packages#add-packages-from-another-repository" >}})
