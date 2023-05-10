---
title: Customize Production Ready Automation
weight: 45
---

This section provides guidance on how to customize and adapt the main individual pieces of the Cumulus Production Ready Automation to suit your own needs and to work for your own environment.

Building a simulation that represents your production network is the first step in taking advantage of next generation NetDevOps style operational workflows. Ideally, you test all network changes in simulation or in a staging environment before they reach production. Cumulus VX is an extremely lightweight and high fidelity simulation platform. With a small memory footprint and every software component being exactly the same as Cumulus Linux running on hardware, you can construct a highly scalable and robust simulation environment that matches the production environment, from interface labels down to MAC addresses.

These main features of the Cumulus Production Ready Automation depend on each other to provide the fully operationalized automated data center:

- **Base simulation** is the NVIDIA reference topology simulation; a common base topology for reuse across many different possible solution architectures.
- **Automation providing Infrastructure as Code (IaC)** lets you store a coded version of your network configuration in a source code repository. NVIDIA Production Ready Automation uses Ansible as its automation engine and applies Ansible best practices that include the use of roles, Jinja2 templates, and structured variable files. Complete Ansible configurations include playbooks, roles, templates, variables, and inventory.
- **Continuous Integration and Continuous Deployment (CI/CD)** has its basis in the idea that you can make changes frequently and at any time of day. However, before you can integrate the changes for deployment into production, you must test to ensure that the change does not cause an unintended consequence. After testing passes and you integrate the change from the continuous integration (CI) stage, you can carry out the continuous deployment (CD) stage automatically. For the network, this means that you can deploy the changes that pass automated testing to the production environment automatically. Automated continuous deployment is still uncommon for network operations.

   {{%notice note%}}

NVIDIA strongly recommends that you deploy a CI strategy, but recommends against a CD strategy. Using CD can lead to network changes during critical business hours with unintended consequences. Only  consider CD if your organization has proper testing and operations in place.

{{%/notice%}}

## System Requirements

For a robust simulation environment and CI/CD with GitLab, NVIDIA recommends a dedicated, always-on, enterprise class server.

{{%notice note%}}

Using the NetQ server in individual development environments is not required and is typically only needed for CI testing, where you installed GitLab Runner and registered it to your CI/CD enabled project.

{{%/notice%}}

### Hardware Requirements

- Memory requirements vary. To estimate the needs for your simulation, use these values:
  - 768MB for each Cumulus Linux node
  - 512MB for each Ubuntu 18.04 host
  - 1024MB for the oob-mgmt-server
  - 768MB for the oob-mgmt-switch
  - 8192MB for netq-ts
- Disk requirements vary. Vagrant and libvirt use thin disk images but a good reference point is:
  - 256GB disk with 64GB or more free memory
  - 1TB or more disk recommended
  - SSD recommended (NetQ requirement)
- High speed broadband or wideband Internet connection for package installs during simulation startup
- A minimum of eight x86_64 CPU cores

### Software Requirements

- Operating Systems:
  - Cumulus Linux 3.7.11 or later
  - Cumulus NetQ 2.4 or later (optional)
  - Ubuntu 16.04 or 18.04 (NVIDIA has *not* tested other Linux distributions)
- Software Packages:
  - Vagrant 2.2.4 or later
  - Libvirt
  - Qemu
  - Git
- Vagrant plugins
  - Vagrant-libvirt
  - Vagrant-scp

To see sample bash scripts used to install the software package and environment dependencies, refer to {{<link title="Example Install Scripts" text="Example Install Scripts">}}.

### CI/CD Requirements

- An account with GitLab.com or your own internal GitLab instance
- A dedicated simulation environment for the GitLab Runner to start and test simulations
- The GitLab Runner package installed on the simulation host machine (set up a GitLab Runner user and environment on the system)
- A project on your GitLab instance set up with simulation, automation, and IaC
- A NetQ Cloud account with a premises/site dedicated for simulation

### Anatomy of a Golden Standard Demo Project

These main features of the Production Ready Automation (base simulation, automation and IaC, and CI/CD) depend on each other to provide the fully operationalized automated data center. In a NVIDIA official golden standard demo repository, the important files and folders map to the three main features as follows:

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

