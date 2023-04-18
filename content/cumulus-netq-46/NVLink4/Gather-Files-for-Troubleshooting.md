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

1. From the **Domains** tab, select the **View details** button.

{{<figure src="/images/netq/file-manager-domains-460.png" alt="" width="1150">}}

2. Navigate to the **Devices** tab.

3. Select up to five switches, then select **Generate sysdump** {{<img src="/images/netq/generate-sysdump-icon.svg" alt="" height="18" width="18">}} above the table. It can take several minutes to generate the system dump file.

4. After the file is generated, a download icon {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" alt="download" height="18" width="18">}} appears above the devices table. Select it to download the file(s).

{{<figure src="/images/netq/downloadsysdumps-460.png" alt="" width="1150">}}

Alternately, download the files via the file manager, located at the top-right corner of the dashboard. Click the file manager, then choose the files you'd like to download. Download them by selecting the download icon {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" alt="download" height="18" width="18">}} from above the list of files.

{{<figure src="/images/netq/file-manager-download-460.png" alt="" width="450">}}

Note that you can download and delete all generated files---including sysdumps and GFM logs---via the file manager.

## Download GFM Logs

1. From the **Domains** tab, select the **Fetch** button.

{{<figure src="/images/netq/fetch-gfm-log-460.png" alt="" width="900">}}

2. After the log is generated, a download icon {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" alt="download" height="18" width="18">}} appears in place of the Fetch button. Select it to download the files.