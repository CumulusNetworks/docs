---
title: Set User Preferences
author: NVIDIA
weight: 150
toc: 4
---
Each user can customize the NetQ application display, change their account password, and manage their workbenches.

## Configure Display Settings

The Display card contains the options for setting the application theme, language, time zone, and date formats. There are two themes: a light theme and a dark theme, which is the default. You can choose to view data in the time zone where you or your data center resides. You can also select the date and time format, choosing words or number format and a 12- or 24-hour clock. All changes take effect immediately.

To configure the display settings:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.
2. Click **Profile & Preferences**.
3. Locate the Display card.

    {{<figure src="/images/netq/user-settings-profile-prefs-display-card-222.png" width="200">}}

4. In the **Theme** field, click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/> to select either dark or light theme. The following figure shows the light theme.

    {{<figure src="/images/netq/user-settings-profile-prefs-light-theme-400.png" width="700">}}

5. In the **Time Zone** field, click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/> to change the time zone from the default.  
    By default, the time zone is set to the user's local time zone. If a time zone has not been selected, NetQ defaults to the current local time zone where NetQ is installed. All time values are based on this setting. This is displayed in the application header, and is based on Greenwich Mean Time (GMT).  

    {{%notice tip%}}

You can also change the time zone from the header display.

    {{%/notice%}}

    {{<figure src="/images/netq/app-hdr-time-zone-222.png" width="75">}}

    If your deployment is not local to you (for example, you want to view the data from the perspective of a data center in another time zone) you can change the display to another time zone. The following table presents a sample of time zones:

    | Time Zone | Description                             | Abbreviation |
    | --------- | --------------------------------------- | ------------ |
    | GMT +12   | New Zealand Standard Time               | NST          |
    | GMT +11   | Solomon Standard Time                   | SST          |
    | GMT +10   | Australian Eastern Time                 | AET          |
    | GMT +9:30 | Australia Central Time                  | ACT          |
    | GMT +9    | Japan Standard Time                     | JST          |
    | GMT +8    | China Taiwan Time                       | CTT          |
    | GMT +7    | Vietnam Standard Time                   | VST          |
    | GMT +6    | Bangladesh Standard Time                | BST          |
    | GMT +5:30 | India Standard Time                     | IST          |
    | GMT+5     | Pakistan Lahore Time                    | PLT          |
    | GMT +4    | Near East Time                          | NET          |
    | GMT +3:30 | Middle East Time                        | MET          |
    | GMT +3    | Eastern African Time/Arab Standard Time | EAT/AST      |
    | GMT +2    | Eastern European Time                   | EET          |
    | GMT +1    | European Central Time                   | ECT          |
    | GMT       | Greenwich Mean Time                     | GMT          |
    | GMT -1    | Central African Time                    | CAT          |
    | GMT -2    | Uruguay Summer Time                     | UYST         |
    | GMT -3    | Argentina Standard/Brazil Eastern Time  | AGT/BET      |
    | GMT -4    | Atlantic Standard Time/Puerto Rico Time | AST/PRT      |
    | GMT -5    | Eastern Standard Time                   | EST          |
    | GMT -6    | Central Standard Time                   | CST          |
    | GMT -7    | Mountain Standard Time                  | MST          |
    | GMT -8    | Pacific Standard Time                   | PST          |
    | GMT -9    | Alaskan Standard Time                   | AST          |
    | GMT -10   | Hawaiian Standard Time                  | HST          |
    | GMT -11   | Samoa Standard Time                     | SST          |
    | GMT -12   | New Zealand Standard Time               | NST          |

6. In the **Date Format** field, select the date and time format you want displayed on the cards.  

    {{<figure src="/images/netq/user-settings-profile-prefs-date-format-222.png" width="200">}}

## Change Your Password

You can change your account password at any time.

To change your password:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.
2. Click **Profile & Preferences**.
3. In the Basic Account Info card, select **Change Password**.

    {{<figure src="/images/netq/user-settings-profile-prefs-basic-acct-info-card-222.png" width="200">}}

4. Enter your current password, followed by your new password.

    {{<figure src="/images/netq/change-passwd-modal-222.png" width="200">}}

5. Click **Save** to change to the new password.

## Manage Your Workbenches

Workbenches are an integral structure of the NetQ UI. They are where you collect and view the data that is important to you. For a detailed overview of workbenches, see {{<link title="Focus Your Monitoring Using Workbenches" text="Focus Your Monitoring Using Workbenches.">}}