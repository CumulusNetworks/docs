---
title: Security Responses and Updates
author: Cumulus Networks
weight: 705
toc: 4
---

NVIDIA believes in the Linux model of security through transparency. NVIDIA constantly monitors security advisories and provides updated packages and notifies users when major vulnerabilities affect Cumulus Linux.

<!--Subscribe to the {{<exlink url="https://lists.cumulusnetworks.com/listinfo/cumulus-security-announce" text="Cumulus Networks Security Announcements">}} mailing list so you can receive notification from NVIDIA whenever the team discovers a security issue.

NVIDIA tracks all security issues on the mailing list and references them in {{<link url="Cumulus-Linux-Security-Announcements" text="this article">}}.-->

## Security Policy
<!-- vale off -->
Because Cumulus Linux is based on Debian, NVIDIA will, within a reasonable time frame, address security problems that adhere to the {{<exlink url="http://www.debian.org/security/" text="Debian policies in place">}}.
<!-- vale on -->
Every Cumulus Linux release includes all applicable security patches available before the build date. NVIDIA evaluates any new vulnerabilities listed by Debian after the release and addresses them in a package update in the {{<exlink url="http://apt.cumulusnetworks.com/repo" text="Cumulus Linux repository">}}.

## Upgrading Cumulus Linux for Security Updates

When {{<link url="Cumulus-Linux-Security-Announcements" text="NVIDIA">}} or {{<exlink url="https://lists.debian.org/debian-security-announce/" text="Debian.org">}} issue a critical security update, NVIDIA updates Cumulus Linux and describes the nature of the update in {{<link url="Security" text="an article in the Security section of the knowledge base">}}. NVIDIA adds other security fixes to the Cumulus Linux repositories without announcements (Debian announces all security updates).

If the article **does not specify a procedure for upgrading Cumulus Linux**, follow these steps instead:

1.  Run `apt-get update`.
2.  Run `apt-get upgrade`.

{{%notice warning%}}

Do not install security patches from Debian directly unless you have consulted with NVIDIA directly.

{{%/notice%}}

## Discovering Security Issues

Users who become aware of a security vulnerability in Cumulus Linux should contact NVIDIA with details of the vulnerability. Send descriptions of any vulnerabilities to <security@cumulusnetworks.com>.

Any vulnerability reported through customers, and not yet reported by {{<exlink url="http://www.debian.org/security/#DSAS" text="Debian">}} get reported to the Debian security team (<security@debian.org> or <team@security.debian.org>). As a result, a bug gets filed in Debian BTS with a tag of *security*.

In addition, NVIDIA works in conjunction with Debian's security team to resolve the issue and publish an advisory as quickly as possible.

## Contacting the NVIDIA Security Team

As noted above, contact <security@cumulusnetworks.com> with any security-related questions and issues.
