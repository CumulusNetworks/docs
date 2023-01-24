---
title: Application Layout
author: NVIDIA
weight: 110
toc: 4
---
The NetQ UI contains two main areas:

- **Application Header**: Contains the main menu, NetQ version, search, validation summary, local time zone, premises list, and account information.
{{<figure src="/images/netq/application-header.png" alt="">}}


- **Workbench**: Contains a task bar and content cards (with status and configuration information about your network and its various components).

{{<figure src="/images/netq/workbench-main-body.png" alt="workbench displaying task bar and 5 cards" width="1200">}}

## Main Menu

Found in the application header, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu to navigate to:

| Header | Menu |
| ------ | ---- |
| <ul><li><strong>Search</strong>: a search bar to quickly find an item on the main menu</li><li><strong>Favorites</strong>: contains link to the user-defined favorite workbenches; <em>Home</em> points to the NetQ Workbench until reset by a user</li><li><strong>Workbenches</strong>: contains links to all workbenches</li><li><strong>Network</strong>: contains links to tabular data about various network elements and the What Just Happened feature</li><li><strong>Notifications</strong>: contains link to threshold-based event rules and notification channel specifications</li><li><strong>Admin</strong>: contains links to application management and lifecycle management features (only visible to users with Admin access role)</li></ul> | {{<figure src="/images/netq/sidenav-light-450.png" alt="" width="300">}} |
## Search

You can search for devices and cards in the Global Search field in the header. It behaves like most searches and can help you quickly find device information.

## NVIDIA Logo

Clicking the NVIDIA logo takes you to your favorite workbench. For details about specifying your favorite workbench, refer to {{<link title="Set User Preferences">}}.

## Validation Summary

Found in the header, the validation summary displays the overall health of your network.

{{<notice note>}}
On initial start up of the application, it can take up to an hour to reach an accurate health indication as some processes only run every 30 minutes.
{{</notice>}}

## Workbenches

A workbench comprises a given set of cards. A pre-configured default workbench, NetQ Workbench, is available to get you started. You can customize your workbenches by adding or removing cards. For more detail about managing your data using workbenches, refer to {{<link title="Focus Your Monitoring Using Workbenches">}}.

## Cards

Cards display information about your network. Each card describes a particular aspect of the network and can be expanded to display information and statistics at increasingly granular levels. You can add and remove cards from a workbench, move between cards and card sizes, and make copies of cards to show different levels of data at the same time. For details about working with cards, refer to {{<link url="Access-Data-with-Cards">}}.

## User Settings

Each user can customize the NetQ application display, time zone and date format; change their account password; and manage their workbenches. This is all performed from User Settings <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> > **Profile & Preferences**. For details, refer to {{<link title="Set User Preferences">}}.
