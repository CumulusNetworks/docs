---
title: Adding New Content
author: Daniel Cawley
weight: 10
siteSlug: contributor-guide
version: 1.0
---

After you install [Hugo](https://gohugo.io/getting-started/installing/),
clone the [GitHub repository](https://github.com/CumulusNetworks/docs), and run
the local server (`hugo server`), you are ready to create new content.
First, `ctrl-c` to quit the docs server in your terminal window.

## Add a New Page

New pages are added in Hugo using
[archetypes](https://gohugo.io/content-management/archetypes/#readout),
which are Markdown (.md) templates that contain the front matter variables
and default values.

Before you add a new page, change to the /content directory within the docs
repository:

    cd docs/content

To create a new Cumulus Linux Page *new-page.md*, run:

    hugo new cumulus-linux/new-page.md

To create a new Cumulus NetQ Page *new-page.md*, run:

    hugo new cumulus-netq/new-page.md

These commands create a Markdown page within the specified section (Cumulus Linux or
Cumulus NetQ, respectively) in  the `/content` directory. Specifying a subdirectory
within the parent product directory enables you to put the file exactly where you
think it belongs. For example:

    hugo new cumulus-linux/Network-Virtualization/foo.md

New pages made with `hugo new` have `draft: true` set in the front matter by default.

### Front Matter

Each page in Hugo contains a .YAML front matter header. For example:

``` markdown
title: 802.1X Interfaces
author: Cumulus Networks
weight: 101
product: Cumulus Linux
version: 3.7
siteSlug: cumulus-linux
```

Hugo uses these parameters in the generation of the site. You only need to configure
the following:

- `title`: Generated from the filename when you created the file with `hugo new`.
- `author`: Feel free to put your name or GitHub username here.
- `weight`: Indicates where this page is ordered within the directory; the higher the
   weight, the further down the page appears in the left side navigation.
- `product`: Can be one of _Cumulus Linux_, _Cumulus NetQ_, _Cumulus VX_, _Cumulus RMP_
   or _Cumulus Chassis_.
- `version`: The latest product version number. Use only X.Y notation.
- `siteSlug`: This is useful if you intend on using the custom
  [_pageref_ shortcode](../Explanation_Of_Shortcodes/#adding-links-and-references).

## Add a New Section

Hugo defines sections by its location within the /content folder, and the name of the .md file.
Adding a section in Hugo is as simple as adding a new subdirectory, and creating an `_index.md` file
within that subdirectory. This can be done using archetypes and the `hugo new` command.

For example, to create a new section called Test_Section in Cumulus Linux, run:

    hugo new cumulus-linux/Test_Section/_index.md

This creates a new section called *Test Section*, at /content/cumulus-linux/Test_Section/_index.md.
Setting `draft=true` in the front matter renders this section in the site and the side menu.

### Top Level Sections and Content Type

Top-level subdirectories under /content have different behavior in this theme. These define
the content _type_ that Hugo uses to build the site. Do not add new top-level directories;
please [file a bug](https://github.com/CumulusNetworks/docs/issues/new) to request such changes
to the site.
