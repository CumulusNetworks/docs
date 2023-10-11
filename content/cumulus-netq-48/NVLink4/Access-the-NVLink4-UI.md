---
title: Access the NVLink4 UI
author: NVIDIA
weight: 1010
toc: 3

---

You can access NVLink4 features via the NetQ UI. This section describes how to log in to NetQ and access NVLink4 UI features, which are hidden by default.

## Log in to NetQ

1. Open a new Chrome or Firefox browser window or tab.
2. Enter the following URL into the address bar: *https://\<hostname-or-ipaddress\>:443*  

 {{<figure src="/images/netq/splashscreen-480.png" alt="NetQ login screen" width="700">}}

3. Log in. 

    The default username and password for UI access is *admin, admin*

After creating a new password and accepting the Terms of Use, the default workbench opens with your username displayed in the upper-right corner.

## Access NVLink4

To reveal NVLink4 in the UI, run `netq features nvl4 enable` on your NetQ server CLI. Return to the UI and refresh the page. The NVL4 icon now appears in the header:

{{<figure src="/images/netq/nvl4-header-450.png" alt="" width="950">}}

To verify that NVLink4 features are enabled, run `netq show features nvl4`.

To hide the NVLink4 features in the UI, run `netq features nvl4 disable`.

