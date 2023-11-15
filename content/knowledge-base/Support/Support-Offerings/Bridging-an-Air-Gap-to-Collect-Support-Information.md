---
title: Bridging an Air Gap to Collect Support Information
author: NVIDIA
weight: 715
toc: 4
---

Often it is not possible to transfer files off of a switch that you are analyzing. One unique opportunity that Cumulus Linux offers is the ability to collect this information via a text console; even for files which do not contain text. This document highlights a technique to share smaller (\~2MB or less) packet captures or `cl-support` files in text-based form using a console to extract the packet capture from the isolated network device.

## Issue

Networks isolated by an air gap are common. However, this necessary security measure can impede rapid troubleshooting of network issues when collecting and exchanging packet captures from the affected devices.

## Cause

An air gap or air wall is a network security measure employed on one or more computers to ensure that a secure computer network is physically isolated from unsecured networks, such as the public Internet or an unsecured LAN.

## Resolution

By using the process below, you can encode a collected Packet Capture (PCAP) or `cl-support` file into base64 encoding, which you can exchange across the air gap and then decode it back into the original file.

{{%notice note%}}

You can get the best results when performing this process with already compressed files, although it is not a requirement.

{{%/notice%}}

1.  Collect traffic of interest into a Packet Capture (PCAP) file using `tcpdump` or generate a `cl-support` file with the `cl-support` utility.

2.  Encode the PCAP (or cl-support) file into base64 encoding:  

        cumulus@switch$ base64 ./traffic.pcap
        obLD1AACAAQAAAAAAAAAAAAA//8AAAAB7gAAABCAAAAQkQ4OQBJzEQ4OQBKTQgARcAA
        --snip--
        QkQ4OQBJAxgAAAAFAAAAAwAD0JAAA9CQAAAAAA==

3.  Copy the encoded base64 text across the air gap and insert the text
    into a text file on another Linux system.

4.  Re-encode the base64 textfile into the original PCAP file:  

        user@device$ base64 --decode ./textfile.txt > traffic.pcap

5.  Analyze the traffic capture in your preferred tool:

        user@device$ wireshark traffic.pcap
