---
title: Continuous Integration
author: NVIDIA
weight: 50
version: "1.0"
product: NVIDIA Air
---

NVIDIA Air supports the ability to integrate a Network Continuous Integration (NetCI) pipeline. It provides workflows to onboard production code and have it tested against a digital simulation of the network.

## Scope
<!-- vale off -->
This feature is currently in early beta testing. To get involved in the beta, reach out to the NVIDIA Cumulus in the Cloud (CITC) team at citc-support@nvidia.com.
<!-- vale on -->
## Requirements

To use the NVIDIA Air Continuous Integration as a Service (CIaaS), you must do the following:

- Deploy Infrastructure as Code (IaC)
- Build the data center topology

### Deploy Infrastructure as Code

You must store the configurations and deployment mechanism in a centralized `git` repository. Common `git` repositories include {{<exlink url="https://github.com" text="GitHub">}} and {{<exlink url="https://gitlab.com" text="GitLab">}}.

{{%notice note%}}

Currently, GitLab is the only supported centralized code repository.

{{%/notice%}}

Infrastructure as code can exist in many ways. Below are two methods that you can use to implement a CI solution.

#### Simple IaC

The simplest form of IaC involves backing up and restoring configurations using a centralized configuration repository. NVIDIA Networking provides a {{<exlink url="https://gitlab.com/cumulus-consulting/features/simple-iac/" text="free publicly available repository simple IaC repository">}} that you can use to back up and restore files. Fork this repository, run it in your environment to back up your configurations, then use it to restore or apply and configuration changes. Any changes committed to the backed up configurations obtained through this repository result in a pipeline run of the CI workflow.

#### Advanced IaC

 One example of an advanced IaC solution is the NVIDIA {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/cumulus_ansible_modules/" text="Production Ready Automation">}} module. This code centralizes not only the configuration backup, but it creates a fully comprehensive automation deployment method including data structures, templates and feature-specific tasks.

### Build the Data Center Topology

You can build the data center topology using one of two methods. For new environments, you can use the Air topology builder tool to create the new topology. For existing environments, it is easier to use a script to convert the existing configuration into a topology file.

#### Topology Builder

You can find more details about this workflow in {{<link url="Custom-Topology/#build-a-custom-topology" text="Build a Custom Topology">}}.

Using the blank canvas, you can generate a full topology using the NVIDIA Air UI:

{{<img src="/images/guides/nvidia-air/CustomTopology.png" width="800px">}}

#### Topology From Existing Network

You can find more details about this workflow in {{<link url="Custom-Topology/#create-a-custom-topology-from-the-production-network" text="Create a Custom Topology from the Production Network">}}.

## Access NetCI

NVIDIA Air's continuous integration functionality is available via the direct link for {{<exlink url="https://air.nvidia.com/netci/" text="NetCI">}}.

Log in by creating a new account.

## Add a NetCI Workflow

After the first login, click **Get Started** to launch the configuration wizard:

{{<img src="/images/guides/nvidia-air/NetCI-GetStarted.png" width="800px">}}

### Connect a Repository

You must link to your `git` repository and allow the NVIDIA Air NetCI platform access to read the repository.

{{<img src="/images/guides/nvidia-air/NetCI-ConnectRepository.png" width="800px">}}

1. Enter the **Repository URL**. The repository URL is the parent level URL directly accessible over the internet. One example of this is:

       https://gitlab.com/cumulus-consulting/goldenturtle/cumulus_ansible_modules

1. Enter the **Access Token**. The repository generates the access token and you can normally get it through the UI. The following steps show how to generate the token from GitLab.

   1. Log in to GitLab, then select **Preferences**.

      {{<img src="/images/guides/nvidia-air/NetCI-GitlabPreferences.png" width="200px">}}

   1. Select **Access Tokens**.

      {{<img src="/images/guides/nvidia-air/NetCI-GitlabAccessTokens.png" width="200px">}}

   1. Create an access token by giving it a name and make sure to select *api* as the selected scope.

      {{<img src="/images/guides/nvidia-air/NetCI-GitlabTokenExample.png" width="600px">}}

   1. Take the newly generated personal access token and copy and paste it into the **Access Token** field in NVIDIA Air.

After you enter the repository URL and access token, the screen looks like this:

{{<img src="/images/guides/nvidia-air/NetCI-ConnectRepositoryPopulated.png" width="800px">}}

### Add a Network

The network defines the architecture that launches in NVIDIA Air as a simulation and the configuration that gets deployed into the simulation. All required input below is relative to the repository.

{{<img src="/images/guides/nvidia-air/NetCI-AddNetworkPopulated.png" width="600px">}}

- **Name**: The name of the network and CI environment to test
- **Topology File Path**: The relative path within the repository linked in the {{<link url="#connect-a-repository" text="previous section">}} that points to a `.dot` format topology file that defines the network
- **Configuration Deployment Command**: The command that when executed from the root directory of the repository can successfully deploy and provision the entire network

### Enable Tests

The NetCI environment has predefined standard set of tests that rely on NVIDIA NetQ as the backend validation tool.

{{<img src="/images/guides/nvidia-air/NetCI-EnableTests.png" width="600px">}}

You can define your own tests; see {{<link url="#add-tests" text="Add Tests">}} below.

### Summary

The last page of the wizard summarizes the entire configuration.

{{<img src="/images/guides/nvidia-air/NetCI-Summary.png" width="600px">}}

## Networks

You define and track networks on the **Networks** tab.

### Test Results

To see all test results, click and expand the desired network in the **Networks** section.

{{<img src="/images/guides/nvidia-air/NetCI-ManualTest.png" width="300px">}}

You can click and expand each stage to see more details of the results of each stage.

## Repositories

You define and track configured repositories on the **Repositories** tab.

## Tests

The **Tests** tab lists all supported tests and allows the user to run a single test at a time against the network infrastructure.

{{<img src="/images/guides/nvidia-air/NetCI-Tests.png" width="600px">}}

### Add Tests

The NetCI environment supports the uploading of individual tests. You define the tests in YAML format. Below are two examples:

Example 1:

```
Verify Underlay BGP: # test title
  version: 1.0.0 # optional version string, NetCI will auto-increment this when you make changes
  group: Baseline - Network Configuration # Test group name
  target: localhost # Node name where the steps should be run (localhost == oob-mgmt-server for Airwolf)
  # optional description, supports markdown
  description: Check all ipv4 unicast BGP peering within the SDN network
  steps: # all commands are run as 'cumulus' user
    - ansible -m shell -a \'echo \"cumulus@\$(hostname):mgmt-vrf:\~\$ net show bgp ipv4 unicast summary \"; net show bgp ipv4 unicast summary;echo \" \"\' network \| grep -v SUCCESS
  summary_regex: '.*' # optional regex; Each test will have "results" and a "summary". "results" is the full stdout/stderr, "summary" is only the part of stdout/stderr matching this regex
```

Example 2:

```
Nessus Scan switch:
  group: Operations and Security
  target: spine01
  description: Ensure fully configured switch can trigger and accept nessus scan.
  steps:
    - run_script
  script:python: |
    def deploy_ansible_config():
        ...
    def run_nessus_scan():
        ...
    def main():
        deploy_ansible_config()
        run_nessus_scan()
    if __name__ == '__main__':
        main()
```

Click **Add Tests** to add a new test.

{{<img src="/images/guides/nvidia-air/NetCI-AddTest.png" width="300px">}}
