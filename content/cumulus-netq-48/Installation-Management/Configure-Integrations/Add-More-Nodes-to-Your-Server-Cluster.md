---
title: Add More Nodes to Your Server Cluster
author: NVIDIA
weight: 395
toc: 3
---

You can add additional nodes to your server cluster on-premises and cloud deployments using the CLI:

{{<tabs "addworkerCLI">}}

{{<tab "On-premises Deployments">}}

Run the following CLI command to add a new worker node for on-premises deployments:

```
netq install cluster add-worker <text-worker-01>
```

{{</tab>}}

{{<tab "Cloud Deployments">}}

Run the following CLI command to add a new worker node for cloud deployments:

```
netq install opta cluster add-worker <text-worker-01>
```

{{</tab>}}

{{</tabs>}}