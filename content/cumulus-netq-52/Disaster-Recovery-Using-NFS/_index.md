---
title: Disaster Recovery Using NFS
author: NVIDIA
weight: 1035
toc: 2
---

You can back up and restore NetQ on-premises virtual machines using three methods. Each method has a specific use case:

- General backup and restore: Use VM-level backups to restore a VM from its own backup data. Earlier NetQ releases used this method to upgrade from one NetQ version to the next.
- Upgrade: Perform an in-place upgrade with data persistence to upgrade NetQ versions.
- Disaster recovery: Follow the backup and restore procedure in this section to set up and configure a Network File System server to re-create NetQ in a new environment after a failure.