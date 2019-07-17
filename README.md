# Cumulus Networks Internal Documentation

This repository houses the source for internal Cumulus Networks Documentation, hosted
at qa-docs.cumulusnetworks.com. This version of the documentation contains sensitive
and unreleased information, and is only accessible to Cumulus Employees and Partners

## Installing the InternalTest Documentation Site
The docs are built with the static site generator [Hugo](https://gohugo.io/documentation/)
Hugo contains a local development server to build and view live changes to the repo. Hugo is
a command line interface.

In order to build and view the live site:

1. Install Hugo
    - https://gohugo.io/getting-started/installing/

2. Verify Hugo is installed with `hugo version` This site supports hugo version 0.55.6

3. Clone this repository with `git clone`

4. Navigate to the docs-internal subdirectory

5. Start the hugo server with `hugo server`

6. The site will be available at http://localhost:1313,
hugo will watch and rebuild the site with any changes to the source.

## Contributing

This repository will contain new development and content added to the docs, and will remain private.
The master branch will sync with the public docs repository
The develop branch will build and deploy to docs-qa.cumulusnetworks.com upon commit
This branch will contain new features and content for review.

If you would like to contribute to the site, please fork and submit a pull request

## Content with Hugo
All site content in hugo is written in Markdown, and hosted in the /content folder.
The site is built with the file tree and organization of this folder.

Hugo supports basic Github markdown syntax. A helpful guide for markdown is right [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
Hugo supports custom shortcodes, which are contained the Writing Guide section of the docs.

### Adding a section
Sections in hugo are subdirectories of the /content folder. In order to add a section,
create a subdirectory, i.e. 'MySection', then add a _index.md file. All first-level subdirectories from /content are default sections, but any nested sections must include _index.md.

### Organization

Content is ordered by the weight parameter in the front matter. Hugo arranges lower weights first, and is relative per section.
Articles with `draft: true` in the front matter will not be built when hugo server is run.
Use `hugo server -D` to include drafts.

## Theme

The site is based off the Hugo Book theme, built by [alex-shpak](https://github.com/alex-shpak/). The NetDocs theme contains custom shortcodes and partial templates, as well as styling customizations and assets not included with the base theme. The layouts directory in the main repo is the final layout override, and contains any site-specific assets. See
[theme components](https://gohugo.io/themes/theme-components/) for information on theme overrides, and https://gohugo.io/templates/lookup-order/ for information on Hugo's default lookup order.


## Resources
  - [Cumulus Networks Documentation](https://docs.cumulusnetworks.com)
  - [Content Organization with Hugo](https://gohugo.io/content-management/organization/)
  - [hugo-theme-book](https://github.com/alex-shpak/hugo-book)
  - [hugo-theme-dockdock](https://github.com/vjeantet/hugo-theme-docdock)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MjQzNzM2OF19
-->