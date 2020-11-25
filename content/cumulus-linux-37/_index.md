---
title: Cumulus Linux 3.7 User Guide
author: NVIDIA
weight: -37
pageID: 8362527
subsection: true
cascade:
    product: Cumulus Linux
    version: "3.7"
    imgData: cumulus-linux
    siteSlug: cumulus-linux
    old: true
    esr: true
---

NVIDIA® Cumulus Linux is the first full-featured Linux operating system for the networking industry. The {{<exlink url="https://www.debian.org/releases/jessie/" text="Debian Jessie" >}}-based, networking-focused distribution runs on hardware produced by a {{<exlink url="https://cumulusnetworks.com/hcl/" text="broad partner ecosystem" >}}, ensuring unmatched customer choice regarding silicon, optics, cables, and systems.

This user guide provides in-depth documentation on the Cumulus Linux installation process, system configuration and management, network solutions, and monitoring and troubleshooting recommendations. In addition, the quick start guide provides an end-to-end setup process to get you started.

## What's New in this Release

For a list of the new features in this release, see {{<link url="Whats-New" text="What's New">}}. For bug fixes and known issues present in this release, refer to the {{<link url="Cumulus-Linux-3.7-Release-Notes" text="Cumulus Linux 3.7 Release Notes">}}.

## Open Source Contributions

To implement various Cumulus Linux features, Cumulus Networks has forked various software projects, like CFEngine, `Netdev` and some Puppet Labs packages. The forked code resides in the Cumulus Networks {{<exlink url="https://github.com/CumulusNetworks" text="GitHub repository" >}}.

<!-- Cumulus Networks has also developed and released new applications as
open source. The list of open source projects is on the
{{ /* link title="Cumulus Linux 3.7 Open Source Packages" text="open source software" */}} page.-->

## Hardware Compatibility List

You can find the most up-to-date hardware compatibility list (HCL)
{{<exlink url="https://cumulusnetworks.com/hcl/" text="here" >}}. Use the HCL to confirm that
your switch model is supported by Cumulus Linux. The HCL is updated
regularly, listing products by port configuration, manufacturer, and SKU
part number.

## Stay up to Date

- Subscribe to our {{<exlink url="https://lists.cumulusnetworks.com/listinfo/cumulus-product-bulletin" text="product bulletin" >}} mailing list to receive important announcements and updates about issues that arise in our products.
- Subscribe to our {{<exlink url="https://lists.cumulusnetworks.com/listinfo/cumulus-security-announce" text="security announcement" >}} mailing list to receive alerts whenever we update our software for security issues.

## Extended Support Release

This version of Cumulus Linux is an Extended Support Release (ESR). Cumulus Linux 3.7 ESR started with Cumulus Linux 3.7.12 and all future releases in the 3.7 product family will all be ESR releases. To learn about ESR, please read {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Support/Support-Offerings/Cumulus-Linux-Release-Versioning-and-Support-Policy/" text="this article">}}.

The PDF of the 3.7.12 ESR user guide is available {{% pdf_link "here." %}} PDFs of pre-ESR 3.7 versions are available below.

| Cumulus Linux Version | Download the User Guide     |
| --------------------- | --------------------------- |
| 3.7.7                 | {{<exlink url="https://drive.google.com/file/d/1EspnJCZXOa3QO2cRJV-qbPWMumKZBtKC/view?usp=sharing" text="3.7.7 PDF" >}} |
| 3.7.6                 | {{<exlink url="https://drive.google.com/file/d/1kbtD3xWh0PTj3i9tiOhYnCGAAQZ159qZ/view?usp=sharing" text="3.7.6 PDF" >}} |
| 3.7.5                 | {{<exlink url="https://drive.google.com/file/d/16TSphHeKpVhsE80DZQJbpExqMGcScDB1/view?usp=sharing" text="3.7.5 PDF" >}} |
| 3.7.4                 | {{<exlink url="https://drive.google.com/file/d/1AWaamaEO7NhwcwZRaxQgWRWrKQyq8hjM/view?usp=sharing" text="3.7.4 PDF" >}} |
| 3.7.3                 | {{<exlink url="https://drive.google.com/file/d/1xK7qWGZsj688opVmVsstb45XN3qKTXgc/view?usp=sharing" text="3.7.3 PDF" >}} |
| 3.7.2                 | {{<exlink url="https://drive.google.com/file/d/1WChlCxlwJVJ7T2l6l2Mve3M5O4jfYSYo/view?usp=sharing" text="3.7.2 PDF" >}} |
| 3.7.0                 | {{<exlink url="https://drive.google.com/file/d/1iUt4m8NaoejBFHWxboCB5O7DY7n7uLHo/view?usp=sharing" text="3.7.0 PDF" >}} |
