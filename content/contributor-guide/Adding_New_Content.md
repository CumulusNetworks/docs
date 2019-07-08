---
title: Adding New Content
author: Daniel Cawley
weight: 15
siteSlug: Writing_Guide
---

After you have installed hugo, cloned the github repository, and run the local server,
it is now time to add new content to the Docs site. First, `ctrl-c` to quit the docs server in your terminal window.

## Adding New Pages

New pages are added in Hugo using archetypes,
.md templates which contain the front matter variables and defaut values.

**To create a new Cumulus Linux Page "test_post.md"**
run `hugo new cumulus-linux/test_post.md`

**To create a new Cumulus NetQ Page "test_post.md"**
run  `hugo new cumulus-netq/test_post.md`

These commands can be used to create any .md page within the according section in /content.
New pages made with `hugo new` will have `draft: true` by default.

These page archetypes will fill and

### Front Matter
Each page in Hugo contains a .YAML front matter header. For example.

```
title: 802.1X Interfaces
author: Cumulus Networks
weight: 101
aliases:
 - /display/DOCS/802.1X+Interfaces
 - /pages/viewpage.action?pageId=8363046
pageID: 8363046
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
```
Hugo uses these parameters in the generation of the site.

## Adding a New Section
Hugo defines sections by its location within the /content folder, and the name of the .md file.
Adding a section in Hugo is as simple as adding a new subdirectory, and creating a `_index.md` file
within that subdirectory. This can be done using archetypes and the `hugo new` commmand.

**To create a new Cumulus Linux Section Test_Section**
run `hugo new cumulus-linux/Test_Section/_index.md`

This will create a new section "Test Section," at /content/cumulus-linux/_index.md
Setting draft=true in the front matter will render this section in the site and the side menu.

### Top Level Sections and Content type
Top-level subdirectories under /content have different behavior in this theme.
These define the content 'type' that Hugo uses to build the site. Additionally,
