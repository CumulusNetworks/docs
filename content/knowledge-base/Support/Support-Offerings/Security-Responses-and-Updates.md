---
title: Security Responses and Updates
author: Cumulus Networks
weight: 705
toc: 4
---

Cumulus Networks believes in the Linux model of security through transparency. Cumulus Networks constantly monitors security advisories and will provide updated packages and notify users when major vulnerabilities affect Cumulus Linux.

Subscribe to the {{<exlink url="https://lists.cumulusnetworks.com/listinfo/cumulus-security-announce" text="Cumulus Networks Security Announcements">}} mailing list so you can receive notification from Cumulus Networks whenever we discover a security issue.

All our security issues are tracked on the mailing list and referenced in {{<link url="Cumulus-Linux-Security-Announcements" text="this article">}}.

## Security Policy

Since Cumulus Linux is based on the Debian distribution, Cumulus Networks will, within a reasonable time frame, address security problems in accordance with the {{<exlink url="http://www.debian.org/security/" text="Debian policies in place">}}.

Every Cumulus Linux release will include all applicable security patches available prior to the build date. Any new vulnerabilities listed by Debian after the release will be evaluated and made available as a package update in the {{<exlink url="http://apt.cumulusnetworks.com/repo" text="Cumulus Linux repository">}}.

## Upgrading Cumulus Linux for Security Updates

When {{<link url="Cumulus-Linux-Security-Announcements" text="Cumulus Networks">}} or {{<exlink url="https://lists.debian.org/debian-security-announce/" text="Debian.org">}} issues a critical security update, Cumulus Networks will update Cumulus Linux and describe the nature of the update in {{<link url="Security" text="an article in the Security section of the knowledge base">}}. Other security fixes are added to the Cumulus repositories without announcements (Debian announces all security updates).

If the article **does not specify a procedure for upgrading Cumulus Linux**, follow these steps instead:

1.  Run `apt-get update`.
2.  Run `apt-get upgrade`.

{{%notice warning%}}

Do not install security patches from Debian directly unless you have consulted with Cumulus Networks directly.

{{%/notice%}}

## Discovering Security Issues

Users who become aware of a security vulnerability in Cumulus Linux should contact Cumulus Networks with details of the vulnerability. Please send descriptions of any vulnerabilities to <security@cumulusnetworks.com>.

Any vulnerability reported through our customers, and not yet reported by {{<exlink url="http://www.debian.org/security/#DSAS" text="Debian">}} will be reported to the Debian security team (<security@debian.org> or <team@security.debian.org>) and a bug will be filed in Debian BTS with a tag of *security*.

In addition, Cumulus Networks will work in conjunction with Debian's
security team to resolve the issue in a timely manner and publish an
advisory as quickly as possible.

## Contacting the Cumulus Networks Security Team

As noted above, please contact us at <security@cumulusnetworks.com> with any security-related questions and issues.
