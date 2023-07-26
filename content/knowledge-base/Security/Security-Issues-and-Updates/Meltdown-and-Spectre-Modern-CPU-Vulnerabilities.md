---
title: Meltdown and Spectre - Modern CPU Vulnerabilities
author: NVIDIA
weight: 458
toc: 4
---

{{%notice info%}}
Cumulus Networks released patches that fix these vulnerabilities. For information on how to apply the patches, read {{<link url="Spectre-and-Meltdown-Vulnerability-Fixes" text="this article">}}.
{{%/notice%}}
<!--
{{%notice note%}}
This issue was announced on the Cumulus Networks {{<exlink url="https://lists.cumulusnetworks.com/pipermail/cumulus-security-announce/2018-January/000011.html" text="security announcement mailing list">}}
on January 4, 2018.
{{%/notice%}}
-->
CPU hardware implementations are vulnerable to side-channel attacks referred to as Meltdown and Spectre. The following organizations describe these attacks in detail:

- CERT/CC's Vulnerability Note {{<exlink url="https://www.kb.cert.org/vuls/id/584653" text="VU#584653">}}.
- The United Kingdom National Cyber Security Centre's guidance on Meltdown and Spectre.
- Google Project Zero (link is external).
- Institute of Applied Information Processing and Communications (IAIK) at Graz University of Technology (TU Graz). They refer to the Linux kernel mitigations for this vulnerability as KAISER, and subsequently KPTI, which aim to improve separation of kernel and user memory pages.

The Common Vulnerabilities and Exposures formally associated with Meltdown and Spectre are:

- {{<exlink url="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753" text="CVE-2017-5753">}}: Bounds check bypass (Spectre)
- {{<exlink url="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715" text="CVE-2017-5715">}}: Branch target injection (Spectre)
- {{<exlink url="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754" text="CVE-2017-5754">}}: Rogue data cache load (Meltdown)

To exploit these vulnerabilities in Cumulus Linux, an attacker needs to have local access to the system.

<!--NVIDIA is evaluating, porting, and testing patches to Cumulus Linux. NVIDIA can release software updates as soon as they become available, and is going to announce any updates on the {{<exlink url="https://lists.cumulusnetworks.com/listinfo/cumulus-security-announce" text="cumulus-security-announce">}} mailing list. At this point, the performance impact of the fixes is unclear; the extent of the impact depends on the operating system, the nature of the fix and the workload of the system.-->