| <div style="width:200px">File/Folder | Description |
| ----------- | ----------- |
| `Automation` | Contains all required files to support the Ansible automation and IaC. |
| `cldemo2/ci-common` | Contains the common scripts used for CI/CD in all the officially supported golden standard demo projects. All the scripts called by the `gitlab-ci.yml` file that perform the work in the CI pipeline exist here. |
| `simulation` | Contains all the files required to support the base NVIDIA reference topology simulation. This is where the `topology_converter`, `Vagrantfile`, and all the associated provisioning scripts for the base reference simulation topology live. |
| `.git` | Contains the Git project data and configuration. This is part of the configuration as code, which does not require modification or customization. Git commands look for this directory to perform work on the project files. If you are creating your own custom project, delete this folder or fork the project in GitLab. |
| `.gitignore` | Informs Git which files to ignore and not track as part of the project. This includes the `.vagrant` directory inside the simulation directory and other dynamic runtime files that are not useful or intended to be part of the source code of the project. <br>Note: Not including the `.vagrant` directory in your `.gitignore` file can lead to an unnecessarily large Git repository. |
| `.gitlab-ci.yml` | Defines the CI pipeline stages and jobs for GitLab CI. This is a type of configuration file. The example provided in the Cumulus Linux golden standard projects is a starting point and reference for how to model your own CI pipeline. Refer to the GitLab CI documentation for more information. |
| `tests` | Contains the CI test scripts for the project. These scripts get copied into the simulation and run from inside the simulation. Each project and demo has a unique set of tests so scripts for this stage of CI break out from the rest of the common CI scripts and remain unique to the project.|

These demo simulations provide a good basis for how to organize your own project. The NVIDIA reference topology provides a common base topology for reuse across many different possible solution architectures. For this reason, a Git submodule includes that base reference topology with the automation repository so it can package everything together. For real world deployments, the use of a Git submodule is unlikely to be necessary or useful. In cases without the use of a submodule, it makes more sense to have the `simulation` folder and the `ci-common` folder under the root of the project instead of inside a subfolder. The submodule feature requires the additional `cldemo2` folder.

{{%notice note%}}

If you do not use a Git submodule, you need to change to the hard-coded relative paths in the `.gitlab-ci.yml` file and the `ci-common scripts` to exclude the `cldemo2` subfolder.

{{%/notice%}}

## Customize a Simulation

Building a custom simulation is the foundation of transforming and automating your network and operations. You generate a custom Vagrant and libvirt topology using Cumulus VX automatically using the `topology_converter` tool.

The `topology_converter` handles the complexity of building, generating, and maintaining the `Vagrantfile`. It produces a `Vagrantfile` and brings with it every associated bootstrap provisioning script to provide the experience of performing a simple `vagrant up` and having a connected network simulation ready to receive further network configuration.

{{%notice note%}}

NVIDIA does not recommended you manually edit and maintain a raw `Vagranfile`. Always use `topology_converter` workflows to make changes to the `Vagrantfile`.

{{%/notice%}}

For detailed information about the `topology_converter` utility and detailed instructions on how to build a `.dot` file, refer to the `topology_converter` GitLab project and documentation.

These are the high level steps required to create a custom Cumulus VX topology:

1. Consider how to handle out-of-band management. The easiest option is to use {{<exlink url="https://gitlab.com/cumulus-consulting/tools/topology_converter/-/tree/master/documentation/auto_mgmt_network" text="Automated Network Management">}}. To more accurately represent your production network, you can create the out-of-band management network in the `topology.dot` file.
2. Create a `topology.dot` file. Ensure that the contents are in Graphviz format and syntax. Use the `cldemo2.dot` file in the NVIDIA reference topology project as a template to define your own set of network nodes, attributes, and links.
3. Put all the `topology_converter` project files and your custom `topology.dot` file in a `simulation` folder for your project. Run the `git clone` command to obtain all the `topology_converter` project files.
4. Create the `Vagrantfile` from your topology definition. Make sure you specify the `-p libvirt` option. If you use Automated Network Management, you must specify the `-c` option in `topology_converter`. For example:

   ```
   python3 ./topology_converter.py ./topology.dot -c -p libvirt
   ```

## Customize Automation and IaC

NVIDIA provides a scalable and extensible framework to store or encode a data center network configuration and deploy it using Ansible automation. IaC lets you think about your network configuration as a form of source code, just like in the software development world.

