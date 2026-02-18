---
title: Manage Licenses
author: NVIDIA
weight: 850
toc: 3
---

NetQ for NVLink includes an evaluation license that is automatically applied during the initial installation. The license is valid for 60 days. After it expires, you need to apply a new subscription license to continue accessing the API.


## Download the License and the License Update Script

You will need to download two files: the license file and the license update script.

1. Log in to the {{<exlink url="http://nvid.nvidia.com/" text="NVIDIA Application Hub">}}. From there, navigate to the {{<exlink url="https://ui.licensing.nvidia.com/" text="NVIDIA Licensing Portal">}}.
2. Download the license.
3. Next, download the `license-update.sh` script. Select **Software Downloads** from the side menu.
4. In the search field above the table, enter **NetQ**.
5. Locate and download the latest *NetQ License Update* file.
6. Copy the `license-update.sh` script to the `/opt/netq-admin/nvl/scripts` directory.


## Apply a New License

1. Create the `/opt/netq-admin/nvl/licenses` directory.
2. Upload the new license file to `/opt/netq-admin/nvl/licenses`. 
3. Run the following script:

```
/opt/netq-admin/nvl/scripts/license-update.sh
```
4. When prompted, select the first option: **Apply new license (replace existing)**
5. Select the license file and confirm that the new license details are correct.

The script concurrently applies the new license and replaces the previous one.

<!--RM 4888290 broke ability to view license
## View License Details

To view license details, including license type, issue date, and expiration date:

1. Run the following script:

``` 
/opt/netq-admin/nvl/scripts/license-config.sh
```

2. When prompted, select the second option, **Get active license information**. 
-->

## Receive License Alerts

If you have {{<link title="Manage Alerts" text="configured a webhook receiver">}} you will receive a notification when your license is about to expire or has already expired. These notifications are sent every 24 hours until the license status is updated.