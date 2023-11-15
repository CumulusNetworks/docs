---
title: Security Responses and Updates
author: NVIDIA
weight: 705
toc: 4
---

NVIDIA believes in the Linux model of security through transparency. NVIDIA constantly monitors security advisories and provides updated packages and notifies users when major vulnerabilities affect Cumulus Linux.

<!--Subscribe to the {{<exlink url="https://lists.cumulusnetworks.com/listinfo/cumulus-security-announce" text="Cumulus Security Announcements">}} mailing list so you can receive notification from NVIDIA whenever the team discovers a security issue.-->

## Security Policy
<!-- vale off -->
Because Cumulus Linux is based on Debian, NVIDIA will, within a reasonable time frame, address security problems that adhere to the {{<exlink url="http://www.debian.org/security/" text="Debian policies in place">}}.
<!-- vale on -->
Every Cumulus Linux release includes all applicable security patches available before the build date. NVIDIA evaluates any new vulnerabilities listed by Debian after the release and addresses them in a package update in the {{<exlink url="http://apt.cumulusnetworks.com/repo" text="Cumulus Linux repository">}}.

## Upgrading Cumulus Linux for Security Updates

When {{<exlink url="https://lists.debian.org/debian-security-announce/" text="Debian.org">}} issue a critical security update, NVIDIA updates Cumulus Linux. NVIDIA adds other security fixes to the Cumulus Linux repositories (Debian announces all security updates).

If the article **does not specify a procedure for upgrading Cumulus Linux**, follow these steps instead:

1.  Run `apt-get update`.
2.  Run `apt-get upgrade`.

{{%notice warning%}}

Do not install security patches from Debian directly unless you have consulted with NVIDIA directly.

{{%/notice%}}

## Discovering Security Issues

If you become aware of a security vulnerability in Cumulus Linux, contact NVIDIA with details of the vulnerability.
