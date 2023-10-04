---
title: Application Layout
author: NVIDIA
weight: 110
toc: 4
---
The NetQ UI contains two main areas:

- **Application Header**: Contains the main menu, NetQ version, search, validation summary, local time zone, premises list, and account information.
{{<figure src="/images/netq/versionless-top-470.png" alt="" width="1300">}}


- **Workbench**: Contains a task bar and cards that display operative status and network configuration information.

{{<figure src="/images/netq/workbench-main-body.png" alt="workbench displaying task bar and 5 cards" width="1200">}}

## Main Menu

Found in the application header, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** to navigate to:

| Description | Menu |
| ------ | ---- |
| <ul><li><strong>Search</strong>: searches items listed under the main menu</li><li><strong>Favorites</strong>: lists a user's favorite workbench</li><li><strong>Workbenches</strong>: lists all workbenches</li><li><strong>Network</strong>: lists various network elements which you can select to monitor your network's state</li><li><strong>Traffic histograms</strong>: lists types of network traffic that can be visualized with histograms</li><li><strong>Notifications</strong>: lets you set up notification channels and create rules for threshold-crossing events</li><li><strong>Admin</strong>: lets administrators manage NetQ itself and access lifecycle management</li></ul> | {{<figure src="/images/netq/side-nav-470.png" alt="" width="300">}} |
## Search

You can search for devices and cards in the Global Search field in the header. It behaves like most searches and provides suggestions to help you quickly find device information or populate your workbench with sets of cards.

## NVIDIA Logo

Selecting the NVIDIA logo takes you to your favorite workbench. For details about specifying your favorite workbench, refer to {{<link title="Set User Preferences">}}.

## Validation Summary

Found in the header, the validation summary displays the overall health of your network.

{{<notice note>}}
On initial start up, it can take up to an hour to reach an accurate health indication as some processes only run every 30 minutes.
{{</notice>}}

## Workbenches

A workbench comprises a given set of cards. A pre-configured default workbench, NetQ Workbench, is available to get you started. You can customize your workbenches by adding or removing cards. For more detail about managing your data using workbenches, refer to {{<link title="Focus Your Monitoring Using Workbenches">}}.

## Cards

Cards display information about your network. Each card describes a particular aspect of the network and can be expanded to display information and statistics at increasingly granular levels. You can add or remove cards from a workbench, move between cards and card sizes, and make copies of cards that display different levels of data for a given time period. For details about working with cards, refer to {{<link url="Access-Data-with-Cards">}}.

## User Settings

Each user can customize the NetQ display, time zone, and date format; change their account password; and manage their workbenches. Navigate to <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> **User Settings** &nbsp;<span aria-label="and then">> **Profile & Preferences**. For details, refer to {{<link title="Set User Preferences">}}.
