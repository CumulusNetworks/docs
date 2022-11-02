# NVIDIA Networking Documentation

This is the source repository for the NVIDIA Ethernet Software Documentation, hosted at docs.nvidia.com/networking-ethernet-software.
This site uses the static site generator [Hugo](https://gohugo.io/documentation/).

## Installing the Documentation and Running the Local Server

Hugo contains a local development server to build and view live changes to the repo. To build and view the live site:

1. Install Hugo version 0.82.0 **extended** from https://github.com/gohugoio/hugo/releases/tag/v0.82.0.

2. Verify Hugo with `hugo version`. This site supports Hugo version 0.82.0. The output of the `hugo version` command should read:

<!-- vale off -->
```
hugo v0.82.0-9D960784+extended linux/amd64 BuildDate=2021-03-21T17:28:04Z VendorInfo=gohugoio
```
<!-- vale on -->
3. Clone this repository with `git clone`.

4. Navigate to the docs subdirectory.

5. Start the Hugo server with `hugo server`.

6. The site is available at http://localhost:1313. Hugo watches and rebuilds the site when you save any changes to source files.

## Contributing to the Documentation

This repository contains the documentation hosted at docs.nvidia.com/networking-ethernet-software. 

If you would like to contribute to the site, please fork and submit a pull request. Commit your changes to the `stage` branch.

The docs team reviews the pull request and, if accepted, publishes the content.

## Content with Hugo
Hugo uses Markdown for all site content. Content pages are in the /content folder.

Hugo supports basic GitHub Markdown syntax. A helpful guide for Markdown is [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

The site uses custom Hugo `shortcodes` extensively. Shortcode details are in the Writing Guide.

### Adding a section
Sections in Hugo are subdirectories of the /content folder. To add a section,
create a subdirectory, for example, 'MySection', then add a \_index.md file. All first-level subdirectories from /content are default sections, but any nested sections must include \_index.md.

### Organization

The `weight` parameter in the front matter determines the page ordering. Hugo arranges lower weights first, and is relative per section.
Pages set to `draft: true` in the front matter do not show when the local server is running.
Use `hugo server -D` to include drafts and display them locally.

## Theme

The site uses the Hugo Book theme, built by [alex-shpak](https://github.com/alex-shpak/). The NetDocs theme contains custom shortcodes and partial templates, as well as styling customizations and assets not included with the base theme. The layouts directory in the main repo is the final layout override, and contains any site-specific assets. See
[theme components](https://gohugo.io/themes/theme-components/) for information on theme overrides and https://gohugo.io/templates/lookup-order/ for information on Hugo's default lookup order.


## Resources
  - [NVIDIA Ethernet Software Documentation](https://docs.nvidia.com/networking-ethernet-software/)
  - [Content Organization with Hugo](https://gohugo.io/content-management/organization/)
  - [hugo-theme-book](https://github.com/alex-shpak/hugo-book)
  - [hugo-theme-dockdock](https://github.com/vjeantet/hugo-theme-docdock)<!-- vale off -->
