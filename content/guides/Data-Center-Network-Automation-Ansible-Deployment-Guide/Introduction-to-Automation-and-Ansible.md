---
title: Introduction to Automation and Ansible
author: NVIDIA
weight: 20
product: Technical Guides
imgData: guides
---
As data centers evolve from physical on-premises to digitized cloud infrastructures, traditional networks also evolve and need to grow based on business demand. This places an increased burden on network operations teams to manage, maintain, and continually adapt to a changing environment with complex and precise configurations. To combat the limitations that come from managing network operations manually, the data center must be automatedso that it can be more agile.

## Automation

Today, businesses operate at high speeds with massive growth in data, making manual monitoring, troubleshooting, and remediation too slow, which can put businesses at risk. Automation can simplify day-zero and day-one setups and make day-two operations almost autonomous. 
Automation brings together the data center infrastructure, allowing for centralized access to most data center resources. This access enables the automation of storage, servers, network, and other data center management tasks.

## NVIDIA User Experience

NVIDIA User Experience (NVUE) is an object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) providing a robust API that allows for multiple interfaces to both view (show) and configure (set and unset) any element within a system running the NVUE software.
NVUE follows a declarative model, removing context-specific commands and settings. It is structured as a big tree that represents the entire state of a Cumulus Linux instance. At the base of the tree are high level branches representing objects, such as router and interface. Under each of these branches are additional branches. As you navigate through the tree, you gain a more specific context. At the leaves of the tree are actual attributes, represented as key-value pairs. The path through the tree is similar to a filesystem path.
You can use the NVUE object model in the following ways:
-	With the **NVUE CLI**, where you configure, monitor, and manage the Cumulus Linux network elements. The CLI commands translate to their equivalent REST APIs, which Cumulus Linux then runs on the NVUE object model.
-	With the **NVUE REST API**, where you run the GET, PATCH, DELETE, and other REST APIs on the NVUE object model endpoints to configure, monitor, and manage the switch. Because of the large user community and maturity of Open API Specifications (OAS) upon which NVUE is based, you can use several popular tools and libraries to create client-side bindings to use the NVUE REST API. The documentation for the NVUE REST API uses Swagger;you can find it here.
The CLI and the REST API are equivalent in functionality; you can run all management operations from the REST API or the CLI. The NVUE object model drives both the REST API and the CLI management operations. All operations are consistent; for example, the CLI nv show commands reflect any PATCH   operation (create) you run through the REST API.

## Ansible

Ansible® is an open-source IT automation tool that automates provisioning, configuration management, application deployment, orchestration, and many other manual IT processes. Ansible works by connecting to your automation target and pushing programs that execute instructions that you typically do manually. These programs utilize Ansible modules written based on the specific expectations of endpoint connectivity, interface, and commands.
An Ansible playbook is a blueprint of automation tasks, which are complex IT actions executed with no need for human involvement. You write Ansible playbooks in human readable {{<exlink url="https://www.redhat.com/en/topics/automation/what-is-yaml" text="YAML">}} format and execute them on a set, group, or classification of hosts, which together make up an Ansible inventory.

### Terminology

**Ansible Galaxy**

An online distribution server for finding and sharing Ansible community content, sometimes referred to as community Galaxy. Also, the command-line utility that lets you install individual Ansible collections, for example `ansible-galaxy collection install nvidia.nvue`.

**Collections**

A packaging format for bundling and distributing Ansible content, including plugins, roles, modules, and more. Collections are release-independent of other collections or ansible-core so features can be available sooner. Some collections are packaged with Ansible (version 2.10 or later). You can install other collections (or other versions of collections) with `ansible-galaxy collection install <namespace.collection>`.

**Collection name**

The second part of a Fully Qualified Collection Name. The collection name divides the collection namespace and usually reflects the function of the collection content. For example, the `nvidia` namespace contains `nvidia.nvue` with content for managing the different NVUE devices maintained by NVIDIA.

**Group**

A group consists of several hosts assigned to a pool that can be conveniently targeted together, as well as given variables that they share in common.

**Group Vars**