In a software context, you build code to produce binaries or executables specific to the operating system and CPU architecture that run it. A compiler renders high level human readable code into a format that the machine can understand. In a network context, the final build product needs to be the flat configuration files running on the network devices that they understand. The automation engine used to deploy to the network usually drives what the base IaC code looks like. For NVIDIA Production Ready Automation using Ansible, the configuration as code examples are a combination of jinja2 templates and structured variable files in the automation folders. During deployment with Ansible, it populates the templates with values from the structured variable files. The process of generating the final configuration from the templates and variables is often referred to as rendering the configuration. Rendering the configuration during Ansible deployment is similar to the process of compiling and linking source code into an executable file in software development.

You have many ways to implement network configuration or infrastructure as code. Flat configuration files are a form of code, so the most primitive version of IaC is storing copies of device configuration files. This primitive example can even have automated deployment; push flat configuration files using your automation tools from the central repository to the devices. That is one way to implement automation and IaC, but without realizing many of the scale and efficiency benefits of the solutions. In this example, configuration files are still modified individually, per device.

Modifying aspects of the Cumulus Production Ready Automation for your unique requirements requires a deep understanding of the underlying technologies that are beyond the scope of this guide, such as Ansible and Ansible roles, jinja2 template engine, and the basics of structuring and representing data using YAML. Cumulus Professional services is available to assist you through this process. Contact your sales representative for more details.

For information about Ansible and roles, refer to the {{<exlink url="https://docs.ansible.com/ansible/latest/user_guide/" text="Ansible User Guide">}}.

## Customize CI/CD

CI/CD is the next logical step after successfully implementing your version of IaC and applying the concept of automatically producing builds of your network code for automated testing and verification.

Cumulus Production Ready Automation uses GitLab for CI/CD. For information about GitLab CI, refer to the {{<exlink url="https://docs.gitlab.com/ee/ci/README.html" text="GitLab CI/CD documentation">}}.

{{%notice note%}}

- Most CI/CD guides and references use classic software development CI workflows for context. The NVIDIA use case for CI/CD is building network simulations as the product of the code, which is a corner case.
- Most cloud-based CI tools run inside containers and do not support running Cumulus VX.
- NVIDIA Production Ready Automation with Vagrant and libvirt only supports a single GitLab Runner per GitLab project.

{{%/notice%}}

A CI pipeline comprises stages that execute in series or connected in a pipeline (one at a time in order until completion). A CI stage consists of one or more jobs that you can execute in parallel. Jobs are individual CI tasks that you design and configure to either pass or fail. A piece of software called a GitLab Runner executes the CI jobs.

### GitLab Runner

GitLab Runner is an agent that you install on the server as the dedicated simulation host that runs the simulations and testing for CI/CD for your project. The GitLab Runner installs like any other software package, and uses a unique registration token to connect and register to your GitLab project for your IaC.

After you register GitLab Runner to the project, it periodically polls outbound to GitLab.com CI as a service to see if there are any jobs in queue that need to run. If it finds a job, it executes according to the `gitlab-ci.yml` file.

GitLab Runner uses the `shell` executor type. There are a unique set of dependencies for building network simulations and heavy system requirements; therefore, NVIDIA requires a dedicated runner for the project. You use native bash scripts to drive the CI jobs.

### Branching Strategy

GitLab CI pipelines build dynamically and then execute when you push code to the remote repository (normally GitLab.com). Different versions of code can exist on different branches as changes move upstream toward `master`, and you can control CI pipelines independently and uniquely for each branch in a project. This ability to customize pipelines per branch are what allow for different automated workflows as you merge changes into upstream branches. For an introduction to GitLab flow best practices, refer to {{<exlink url="https://docs.gitlab.com/ee/topics/gitlab_flow.html" text="Introduction to GitLab Flow">}}.

NVIDIA recommends the following branching strategy as a simple starting point:

- The `master` branch represents what is currently deployed on the network. The pipeline that runs against this branch can deploy to your live network. This is the CD.
- The development or staging branch (`dev`) represents changes that get deployed to the staging or development network and thoroughly tested.
- Private or working branches that originate from the `dev` branch are where operators perform their work. A branch usually represents a change or set of changes for a common purpose. For example, a branch to track changes for each change request ticket maps nicely onto existing change control workflows. These branches get merged back into the `dev` branch after the work finishes.

