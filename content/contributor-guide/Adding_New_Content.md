---
title: Adding New Content
author: Daniel Cawley
weight: 10
siteSlug: contributor-guide
---

After you have installed [hugo](https://gohugo.io/getting-started/installing/), 
cloned the [GitHub repository](https://github.com/CumulusNetworks/docs), and run 
the local server (`hugo server`), you are ready to add new content. 
First, `ctrl-c` to quit the docs server in your terminal window.

## Add New Pages

New pages are added in Hugo using 
[archetypes](https://gohugo.io/content-management/archetypes/#readout), 
which are Markdown (.md) templates that contain the front matter variables 
and default values.

To create a new Cumulus Linux Page *new-page.md*, run:

    hugo new cumulus-linux/new-page.md

To create a new Cumulus NetQ Page *new-page.md*, run:

    hugo new cumulus-netq/new-page.md

These commands can be used to create any Markdown page within the specified section
(Cumulus Linux or Cumulus NetQ, respectively) in  the `/content` directory.

New pages made with `hugo new` will have `draft: true` by default.

These page archetypes will fill and

### Front Matter

Each page in Hugo contains a .YAML front matter header. For example:

``` markdown
title: 802.1X Interfaces
author: Cumulus Networks
weight: 101
aliases:
 - /display/DOCS/802.1X+Interfaces
 - /pages/viewpage.action?pageId=8363046
pageID: 8363046
product: Cumulus Linux
version: 3.7
imgData: cumulus-linux
siteSlug: cumulus-linux
```

Hugo uses these parameters in the generation of the site.

## Add a New Section

Hugo defines sections by its location within the /content folder, and the name of the .md file.
Adding a section in Hugo is as simple as adding a new subdirectory, and creating a `_index.md` file
within that subdirectory. This can be done using archetypes and the `hugo new` commmand.

To create a new Cumulus Linux Section Test_Section, run:

    hugo new cumulus-linux/Test_Section/_index.md

This will create a new section called *Test Section*, at /content/cumulus-linux/Test_Section/_index.md
Setting `draft=true` in the front matter will render this section in the site and the side menu.

### Top Level Sections and Content Type

Top-level subdirectories under /content have different behavior in this theme.
These define the content 'type' that Hugo uses to build the site. Additionally,
