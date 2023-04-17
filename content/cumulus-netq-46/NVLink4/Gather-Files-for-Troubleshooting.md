---
title: Gather Files for Troubleshooting
author: NVIDIA
weight: 1154
toc: 4
---

Use the UI to generate and download system diagnostic files (sysdump) for L1 and L2 NVSwitches, as well as GFM logs. You can view, download, and delete these files via the file manager.

Get started by selecting the NVL4 icon in the UI header.

## Download Dump Files

To generate and download a system dump as a tar file:

1. From the **Domains** tab, select the **View details**

{{<figure src="/images/netq/file-manager-domains-460.png" alt="" width="1150">}}

2. Navigate to the **Devices** tab.

3. Select up to five switches, then select the **Generate sysdump** icon above the table. It can take several minutes to generate the system dump file.

{{<figure src="/images/netq/generate-sysdump-460.png" alt="" width="1150">}}

4. Downloaded files appear in the file manager, located at the top-right corner of the dashboard. Select it to display a list of files. Choose the files you'd like to download, then select the download icon from above the list.

{{<figure src="/images/netq/file-manager-download-460.png" alt="" width="650">}}

## Download GFM Logs

1. From the **Domains** tab, select **Fetch**.

{{<figure src="/images/netq/fetch-gfm-log-460.png" alt="" width="1000">}}

2. After the log is generated, a download icon {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" alt="download" height="18" width="18">}} appears in place of the Fetch button. Select {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" alt="download" height="18" width="18">}} **Download**.

3. (Optional) You can also view, delete, and download files via the file manager, as described in step 4 of the previous section.