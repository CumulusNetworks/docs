---
title: Ansible Simple Playbook Example with an FRR Template
author: Cumulus Networks
weight: 331
toc: 4
---

This article describes a very simple Ansible example. Use it to learn Ansible; **don't** use it as a production-level script. Please refer to the {{<link url="Demos-and-Training" text="Demos and Training section">}} for more robust examples with Ansible and other DevOp tools.

{{<img src="/images/knowledge-base/ansible-simple-playbook.png" alt="Ansible simple playbook">}}

## Playbook Requirements

The following is always required to run a playbook:

- {{<exlink url="http://docs.ansible.com/intro_installation.html#installation" text="Installing Ansible">}}
- {{<exlink url="http://docs.ansible.com/intro_inventory.html" text="An inventory file">}}
- {{<exlink url="http://docs.ansible.com/playbooks.html" text="A playbook `.yml` file">}}

Optional files used in this example:

- {{<exlink url="http://docs.ansible.com/playbooks_variables.html#variables" text="Jinja2 template file">}}

## Install Ansible

The following was performed on Ubuntu:

    cumulus@wbench:~$ sudo apt-get update
    cumulus@wbench:~$ sudo apt-get install ansible

If you don't have Ubuntu, you can install Ansible on Red Hat, Debian,
CentOS, MacOS, any BSD distro, and so on. {{<exlink url="http://docs.ansible.com/intro_installation.html" text="See this page on ansible.com">}}.

## Configure the Necessary Files

Simply cut and paste the code snippets from the code blocks below. Here
are all the pieces of code used in the example.

### Inventory File

The inventory is a single file called `host` with the contents \"leaf1\"
inside.

    cumulus@wbench:~$ cat host
    leaf1

Again, this is a very simple example. Please {{<exlink url="http://docs.ansible.com/intro_inventory.html" text="read more about creating inventory files on ansible.com">}}.

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
| tasks | There are two tasks listed, one uses the {{<exlink url="http://docs.ansible.com/template_module.html" text="template module">}} and one uses the {{<exlink url="http://docs.ansible.com/service_module.html" text="service module">}}. |
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

- {{<exlink url="/hc/en-us/articles/201955173-Setting-up-a-Basic-Ansible-Lab" text="Setting up a Basic Ansible Lab">}}
- {{<exlink url="/hc/en-us/articles/202025106-Ansible-Gathering-Facts-on-Cumulus-Linux" text="Ansible: Gathering Facts on Cumulus Linux">}}