Example workflow guidelines:

- All operators must have access to a development environment where they can stand up their own private versions of the network simulation to perform their work and local unit testing.
- (optional) Operators can develop test scripts for their CI testing phase to check specific changes.
- All operators start work (clone) from the `dev` branch.
- All operators perform all their own work in their private or working branch.
- After operators complete their changes, they merge their working branch into the `dev` branch.
- After a merge to `dev`, the CI pipeline runs to build, deploy, and test the network based on the current code in the `dev` branch (including the changes from the merge).
- Merge `dev` into the `master` branch only after the CI pipeline succeeds and all testing passes.
- Deploy the code from the `master` branch to the live network.

Perform the last step manually in the NVIDIA Production Ready Automation examples. Automating the deployment to the live network from the `master` branch CI pipeline is the full realization of a completely automated CI/CD-enabled network operations workflow. In a fully automated workflow, only the CI pipeline makes deployments to the live network when there is a merge to `master`. The merges to `master` are also automatic as a result of robust automated testing and a pass result from testing against the `dev` branch.

It is uncommon to need to fully automate deployments to the live production network. This is the continuous delivery component of the CI/CD paradigm. Most network operators still prefer to queue up changes in a batch and deploy to the live network manually from the `master` branch on a periodic schedule.

### Install and Register GitLab Runner

All jobs run on the server and in the environment as the GitLab Runner user. Perform at least some manual testing and initial development for CI on your GitLab Runner server under that user, as some vagrant plugins might differ per user.

Refer to {{<link title="Example Install Scripts" text="Example Install Scripts">}} to see a basic shell script that covers the baseline dependencies.

1. Install the GitLab Runner software.
2. Create the GitLab Runner user and set up the user environment:
    1. As root, add the GitLab Runner user to the `libvirtd` group:

      ```
      user@host:~# adduser gitlab-runner libvirtd
      ```

    2. Change to GitLab Runner user:

       ```
       user@host:~# sudo su - gitlab-runner
       ```

    3. Append `/usr/sbin` to the `$PATH` variable and put it in `.bashrc`:

       ```
       user@host:~# echo 'PATH=/usr/sbin:$PATH' >> ./.bashrc
       ```

    4. Install the vagrant plugins that the GitLab Runner user needs to run the CI jobs:

       ```
       user@host:~# vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp
       ```

3. Locate the GitLab Runner registration token for your project. You can find the registration token for your project on GitLab.com. On the left panel, browse through Settings -> CI/CD, then expand the *Runners* Section. Scroll down to the *Set up a specific Runner manually* section. The registration token is in step 3. It looks similar to this: `zLZLhVDkfJPq7eWXV6rw`

4. Perform the GitLab Runner registration. The GitLab Runner registration parameters are:

    | GitLab Parameter | Setting |
    | ---------------- | ------- |
    | Gitlab-ci coordinator URL | https://gitlab.com |
    | Gitlab-ci token |  From step 3 above. |
    | Gitlab-ci description for this runner | Any informative description of this server. |
    | Gitlab-ci tags | None. Leave Blank. Press Return. |
    | Executor | shell |

    ```
    user@host:~# gitlab-runner register
    Runtime platform                         arch=amd64 os=linux pid=143019 revision=4c96e5ad version=12.9.0
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
    Runner registered successfully. Feel free to start it, but if it is running already the config should be automatically reloaded!
    ```

5. Start GitLab Runner:

   ```
   user@host:~# gitlab-runner start
   Runtime platform                    arch=amd64 os=linux pid=145596 revision=4c96e5ad version=12.9.0
   user@host:~#
   ```

6. Confirm the runner status on GitLab.com. On your project on GitLab.com, browse through **Settings**|**CI/CD** on the left panel, then expand the *Runners* section. Scroll down to the *Runners activated for this project* section. Check to make sure that the runner you registered is present in this list with a green ready indicator.

### Gitlab CI Variables

GitLab CI provides many built-in environment variables for use in CI scripts. For a list of all the available variables provided by GitLab, refer to {{<exlink url="https://docs.gitlab.com/ee/ci/variables/predefined_variables.html" text="Predefined Variables">}}.

