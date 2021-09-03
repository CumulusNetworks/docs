---
title: Pre-built Demos
author: NVIDIA
weight: 50
version: "1.0"
---

NVIDIA Air supports the ability to integrate a Continuous Integration pipeline. It provides workflows to onboard production code and have it tested against a digital simulation of the network.


## Requirements

In order to use the NVIDIA Air Continuous Integration as a Service (CIaaS), the following requirements must be met.

1. Infrastructure as Code
2. Topology of Data Center

### Infrastructure as Code

The configurations and deployment mechanism must be stored in a centralized git repository. Common git repositories include {{<exlink url="https://github.com" text="Github">}} and {{<exlink url="https://gitlab.com" text="Gitlab">}}.

Infrastructure as code can exist in many way. An example of an advanced solution can be obtained through the NVIDIA {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/cumulus_ansible_modules/" text="Production Ready Automation">}}.