---
title: Back up Existing Ansible Configurations - NCLU
author: NVIDIA
weight: 323
toc: 4
---

While you can build a network from the ground up with Ansible using modules or templates, it is possible to grab the networking configuration from a pre-configured network, and even push it back out to the switch.

This type of model can be beneficial for:

- Upgrade scenarios
- Taking a snapshot of the network before trying something new
- Reverting quickly back to a snapshot
- Providing an introduction to automation

{{<img src="/images/knowledge-base/Ansible-fetch-copy.png" width="600px">}}

## Requirements

- Cumulus Linux switch
- Server/laptop for running Ansible
- {{<exlink url="https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html" text="Install Ansible on the server/laptop">}}

## Ansible Modules

The two examples below primarily use these four core Ansible modules:

- {{<exlink url="https://docs.ansible.com/ansible/latest/collections/ansible/builtin/fetch_module.html" text="Fetch">}}
- {{<exlink url="https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html" text="Copy">}}
- {{<exlink url="https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html" text="Command">}}
- {{<exlink url="https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html" text="Service">}}

## Example Fetch

On the server is a folder with one file called `fetch.yml`.

    user@server ~/consulting/fetch $ ls
    fetch.yml

The content of the file is very simple:

    ---
    - hosts: leaf1
      become: yes
      tasks:
        - name: Fetch ports.conf
          fetch: dest=save/{{ansible_hostname}}/ports.conf src=/etc/cumulus/ports.conf flat=yes

        - name: Fetch interfaces Configuration
          fetch: dest=save/{{ansible_hostname}}/interfaces src=/etc/network/interfaces flat=yes

        - name: Fetch FRR daemons file
          fetch: dest=save/{{ansible_hostname}}/daemons src=/etc/frr/daemons flat=yes

        - name: Fetch frr.conf
          fetch: dest=save/{{ansible_hostname}}/frr.conf src=/etc/frr/frr.conf flat=yes

To run the playbook, run the `ansible-playbook` command:

    user@server ~/consulting/fetch $ ansible-playbook fetch.yml

    PLAY [leaf1] ******************************************************************

    GATHERING FACTS ***************************************************************
    ok: [leaf1]

    TASK: [Fetch ports.conf] ******************************************************
    changed: [leaf1]

    TASK: [Fetch interfaces Configuration] ******************************************************
    changed: [leaf1]

    TASK: [Fetch FRR daemons file] **********************************************
    changed: [leaf1]

    TASK: [Fetch frr.conf] ******************************************************
    ok: [leaf1]

    PLAY RECAP ********************************************************************
    leaf1                      : ok=5    changed=3    unreachable=0    failed=0

The playbook copies these four commonly used Cumulus Linux files to the server:

| File Name               | Description                        |
| ----------------------- | ---------------------------------- |
| /etc/cumulus/ports.conf | Configuration for breakout ports   |
| /etc/network/interfaces | Network configuration File         |
| /etc/frr/daemons        | Daemons configuration file for FRR |
| /etc/frr/frr.conf       | FRR Configuration file             |

For more information on which files to back up and what Cumulus Linux uses, read [Upgrading Cumulus Linux]({{<ref "/cumulus-linux-43/Installation-Management/Upgrading-Cumulus-Linux#before-you-upgrade" >}}).

The playbook copies the files to a directory called `save`:

    user@server ~/consulting/fetch $ ls
    fetch.yml  save

The playbook puts the files into a directory based on the hostname. This particular example shows the playbook ran only on one switch named leaf1:

    user@server ~/consulting/fetch/save $ ls
    leaf1

The playbook stores all the files in the `leaf1` directory:

    user@server ~/consulting/fetch/save/leaf1 $ ls
    daemons  interfaces  ports.conf  frr.conf

## Example Copy

On the server, Ansible added a file called `copy.yml` to the directory; the file has this content:

    ---
    - hosts: leaf1
      become: yes
      tasks:
        - name: Restore ports.conf
          copy: src=save/{{ansible_hostname}}/ports.conf dest=/etc/cumulus/
        - name: Restore Interface Configuration
          copy: src=save/{{ansible_hostname}}/interfaces dest=/etc/network/
        - name: Restore FRR daemons file
          copy: src=save/{{ansible_hostname}}/daemons dest=/etc/frr/daemons
        - name: Restore frr.conf
          copy: src=save/{{ansible_hostname}}/frr.conf dest=/etc/frr/frr.conf

        - name: reload switchd
          service: name=switchd state=restarted
        - name: reload networking
          command: /sbin/ifreload -a
        - name: restart frr
          service: name=frr state=restart

This file just pushes back the already saved files, then restarts the corresponding services using the service and command module. Instead of issuing a `service=networking` command, the `ifreload -a` command ran directly.

    user@server ~/consulting/fetch $ ansible-playbook copy.yml

    PLAY [leaf1] ******************************************************************

    GATHERING FACTS ***************************************************************
    ok: [leaf1]

    TASK: [Restore ports.conf] *******************************************************
    ok: [leaf1]

    TASK: [Restore Interface Configuration] *******************************************************
    ok: [leaf1]

    TASK: [Restore FRR daemons file] ***************************************************
    ok: [leaf1]

    TASK: [Restore frr.conf] ******************************************************
    changed: [leaf1]

    TASK: [reload switchd] ********************************************************
    changed: [leaf1]

    TASK: [reload networking] *****************************************************
    changed: [leaf1]

    TASK: [restart frr] *********************************************************
    changed: [leaf1]


    PLAY RECAP ********************************************************************
               to retry, use: --limit @/home/user/copy.retry

    leaf1                      : ok=8    changed=4    unreachable=0    failed=0

With the files pushed back to the switch, it now operates on the previous snapshot.

You could base the `save` directory on the time of day rather than a generic folder called `save` by using:

    {{ansible_date_time.time}}

You can find more information on which facts Ansible gathers by reading {{<link url="Gathering-Ansible-Facts-on-Cumulus-Linux" text="this article">}}.
