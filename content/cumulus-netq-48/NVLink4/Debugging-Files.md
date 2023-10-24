---
title: Debugging Files
author: NVIDIA
weight: 1153
toc: 3

---

Use the NetQ UI to generate and download diagnostic files for debugging. You can generate system dumps for NVLink L1 and L2 switches and GFM logs for a given domain. Note that after you delete a domain, you will not be able to generate or download debugging files and any files previously generated for the domain will also be deleted.

## Create and Download a System Dump

1. From the NVLink4 management dashboard, locate the domain and select the **View details** button.

2. Navigate to the **Devices** tab.

3. Select up to 5 devices, then select the **Generate sysdump** icon above the table. 

{{<figure src="/images/netq/gen-sysdump-480.png" alt="" width="700">}}

You can monitor the progress of the system dump file in the **Sysdump file status** column. If the system dump file fails to generate, the column indicates a failed status along with a tooltip indicating the reason for the failure.

4. Open the **File manager** at the top of the screen.

{{<figure src="/images/netq/file-manager-button-480.png" alt="" width="400">}}

5. Select the files you'd like to download, then select the download icon above the table. 

{{<figure src="/images/netq/file-manager-pop-480.png" alt="" width="700">}}

## Create and Download GFM Log Files

1. Generate GFM logs by selecting the **Fetch** button on a given domain.

{{<figure src="/images/netq/gfm-fetch-480.png" alt="" width="1100">}}

2. After the file is generated, a download icon appears in place of the **Fetch** button. Select the icon to download the logs. You can also download the file via the file manager, as described in the previous section.
  