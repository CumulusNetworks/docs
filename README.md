# Cumulus Networks Test Documentation Site

This a development website for Cumulus Networks Technical Documentation.
The site is built with the static site generator [Hugo](https://gohugo.io/documentation/)

## Installing the Test Documentation Site

In order to run the site locally

1. Install Hugo
    - https://gohugo.io/getting-started/installing/

2. Verify Hugo is installed with `hugo version`

3. Clone this repository with `git clone`

  - Note the site is dependent on the Book theme,
  added as a submodule in the /themes directory

4. run `git submodule init`

5. run `git submodule update`

6. Navigate to the testDocs directory

7. Start the hugo server with `hugo server`

The site will be available at http://localhost:1313,
hugo will watch and rebuild the site with any changes to the repo.


## Content with Hugo

All site content in hugo is written in Markdown, and hosted in the /content folder.
The site is built with the file tree and organization of this folder.

### Shortcodes

Hugo supports basic markdown syntax. A helpful guide for markdown is right [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
Hugo also supports shortcodes, insertable templates that allow the extension of markdown. Hugo includes a set of
[default shortcodes](https://gohugo.io/content-management/shortcodes/). A set of custom shortcodes are included with this repo.

### Adding a section
Sections in hugo are subdirectories of the /content folder. In order to add a section,
create a subdirectory, i.e. 'MySection', then add a _index.md file. All first-level subdirectories from /content are default sections, but any nested sections must include _index.md.

Subdirectories can also be organized as page-bundles, which hugo explains in their [documentation.](https://gohugo.io/content-management/page-bundles/) These are denoted by a index.md file, locaed in the subdirectory.

### Front Matter

Each page in Hugo contains a .YAML front matter header. For example.

```
---
title: Quick Start Guide
author: Unknown
weight: 11
pageID: 8362542
aliases:
 - /old/Quick_Start_Guide.html
---
```
Hugo uses these parameters in the generation of the site.

### Organization

Content is ordered by the weight parameter in the front matter. Hugo arranges lower weights first, and is relative per section.
Articles with `draft: true` in the front matter will not be built when hugo server is run.
Use `hugo server -D` to include drafts.

## Theme

The site is based off the Hugo Book theme, built by [alex-shpak](https://github.com/alex-shpak/). The NetDocs theme contains custom shortcodes and partial templates, as well as styling customizations and assets not included with the base theme. The layouts directory in the main repo is the final layout override, and contains any site-specific assets. See
[theme components](https://gohugo.io/themes/theme-components/) for information on theme overrides, and https://gohugo.io/templates/lookup-order/ for information on Hugo's default lookup order.

## Contributing

The master branch hosts the current, most stable version of the site.
Dev branch contains the unstable version, where new features and content are added continually.

If you would like to contribute to the site, please fork and submit a pull request

## Resources
  - [Cumulus Networks Documentation](https://docs.cumulusnetworks.com)
  - [Content Organization with Hugo](https://gohugo.io/content-management/organization/)
  - [hugo-theme-book](https://github.com/alex-shpak/hugo-book)
  - [hugo-theme-dockdock](https://github.com/vjeantet/hugo-theme-docdock)
