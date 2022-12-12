---
title: NVUE Object Model
author: NVIDIA
weight: 117
toc: 3
---

The NVUE object model definition uses the {{<exlink url="https://github.com/OAI/OpenAPI-Specification" text="OpenAPI specification (OAS)">}}. Similar to YANG {{<exlink url="https://datatracker.ietf.org/doc/html/rfc6020" text="(RFC 6020">}} and {{<exlink url="https://datatracker.ietf.org/doc/html/rfc7950" text="RFC 7950)">}}, OAS is a data definition, manipulation, and modeling language (DML) that lets you build model-driven interfaces for both humans and machines. Although the computer networking and telecommunications industry commonly uses YANG (standardized by IETF) as a DML, the adoption of OpenAPI is broader, spanning cloud to compute to storage to IoT and even social media. The {{<exlink url="https://www.openapis.org/about" text="OpenAPI Initiative (OAI) consortium">}} leads OpenAPI standardization, a chartered project under the Linux Foundation.

The OAS schema forms the management plane model with which you configure, monitor, and manage the Cumulus Linux switch. The v3.0.2 version of OAS defines the NVUE data model.

Like other systems that use OpenAPI, the NVUE OAS schema defines the endpoints (paths) exposed as RESTful APIs. With these REST APIs, you can perform various create, retrieve, update, delete, and eXecute (CRUDX) operations. The OAS schema also describes the API inputs and outputs (data models).

You can use the NVUE object model in these two ways:

- Through the NVUE REST API, where you run the GET, PATCH, DELETE, and other REST APIs on the NVUE object model endpoints to configure, monitor, and manage the switch. Because of the large user community and maturity of OAS, you can use several popular tools and libraries to create client-side bindings to use the NVUE REST API.
- Through the NVUE CLI, where you configure, monitor and manage the Cumulus Linux network elements. The CLI commands translate to their equivalent REST APIs, which Cumulus Linux then runs on the NVUE object model.

The CLI and the REST API are equivalent in functionality; you can run all management operations from the REST API or the CLI. The NVUE object model drives both the REST API and the CLI management operations. All operations are consistent; for example, the CLI `nv show` commands reflect any PATCH operation (create) you run through the REST API.

<!-- vale off -->
NVUE follows a declarative model, removing context-specific commands and settings. It is structured as a *big tree* that represents the entire state of a Cumulus Linux instance. At the base of the tree are high level branches representing objects, such as *router* and *interface*. Under each of these branches are further branches. As you navigate through the tree, you gain a more specific context. At the leaves of the tree are actual attributes, represented as key-value pairs. The path through the tree is similar to a filesystem path.
<!-- vale on -->
{{<img src = "/images/cumulus-linux/nvue-architecture.png">}}

Cumulus Linux installs NVUE by default and enables the NVUE service `nvued`.
