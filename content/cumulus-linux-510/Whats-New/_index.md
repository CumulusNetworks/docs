---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.10 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.10, see the {{<link title="Cumulus Linux 5.10 Release Notes" text="Cumulus Linux 5.10 Release Notes">}}.
- To upgrade to Cumulus Linux 5.10, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->

Cumulus Linux 5.10 is an Extended-Support Release (ESR). For more information, refer to {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/knowledge-base/Support/Support-Offerings/Cumulus-Linux-Release-Versioning-and-Support-Policy" text="this Knowledge base article">}}.

## What's New in Cumulus Linux 5.10

- {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```

```

{{< /tab >}}
{{< tab "nv set ">}}

```

```

{{< /tab >}}
{{< tab "nv unset ">}}

```

```

{{< /tab >}}
{{< tab "nv action ">}}

```

```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

## Release Considerations

Cumulus Linux 5.10 includes the NVUE object model. After you upgrade to Cumulus Linux 5.10, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
