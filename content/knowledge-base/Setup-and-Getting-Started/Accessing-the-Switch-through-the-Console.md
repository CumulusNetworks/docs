---
title: Accessing the Switch through the Console
author: Cumulus Networks
weight: 101
toc: 3
---

Any switch on the Cumulus Networks {{<exlink url="https://cumulusnetworks.com/support/hcl/" text="HCL">}} can be accessed via the console. The standard command to use for console access depends on your host operating system.

For MacOS:

    screen /dev/cu.usbserial 115200

For Linux:

    picocomm -b 115200 /dev/ttyUSB0

USB0 can be USB1 or USB2, and so forth.

Most switches on the Cumulus Networks HCL are set at either 9600 or 115200. This depends on the factory setting.
