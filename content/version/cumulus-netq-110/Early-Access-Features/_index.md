---
title: Early Access Features
author: Cumulus Networks
weight: 33
aliases:
 - /display/NETQ110/Early-Access-Features
 - /pages/viewpage.action?pageId=7111337
pageID: 7111337
product: Cumulus NetQ
version: 1.1.0
imgData: cumulus-netq-110
siteSlug: cumulus-netq-110
---
NetQ has [early
access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878-Early-Access-Features-Defined)
features that provide advanced access to new functionality before it
becomes generally available. The following features are early access in
NetQ 1.1:

In NetQ 1.1, early access features are bundled into the `netq-apps`
package; there is no specific EA package like there typically is with
Cumulus Linux. You can enable early access features by running the `netq
config add experimental` command.

{{%notice tip%}}

For NetQ 1.1, the only feature enabled by this command is for the
[custom
commands](/version/cumulus-netq-110/Early-Access-Features/Extending-NetQ-with-Custom-Commands).

There is nothing to enable for Facebook Backpack; however, the chassis
is considered to be an early access feature, so do not run NetQ on it in
production.

{{%/notice%}}

You can disable the early access features by running the `netq config
del experimental` command.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
