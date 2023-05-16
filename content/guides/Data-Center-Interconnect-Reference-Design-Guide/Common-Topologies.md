---
title: Common DCI Topologies
author: Cumulus Networks
weight: 20
product: Cumulus Networks Guides
imgData: guides
---

## Physical Layer Topologies

## Using a Third-Party Ethernet Services Provider

### MTU and Jumbo Frame Support

### Security

Security is an important design consideration for a DCI service obtained from a 3rd-party provider. Securing an L2 or L3 VPN service, either through a 3rd-party provider or a dark fiber, is essential for customers who place an emphasis on security. 

In the DCI context, security mainly refers to the data security pillar called “Confidentiality.” Confidentiality means that your data is protected from unauthorized access and cannot be altered. There are two main ways to achieve confidentiality on the network layer for a point-to-point line. One of them is IPSEC, which operates on layer 3 of the OSI model and the other is MACsec, which operates on layer 2.

NVIDIA Spectrum-4 supports MACsec encryption {{link to https://resources.nvidia.com/en-us-accelerated-networking-resource-library/ethernet-switches-pr#page=1}}   

IPSEC is not typically used for switching hardware and is usually covered by vendors implementing firewall hardware and software. 

Because MACsec operates at Layer2, MACSEC-encrypted traffic cannot cross a Layer 2 boundary, therefore MACSEC-encrypted traffic cannot be routed across an IP network. The main use case for MACSEC encryption is using a dark-fiber or CWDM / DWDM for DCI.  