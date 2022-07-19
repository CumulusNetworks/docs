---
title: Spanning Tree Protocol
author: NVIDIA
weight: 900
toc: 3
---

You use the Spanning Tree Protocol (STP) in Ethernet-based networks to prevent communication loops when you have redundant paths on a bridge or switch. Loops cause excessive broadcast messages greatly impacting the network performance.

<!-- vale off -->
With NetQ, you can view the STP topology on a bridge or switch to ensure no loops have been created using the `netq show stp topology` command. You can also view the topology information for a prior point in time to see if any changes occurred around then.
<!-- vale on -->

The syntax for the show command is:

```
netq <hostname> show stp topology [around <text-time>] [json]
```

This example shows the STP topology as viewed from the *spine1* switch.

```
cumulus@switch:~$ netq spine1 show stp topology
Root(spine1) -- spine1:sw_clag200 -- leaf2:EdgeIntf(sng_hst2) -- hsleaf21
                                    -- leaf2:EdgeIntf(dual_host2) -- hdleaf2
                                    -- leaf2:EdgeIntf(dual_host1) -- hdleaf1
                                    -- leaf2:ClagIsl(peer-bond1) -- leaf1
                                    -- leaf1:EdgeIntf(sng_hst2) -- hsleaf11
                                    -- leaf1:EdgeIntf(dual_host2) -- hdleaf2
                                    -- leaf1:EdgeIntf(dual_host1) -- hdleaf1
                                    -- leaf1:ClagIsl(peer-bond1) -- leaf2
                -- spine1:ClagIsl(peer-bond1) -- spine2
                -- spine1:sw_clag300 -- edge1:EdgeIntf(sng_hst2) -- hsedge11
                                    -- edge1:EdgeIntf(dual_host2) -- hdedge2
                                    -- edge1:EdgeIntf(dual_host1) -- hdedge1
                                    -- edge1:ClagIsl(peer-bond1) -- edge2
                                    -- edge2:EdgeIntf(sng_hst2) -- hsedge21
                                    -- edge2:EdgeIntf(dual_host2) -- hdedge2
                                    -- edge2:EdgeIntf(dual_host1) -- hdedge1
                                    -- edge2:ClagIsl(peer-bond1) -- edge1
Root(spine2) -- spine2:sw_clag200 -- leaf2:EdgeIntf(sng_hst2) -- hsleaf21
                                    -- leaf2:EdgeIntf(dual_host2) -- hdleaf2
                                    -- leaf2:EdgeIntf(dual_host1) -- hdleaf1
                                    -- leaf2:ClagIsl(peer-bond1) -- leaf1
                                    -- leaf1:EdgeIntf(sng_hst2) -- hsleaf11
                                    -- leaf1:EdgeIntf(dual_host2) -- hdleaf2
                                    -- leaf1:EdgeIntf(dual_host1) -- hdleaf1
                                    -- leaf1:ClagIsl(peer-bond1) -- leaf2
                -- spine2:ClagIsl(peer-bond1) -- spine1
                -- spine2:sw_clag300 -- edge2:EdgeIntf(sng_hst2) -- hsedge21
                                    -- edge2:EdgeIntf(dual_host2) -- hdedge2
                                    -- edge2:EdgeIntf(dual_host1) -- hdedge1
                                    -- edge2:ClagIsl(peer-bond1) -- edge1
                                    -- edge1:EdgeIntf(sng_hst2) -- hsedge11
                                    -- edge1:EdgeIntf(dual_host2) -- hdedge2
                                    -- edge1:EdgeIntf(dual_host1) -- hdedge1
                                    -- edge1:ClagIsl(peer-bond1) -- edge2
```

If you do not have a bridge in your configuration, the output indicates such.
