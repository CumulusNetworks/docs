---
title: Set User Preferences
author: NVIDIA
weight: 150
toc: 4
---
Each user can customize the NetQ application display, change their account password, and manage their workbenches.

## Configure Display Settings

The Display card contains the options for setting the application theme (light or dark), language, time zone, and date formats.

To configure the display settings:

1. Select <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.
2. Select **Profile & Preferences**.
3. Locate the Display card:

    {{<figure src="/images/netq/user-settings-display-card.png" alt="display card with fields specifying theme, language, time zone, and date format." width="200">}}

4. In the **Theme** field, click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/> to select either dark or light theme. The following figure shows the light theme:

    {{<figure src="/images/netq/user-settings-light-theme.png" alt="NetQ workbench displayed in light theme" height="275" width="1000">}}

5. In the **Time Zone** field, click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/> to change the time zone from the default.  
    
    By default, the time zone is set to the user's local time zone. If a time zone has not been selected, NetQ defaults to the current local time zone where NetQ is installed. All time values are based on this setting. This is displayed (and can also be changed) in the application header, and is based on Greenwich Mean Time (GMT).  If your deployment is not local to you (for example, you want to view the data from the perspective of a data center in another time zone) you can change the display to a different time zone.

6. In the **Date Format** field, select the date and time format you want displayed on the cards.  

    {{<figure src="/images/netq/date-format-field.png" alt="" width="200">}}

## Change Your Password

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.
2. Click **Profile & Preferences**.
3. In the Basic Account Info card, select **Change password**.

    {{<figure src="/images/netq/basic-reset-password.png" alt="" width="200">}}

4. Enter your current password, followed by your new password.

5. Select **Save**.

To reset the password for an admin account, follow {{<link title="Add and Manage Accounts#Reset an Admin Password" text="these instructions">}}.

## Manage Your Workbenches

A workbench is similar to a dashboard. This is where you collect and view the data that is important to you. You can have more than one workbench and manage them with the Workbenches card located in **Profile & Preferences**. From the Workbenches card, you can view, sort, and delete workbenches. For a detailed overview of workbenches, see {{<link title="Focus Your Monitoring Using Workbenches" text="Focus Your Monitoring Using Workbenches.">}}