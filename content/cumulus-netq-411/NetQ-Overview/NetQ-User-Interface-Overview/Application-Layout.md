---
title: Application Layout
author: NVIDIA
weight: 110
toc: 4
---
The NetQ UI contains two main areas:

- **Application Header**: Contains the main menu, NetQ version, global search field, device count, premises list, and account information.
{{<figure src="/images/netq/header-layout-411.png" alt="" width="1300">}}


- **Workbench**: Contains a task bar and cards that display operative status and network configuration information.

{{<figure src="/images/netq/workbench-full-411.png" alt="workbench displaying task bar and dashboard" width="1200">}}

## Main Menu

Select the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** in the top-left corner to navigate to:

| Description | Menu |
| ------ | ---- |
| <ul><li><strong>Search</strong>: searches items listed under the main menu</li><li><strong>Inventory</strong>: lists network's inventory of devices </li><li><strong>Fabric</strong>: lists various network elements which you can select to monitor your network's state </li><li><strong>Spectrum-X</strong>: lists network monitoring tools exclusive to Spectrum switches </li><li><strong>Tools</strong>: lists tools to visualize and validate network operations</li><li><strong>Alerts</strong>: lets you set up notification channels and create rules for threshold-crossing events</li><li><strong>Admin</strong>: lets administrators manage NetQ itself and access lifecycle management</li></ul> | {{<figure src="/images/netq/sidebar-menu-411.png" alt="" width="300">}} |
## Search

You can search for devices or cards in the global search field in the header. Right-click the hostname of any switch in your network to open a dashboard in a new tab that displays a comprehensive overview of platform information, events, and interfaces for that switch.

{{<figure src="/images/netq/global-search-exit-411.png" alt="" width="350">}}

## NVIDIA Logo

Selecting the NVIDIA logo takes you to your favorite workbench. For details about specifying your favorite workbench, refer to {{<link title="Set User Preferences">}}.

## Workbenches

A workbench is a dashboard that displays a set of cards. A pre-configured default workbench, NetQ Workbench, is available to get you started. You can create multiple workbenches and customize them by adding or removing cards. For more detail about managing your data using workbenches, refer to {{<link title="Focus Your Monitoring Using Workbenches">}}.

## Cards

Cards display information about your network. Each card describes a particular aspect of the network and can be expanded to display information and statistics at increasingly granular levels. You can add or remove cards from a workbench, move between cards and card sizes, and make copies of cards that display different levels of data for a given time period. For details about working with cards, refer to {{<link url="Access-Data-with-Cards">}}.

## User Settings

Each user can customize the NetQ display, time zone, and date format; change their account password; and manage their workbenches. Navigate to <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> **User Settings** &nbsp;<span aria-label="and then">> **Profile & Preferences**. For details, refer to {{<link title="Set User Preferences">}}.
