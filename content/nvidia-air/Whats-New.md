---
title: What's New
author: NVIDIA
weight: 20
product: NVIDIA Air
---
<!-- vale off -->
Check out the latest updates to {{<exlink url="https://air.nvidia.com" text="NVIDIA Air">}}.

## September 2023
<!-- Air:WhatsNew -->
### 82.2023.0911-012
- Improved messaging when a resource budget is exceeded
- Fixed a bug related to display of the NIC model for Ubuntu nodes
- Fixed a bug where new members of an organization were not allocated the appropriate resource budgets
- Updated config migrator to use Cumulus Linux 5.6.0
<!-- Air:WhatsNew -->

### 82.2023.0918-011
- Updated oob-mgmt-switch image
- Fixed an issue related to logging level of the Air Agent

## August 2023
### 82.2023.0824-012
- Added a new `link_id` field to the `/v1/interface/` API response

### 82.2023.0822-011
- Fixed an issue during creation of the configuration file for the Air agent on some nodes
- Fixed an issue where parallel jobs could result in an invalid simulation state
- Fixed an issue where stalled requests could prevent API access by some clients

## July 2023
### 82.2023.0724-011
- Updated API to support ordering
- Fixed an issue related to interface count limitations on certain platforms

### 82.2023.0717-011
- Updated user authorization process

### 82.2023.0706-012
- Fixed an issue when deleting a topology associated with active simulations
- Fixed an issue where links could be connected to the same interface on both ends

## June 2023
### 82.2023.0622-012
- Fixed an issue that caused the oob-mgmt-switch to lose the default route after reboot
- Increased resource budget limits for non-company emails

### 82.2023.0612-011
- Fixed an error encountered by the agent when a node woke up from sleep
- Added Cumulus Linux 5.5.1 to OS dropdown in the builder
- Added support for IPv4 based services

## May 2023
### 82.2023.0525-012
- Fixed a bug impacting simulation creation including a fake device with more than 256 interfaces

### 82.2023.0518-011
- Fixed a bug related to simulation state control and resource budgets
- Improved validation for the link API

### 82.2023.0515-016
- Added Cumulus Linux 5.5.0 to OS dropdown in the builder

### 82.2023.0511-015
- Added Cumulus Linux 5.5.0
- Fixed an issue related to image uploads

### 82.2023.0504-012
- Updated oob-mgmt-server to Ubuntu 22.04
- Added a limit of 256 for the maximum number of interfaces on a single node
- Updated resource budget limits for accounts using a company email
- Fixed a bug that prevented some simulations with TPM/UEFI from loading
- Fixed a bug in validation of image uploads

## April 2023
### 82.2023.0424-012
- Fixed an incorrect calculation for resource budgets in some scenarios
- Fixed an issue causing the login page to be shown instead of a node's console in some scenarios
- Applied new security updates

### 82.2023.0420-012
- Updated sleep handling for longer running simulations
- Fixed an issue related to reporting current state when loading larger simulations

### 82.2023.0418-011
- Added support for copying images between organizations
- Updated default resource limits

### 82.2023.0410-012
- Added Ubuntu 22.04
- Added SONiC 202205_2
- Backend infrastructure improvements

## March 2023
### 82.2023.0330-011
- Added new mechanism for anonymous simulation handling

### 82.2023.0323-011
- Added Cumulus Linux 4.3.1
- Added Cumulus Linux 4.4.5
- Added NetQ 4.5.0
- Updated Cumulus Linux 5.4.0

### 82.2023.0321-012
- Fixed a bug impacting automatic NetQ instructions impacting certain versions of Cumulus Linux
- Fixed a bug related to resource budget calculation

### 82.2023.0316-011
- Updated default resource limits
- Fixed a bug impacting filtering in the Demo Marketplace

### 82.2023.0306-011
- Added cookie management options

## February 2023
### 82.2023.0216-011
- Added Cumulus Linux 5.4.0
- Builder defaults to Cumulus Linux 5.4.0 for new nodes
- API documentation fixes

### 82.2023.0213-012
- Updated Cumulus Linux 3.7.9 image
- Updated Cumulus Linux 3.7.10 image
- Updated Cumulus Linux 3.7.11 image
- Updated Cumulus Linux 3.7.12 image
- Updated Cumulus Linux 3.7.13 image
- Updated Cumulus Linux 3.7.14 image
- Updated Cumulus Linux 3.7.14.2 image
- Updated Cumulus Linux 3.7.15 image
- Updated Cumulus Linux 3.7.16 image
- Fix for CVE-2022-25927

### 82.2023.0206-012
- API updates to protect against unsupported changes for running simulations

## January 2023
### 82.2023.0119-011
- Added Cumulus Linux 5.3.1

### 82.2023.0112-011
- Updated oob-mgmt-server image
  - Added socat package
- Updated generic/ubuntu1804 image
<!-- vale on -->
