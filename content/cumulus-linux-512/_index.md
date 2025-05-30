---
title: Cumulus Linux 5.12 User Guide
author: NVIDIA
weight: -42
subsection: true
cascade:
    product: Cumulus Linux
    version: "5.12"
    old: true
toc: 1
---
NVIDIA® Cumulus Linux is the first full-featured {{<exlink url="https://www.debian.org/releases/bookworm/" text="Debian bookworm" >}}-based, Linux operating system for the networking industry.

This user guide provides in-depth documentation on the Cumulus Linux installation process, system configuration and management, network solutions, and monitoring and troubleshooting recommendations. In addition, the quick start guide provides an end-to-end setup process to get you started.

Cumulus Linux 5.12 includes the NVIDIA NetQ agent and CLI. You can use NetQ to monitor and manage your data center network infrastructure and operational health. Refer to the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq" text="NVIDIA NetQ documentation" >}} for details.

For a list of the new features in this release, see {{<link url="Whats-New" text="What's New">}}. For bug fixes and known issues present in this release, refer to the {{<link url="Cumulus-Linux-5.12-Release-Notes" text="Cumulus Linux 5.12 Release Notes">}}.
<!-- vale off -->
## Try It Pre-built Demos
<!-- vale on -->
The Cumulus Linux documentation includes pre-built Try It demos for certain Cumulus Linux features. The Try It demos run a simulation in NVIDIA Air; a cloud hosted platform that works exactly like a real world production deployment. Use the Try It demos to examine switch configuration for a feature. For more information, see {{<link url="Try-It-Pre-built-Demos" text="Try It Pre-built Demos">}}.

## Open Source Contributions

To implement various Cumulus Linux features, NVIDIA has forked various software projects, like CFEngine `Netdev` and some Puppet Labs packages. Some of the forked code resides in the NVIDIA Networking {{<exlink url="https://github.com/CumulusNetworks" text="GitHub repository" >}} and some is available as part of the Cumulus Linux repository as Debian source packages.

NVIDIA has also developed and released new applications as open source. The list of open source projects is on the {{<link title="Cumulus Linux 5.12 Packages" text="Cumulus Linux packages" >}} page.

## Download the User Guide

Use one of the following methods to download the Cumulus Linux user guide and view it offline:

- Host the documentation on a local host {{<exlink url="https://github.com/CumulusNetworks/docs" text="using hugo.">}}
- For a fully functional copy of the user guide, download a zip file of an {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-512/CL512-html.zip" text="HTML documentation build">}} for offline use. Download the desired version, extract it locally, then open `cumulus-linux-512.html` in your web browser.
- To view this user guide as a single page to print to a PDF with limited functionality, click {{% pdf_link "here." %}} Click the link one time and use the web browser print-to-PDF option to save the PDF locally.
