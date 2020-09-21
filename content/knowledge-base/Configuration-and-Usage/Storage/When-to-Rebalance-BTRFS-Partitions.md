---
title: When to Rebalance BTRFS Partitions
author: Cumulus Networks
weight: 451
toc: 4
---

Customers running Cumulus Linux, 3.y.z, which uses BTRFS (the b-tree file system), might experience issues with disk space management. This is a known problem of BTRFS because it does not perform periodic garbage collection, or rebalancing. If left unattended, these errors can make it impossible to rebalance the partitions on the disk. To avoid this issue, Cumulus Networks recommends rebalancing the BTRFS partitions in a preemptive manner, but only when absolutely needed to avoid reduction in the lifetime of the disk. By tracking the state of the disk space usage, users can determine when rebalancing should be performed.

This article describes one approach to determine the proper time to perform a BTRFS rebalance.

## Issue Presentation

The issue presents itself when BTRFS is running and just the right pattern of disk I/O and file sizes are present. This causes inefficient use of the disk space and ultimately prevents new writes to the disk. The issue is indicated by the receipt of "No space left on device" errors.

## When to Rebalance

There are several factors to consider when determining when a rebalance should be performed:

- How often should a check be performed?
- Does the partition have a large amount of allocated space?
- Would a rebalance free up any space?

### Check Interval

It is assumed that this problem happens gradually, with just the right disk I/O over a long period of time. The expectation is that the time period from "everything is fine" to "no space left" (even though there is not much data on the device), is at least one week. The smaller this time period is, the more frequently the check must be performed. While the check does not incur significant disk I/O, it does consume some, as well as CPU cycles. Therefore, it is desired that the check be done as infrequently as possible.

### Allocated Space Check

There is no need to execute a rebalance if BTRFS has not allocated a significant portion of the partition. A 15 GB partition in which BTRFS has allocated only 4 GB has plenty of unallocated space and is in no need of a rebalance. A rebalance on such a volume would free up little or no allocated space. Therefore, the first check is to determine if BTRFS has allocated a significant portion of the partition, where "significant portion” is defined as the greater of:

- 80% of the partition size, or
- all but 2 GB of partition size.

By this definition, a 14.66 GB partition qualifies as having a significant portion of disk allocated if either the maximum of (14.66 x 0.80) or (14.66 - 2) is true. That calculates to a maximum of 11.728 GB or 12.66 GB. Since 12.66 GB is greater than 11.728 GB, then 12.66 GB is the determining factor of significant allocation for the disk.

These parameters were chosen because BTRFS appears to allocate chunks as large as 1/10th the size of the partition, up to a maximum of 1 GB. The desire is to have at least one chunk unallocated to use during the rebalance operation. Running a rebalance when the unallocated portion of a partition crosses the 2 GB or 20 % threshold guarantees that at least one chunk is free for the rebalance operation.

If a partition goes from the condition where there is not a significant portion of its space allocated, to less than one chunk unallocated, there is a danger that the rebalance operation cannot be performed. In this case the check interval may need to be reduced. The amount of allocated space is not sufficient for determining if a rebalance operation should be performed. Consider, for example, if the partition is truly 97% full of data, the allocated space check would show that a significant portion of the partition is allocated. A rebalance, in this case, would not free up used space because the disk is actually almost full. Therefore, another criteria must be added to determine if a rebalance operation is needed.

### Data Storage Efficiency Check

To determine if space would be freed when executing a rebalance, the amount of space allocated for data is compared against the amount of space used by that data. If the difference between these two is greater than the largest size of a chunk, then a rebalance will likely free up some space. The largest size of a chunk is the minimum of 1 GB or 10% of the partition.

By this definition, for a 14.66 GB partition with 13.94 GB of space allocated for data, and only 2.30 GB of space used by that data, the amount of allocated but unused space is 13.94 GB - 2.30 GB, or 11.64 GB. The largest chunk size is the smaller of (14.66 GB \* 0.10) or 1 GB. Since 1 GB is less than 1.466 GB, the largest chunk size is 1 GB. Now to compare these two, 11.64 GB is greater than 1 GB, indicating that a rebalance is required.

