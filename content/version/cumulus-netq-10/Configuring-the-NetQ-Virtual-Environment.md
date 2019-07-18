---
title: Configuring the NetQ Virtual Environment
author: Cumulus Networks
weight: 27
aliases:
 - /display/NETQ10/Configuring-the-NetQ-Virtual-Environment
 - /pages/viewpage.action?pageId=6488222
pageID: 6488222
product: Cumulus NetQ
version: 1.0.0
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
---
A virtual NetQ demo environment is available on the [Cumulus Networks
GitHub site](https://github.com/CumulusNetworks/netqdemo-1.0), allowing
you to try out NetQ on your own, or to test/validate updates to your
network before deploying them into production.

The environment uses a series of Cumulus VX virtual machines built using
the Cumulus Networks [reference
topology](https://github.com/cumulusnetworks/cldemo-vagrant). This
section provides high level instructions for installing and configuring
the virtual environment.

## <span>Setting up the Demo Environment with Vagrant and VirtualBox</span>

{{%notice note%}}

These steps assume that both Vagrant and VirtualBox have been
downloaded. For more information on downloading Vagrant and VirtualBox,
refer to the [Cumulus VX Getting Started](/cumulus-vx/Getting-Started/)
documentation.

{{%/notice%}}

1.  Download the NetQ Telemetry Server, available from the *NetQ
    Virtual* option in the **Product** menu of the [Cumulus Networks
    website](https://cumulusnetworks.com/downloads/).

2.  In a terminal, add the NetQ Telemetry Server to Vagrant:

        user@machine:~$ vagrant box add cumulus-netq-telemetry-server-amd64-1.0.0-vagrant.box --name=cumulus/ts

3.  Clone the demo:

        user@machine:~$ git clone https://github.com/cumulusnetworks/netqdemo-1.0 netqdemo

4.  From the `netqdemo` directory, run the `vagrant up` command to start
    the demo.

        user@machine:~$ cd netqdemo
        user@machine:~/netqdemo$ vagrant up

5.  Once the vagrant instance has started, ssh into the NetQ Telemetry
    Server, which serves as the `oob-mgmt-server` in the topology:

        user@machine:~$ vagrant ssh oob-mgmt-server

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

<script src="js/lunr.js"></script>

<script src="js/lunr-extras.js"></script>

<script src="assets/js/scroll-search.js"></script>
