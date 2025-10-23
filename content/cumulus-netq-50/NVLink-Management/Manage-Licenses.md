---
title: Manage Licenses
author: NVIDIA
weight: 1005
toc: 3
---

NetQ for NVLink includes an evaluation license that is automatically applied during the initial installation. The license is valid for 60 days. After it expires, you need to apply a new license to continue accessing the API.


## Download the License

1. Log in to the {{<exlink url="http://ui.licensing.nvidia.com/" text="NVIDIA Licensing Portal">}}.
2. From the menu, select **Entitlements&nbsp;<span aria-label="and then">></span> Networking**.
3. Locate the license file. From the *Actions* column, select the three-dot menu to download the license. 


## Apply a New License

1. Upload the new license file to `/opt/netq-admin/nvl/licenses`. 
2. Run the following script:

```
/opt/netq-admin/nvl/scripts/license-config.sh
```
3. When prompted, select the first option: **Apply new license (replace existing)**
4. Select the license file and confirm that the new license details are correct.

The script concurrently applies the new license and replaces the previous one.

## View License Details

To view license details, including license type, issue date, and expiration date:

1. Run the following script:

``` 
/opt/netq-admin/nvl/scripts/license-config.sh
```

2. When prompted, select the second option, **Get active license information**. 


## Receive License Notifications

If you have configured a webhook receiver<!--link out to Alerts Management-->, you will receive a notification when your license is about to expire or has already expired. These notifications are sent every 24 hours until the license status is updated.

NetQ for NVLink broadcasts two types of license notifications: expires soon and expired.

- *Expires soon* indicates that the license will expire within 60 days. The notification includes the following parameters:
    - Job: `licensing`
    - Alert name: `LicenseValidation`
    - Severity: `warning`
- *Expired* indicates the license is expired. The notification includes the following parameters:
    - Job: `licensing`
    - Alert name: `LicenseValidation`
    - Severity: `critical`