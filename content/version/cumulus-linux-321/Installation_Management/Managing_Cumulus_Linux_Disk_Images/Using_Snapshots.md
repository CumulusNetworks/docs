---
title: Using Snapshots
author: Cumulus Networks
weight: 243
aliases:
 - /display/CL321/Using+Snapshots
 - /pages/viewpage.action?pageId=5126828
pageID: 5126828
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
Cumulus Linux supports the ability to take snapshots of the complete
file system as well as the ability to roll back to a previous snapshot.
Snapshots are performed automatically right before and after you upgrade
Cumulus Linux and right before and after you commit a switch
configuration using
[NCLU](/version/cumulus-linux-321/System_Configuration/Network_Command_Line_Utility).
In addition, you can take a snapshot at any time. You can roll back the
entire file system to a specific snapshot or just retrieve specific
files.

The primary snapshot components are:

  - [btrfs](https://btrfs.wiki.kernel.org/index.php/Main_Page) — an
    underlying file system in Cumulus Linux, which supports snapshots.

  - [snapper](http://snapper.io/documentation.html) — a userspace
    utility to create and manage snapshots on demand as well as taking
    snapshots automatically before and after running `apt-get
    upgrade|install|remove|dist-upgrade`. You can use `snapper` to roll
    back to earlier snapshots, view existing snapshots, or delete one or
    more snapshots.

  - [NCLU](/version/cumulus-linux-321/System_Configuration/Network_Command_Line_Utility)
    — takes snapshots automatically before and after committing network
    configurations. You can use NCLU to roll back to earlier snapshots,
    view existing snapshots, or delete one or more snapshots.

## <span>Installing the Snapshot Package</span>

If you're upgrading from a version of Cumulus Linux earlier than version
3.2, you need to install the `cumulus-snapshot` package before you can
use snapshots.

    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install cumulus-snapshot
    cumulus@switch:~$ sudo apt-get upgrade

## <span>Taking and Managing Snapshots</span>

As described above, snapshots are taken automatically:

  - Before and after you update your switch configuration by running
    `net commit`, via NCLU.

  - Before and after you update Cumulus Linux by running `apt-get
    upgrade|install|remove|dist-upgrade`, via `snapper`.

You can also take snapshots as needed using the `snapper` utility. Run:

    cumulus@switch:~$ sudo snapper create -d SNAPSHOT_NAME

For more information about using `snapper`, run `snapper --help` or `man
snapper(8)`.

### <span>Viewing Available Snapshots</span>

You can use both NCLU and `snapper` to view available snapshots on the
switch.

    cumulus@switch:~$ net show commit history 
      #  Date                             Description
    ---  -------------------------------  --------------------------------------
     20  Thu 01 Dec 2016 01:43:29 AM UTC  nclu pre  'net commit' (user cumulus)
     21  Thu 01 Dec 2016 01:43:31 AM UTC  nclu post 'net commit' (user cumulus)
     22  Thu 01 Dec 2016 01:44:18 AM UTC  nclu pre  '20 rollback' (user cumulus)
     23  Thu 01 Dec 2016 01:44:18 AM UTC  nclu post '20 rollback' (user cumulus)
     24  Thu 01 Dec 2016 01:44:22 AM UTC  nclu pre  '22 rollback' (user cumulus)
     31  Fri 02 Dec 2016 12:18:08 AM UTC  nclu pre  'ACL' (user cumulus)
     32  Fri 02 Dec 2016 12:18:10 AM UTC  nclu post 'ACL' (user cumulus)

However, `net show commit history` only displays snapshots taken when
you update your switch configuration. It does not list any snapshots
taken directly with `snapper`. To see all the snapshots on the switch,
run:

``` 
cumulus@switch:~$ sudo snapper list
Type   | #  | Pre # | Date                            | User | Cleanup | Description                            | Userdata     
-------+----+-------+---------------------------------+------+---------+----------------------------------------+--------------
single | 0  |       |                                 | root |         | current                                |              
single | 1  |       | Sat 24 Sep 2016 01:45:36 AM UTC | root |         | first root filesystem                  |              
pre    | 20 |       | Thu 01 Dec 2016 01:43:29 AM UTC | root | number  | nclu pre  'net commit' (user cumulus)  |              
post   | 21 | 20    | Thu 01 Dec 2016 01:43:31 AM UTC | root | number  | nclu post 'net commit' (user cumulus)  |              
pre    | 22 |       | Thu 01 Dec 2016 01:44:18 AM UTC | root | number  | nclu pre  '20 rollback' (user cumulus) |              
post   | 23 | 22    | Thu 01 Dec 2016 01:44:18 AM UTC | root | number  | nclu post '20 rollback' (user cumulus) |              
single | 26 |       | Thu 01 Dec 2016 11:23:06 PM UTC | root |         | test_snapshot                          |              
pre    | 29 |       | Thu 01 Dec 2016 11:55:16 PM UTC | root | number  | pre-apt                                | important=yes
post   | 30 | 29    | Thu 01 Dec 2016 11:55:21 PM UTC | root | number  | post-apt                               | important=yes
pre    | 31 |       | Fri 02 Dec 2016 12:18:08 AM UTC | root | number  | nclu pre  'ACL' (user cumulus)         |              
post   | 32 | 31    | Fri 02 Dec 2016 12:18:10 AM UTC | root | number  | nclu post 'ACL' (user cumulus)         |            
```

### <span>Viewing Differences between Snapshots</span>

To see a line by line comparison of changes between two snapshots, run:

    cumulus@switch:~$ sudo snapper diff 20..21
    --- /.snapshots/20/snapshot/etc/cumulus/acl/policy.d/50_nclu_acl.rules  2016-11-30 23:00:42.675092103 +0000
    +++ /.snapshots/21/snapshot/etc/cumulus/acl/policy.d/50_nclu_acl.rules  2016-12-01 01:43:30.029171289 +0000
    @@ -1,7 +0,0 @@
    -[iptables]
    -# control-plane: acl ipv4 EXAMPLE1 inbound
    --A INPUT --in-interface swp+ -j ACCEPT -p tcp -s 10.0.0.11/32 -d 10.0.0.12/32 --dport 110
    -
    -# swp1: acl ipv4 EXAMPLE1 inbound
    --A FORWARD --in-interface swp1 --out-interface swp2 -j ACCEPT -p tcp -s 10.0.0.11/32 -d 10.0.0.12/32 --dport 110
    -
    --- /.snapshots/20/snapshot/var/lib/cumulus/nclu/nclu_acl.conf  2016-11-30 23:00:18.030079000 +0000
    +++ /.snapshots/21/snapshot/var/lib/cumulus/nclu/nclu_acl.conf  2016-12-01 00:23:10.096136000 +0000
    @@ -1,8 +1,3 @@
    -acl ipv4 EXAMPLE1 priority 10 accept tcp 10.0.0.11/32 10.0.0.12/32 pop3 outbound-interface swp2
     
    -control-plane
    -    acl ipv4 EXAMPLE1 inbound
     
    -iface swp1
    -    acl ipv4 EXAMPLE1 inbound

You can view the diff for a single file by specifying the name in the
command:

    cumulus@switch:~$ sudo snapper diff 20..21 /var/lib/cumulus/nclu/nclu_acl.conf 
    --- /.snapshots/20/snapshot/var/lib/cumulus/nclu/nclu_acl.conf  2016-11-30 23:00:18.030079000 +0000
    +++ /.snapshots/21/snapshot/var/lib/cumulus/nclu/nclu_acl.conf  2016-12-01 00:23:10.096136000 +0000
    @@ -1,8 +1,3 @@
    -acl ipv4 EXAMPLE1 priority 10 accept tcp 10.0.0.11/32 10.0.0.12/32 pop3 outbound-interface swp2
     
    -control-plane
    -    acl ipv4 EXAMPLE1 inbound
     
    -iface swp1
    -    acl ipv4 EXAMPLE1 inbound

For a higher level view, displaying the names of changed/added/deleted
files only, run:

    cumulus@switch:~$ sudo snapper status 20..21
    c..... /etc/cumulus/acl/policy.d/50_nclu_acl.rules
    c..... /var/lib/cumulus/nclu/nclu_acl.conf

### <span>Deleting Snapshots</span>

You can remove one or more snapshots using both NCLU and snapper.

{{%notice warning%}}

Take care when deleting a snapshot, as you cannot restore it once it's
been deleted.

{{%/notice%}}

To remove a single snapshot or a range of them created with NCLU, run:

    cumulus@switch:~$ net commit delete SNAPSHOT|SNAPSHOT1-SNAPSHOT2

To remove a single snapshot or a range of snapshots using `snapper`,
run:

    cumulus@switch:~$ sudo snapper delete SNAPSHOT|SNAPSHOT1-SNAPSHOT2

{{%notice note%}}

Snapshot 0 is the running configuration. You can't roll back to it or
delete it. However, you can take a snapshot of it.

Snapshot 1 is the root file system.

{{%/notice%}}

The `snapper` utility preserves a number of snapshots, and automatically
deletes older snapshots once the limit is reached. It does this in two
ways.

By default, `snapper` preserves 10 snapshots that are labeled
*important*. A snapshot is labeled important if it was created when you
run `apt-get`. To change this number, run:

    cumulus@switch:~$ sudo snapper set-config NUMBER_LIMIT_IMPORTANT=<NUM>

{{%notice tip%}}

You should always make `NUMBER_LIMIT_IMPORTANT` an even number since two
snapshots are always taken before and after an upgrade. This does not
apply to `NUMBER_LIMIT`, described next.

{{%/notice%}}

`snapper` also deletes unlabeled snapshots. The default number of
snapshots `snapper` preserves is 5. To change this number, run:

    cumulus@switch:~$ sudo snapper set-config NUMBER_LIMIT=<NUM>

Also, you can prevent snapshots from being taken automatically before
and running `apt-get upgrade|install|remove|dist-upgrade`. Edit
`/etc/cumulus/apt-snapshot.conf` and set:

    APT_SNAPSHOT_ENABLE=no

## <span>Rolling Back to Earlier Snapshots</span>

If you need to restore Cumulus Linux to an earlier state, you can roll
back to an older snapshot.

For a snapshot created with NCLU, you can revert to a specific snapshot
listed in the output from `net show commit history`, or you can revert
to the previous snapshot by specifying *last* when you run:

    cumulus@switch:~$ net rollback SNAPSHOT_NUMBER|last

For any snapshot on the switch, you can use `snapper` to roll back to a
specific snapshot. When running `snapper rollback`, you must reboot the
switch for the rollback to complete:

    cumulus@switch:~$ sudo snapper rollback SNAPSHOT_NUMBER
    cumulus@switch:~$ sudo reboot

You can also revert to an earlier version of a specific file instead of
rolling back the whole file system:

    cumulus@switch:~$ sudo snapper undochange 31..32 /etc/cumulus/acl/policy.d/50_nclu_acl.rules

{{%notice tip%}}

You can also copy the file directly from the snapshot directory:

    cumulus@switch:~$ cp /.snapshots/32/snapshot/etc/cumulus/acl/policy.d/50_nclu_acl.rules /etc/cumulus/acl/policy.d/

{{%/notice%}}

## <span>Configuring Automatic Time-based Snapshots</span>

You can configure Cumulus Linux to take hourly snapshots. You need to
enable `TIMELINE_CREATE` in the snapper configuration:

    cumulus@switch:~$ sudo snapper set-config TIMELINE_CREATE=yes
    cumulus@switch:~$ sudo snapper get-config                                                                                            
    Key                    | Value
    -----------------------+------
    ALLOW_GROUPS           |      
    ALLOW_USERS            |      
    BACKGROUND_COMPARISON  | yes  
    EMPTY_PRE_POST_CLEANUP | yes  
    EMPTY_PRE_POST_MIN_AGE | 1800 
    FSTYPE                 | btrfs
    NUMBER_CLEANUP         | yes  
    NUMBER_LIMIT           | 5    
    NUMBER_LIMIT_IMPORTANT | 10   
    NUMBER_MIN_AGE         | 1800 
    QGROUP                 |      
    SPACE_LIMIT            | 0.5  
    SUBVOLUME              | /    
    SYNC_ACL               | no   
    TIMELINE_CLEANUP       | yes  
    TIMELINE_CREATE        | yes  
    TIMELINE_LIMIT_DAILY   | 5    
    TIMELINE_LIMIT_HOURLY  | 5    
    TIMELINE_LIMIT_MONTHLY | 5    
    TIMELINE_LIMIT_YEARLY  | 5    
    TIMELINE_MIN_AGE       | 1800 

## <span>Caveats and Errata</span>

### <span>root Partition Mounted Multiple Times</span>

You may notice that the root partition gets mounted multiple times. This
is due to the way the `btrfs` file system handles subvolumes, mounting
the root partition once for each subvolume. `btrfs` keeps one subvolume
for each snapshot taken, which stores the snapshot data. While all
snapshots are subvolumes, not all subvolumes are snapshots.

Cumulus Linux excludes a number of directories when it takes a snapshot
of the root file system (and from any rollbacks):

| Directory                                                        | Reason                                                                                                                                                                                                |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /home                                                            | Excluded to avoid user data loss on rollbacks.                                                                                                                                                        |
| /var/log, /var/support                                           | Log file and Cumulus support location. Excluded from snapshots to allow post-rollback analysis.                                                                                                       |
| /tmp, /var/tmp                                                   | No need to rollback temporary files.                                                                                                                                                                  |
| /opt, /var/opt                                                   | Third-party software usually are installed in /opt. Exclude /opt to avoid re-installing these applications after rollbacks.                                                                           |
| /srv                                                             | Contains data for HTTP and FTP servers. Excluded this directory to avoid server data loss on rollbacks.                                                                                               |
| /usr/local                                                       | This directory is used when installing locally built software. Exclude this directory to avoid re-installing these software after rollbacks.                                                          |
| /var/spool                                                       | Exclude this directory to avoid loss of mail after a rollback.                                                                                                                                        |
| /var/lib/libvirt/images                                          | This is the default directory for libvirt VM images. Exclude from the snapshot. Additionally disable Copy-On-Write (COW) for this subvolume as COW and VM image I/O access patterns do not play nice. |
| /boot/grub/i386-pc, /boot/grub/x86\_64-efi, /boot/grub/arm-uboot | The GRUB kernel modules must stay in sync with the GRUB kernel installed in the master boot record or UEFI system partition.                                                                          |