The included `ci-common` and `test` scripts rely on the following built-in variables:

```
$CI_COMMIT_SHORT_SHA
$CI_COMMIT_BRANCH
$CI_PROJECT_NAME
```

GitLab also provides a way for you to define custom environment variables for the runner for that project. Access to view, change, or add variables require that you have developer or maintainer privileges on the project and can access the project settings.

Because the NetQ installation requires unique configuration and access keys, these get stored as masked variables with the GitLab project (you can configure the keys to be valid only on protected branches). These variables get called during the NetQ provisioning CI job to allow for programmatic provisioning of NetQ in the automated CI pipeline.

It is best practice to configure a dedicated or dummy CI and CLI user in NetQ Cloud User Management. This allows the generated access-key and secret-key from this account to be more easily disposable in case you need to revoke or change them. For more information about setting up NetQ users and generating auth keys to store with your CI/CD enabled GitLab project, refer to the {{<kb_link latest="netq" text="NetQ documentation">}}.

If you want to use the reference `ci-common` and `test` scripts unmodified, configure the following variables in the **Settings**|**CI/CD**|**Variables** area in GitLab on your project:

|Variable Name | Descritpion |
|------------- | ----------- |
| `CONCURRENCY_ID` | An integer value to help the simulation host support concurrent simulations for concurrent projects. You must specify this variable if your GitLab Runner supports multiple projects that can run simulations concurrently.<br>For example:<br> `1` |
| `NETQ_ACCESS_KEY` | A valid access\-key generated from the NetQ Cloud User Management page.<br>For example:<br> `bf5802fd59456d7be723d85f99c303b5c943c536f75b86e1da8fb94a48a18dfa` |
| `NETQ_BOOTSTRAP_TARBALL` | The URL to the NetQ bootstrap tarball on netq-ts. For more information, refer to the {{<kb_link latest="netq" text="NetQ documentation">}}. You must store this variable in GitLab as base64 encoded due to the slash characters (/) in the path.<br>For example:<br> `L21udC9pbnN0YWxsYWJsZXMvbmV0cS1ib290c3RyYXAtMi40LjEudGd6` |
| `NETQ_CONFIG_KEY` | The config-key for your dedicated premises for CI and simulation from the Cumulus NetQ Cloud Onboarding process email.<br>For example:<br> `CXx0Dh1zY3XucHJXZDMubmV0cx5jdX11bHVzbmV0d29Ya3MuYd9tGLsD` |
| `NETQ_OPTA_TARBALL` | The URL of the NetQ OPTA install tarball. You must store this variable in GitLab as base64 encoded due to the slash characters (/) in the path.<br>For example:<br> `L21udC9pbnN0YWxsYWJsZXMvTmV0US0yLjQuMS1vcHRhLnRneg==` |
| `NETQ_PREMISE_NAME` | The string of your premises name for this dedicated CI/CD simulation environment.<br>For example:<br> `netq-demo-dc-6` |
| `NETQ_SECRET_KEY` | The valid secret-key for the associated access-key that is also provided. Only available one time at generation in NetQ Cloud User Management.<br>For example:<br> `hxXoSwlcJqKVyu7V/FT7eHpSKrz4jKIr15OMX9Z9MTI=` |

### Customize the CI Pipeline

GitLab CI uses a configuration file in the project files to define the pipeline. A pipeline consists of a series of sequential stages. A stage comprises one or more jobs that can run in parallel. The `.gitlab-ci.yml` file defines the stages, jobs, what occurs in each job, and the order in which the stages execute.

CI/CD for a network as code departs slightly from a traditional software code workflow. NVIDIA builds and provisions a simulation network that represents production first. Building a simulation from scratch is the current paradigm used for the golden standard configurations. After creating a fresh simulation, the IaC that contains the changes gets deployed. Then, with those changes, the testing phase begins to ensure that the network is functional for your needs. If all provisioning, deploying, and testing is successful, you can be confident that the same process, on production equipment, has the same success.

{{%notice note%}}

It is also possible to build a CI/CD pipeline for a simulation environment in *always-on* mode, where the staging and development simulation is not destroyed after each pipeline run. However, this creates additional challenges, such as rollback integrity after failed runs.

{{%/notice%}}

#### Example GitLab CI Stages