The `group_vars` files live in a directory alongside an inventory file, with an optional filename named after each group. This is a convenient place to put variables that are provided to a given group, especially complex data structures, so that these variables do not have to be embedded in the file or playbook.

**Host**

A host is a remote machine that Ansible manages. You can assign individual variables to a host and can also organize them in groups. All hosts have a name, which is either an IP address or a domain name and, optionally, a port number in case   access is not allowed on the default SSH port.

**Inventory**

A file (by default, Ansible uses a simple INI format) that describes {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Host" text="Hosts">}} and {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Group" text="Groups">}} in Ansible. You can also provide inventory through an {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Inventory-Script" text="Inventory Script">}} (sometimes called an External Inventory Script).

**Inventory Script**

A very simple program (or a complicated one) that looks up {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Host" text="hosts">}}, {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Group" text="group">}} membership for hosts, and variable information from an external resource – an SQL database, a CMDB solution, or a solution similar to LDAP. This concept is adapted from Puppet (where it is called an External Nodes Classifier) and works in more or less the same way.

**Jinja2**

Jinja2 is the preferred templating language of the Ansible template module. It is a very simple Python template language that is generally readable and easy to write.

**Modules**

Modules are the units of work that Ansible ships out to remote machines. Modules are kicked off by either `/usr/bin/ansible` or `/usr/bin/ansible-playbook` (where multiple tasks use lots of different modules). You can implement modules in any language, including Perl, Bash, or Ruby. You can take advantage of some useful communal library code if written in Python. Modules just have to return {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-JSON" text="JSON">}}. After you execute modules on remote machines, they are removed, so that no long running daemons are used. Ansible refers to the collection of available modules as a {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Library" text="library">}}.

**Playbooks**

Playbooks are the language by which Ansible orchestrates, configures, administers, or deploys systems. They are called playbooks partially to use a sports analogy as it is supposed to be fun using them. They are not workbooks.

**Plays**

A {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Playbooks" text="playbook">}} is a list of plays. A play is minimally a mapping between a set of {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Host" text="hosts">}} selected by a host specifier (usually chosen by {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Group" text="groups">}} but sometimes by hostname {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Globbing" text="globs">}}) and the {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Tasks" text="tasks">}} that run on those hosts to define the role that those systems perform. There can be one or many plays in a playbook.

**Roles**

Roles are units of organization in Ansible. Assigning a role to a group of {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Host" text="hosts">}} (or a set of {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Group" text="groups">}}, or {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Globbing" text="host patterns">}}, and so on) implies that they should implement a specific behavior. A role might include applying certain variable values, certain {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Tasks" text="tasks">}}, and certain {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Handlers" text="handlers">}} – or just one or more of these things. Because of the file structure associated with a role, roles become redistributable units that enable you to share behavior among {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Playbooks" text="playbooks">}} – or even with other users.

**Task**

{{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Playbooks" text="Playbooks">}} exist to run tasks. Tasks combine an {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Action" text="action">}} (a module and its arguments) with a name and, optionally, some other keywords (like {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Loops" text="looping keywords">}}). {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Handlers" text="Handlers">}} are also tasks, but they are a special kind of task that do not run unless they are notified by name when a task reports an underlying change on a remote system.

**Templates**

Ansible can easily transfer files to remote systems but often, it is desirable to substitute variables in other files. Variables can come from the {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Inventory" text="inventory">}} file, {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Host-Vars" text="Host Vars">}}, {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Group-Vars" text="Group Vars">}}, or {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Facts" text="facts">}}. Templates use the {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Jinja2" text="Jinja2">}} template engine and can also include logical constructs like loops and if statements

**YAML**

Ansible does not want to force people to write programming language code to automate infrastructure, so Ansible uses YAML to define {{<exlink url="https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Playbooks" text="playbook">}} configuration languages and also variable files. YAML has minimal syntax and is very clean and easy for you to skim. It is a good data format for configuration files and humans, and is also machine readable. Ansible’s usage of YAML stemmed from Michael DeHaan’s first use of it inside of Cobbler around 2006. YAML is fairly popular in the dynamic language community and the format has libraries available for serialization in many languages (Python, Perl, Ruby, and so on).
