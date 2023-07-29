---
title: Deploying Ansible Modules
author: NVIDIA
weight: 40
product: Technical Guides
imgData: guides
---
The NVUE ansible modules have been certified by RedHat and are available on Ansible Galaxy {{<exlink url="https://galaxy.ansible.com/nvidia/nvue" text="here">}} and the Automation Hub {{<exlink url="https://console.redhat.com/ansible/automation-hub/repo/published/nvidia/nvue/" text="here">}} (requires login).

## Important points to remember

- The modules have been tested with ansible core 2.11, 2.12 and 2.13.
- The modules support Python 3.6 and later.
- The modules have been validated against Cumulus Linux 5.4 and 5.5.

## Installing the modules

### Installing from Ansible Galaxy

You can install the NVIDIA NVUE collection with the Ansible Galaxy CLI:

```
cumulus@oob-management:~$ ansible-galaxy collection install nvidia.nvue
```

You can also include the NVIDIA NVUE collection in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```
---
collections:
  - name: nvidia.nvue
```

### Installing from git

You can install the NVIDIA NVUE collection using the git URL:

```
cumulus@oob-management:~$ ansible-galaxy collection install git+https://gitlab.com/nvidia-networking/systems-engineering/nvue.git
```

## Verifying the installation

You can verify the installation using the following ansible-galaxy command:

```
cumulus@oob-management:~$ ansible-galaxy collection list

Sample Output:
# /home/ubuntu/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
ansible.netcommon 5.1.2
ansible.utils     2.10.3
nvidia.nvue       1.0.1

# /usr/lib/python3/dist-packages/ansible_collections
Collection                    Version
----------------------------- -------
amazon.aws                    5.2.0
ansible.netcommon             4.1.0
ansible.posix                 1.5.1
ansible.utils                 2.9.0
ansible.windows               1.13.0
arista.eos                    6.0.0
awx.awx                       21.12.0
azure.azcollection            1.14.0
check_point.mgmt              4.0.0
chocolatey.chocolatey         1.4.0
...
```