The Data Storage Efficiency check is also not sufficient on its own, and must be used in conjunction with the Allocated Space check. Consider a 14.66 GB partition with 4 GB allocated for data and only 1 GB used by that data. Although a rebalance may free up some space, a rebalance does not need to be performed because there is plenty of space left on the device to store additional data. Running a rebalance at this point would cause additional, unnecessary, wear on the disk.

{{%notice note%}}

The BTRFS information stored in Metadata and System chunks are not considered in this check. They are assumed to be a small portion of the partition usage.

{{%/notice%}}

In summary, if both the Allocated Space Check and the Data Storage Efficiency check return positive results, then a rebalance is recommended. If only one check returns true, a rebalance is not yet needed.

## Perform the Checks: An Example

The BTRFS filesystem usage command output contains all of the
information needed to perform the checks described above. Here is an
example of the output:

<pre>$ sudo btrfs fi usage -b /
Overall:
     Device size:                    <span style="color: red";>7474450432</span>
     Device allocated:               <span style="color: red";>2028994560</span>
     Device unallocated:             5445455872
     Device missing:                          0
     Used:                            904900608
     Free (estimated):               6199468032   (min: 3476740096)
     Data ratio:                           1.00
     Metadata ratio:                       2.00
     Global reserve:                   16777216   (used: 0)

Data,single: Size:<span style="color: red";>1568669696</span>, Used:<span style="color: red";>814657536</span>
   /dev/sda4 1568669696

Metadata,DUP: Size:196608000, Used:45105152
   /dev/sda4 393216000

System,DUP: Size:33554432, Used:16384
   /dev/sda4  67108864

Unallocated:
   /dev/sda4 5445455872
</pre>

The numbers shown in red are used for the checks.

First, perform the allocated space check. Is the allocated space greater
than the maximum of a) 80% of the partition size or, b) all but 2 GB of
the partition?

1. Calculate condition A: 7474450432 \* 0.80 = 5,979,560,345
2. Calculate condition B: 7474450432 - 2147483648 = 5,326,966,784
3. Take the greater of condition A and B and compare to disk allocation: 2,028,994,560 \< 5,979,560,345

Since the disk allocation is less than the condition, the check is False
and there is no need to run a BTRFS rebalance on this partition.

In this example, because the Allocated Space check passes, you would not
need to perform the Data Storage Efficiency check. However, should it
have failed you would also need to perform this second test to be sure a
rebalance was not needed. If we assume the first test failed, and for
this same partition, you would check if the amount of space allocated
for the data information minus the amount of space used for the data
information is greater than the chunk size:

1. Calculate the difference between space allocated and used: 1568669696 - 814657536 = 754,012,160
2. Calculate the chunk size: smaller of (7474450432 \* 0.10) or 1073741824 = 747,445,043
3. Compare these two values: 754,012,160 \> 747,445,043

Since the difference is greater than the chunk size, the check is True
and space may be freed by running a rebalance. If both checks fail, a
rebalance is needed. If only this check fails, a rebalance is not
needed.

## Conclusion

Although the BTRFS file system does not have a built-in garbage
collection facility, a reasonable analog of this capability can be
created by periodically examining the BTRFS statistics. When the amount
of space allocated by BTRFS becomes large *and* it is likely that
running a rebalance can free up some space (both checks are true), a
rebalance should be run. This can prevent the system from getting into a
situation where BTRFS allocates the entire partition, but only a small
portion of the disk is in use.

## References

- A {{<exlink url="http://marc.merlins.org/perso/btrfs/post_2014-05-04_Fixing-Btrfs-Filesystem-Full-Problems.html" text="blog post">}} by Marc Merlin
- BTRFS wiki on {{<exlink url="https://btrfs.wiki.kernel.org/index.php/FAQ#Help.21_I_ran_out_of_disk_space.21" text="out of disk space">}} issues
- BTRFS wiki on {{<exlink url="https://btrfs.wiki.kernel.org/index.php/Balance_Filters" text="balance filters">}}
- BTRFS  {{<exlink url="https://btrfs.wiki.kernel.org/index.php/Glossary" text="glossary">}}
- BTRFS sources of  {{<exlink url="https://btrfs.wiki.kernel.org/index.php/Main_Page#Guides_and_usage_information" text="documentation">}}
