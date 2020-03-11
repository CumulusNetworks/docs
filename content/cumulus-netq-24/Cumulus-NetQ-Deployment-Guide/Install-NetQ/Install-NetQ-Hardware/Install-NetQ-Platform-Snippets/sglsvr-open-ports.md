---
title: Port Access Requirements
author: Cumulus Networks
weight: 
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
toc: 5
---
You must also open the following ports on your NetQ Platform (or platforms if you are planning to deploy a server cluster).

For external connections:

| Port  |  Protocol | Component Access |
| ------: |  :-----: | ----- |
| 8443 |  TCP | Admin UI |
| 443 | TCP | NetQ UI |
| 31980 | TCP | NetQ Agent communication |
| 32708 | TCP | API Gateway |
| 22 | TCP | SSH |

{{%notice tip%}}
Port 32666 is no longer used for the NetQ UI.
{{%/notice%}}
