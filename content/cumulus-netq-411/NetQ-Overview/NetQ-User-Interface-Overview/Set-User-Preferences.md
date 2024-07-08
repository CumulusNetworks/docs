---
title: Set User Preferences
author: NVIDIA
weight: 150
toc: 4
---
This section describes how to customize your NetQ display, change your password, and manage your workbenches.

## Configure Display Settings

The Display card contains the options for setting the application theme (light or dark), language, time zone, and date formats.

To configure the display settings:

1. Select <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> **User Settings** in the top-right corner.
2. Select **Profile & Preferences**.
3. Locate the Display card:

    {{<figure src="/images/netq/display-card-411.png" alt="display card with fields specifying theme, language, time zone, and date format." width="200">}}

4. Select the **Theme** field and choose either dark or light. The following figure shows the light theme:

    {{<figure src="/images/netq/light-theme-411.png" alt="NetQ workbench displayed in light theme" width="1000">}}

5. Select the **Time zone** field to adjust the time zone.
    
    By default, the time zone is set to the user's local time zone. If a time zone has not been selected, NetQ defaults to the current local time zone where NetQ is installed. All time values are based on this setting. If your deployment is not local to you (for example, you want to view the data from the perspective of a data center in another time zone) you can change the display to a different time zone.

6. In the **Date format** field, select the date and time format you want displayed on the cards.  

    {{<figure src="/images/netq/date-format-field.png" alt="" width="200">}}

## Change Your Password

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> **User Settings** in the top-right corner.
2. Click **Profile & Preferences**.
3. In the Basic Account Info card, select **Change password**.

    {{<figure src="/images/netq/basic-reset-password.png" alt="" width="200">}}

4. Enter your current password, followed by your new password. Then select **Save**.

{{<notice note>}}
To reset the password for an admin account, refer to {{<link title="Add and Manage Accounts#Reset an Admin Password" text="Reset an Admin Password">}}.
{{</notice>}}