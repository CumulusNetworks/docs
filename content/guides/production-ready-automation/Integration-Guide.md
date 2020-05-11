---
title: Customize the Production Ready Automation
author: Cumulus Networks
weight: 40
product: Cumulus Networks Guides
version: "1.0"
draft: true
---
This section provides guidance on how to customize and adapt the main individual pieces of the Cumulus Production Ready Automation to suit your own needs and work for your own environment.

These main features of the Cumulus Production Ready Automation depend on each other to provide the fully operationalized automated data center.

- Base simulation
- Automation providing infrastructure as code (IaC)
- Continuous Integration/Continuous Deployment (CI/CD)

Building a simulation that represents your production network is the first step in taking advantage of next generation NetDevOps style operational workflows. Ideally, you test all network changes in simulation or in a staging environment before they reach production. Cumulus VX is an extremely lightweight and high fidelity simulation platform. With a small memory footprint and all of the software components being exactly the same as Cumulus Linux running on hardware, you can construct a highly scalable and robust simulation environment  that matches the production environment; from interface labels down to MAC addresses.

{{% notice note %}}

For more about why Cumulus Networks made the choices they did for Production Ready Automation read the [blog post](https://cumulusnetworks.com/blog/production-ready-automation/) that describes our motivations and technical reasoning.

{{% /notice %}}

## Infrastructure as Code

IaC or (Infrastructure as code) is an abstract concept that lets you store your network configurations, or a coded version of your network configuration, normally in a source code repository. The choice of your automation engine or automation tools drives and influences the ways you can turn your network configurations into more highly scalable and repeatable chunks of “code" that get rendered by the automation tools during deployment.

Cumulus Production Ready Automation uses Ansible as its automation engine. Due to this choice, our version of infrastructure as code are the Ansible best practices that include the use of roles, Jinja2 templates, and structured variable files.

As part of the Production Ready Automation, complete Ansible configurations include:

- playbooks
- roles
- templates
- variables
- inventory

## Continuous Integration and Continuous Delivery

CI/CD is an abbreviation for Continuous Integration and Continuous Deployment. These terms are normally used together, but are distinct and separate stages. It is possible to perform just CI, without CD, for example, but you don't normally implement CD without CI.

Continuous Integration is based on the idea that changes should be able to happen frequently and at any time of day. But before changes can be “integrated" or accepted and be considered for deployment into production, the whole network, with those changes, must be able to pass a set of testing to ensure that the change does not cause an unintended consequence or is an otherwise bad change.

Once testing passes and the change is integrated from the CI stage, the CD stage or “continual deployment" stage is optionally also carried out automatically. For the network, this could mean that changes that pass automated testing from CI, could then be automatically deployed to the production environment. Automated CD is still uncommon for network operations.

{{%notice note%}}

Cumulus Networks strongly recommends that all customers deploy a CI strategy. We recommend against a CD strategy for most customers. Using CD can lead to network changes during critical business hours with unintended consequences. Only organizations with proper testing and operations in place should consider CD.

{{%/notice%}}

## System Requirements

For a robust simulation environment and CI/CD with gitlab, a dedicated, always-on, enterprise class server is recommended. Using the NetQ server in individual development environments is not normally required and is normally only needed for CI testing where the gitlab-runner is installed and registered to your CI/CD enabled project.

### Hardware Requirements

- Memory requirements vary. To estimate the needs for your simulation, use these values:
    - 768MB for each Cumulus Linux Node
    - 512MB for each Ubuntu 18.04 host
    - 1024MB for the oob-mgmt-server
    - 768MB for the oob-mgmt-switch
    - 8192MB for Netq-ts
- Disk requirements vary. Vagrant/libvirt uses thin disk images but a good reference point is
    - 256GB Disk with 64GB or more free memory
    - Recommended 1TB or more disk
    - SSD Recommended (NetQ Requirement)
- High Speed Broadband/Wideband Internet Connection for package installs during simulation bringup
- A minimum of eight x86_64 CPU cores

### Software Requirements and Dependencies

- Operating Systems:
  - Cumulus Linux 3.7.11 or later
  - Cumulus NetQ 2.4 or later (optional)
  - Ubuntu 16.04 or 18.04 (Cumulus Networks has *not* tested other Linux distributions, such as CentOS or RHE)
- Software Packages:
  - Vagrant 2.2.4 or later
  - Libvirt
  - Qemu
  - Git
- Vagrant plugins
  - Vagrant-libvirt
  - Vagrant-scp

Refer to {{<link title="Example Install Scripts" text="Example Install Scripts">}} for sample bash scripts used to install the software package and environment dependencies.

### CI/CD Requirements and Dependencies

- An account with gitlab.com or your own internal GitLab instance
- A dedicated simulation environment for the GitLab Runner to start and test simulations
- GitLab Runner package installed on the simulation host machine
  - Setup a GitLab Runner user & environment on the system
- A project on your gitlab instance that is set up with simulation, automation, anf IAC
- A NetQ Cloud account with a premises/site dedicated for simulation

### Anatomy of a Golden Standard Demo Project

These main features of the Cumulus Production Ready Automation depend on each other to provide the fully-operationalized automated data center:

- Base simulation
- Automation and IaC
- CI/CD

In a Cumulus Networks official golden standard demo repository, the important files and folders map to the three main features above in the following way:

```
dc_configs_vxlan_evpnsym/
├── automation
├── cldemo2
│   ├── ci-common
│   ├── documentation
│   ├── LICENSE
│   ├── README.md
│   ├── simulation
│   └── tests
├── .git
├── .gitignore
├── .gitlab-ci.yml
├── LICENSE
├── README.md
├── start-demo.sh
└── tests
```

### File and Folder Descriptions

| File/Folder | Description |
| ----------- | ----------- |
| `Automation` | This directory contains all of the required files to support the Ansible automation and IaC. |
| `cldemo2/ci-common` | This directory contains the common scripts used for CI/CD in all of the officially supported colden standard demo projects. All of the scripts called by the `gitlab-ci.yml` file that perform the work in the CI pipeline exist here. |
| `simulation` | This directory contains all the files required to support the base Cumulus Networks Reference Topology simulation. This is where the `topology_converter`, `Vagrantfile`, and all the associated provisioning scripts for the base reference simulation topology live. |
| `.git` | This directory contains the Git project data and configuration. This is technically part of the configuration as code, but should really never need to be manually modified or customized. Git commands look for this directory to perform their work on the files of the project. If you are creating your own custom project, delete this folder or fork the project in GitLab. |
| `.gitignore` | This file informs Git which files to ignore and not track as part of the project. This  includes the `.vagrant` directory inside the simulation directory and other dynamic runtime files that are not useful or intended to be part of the source code of the project. <br>Note: Not including the `.vagrant` directory in your `.gitignore` file can lead to an unnecessarily large Git repository. |
| `├── .gitlab-ci.yml` | This file defines the CI pipeline stages and jobs for GitLab CI. This is a type of configuration file. The example provided in the Cumulus Linux golden standard projects is a starting point and reference for how to model your own CI pipeline. Refer to the GitLab CI documentation for more information. |
| `└── tests` | This folder contains the CI test scripts for the project. These scripts are copied into the simulation and run from inside of the simulation. Each project and demo has a unique set of tests so scripts for this stage of CI are broken out from the rest of the common CI scripts and remain unique to the project.|

These demo simulations are a good basis for how to organize your own project. In our unique use case we are providing a common base topology for reuse across many different possible solution architectures. For this reason, we are using a Git submodule to include that base reference topology with the automation repository so everything can be packaged together.

For real world deployments, the use of a Git submodule is unlikely to be necessary or useful. It makes more sense, in cases without the use of a submodule, have the `simulation` folder and the `ci-common` folder be under the root of the project instead of inside a subfolder as they are in the golden standard demos. This additional cldemo2 folder is imposed by the submodule feature.

{{%notice note%}}

If you choose to make this suggested change, it has an impact and requires changes to the hard-coded relative paths in the `.gitlab-ci.yml` file and the ci-common scripts to not include the cldemo2 subfolder.

{{%/notice%}}

## Customize a Simulation

Building a custom simulation is the foundation of transforming and automating your network and operations. A custom Vagrant/libvirt topology using Cumulus VX is generated automatically by using the `topology_converter` tool.

The `topology_converter` handles the complexity of building, generating, and maintaining the Vagrantfile. The `topology_converter` produces a Vagrantfile and brings with it all of the associated bootstrap provisioning scripts to be able to provide the experience of performing a simple `vagrant up` and having a connected network simulation ready to receive further network configuration.

Because a Vagrantfile is difficult to build, modify, and maintain by hand, there is really no other feasible way to manage a custom simulation other than by using and relying on the `topology_converter` utility.

{{%notice note%}}

Cumulus Networks does not recommended you manually edit and maintain a raw Vagranfile. Always use `topology_converter` workflows to make changes to the Vagrantfile.

{{%/notice%}}

Refer to the `topology_converter` GitLab project and documentation for detailed information about the `topology_converter` utility, all of its options, and detailed instructions on how to build a `.dot` file. These are the high level steps required to create a custom Cumulus VX topology:

1. Consider how to handle out-of-band management. The easiest option is to use the [“Automated Network Management" feature](https://gitlab.com/cumulus-consulting/tools/topology_converter/-/tree/master/documentation/auto_mgmt_network). Alternatively, the out of band management network can be manually created in the topology.dot file to more accurately represent your production network.
2. Create a `topology.dot` file. The name of the file does not have to be topology.dot, but the contents must be in the graphviz format and syntax. Use the cldemo2.dot file in the Cumulus Linux Reference Topology project as a reference or template to define your own set of network nodes, attributes and links.
3. Put all of the topology_converter project files and your custom topology.dot file in a ‘simulation’ folder of your project. Perform a git clone to obtain all of the topology_converter project files. Copying the topology_converter files from the ‘simulation’ directory of The Cumulus Linux Reference Topology (cldemo2) is possible, but has a number of extr
4. Create the Vagrantfile from your topology definition. Ensure the `-p libvirt` option is specified. If the “automated Network Management" feature is used, the `-c` option in `topology_converter` is required.

`python3 ./topology_converter.py ./topology.dot -c -p libvirt`

### Customize Automation and IaC

Cumulus Networks has provided a scalable and extensible framework for how to store or encode a data center network configuration and deploy it using Ansible automation. IaC or infrastructure as code is the concept of thinking about your network configuration as a form of source code just like in the software development world.

Modifying these aspects of the Cumulus Production Ready Automation commands a deep understanding of the underlying technologies which are beyond the scope of this guide. Namely Ansible and Ansible roles, jinja2 template engine and the basics of structuring and representing data using yaml. Cumulus Professional services is available to assist you through a process of customizing and operationalizing this Production Ready Automation custom for your unique requirements. Contact your sales representative for more details.

In a software context, code is “built" to produce “binaries" or executable code specific for the OS and CPU architecture that will run it. A compiler is used to render high level human readable code into a format that’s understood by the machine. In a network context, the final build product needs to be the flat configuration files running on the network devices that they understand. The automation engine used to deploy to the network usually drives what the base IaC code will look like. For Cumulus Production Ready Automation using Ansible, the config as code examples are a combination of jinja2 templates and structured variable files in the automation folders. During deployment with Ansible, the templates are populated with values from the structured variable files. The process of generating the final configuration from the templates and variables is sometimes referred to as “rendering" the configuration. In continuing the analogy to software development, “rendering" the configuration during Ansible deployment is similar to the process of compiling and linking source code into an executable file.

There are a nearly infinite number of ways to implement network configuration or infrastructure as code. Flat configuration files are a form code, so the most primitive version of IaC could be simply storing copies of device configuration files. This primitive example can even have deployment be automated; simply push flat configuration files using your automation tools, from the central repository to the devices. That would be one way to implement automation and IaC, but without realizing many of the scale and efficiency benefits of the solutions. In this example, configuration files are still modified individually, per device. 

Customizing the Ansible automation to create or modify roles and modify the playbooks requires proficiencies using Ansible that are out of scope of this guide. The core concept in use to provide the granular control of the inventory is based on Ansible roles. Please see Ansible’s documentation on using roles [here](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html).

## Customize and Set Up CI/CD

### Network CI/CD on Gitlab

CI/CD is the next logical step after successfully implementing your version of IaC and thinking about applying the concept of automatically producing builds of your network code for automated testing and verification.

Cumulus Production Ready Automation uses Gitlab for CI/CD. References for Gitlab CI can be found [here](https://docs.gitlab.com/ee/ci/README.html). **Caution**: Most CI/CD Guides and references are contextualized for classic software development CI workflows. Our use case of CI/CD for the network is building network simulations as the product of the code is a corner case.

{{%notice note%}}

- Most cloud based CI tools are run inside containers and do not support running Cumulus Vx.
- Cumulus Production Ready Automation with Vagrant/libvirt only supports a single gitlab runner per Gitlab project.

{{%/notice%}}

A CI Pipeline is made up of stages that are executed in series or connected in a Pipeline. (One at a time in order until completion). A CI Stage consists of one or more jobs that can be executed in parallel. Jobs are individual CI tasks that you design and configure to either pass or fail. CI jobs are executed by a piece of software called a gitlab-runner.

### Gitlab Runner

`gitlab-runner` is an agent that you install on the server that is your dedicated simulation-host that will run the simulations and testing for CI/CD for your project. The gitlab-runner installs like any other software package and uses a unique registration token to connect and register to your gitlab project for your IaC.

After being registered to the project, it periodically polls outbound to gitlab.com CI as a service to see if there are any jobs in queue that it needs to run. If it finds a job, it executes it according to the `gitlab-ci.yml` file.

The `gitlab-runner` uses the `shell` executor type. We have a unique set of dependencies for building network simulations and heavy system requirements such that we require a dedicated runner for our project. The shell executor can be thought of as if a user were executing commands on the server from a bash shell. Due to this, native bash scripts are used to drive the CI jobs. See the gitlab-ci.

### Branching Strategy

Gitlab CI pipelines are dynamically built and then executed when code is pushed to the remote repository (normally gitlab.com). Different versions of code can exist on different branches as changes move upstream toward `master` and CI pipelines can be controlled independently and uniquely for each branch in a project. This ability to customize pipelines per branch are what allow for different automated workflows as changes are merged into upstream branches. An introduction to the gitlab flow best practices are [here](https://docs.gitlab.com/ee/topics/gitlab_flow.html) although be cautioned that a network and IaC operational workflow is a still a novel use case of most CI/CD implementations.

Cumulus Networks suggests the following branching strategy and as a simple starting point:
- `master` branch - represents what is currently deployed on the network. The pipeline that runs against this branch could deploy to your live network. This is the CD (continuous delivery or continuous deployment) 
- `dev` or Development or Staging Branch - represents changes that get deployed to the staging or development network and thoroughly tested. Referred to as `dev` branch moving forward.
- Private/working Branches - Branches that originate from the dev branch. These branches are where operators perform their work. A branch usually represents a change or set of changes for a common purpose. For example, a branch to track changes for each change request ticket maps nicely onto existing change control workflows. These branches are merged back into the `dev` branch after the work is completed.

Example Workflow Guidelines:
- All operators must have access to a development environment where they can stand up their own private versions of the network simulation to perform their work and local unit testing.
- (optional) Operators can develop test scripts for their CI testing phase to confirm/check their specific changes.
- All operators start work (clone) from the `dev` branch 
- All operators perform all of their own work in their private/working branch.
- After operators have complete their changes, their working branch is merged into the `dev` branch
- After merge to `dev`, the CI pipeline runs to build, deploy and test the network based on the current code in the `dev` branch (now with the changes from the merge)
- Only after the CI pipeline succeeds and all testing passes, should dev be allowed to be merged into the `master` branch.
- The code from the `master` branch is deployed to the live network.

The last step is currently expected to be performed manually in the Cumulus Networks Production Ready Automation examples. Automating the deployment to the live network from the `master` branch CI pipeline is the full realization of a completely automated CI/CD enabled network operations workflow. In a fully automated workflow, only the CI pipeline makes deployments to the live network when there is a merge to `master`. The merges to `master` are also automatic as a result of robust automated testing and a pass result from testing against the `dev` branch.

As a matter of practice, it is uncommon to need to fully automate deployments to the live production network. This is the “CD" “continuous delivery" component of the CI/CD paradigm. Most network operators still prefer to queue up changes in a batch and deploy to the live network manually from the `master` branch on a periodic schedule.

### Install and Register GitLab Runner to your Project

Installing and registering `gitlab-runner` to the project is a relatively simple task. It is important to remember that all jobs will run on the server and in the environment as the `gitlab-runner` user. Therefore, perform at least some manual testing and initial development for CI on your GitLab Runner server under that user as there are occasionally some thing such as vagrant plugins that differ per user.

See {{<link title="Example Install Scripts" text="Example Install Scripts">}} for a basic shell script to cover the baseline dependencies. This is only tested on Ubuntu 16.04 and Ubuntu 18.04.

1. Install the gitlab-runner software. The official instructions can be found here
2. Create the gitlab-runner user and setup the user environment:
    - Starting as root, add the gitlab-runner user to the `libvirtd` group
`adduser gitlab-runner libvirtd`
    - Change to gitlab-runner user
`sudo su - gitlab-runner`
    - Append `/usr/sbin` to the $PATH variable and put it in `.bashrc`
`echo 'PATH=/usr/sbin:$PATH' >> ./.bashrc`
    - Install the vagrant plugins that are needed when the gitlab-runner user runs CI jobs
`vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp`
3. Locate the gitlab-runner registration token for your project. This can be found on your project on gitlab.com. On the left panel, browse through Settings -> CI/CD. Then expand the “Runners" Section. Scroll down to the section “Set up a specific Runner manually" The registration token is in step 3. It will look something like this: `zLZLhVDkfJPq7eWXV6rw`
4. Perform the gitlab-runner registration.

Gitlab runner registration parameters:

| Gitlab Parameter | Setting |
| ---------------- | ------- |
| Gitlab-ci coordinator URL | https://gitlab.com |
| Gitlab-ci token |  From Step #3 above |
| Gitlab-ci description for this runner | Any informative description of this server |
| Gitlab-ci tags | None. Leave Blank. Press Return |
| Executor | shell |

```
user@hosti:~# gitlab-runner register
Runtime platform                                    arch=amd64 os=linux pid=143019 revision=4c96e5ad version=12.9.0
Running in system-mode.

Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com/):
https://gitlab.com
Please enter the gitlab-ci token for this runner:
<Registration-token-from-step#3>
Please enter the gitlab-ci description for this runner:
[host]: <any-description-here>
Please enter the gitlab-ci tags for this runner (comma separated):
<Leave this blank! Just press enter here for NO TAGS>
Registering runner... succeeded                     runner=qfzmHDDk
Please enter the executor: docker+machine, parallels, virtualbox, docker-ssh, shell, ssh, docker-ssh+machine, kubernetes, custom, docker:
shell
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!
```

1. Start the gitlab-runner runner

```
user@host:~# gitlab-runner start
Runtime platform                                    arch=amd64 os=linux pid=145596 revision=4c96e5ad version=12.9.0
user@host:~#
```

2. Confirm the runner status on gitlab.com

On your project on gitlab.com, on the left panel, browse through Settings -> CI/CD. Then expand the “Runners" Section. Scroll down to the section “Runners activated for this project". Check to make sure the runner that was just registered is present in this list with a green “ready" indicator.

## Gitlab CI Variables

Gitlab CI provides a number of built in environment variables for use in CI scripts. A list of all of the available variables provided by gitlab can be found [here](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)

The included ci-common and test scripts rely on the following built in variables:

```
$CI_COMMIT_SHORT_SHA
$CI_COMMIT_BRANCH
$CI_PROJECT_NAME
```
Gitlab also provides a way for a user to define custom environment variables for the runner for that project. Access to view, change, or add variables require that you have developer or maintainer privileges on the project and can access the project's settings.

Since NetQ installation requires unique configuration and access keys, these are stored as masked (and can optionally be configured to be used/valid only on protected branches) variables with the Gitlab project. Then these variables are called during the NetQ provisioning CI job to allow for programmatic provisioning of NetQ in the automated CI pipeline. 

It is generally considered best practice to configure a dedicated/dummy CI and CLI user in NetQ cloud User Management. This allows the generated access-key and secret-key from this account to be more easily disposable in the event they need to be revoked or changed. See the NetQ documentation for more information about setting up netQ users and generating auth keys to store with your CI/CD enabled gitlab project.
Variables required to support the provided CI scripts
Configure the following variables in the Settings -> CI/CD -> Variables area in Gitlab on your project if you wish to use the reference ci-common and test scripts unmodified:

|Variable Name | Descritpion |
|------------- | ----------- |
| `CONCURRENCY_ID` | An integer value to help the simulation\-host be able to support concurrent simulations for concurrent projects. This is requires if your gitlab runner supports multiple projects that may run simulations concurrently.<br>For example:<br> `1` |
| `NETQ_ACCESS_KEY` | A valid access\-key generated from the NetQ cloud user Management page.<br>For example:<br> `bf5802fd59456d7be723d85f99c303b5c943c536f75b86e1da8fb94a48a18dfa` |
| `NETQ_BOOTSTRAP_TARBALL` | The URL to the NetQ bootstrap tarball on the netq-ts. See the staging the NetQ installation tarballs for more information. This variable must be entered/stored in gitlab as base64 encoded due to the / characters in the path.<br>For example:<br> `L21udC9pbnN0YWxsYWJsZXMvbmV0cS1ib290c3RyYXAtMi40LjEudGd6` |
| `NETQ_CONFIG_KEY` | The config-key for your your dedicated premises for CI and simulation from Cumulus NetQ Cloud Onboarding process email.<br>For example:<br> `CXx0Dh1zY3XucHJXZDMubmV0cx5jdX11bHVzbmV0d29Ya3MuYd9tGLsD` |
| `NETQ_OPTA_TARBALL` | The URL of the NetQ OPTA install tarball. See the staging the NetQ installation tarballs section for more information. This variable must be entered/stored in gitlab as base64 encoded to due to the / characters in the path.<br>For example:<br> `L21udC9pbnN0YWxsYWJsZXMvTmV0US0yLjQuMS1vcHRhLnRneg==` |
| `NETQ_PREMISE_NAME` | The string of your premises name for this dedicated CI/CD simulation environment.<br>For example:<br> `netq-demo-dc-6` |
| `NETQ_SECRET_KEY` | The valid secret-key for the associated access-key that is also provided. Only available once at generation in NetQ Cloud User Management.<br>For example:<br> `hxXoSwlcJqKVyu7V/FT7eHpSKrz4jKIr15OMX9Z9MTI=` |

### Customize the CI Pipeline
Gitlab CI uses a configuration file contained in the project files to define the pipeline. A pipeline is made of up a series of sequential stages. A stage is made up of one or more jobs that may run in parallel. The .gitlab-ci.yml file defines the stages, jobs, what occurs in each job and also the order in which the stages are executed.

CI/CD for a network as code departs slightly from a traditional software code workflow. For our use case, first we must build and provision a simulation network that represents production. Building a simulation from scratch is the current paradigm that we use for our golden standard configurations. After creating a fresh simulation, we can then deploy our IaC to that contains our changes. Then, with those changes, we perform a testing phase to ensure that the network is functional for our needs. If all of that provisioning, deploying, and testing is successful, we can be confident that the same process, on production equipment, will share that same success.

{{%notice note%}}

It would also be possible to build a CI/CD pipeline for a simulation environment in an “always-on" mode; where the staging/development simulation is not destroyed after each pipeline run. This creates additional challenges such as rollback integrity after failed runs such as, “How do we ensure the pipeline properly undoes what it attempted, and failed to do?"

{{%/notice%}}

### Example GitLab CI Stages

lint - In the lint stage, basic yaml syntax checking is performed. This stage helps catch basic syntax and format errors that would cause failures in later stages and ensures good formatting.

prep simulation environment - This stage prepares the environment for the rest of the pipeline stages. Special dependencies for the CI pipeline jobs in later stages should be checked for and optionally installed or remediated in this stage.

oob-mgmt bringup - This stage is responsible for bringing up the devices that makeup the out of band management network. This comprises of the `oob-mgmt-server`, `oob-mgmt-switch`, and the `netq-ts`. This stage also copies the `automation` folder and `tests` folder from the demo project into the oob-mgmt-server and netq-ts. The `automation` folder contains the ansible playbooks, roles and inventory that will configure the network. The `tests` folder contains the testing scripts that are used in the later `test simulation` stage

network bringup - The network bringup stage consists of two jobs. These jobs are not related to each other and can run in parallel (if the gitlab-runner is configured with enough workers) to help speedup pipeline runs. The first job is the `network bringup` job. This job’s purpose is to simply use vagrant to build out the rest of the simulation network beyond simply the out of band management network. The other job that runs in this stage is the NetQ provisioning job. This job is simple in its steps, but takes the longest amount of time. This stage installed NetQ cloud from its two component tarball files. Bringing the out of band management network up first, allows us to immediately move into provisioning the NetQ Cloud server while the rest of the network is also being created and built.

provision simulation - This stage is responsible for running ansible playbooks on the oob-mgmt-server that provision the network with the changes that have been made to the branch.

test simulation - This stage also has two jobs that run in parallel. Testing is performed using NetQ and then additional network testing can be performed from the oob-mgmt-server. Each testing runs as it’s own job and thus both may run at the same time, in parallel.

cleanup simulation - In this final stage, the NetQ Cloud premises is cleaned up for the next simulation and the simulation itself is destroyed.

#### General Procedure - Customize CI Pipeline

With GitLab CI, the `.gitlab-ci.yml` file describes the CI Pipeline, its jobs and what each job does. This section focuses on reusing a `.gitlab-ci.yml` file from the Cumulus Production Ready Automation package for your own use.

The included example `.gitlab-ci.yml` files are created and defined specifically to separate out the complex logic of each job from the pipeline and job definition. In the `.gitlab-ci.yml` examples, each job has a single `script:` line. Each single `script:` line is a call to another shell script. This makes the `.gitlab-ci.yml` file neater, cleaner, and easier from which to start.

As a starting point, use a `.gitlab-ci.yml` file from one of the golden standard demo topologies as the starting point for your `.gitlab-ci.yml` file. The `.gitlab-ci.yml` file from the Cumulus Networks reference topology (cldemo2) does not contain a provision stage that calls an Ansible playbook to deploy a network configuration.

In our examples on Gitlab, we make use of [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to package the the base CI/CD scripts and the Cumulus Reference Topology itself (the Vagrantfile). This is only due to the need for reuse, but for production networks, this can all be packaged together in the same project. We do not normally recommend using a submodule unless there will be shared code across multiple projects.

When Git submodules are not in use for the project, you can remove the `variables:` key in a job, which is only required when the project is using a submodule. For example:

```
prep:
  stage: prep simulation environment
  variables:
    GIT_SUBMODULE_STRATEGY: recursive
  script:
    - bash ./cldemo2/ci-common/prep.sh
  only:
    - /^dev.*$/
```

You can modify this yaml output:

```
prep:
  stage: prep simulation environment
  script:
    - bash ./cldemo2/ci-common/prep.sh
  only:
    - /^dev.*$/
```

{{%notice note%}}

 If you are not using any submodules in your project, remove these two lines for each job when working from the `.gitlab-ci.yml` examples.

{{%/notice%}}

For each job that is defined in the `.gitlab-ci.yml` file, check the `script:` lines to ensure that the path is correct to each shell script. In the published Production Ready Automation examples, the paths to the shell scripts are inside the cldemo2 submodule.

### Add or Enable CI/CD to your Existing GitLab Project

The following steps provide a high level overview of how to implement and enable CI for your project using the model of calling discrete and modular bash scripts for each job in the provided example:

1. Plan a permanent dedicated GitLab Runner simulation host machine. Review system requirements and package dependencies.
2. Install GitLab Runner and package dependencies (see {{<link title="Example Install Scripts" text="Example Install Scripts">}} )
3. {{<link text="Register GitLab Runner to the project" title="#Install and register the gitlab-runner to your project" >}}. Pause GitLab Runner on the project until the rest of the supporting CI/CD scripts are in place. Disable shared and public runners for the project.
4. Evaluate the example CI pipeline design and stages. Use the `.gitlab-ci.yml` file as an example.
5. Place your `.gitlab-ci.yml` file in the root of your project.
6. Determine the CI scripts required for each job from your `.gitlab-ci.yml` file.
7. Create a folder to contain the CI scripts for your CI jobs. This is the `ci-common` scripts directory in the `cldemo2` project.
8. Populate your project’s CI scripts folder with the scripts called by the `.gitlab-ci.yml` file jobs (in the script: block).
9. Resume GitLab Runner on the project and start testing your CI pipeline by making commits and pushing to your project.
