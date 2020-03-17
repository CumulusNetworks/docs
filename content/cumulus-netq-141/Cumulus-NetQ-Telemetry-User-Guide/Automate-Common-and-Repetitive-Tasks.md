---
title: Automate Common and Repetitive Tasks
author: Cumulus Networks
weight: 71
aliases:
 - /display/NETQ141/Automate+Common+and+Repetitive+Tasks
 - /pages/viewpage.action?pageId=10453520
pageID: 10453520
---
NetQ commands can also be run in an automation tool, such as Ansible,
Chef, or Puppet; depending on the outcome of the automation tests, the
script can either continue the deployment, or roll back the changes
until the issues are addressed.

## Run NetQ Commands in Automation Scripts

Using NetQ for preventative care of your network pairs well with
automation scripts and playbooks to prevent errors on your network
before deploying the configuration to your production network. Red Hat
Ansible, Chef and Puppet automation tools, as well as custom automation
scripts, all support scripting with NetQ commands.

For example, you can use NetQ in your Ansible playbook to help you
configure your network topology. The playbook could pull in BGP data in
JSON format before it starts creating the topology:

    - hosts: localhost leaf spine
      gather_facts: False
      tasks:
         - name: Gather BGP Adjanceny info in JSON format
           local_action: command netq show bgp json
           register: result
           #delegate_to: localhost
           run_once: true

Based on the outcome, the playbook can then respond appropriately.
Later, it can check IP addresses to verify the connections:

    #ipv6 address check
         - name: run ipv6check on broken_dict
           command: netq show ipv6 addresses {{item.key}} {{item.value}} json
           with_dict: "{{broken_dict}}"
           register: command_outputs
           delegate_to: localhost
           run_once: true
