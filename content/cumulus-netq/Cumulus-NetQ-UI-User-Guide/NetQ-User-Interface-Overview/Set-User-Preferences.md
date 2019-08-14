---
title: Set User Preferences
author: Cumulus Networks
weight: 511
aliases:
 - /display/NETQ22/NetQ-User-Interface-Overview
 - /pages/viewpage.action?pageId=12321856
pageID: 12321856
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
Each user can customize the NetQ application display, change his account
password, and manage his workbenches.

## Configure Display Settings

The Display card contains the options for setting the application theme,
language, time zone, and date formats. There are two themes available: a
Light theme and a Dark theme (default). The screen captures in this
document are all displayed with the Dark theme. English is the only
language available for this release. You can choose to view data in the
time zone where you or your data center resides. You can also select the
date and time format, choosing words or number format and a 12- or
24-hour clock. All changes take effect immediately.

To configure the display settings:

1.  Click {{% imgOld 44 %}} in the application header to open the **User Settings** options.

    {{% imgOld 45 %}}

2.  Click **Profile & Preferences**.
3.  Locate the Display card.

    {{% imgOld 46 %}}

4.  In the **Theme** field, click {{% imgOld 47 %}} to select your choice of theme. This figure shows the light theme. Switch back and forth as desired.

    {{% imgOld 48 %}}

5.  In the **Time Zone** field, click {{% imgOld 49 %}} to change the time zone from the default.  
    By default, the time zone is set to the user's local time zone. If a
    time zone has not been selected, NetQ defaults to the current local
    time zone where NetQ is installed. All time values are based on this
    setting. This is displayed in the application header, and is based
    on Greenwich Mean Time (GMT).  

    {{% imgOld 50 %}}

    **Note**: You can also change the time zone from the header
    display.

    If your deployment is not local to you (for example, you want to
    view the data from the perspective of a data center in another time
    zone) you can change the display to another time zone. The
    following table presents a sample of time zones:

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


6.  In the **Date Format** field, select the data and time format you
    want displayed on the cards.  

    {{% imgOld 51 %}}

    The four options include the date displayed in words or abbreviated
    with numbers, and either a 12- or 24-hour time representation.

7.  Return to your workbench by clicking {{% imgOld 52 %}} and selecting a workbench from the NetQ list.

## Change Your Password

You can change your account password at any time should you suspect
someone has hacked your account or your administrator requests you to do
so.

To change your password:

1.  Click {{% imgOld 53 %}} in the application header to open the **User Settings** options.

    {{% imgOld 54 %}}

2.  Click **Profile & Preferences**.
3.  Locate the Basic Account Info card.

    {{% imgOld 55 %}}

4.  Click **Change Password**.
5.  Enter your current password.
6.  Enter and confirm a new password.

    {{% imgOld 56 %}}

7.  Click **Save** to change to the new password, or click **Cancel** to
    discard your changes.
8.  Return to your workbench by clicking {{% imgOld 57 %}} and selecting a workbench from the NetQ list.

## Manage Your Workbenches

You can view all of your workbenches in a list form, making it possible
to manage various aspects of them. There are public and private
workbenches. Public workbenches are visible by all users. Private
workbenches are visible only by the user who created the workbench. From
the Workbenches card, you can:

  - **Specify a favorite workbench**: This tells NetQ to open with that
    workbench when you log in instead of the default Cumulus Workbench.
  - **Search for a workbench**: If you have a large number of
    workbenches, you can search for a particular workbench by name, or
    sort workbenches by their access type or cards that reside on them.
  - **Delete a workbench:** Perhaps there is one that you no longer use.
    You can remove workbenches that you have created (private
    workbenches). An administrative role is required to remove
    workbenches that are common to all users (public workbenches).

    {{%notice info%}}

It is strongly recommended that you do not delete the default
    Cumulus Networks workbench. Once deleted, you must contact support
    to regain access to it. Extreme caution is recommended when deleting
    all other workbenches. Once they have been deleted, they cannot be
    restored.

    {{%/notice%}}

To manage your workbenches:

1.  Click {{% imgOld 58 %}} in the application header to open the **User Settings** options.

    {{% imgOld 59 %}}

2.  Click **Profile & Preferences**.
3.  Locate the Workbenches card.

    {{% imgOld 60 %}}

4.  To specify a favorite workbench, click and drag {{% imgOld 61 %}} next to the left of the desired workbench name.
5.  To search and/or sort the workbench list by name, access type, and
    cards present on the workbench, click the relevant header and begin
    typing your search criteria.
6.  To delete a workbench, hover over the workbench name to view the
    **Delete** button. As an administrator, you can delete both private
    and public workbenches.
7.  Return to your workbench by clicking {{% imgOld 62 %}} and selecting a workbench from the NetQ list.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
