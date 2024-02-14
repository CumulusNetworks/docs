---
title: Cumulus Linux 5.6 User Guide
author: NVIDIA
weight: -42
subsection: true
cascade:
    product: Cumulus Linux
    version: "5.6"
    old: true
toc: 1
---
NVIDIA® Cumulus Linux is the first full-featured {{<exlink url="https://www.debian.org/releases/buster/" text="Debian Buster" >}}-based, Linux operating system for the networking industry.

This user guide provides in-depth documentation on the Cumulus Linux installation process, system configuration and management, network solutions, and monitoring and troubleshooting recommendations. In addition, the quick start guide provides an end-to-end setup process to get you started.

Cumulus Linux 5.6 includes the NVIDIA NetQ agent and CLI. You can use NetQ to monitor and manage your data center network infrastructure and operational health. Refer to the [NVIDIA NetQ documentation]({{<ref "/cumulus-netq-47" >}}) for details.

For a list of the new features in this release, see {{<link url="Whats-New" text="What's New">}}. For bug fixes and known issues present in this release, refer to the {{<link url="Cumulus-Linux-5.6-Release-Notes" text="Cumulus Linux 5.6 Release Notes">}}.
<!-- vale off -->
## Try It Pre-built Demos
<!-- vale on -->
The Cumulus Linux documentation includes pre-built Try It demos for certain Cumulus Linux features. The Try It demos run a simulation in NVIDIA Air; a cloud hosted platform that works exactly like a real world production deployment. Use the Try It demos to examine switch configuration for a feature. For more information, see {{<link url="Try-It-Pre-built-Demos" text="Try It Pre-built Demos">}}.

## Open Source Contributions

To implement various Cumulus Linux features, NVIDIA has forked various software projects, like CFEngine `Netdev` and some Puppet Labs packages. Some of the forked code resides in the NVIDIA Networking {{<exlink url="https://github.com/CumulusNetworks" text="GitHub repository" >}} and some is available as part of the Cumulus Linux repository as Debian source packages.

NVIDIA has also developed and released new applications as open source. The list of open source projects is on the {{<link title="Cumulus Linux 5.6 Packages" text="Cumulus Linux packages" >}} page.

## Hardware Compatibility List

You can find the most up-to-date hardware compatibility list (HCL) {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="here" >}}. Use the HCL to confirm that Cumulus Linux supports your switch model. The HCL lists products by port configuration, manufacturer and SKU part number.

## Download the User Guide

Use one of the following methods to download the Cumulus Linux user guide and view it offline:

- Host the documentation on a local host {{<exlink url="https://github.com/CumulusNetworks/docs" text="using hugo.">}}
- Download a zip file of an {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-56/CL56-html.zip" text="HTML documentation build">}} for offline use. Download the desired version, extract it locally, then open `cumulus-linux-56.html` in your web browser.<!-- vale off -->
<!-- - You can view the complete Cumulus Linux {{% version %}} user guide as a single page to print to PDF {{% pdf_link "here." %}} Click on the link one time and use the web browser print-to-PDF option to save the PDF locally.-->
<!-- vale on -->