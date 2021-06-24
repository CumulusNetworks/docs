---
title: Removed Commands
author: NVIDIA
weight: 1108
toc: 3
pdfhidden: true
---
This topic lists all commands that have been deprecated from NetQ 1.4.1 and later releases. They are listed alphabetically by command name.

| Command | Alternate Command | Last Available Release |
| --- | --- | --- |
| netq check license, netq show license, netq show unit-tests license | Cumulus Linux license checks are no longer needed in order for NetQ to operate.| 3.3.1 |
| netq check lnv, netq show lnv | LNV was deprecated in Cumulus Linux 3.7.4 and was removed from Cumulus Linux 4.0.0. NetQ continues to support and return LNV data as long as you are running a supported version of Cumulus Linux earlier than 4.0.0). For information on the support timeline, read this [knowledge base article]({{<ref "knowledge-base/Support/Support-Offerings/Cumulus-Linux-Release-Versioning-and-Support-Policy">}}). | 2.4.1 |
| netq config ts (add \| del \| show) (notifier \| server) | netq (add \| del \| show) notification and netq config (add \| del \| show) (agent \| cli server) | 2.1.0 |
| netq config ts (start \| stop \| status \| restart) notifier | None. No longer necessary. | 2.1.0 |
| netq config ts decommission | netq config del agent server | 2.1.0 |
| netq example | netq help | 2.1.0 |
| netq hello | None | 2.4.0 |
| netq resolve | None | 2.1.0 |
| netq-shell | None. The netq-shell has been removed because all NetQ commands can be run from any node where a NetQ Agent is installed. | 2.1.0 |
| netq [\<hostname\>] show docker | netq [\<hostname\>] show kubernetes | 2.1.0 |
| netq update opta config-key \<text-opta-key\> | netq install opta activate-job config-key \<text-opta-key\> | 2.4.0 |
| netq upgrade opta tarball (\<text-tarball-name\> \| download \| download \<text-opta-version\>) [proxy-host \<text-proxy-host\> proxy-port \<text-proxy-port\>] | netq upgrade bundle \<text-bundle-url\>	| 2.4.0 |
| netq query \<wildcard-query\> [json] | None | 1.4.1 |
| netq query show fields \<netq-table\> | None | 1.4.1 |
| netq query show tables | None | 1.4.1 |
