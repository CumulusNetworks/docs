---
title: Accessing the Switch through the Console
author: NVIDIA
weight: 101
toc: 3
---

You can access any NVIDIA switch through the console. The standard command to use for console access depends on your host operating system.

For MacOS:

    screen /dev/cu.usbserial 115200

For Linux:

    picocomm -b 115200 /dev/ttyUSB0

USB0 can be USB1 or USB2, and so forth.
