---
title: Set User Preferences
author: NVIDIA
weight: 150
toc: 4
---
Each user can customize the NetQ application display, change his account password, and manage his workbenches.

## Configure Display Settings

The Display card contains the options for setting the application theme, language, time zone, and date formats. Two themes are available: a Light theme and a Dark theme (default). The screen captures in this document are all displayed with the Dark theme. English is the only language available for this release. You can choose to view data in the time zone where you or your data center resides. You can also select the date and time format, choosing words or number format and a 12- or 24-hour clock. All changes take effect immediately.

To configure the display settings:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.

    {{<figure src="/images/netq/user-settings-profile-prefs-selected-222.png" width="150">}}

2. Click **Profile & Preferences**.
3. Locate the Display card.

    {{<figure src="/images/netq/user-settings-profile-prefs-display-card-222.png" width="200">}}

4. In the **Theme** field, click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/> to select your choice of theme. This figure shows the light theme. Switch back and forth as desired.

    {{<figure src="/images/netq/user-settings-profile-prefs-light-theme-320.png" width="700">}}

5. In the **Time Zone** field, click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/> to change the time zone from the default.  
    By default, the time zone is set to the user's local time zone. If a time zone has not been selected, NetQ defaults to the current local time zone where NetQ is installed. All time values are based on this setting. This is displayed in the application header, and is based on Greenwich Mean Time (GMT).  

    **Tip**: You can also change the time zone from the header display.

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

    The four options include the date displayed in words or abbreviated with numbers, and either a 12- or 24-hour time representation. The default is the third option.

7. Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> and selecting a workbench from the NetQ list.

## Change Your Password

You can change your account password at any time should you suspect someone has hacked your account or your administrator requests you to do so.

To change your password:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.

    {{<figure src="/images/netq/user-settings-profile-prefs-selected-222.png" width="150">}}

2. Click **Profile & Preferences**.
3. Locate the Basic Account Info card.

    {{<figure src="/images/netq/user-settings-profile-prefs-basic-acct-info-card-222.png" width="200">}}

4. Click **Change Password**.
5. Enter your current password.
6. Enter and confirm a new password.

    {{<figure src="/images/netq/change-passwd-modal-222.png" width="200">}}

7. Click **Save** to change to the new password, or click **Cancel** to
    discard your changes.
8. Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> and selecting a workbench from the NetQ list.

## Manage Your Workbenches

You can view all of your workbenches in a list form, making it possible to manage various aspects of them. There are public and private workbenches. Public workbenches are visible by all users. Private workbenches are visible only by the user who created the workbench. From the Workbenches card, you can:

- **Specify a home workbench**: This tells NetQ to open with that workbench when you log in instead of the default Cumulus Workbench.
- **Search for a workbench**: If you have a large number of workbenches, you can search for a particular workbench by name, or sort workbenches by their access type or cards that reside on them.
- **Delete a workbench:** Perhaps there is one that you no longer use. You can remove workbenches that you have created (private workbenches). An administrative role is required to remove workbenches that are common to all users (public workbenches).

To manage your workbenches:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.

    {{<figure src="/images/netq/user-settings-profile-prefs-selected-222.png" width="150">}}

2. Click **Profile & Preferences**.
3. Locate the Workbenches card.

    {{<figure src="/images/netq/user-settings-profile-prefs-wbs-card-222.png" width="500">}}

4. To specify a home workbench, click to the left of the desired workbench name. <img src="https://icons.cumulusnetworks.com/49-Building-Construction/01-Houses/house-heart.svg" height="18" width="18"/> is placed there to indicate its status as your favorite workbench.
5. To search the workbench list by name, access type, and cards present on the workbench, click the relevant header and begin typing your search criteria.
6. To sort the workbench list, click the relevant header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/35-Text-Options/arrange-letter.svg" height="18" width="18"/>.
7. To delete a workbench, hover over the workbench name to view the **Delete** button. As an administrator, you can delete both private and public workbenches.
8. Return to your workbench by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> and selecting a workbench from the NetQ list.
