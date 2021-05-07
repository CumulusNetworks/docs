---
title: Ansible Simple Playbook Example with an FRR Template
author: NVIDIA
weight: 325
toc: 4
---

This article describes a very simple Ansible example. Use it to learn Ansible; **don't** use it as a production-level script. Please refer to the {{<link url="Demos-and-Training" text="Demos and Training section">}} for more robust examples with Ansible and other DevOp tools.

{{<img src="/images/knowledge-base/ansible-simple-playbook.png" alt="Ansible simple playbook" width="500px">}}

## Playbook Requirements

The following is always required to run a playbook:

- {{<exlink url="https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html" text="Installing Ansible">}}
- {{<exlink url="https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory" text="An inventory file">}}
- {{<exlink url="https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#about-playbooks" text="A playbook `.yml` file">}}

Optional files used in this example:

- {{<exlink url="https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html#playbooks-templating" text="Jinja2 template file">}}

## Install Ansible

The following was performed on Ubuntu:

    cumulus@wbench:~$ sudo apt-get update
    cumulus@wbench:~$ sudo apt-get install ansible

If you don't have Ubuntu, you can install Ansible on Red Hat, Debian,
CentOS, MacOS, any BSD distro, and so on. {{<exlink url="https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html" text="See this page on ansible.com">}}.

## Configure the Necessary Files

Simply cut and paste the code snippets from the code blocks below. Here
are all the pieces of code used in the example.

### Inventory File

The inventory is a single file called `host` with the contents \"leaf1\"
inside.

    cumulus@wbench:~$ cat host
    leaf1

Again, this is a very simple example. Please {{<exlink url="https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory" text="read more about creating inventory files on ansible.com">}}.

### Playbook .yml File

    cumulus@wbench:~$ cat sample-playbook.yml
    ---
    - hosts: leaf1
      vars:
        description: “this is a leaf switch”
      remote_user: root
      tasks:
      - name: write the frr config file
        template: src=frr.j2 dest=/etc/frr/frr.conf
        notify:
        - restart frr
      - name: ensure frr is running
        service: name=frr state=started
      handlers:
        - name: restart frr
          service: name=frr state=restarted

This `sample-playbook.yml` contains one variable, two tasks, and a handler. Each component is described below:

| Component | Description |
| --------- | ----------- |
| hosts:leaf1 | Only run this playbook on the host leaf1. |
| vars | These are the variables defined for the playbook. There is only one variable, called `description`. |
| remote\_user | This is the user who will run the playbook on the remote system. |
| tasks | There are two tasks listed, one uses the {{<exlink url="https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html" text="template module">}} and one uses the {{<exlink url="https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html" text="service module">}}. |
| handlers | Handlers are tasks that only run if a task notifies it. A task will only notify it if something has changed. In this example, FRR gets restarted only if `frr.conf` changes. |
  
### jinja2 Template File

The template file can use any of the defined variables. The script below
replaces the {{description}} with the one listed under `vars`:

    cumulus@wbench:~$ cat frr.j2
    !
    interface lo
      description {{description}}
    !

## Run the Playbook

Use the `ansible-playbook` command to run the `sample-playbook.yml`
file. Use the optional argument `-i` to point to the inventory file. If
the `-i` option is not used, and there is no `ansible.cfg` folder
indicating otherwise, Ansible will automatically use
`/etc/ansible/hosts`. Alternately, instead of creating the file host
with leaf1 in it, simply add leaf1 to `/etc/ansible/hosts`.

    cumulus@wbench:~$ ansible-playbook sample-playbook.yml -i host

    PLAY [leaf1] ******************************************************************

    GATHERING FACTS ***************************************************************
    ok: [leaf1]

    TASK: [write the frr config file] ******************************************
    changed: [leaf1]

    TASK: [ensure frr is running] **********************************************
    ok: [leaf1]

    NOTIFIED: [restart frr] ****************************************************
    changed: [leaf1]

    PLAY RECAP ********************************************************************
    leaf1                      : ok=4    changed=2    unreachable=0    failed=0

The playbook above runs both tasks. Since FRR was changed, it
notifies the tasks, which restarts the FRR service. The playbook
assumes that FRR was already running, otherwise this playbook will
fail.

## Related Information

- {{<link url="Set-up-a-Basic-Ansible-Lab">}}
- {{<link url="Gathering-Ansible-Facts-on-Cumulus-Linux">}}
