---
title: Application Layout
author: Cumulus Networks
weight: 250
toc: 4
---
The NetQ UI contains two main areas:

- **Application Header** (1): Contains the main menu, recent actions history, search capabilities, NetQ version, quick health status chart, local time zone, premises list (cloud-only), and user account information.
- **Workbench** (2): Contains a task bar and content cards (with status and configuration information about your network and its various components).

{{< figure src="/images/netq/app-layout-cumulus-wb-areas-highlighted-241.png" width="700" >}}

## Main Menu

Found in the application header, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> to open the main menu which provides navigation to:

- **Favorites**: contains link to the user-defined favorite workbenche; Home is listed by default and points to the Cumulus Workbench
- **NetQ**: contains links to all workbenches
- **Network**: contains links to tabular data about various network elements and the What Just Happened feature
- **Admin**: contains link to user documentation and application management features
- **Notifications**: contains link to event notification configuration

{{< figure src="/images/netq/main-menu-241.png" width="500" >}}

## Recent Actions

Found in the header, Recent Actions keeps track of every action you take on your workbench and then saves each action with a timestamp. This enables you to go back to a previous state or repeat an action.

To open Recent Actions, click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-clock.svg" height="18" width="18"/>. Click on any of the actions to perform that action again.

{{< figure src="/images/netq/recent-actions-222.png" width="250" >}}

## Search

The Global Search field in the UI header enables you to search for devices. It behaves like most searches and can help you quickly find device information. For more detail on creating and running searches, refer to {{<link title="Create and Run Searches">}}.

## Cumulus Networks Logo

Clicking on the Cumulus logo takes you to your favorite workbench. For details about specifying your favorite workbench, refer to {{<link title="Set User Preferences">}}.

## Quick Network Health View

Found in the header, the graph and performance rating provide a view into the health of your network at a glance.

{{< figure src="/images/netq/quick-ntwk-health-header-222.png" width="200" >}}

{{%notice note%}}
On initial start up of the application, it may take up to an hour to reach an accurate health indication as some processes run every 30 minutes.
{{%/notice%}}

## Workbenches

A workbench is comprised of a given set of cards. A pre-configured default workbench, Cumulus Workbench, is available to get you started. It contains Device Inventory, Switch Inventory, Alarm and Info Events, and Network Health cards. On initial login, this workbench is opened. You can create your own workbenches and add or remove cards to meet your particular needs. For more detail about managing your data using workbenches, refer to {{<link title="Focus Your Monitoring Using Workbenches">}}.

## Cards

Cards present information about your network for monitoring and troubleshooting. This is where you can expect to spend most of your time. Each card describes a particular aspect of the network. Cards are available in multiple sizes, from small to full screen. The level of the content on a card varies in accordance with the size of the card, with the highest level of information on the smallest card to the most detailed information on the full-screen view. Cards are collected onto a workbench where you see all of the data relevant to a task or set of tasks. You can add and remove cards from a workbench, move between cards and card sizes, and make copies of cards to show different levels of data at the same time. For details about working with cards, refer to {{<link title="Access Data with Cards">}}.

## User Settings

Each user can customize the NetQ application display, change their account password, and manage their workbenches. This is all performed from User Settings <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> > Profile & Preferences. For details, refer to {{<link title="Set User Preferences">}}.

## Format Cues

Color is used to indicate links, options, and status within the UI.

| Item                                | Color  |
| ----------------------------------- | ------ |
| Hover on item                       | Blue   |
| Clickable item                      | Black  |
| Selected item                       | Green  |
| Highlighted item                    | Blue   |
| Link                                | Blue   |
| Good/Successful results             | Green  |
| Result with critical severity event | Pink   |
| Result with high severity event     | Red    |
| Result with medium severity event   | Orange |
| Result with low severity event      | Yellow |