| Stage  | Description |
| ------ | ----------- |
| lint | Performs basic YAML syntax checking to help catch basic syntax and format errors that might cause failures in later stages, and ensures good formatting. |
| prep simulation environment | Prepares the environment for the rest of the pipeline stages. Check special dependencies for the CI pipeline jobs in later stages and optionally install or remediate in this stage.|
|oob-mgmt bringup | Starts up the devices in the out-of-band management network (`oob-mgmt-server`, `oob-mgmt-switch`, and `netq-ts`). This stage also copies the `automation` folder and `tests` folder from the demo project into the oob-mgmt-server and netq-ts. The `automation` folder contains the Ansible playbooks, roles, and inventory that configures the network. The `tests` folder contains the testing scripts used in the `test simulation` stage, later.|
| network bringup | Consists of two jobs that are not related to each other and can run in parallel (if you configure the GitLab Runner with enough workers) to help speed up pipeline runs. The `network bringup` job uses vagrant to build out the rest of the simulation network beyond the out-of-band management network. The NetQ provisioning job is simple in its steps, but takes the longest amount of time. This stage installs NetQ Cloud from its two component tarball files. Bringing the out-of-band management network up first allows you to immediately move into provisioning the NetQ Cloud server while creating and building the rest of the network. |
| provision simulation | Runs Ansible playbooks on the oob-mgmt-server that provision the network with the changes made to the branch. |
| test simulation | Consists of two jobs that run in parallel. You perform testing using NetQ, then you perform additional network testing from the oob-mgmt-server. |
| cleanup simulation | Cleans up the NetQ Cloud premises for the next simulation and destroys the simulation. |

#### General Procedure

With GitLab CI, the `.gitlab-ci.yml` file describes the CI Pipeline, its jobs and what each job does. This section describes how to reuse a `.gitlab-ci.yml` file from the NVIDIA Production Ready Automation package for your own use.

<!-- vale off -->
The included example `.gitlab-ci.yml` files are created and defined specifically to separate the complex logic of each job from the pipeline and job definition. In the `.gitlab-ci.yml` examples, each job has a single `script:` line. Each `script:` line is a call to another shell script. This makes the `.gitlab-ci.yml` file neater, cleaner, and easier from which to start.
<!-- vale on -->

Use a `.gitlab-ci.yml` file from one of the golden standard demo topologies as the starting point for your `.gitlab-ci.yml` file. The `.gitlab-ci.yml` file from the NVIDIA reference topology (cldemo2) does not contain a provision stage that calls an Ansible playbook to deploy a network configuration.

The examples on GitLab make use of [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to package the base CI/CD scripts and the NVIDIA reference topology itself (the `Vagrantfile`). This is only due to the need for reuse, but for production networks, you can package all this together in the same project. NVIDIA does not recommend using a submodule unless you have shared code across multiple projects.

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

Modify the above YAML output as follows:

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

For each job defined in the `.gitlab-ci.yml` file, check the `script:` lines to ensure that the path is correct to each shell script. In the published Production Ready Automation examples, the paths to the shell scripts are inside the `cldemo2` submodule.

### Add CI/CD to your Existing GitLab Project

The following steps provide a high level overview of how to implement and enable CI for your project by calling discrete and modular bash scripts for each job:

1. Plan a permanent dedicated GitLab Runner simulation host machine. Review system requirements and package dependencies.
2. Install GitLab Runner and package dependencies (see {{<link title="Example Install Scripts" text="Example Install Scripts">}}).
3. {{<link text="Register GitLab Runner to the project" title="#install and register gitlab runner" >}}. Pause GitLab Runner on the project until the rest of the supporting CI/CD scripts are in place. Disable shared and public runners for the project.
4. Evaluate the example CI pipeline design and stages. Use the `.gitlab-ci.yml` file as an example.
5. Place your `.gitlab-ci.yml` file in the root of your project.
6. Determine the CI scripts required for each job from your `.gitlab-ci.yml` file.
7. Create a folder to contain the CI scripts for your CI jobs. This is the `ci-common` scripts directory in the `cldemo2` project.
8. Populate the CI `scripts` folder in your project with the scripts called by the `.gitlab-ci.yml` file jobs (in the `script:` block).
9. Resume GitLab Runner on the project and start testing your CI pipeline by making commits and pushing to your project.

