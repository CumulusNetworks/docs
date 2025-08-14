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

NVIDIA® Cumulus Linux is the first full-featured Linux operating system for the networking industry. The {{<exlink url="https://www.debian.org/releases/jessie/" text="Debian Jessie" >}}-based, networking-focused distribution runs on hardware produced by a broad partner ecosystem, ensuring unmatched customer choice regarding silicon, optics, cables, and systems.

This user guide provides in-depth documentation on the Cumulus Linux installation process, system configuration and management, network solutions, and monitoring and troubleshooting recommendations. In addition, the quick start guide provides an end-to-end setup process to get you started.

## What's New in this Release

For a list of the new features in this release, see {{<link url="Whats-New" text="What's New">}}. For bug fixes and known issues present in this release, refer to the {{<link url="Cumulus-Linux-3.7-Release-Notes" text="Cumulus Linux 3.7 Release Notes">}}.

## Open Source Contributions

To implement various Cumulus Linux features, Cumulus Networks has forked various software projects, like CFEngine, `Netdev` and some Puppet Labs packages. The forked code resides in the Cumulus Networks {{<exlink url="https://github.com/CumulusNetworks" text="GitHub repository" >}}.

## Extended Support Release

This version of Cumulus Linux is an Extended Support Release (ESR). Cumulus Linux 3.7 ESR started with Cumulus Linux 3.7.12 and all future releases in the 3.7 product family will all be ESR releases. To learn about ESR, please read [this article]({{<ref "/knowledge-base/Support/Support-Offerings/Cumulus-Linux-Release-Versioning-and-Support-Policy" >}}).

The PDF of the 3.7.12 ESR user guide is available {{% pdf_link "here." %}} PDFs of pre-ESR 3.7 versions are available below.

| Cumulus Linux Version | Download the User Guide     |
| --------------------- | --------------------------- |
| 3.7.7                 | {{<exlink url="https://drive.google.com/file/d/1yuEINc9hfLlFT6TCFtKQoVF2XkCW3HrX/view?usp=sharing" text="3.7.7 PDF" >}} |
| 3.7.6                 | {{<exlink url="https://drive.google.com/file/d/1cAebIz7Da9zcGpxcMmWZo_kSXzu4j_nw/view?usp=sharing" text="3.7.6 PDF" >}} |
| 3.7.5                 | {{<exlink url="https://drive.google.com/file/d/12_T1n8nf1e4oEF1tEiSl7Hv8yvxf8xE_/view?usp=sharing" text="3.7.5 PDF" >}} |
| 3.7.4                 | {{<exlink url="https://drive.google.com/file/d/1ahhyXTuTvLOK13T557wB0j3cLFsiXyk-/view?usp=sharing" text="3.7.4 PDF" >}} |
| 3.7.3                 | {{<exlink url="https://drive.google.com/file/d/1TjcZiGyJs5zcTr37h1cQJdNWcMP9WoiS/view?usp=sharing" text="3.7.3 PDF" >}} |
| 3.7.2                 | {{<exlink url="https://drive.google.com/file/d/1kJSHYGwVpFSJ7o3nrgsYFoWBZuT4obzl/view?usp=sharing" text="3.7.2 PDF" >}} |
| 3.7.0                 | {{<exlink url="https://drive.google.com/file/d/1qm08ZEe1XoO5UUMwAm8aGIh3zEkyxTjB/view?usp=sharing" text="3.7.0 PDF" >}} |
