---
title: Adding New Content
author: Daniel Cawley
weight: 15
siteSlug: Writing_Guide
---

After you have installed hugo, cloned the github repository, and run the local server,
it is now time to add new content to the Docs site. First, `ctrl-c` to quit the docs server in your terminal window.

### Adding New Pages

New pages are added in Hugo using archetypes,
.md templates which contain the front matter variables and defaut values.

**To create a new Cumulus Linux Page "test_post.md"**
run `hugo new Cumulus_Linux/test_post.md`

**To create a new Cumulus NetQ Page "test_post.md"**
run  `hugo new Cumulus_NetQ/test_post.md`

These commands can be used to create any .md page within the according section in /content.
New pages made with `hugo new` will have `draft: true` by default.

## Adding a New Section
Hugo defines sections by its location within the /content folder, and the name of the .md file.
Adding a section in Hugo is as simple as adding a new subdirectory, and creating a `_index.md` file
within that subdirectory. This can be done using archetypes and the `hugo new` commmand.

**To create a new Cumulus Linux Section Test_Section**
run `hugo new Cumulus_Linux/Test_Section/_index.md`

This will create a new section "Test Section," at /content/Cumulus_Linux/_index.md
Setting draft=true in the front matter will render this section in the site and the side menu.

### Top Level Sections and Content type
Top-level subdirectories under /content have different behavior in this theme.
These define the content 'type' that Hugo uses to build the site. Additionally,
