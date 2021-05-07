---
title: Sharing Large Files with Cumulus Networks Support
author: Cumulus Networks
weight: 708
toc: 4
---

Cumulus Networks provides two methods for sharing files with our support team:

- Uploading files directly to the case inside the {{<exlink url="https://support.mellanox.com/s/contact-support-page" text="Web tool">}}
- Using FTP to upload files directly to Cumulus Networks

This article discusses when and how to use FTP to upload files to Cumulus Networks.

## Issue

Sending large files (100MB+) to Cumulus Networks for analysis can require an additional time-consuming transfer to an intermediate device in order to post the file to the support case via the Web tool.

Uploading the output from the `cl-support` utility or other large files directly from your network infrastructure to Cumulus Networks for analysis is sometimes the only method available due to file size or time sensitivity. This option saves you from making an extra transfer to another device and simplifies the process of moving and analyzing large files.

## Solution

To support this process, Cumulus Networks offers an FTP upload option described below.

{{%notice note%}}

Once uploaded, you must inform your support case owner that you have uploaded a file using the FTP upload option.

{{%/notice%}}

1.  In a terminal, FTP to  **ftp.cumulusnetworks.com**, authenticating with user **anonymous** and providing your email address as the password:  

        user@host:~$ ftp ftp.cumulusnetworks.com
        Connected to ftp.cumulusnetworks.com.
        220 ProFTPD 1.3.4a Server (ftp.cumulusnetworks.com) [::ffff:107.170.246.63]
        Name (ftp.cumulusnetworks.com:user): anonymous
        331 Anonymous login ok, send your complete email address as your password
        Password:
        230 Anonymous access granted, restrictions apply
        Remote system type is UNIX.
        Using binary mode to transfer files.

2.  Set the transfer mode to binary:  

        ftp> binary
        200 Type set to I

3.  Use the `put` command to upload the file. In the following example, the file is named `large_file.tar.gz`:  

        ftp> put large_file.tar.gz
        200 PORT command successful
        150 Opening BINARY mode data connection for large_file.tar.gz
        226 Transfer complete
        ftp: 104527608 bytes sent in 142.53Seconds 733.36Kbytes/sec.
        ftp>

    {{%notice note%}}

It is not possible to view the uploaded file due to folder permissions in the upload directory. This is intentional for the sake of privacy and security.

    {{%/notice%}}
