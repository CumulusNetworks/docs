---
title: Hugo Directory Structure
author: Daniel Cawley
weight: 1
siteSlug: Writing_Guide
---

1. /content
  - This directory contains all of the sections and page resources built into the main site. (.md files, images, etc.)
  - It’s arrangement determines the structure and hierarchy of the final site.
  - More on this folder later
2. /archetypes
  - Contains template files for new content (.md files)
  - Builds .md file structure by calling hugo new
  - Populates and adds default front matter
3. /layouts
  - Holds go-html templates (.html files) that build pages from /content folder
  - Hugo will search for templates in this folder before looking in /themes
4. /assets
  - Contains .js and .scss files used by hugo templates
  - Not published to static site unless piped in by templates
5. /static
  - Holds any static files
  - Published to built site at /
6. /data
  - Contains any .JSON, .YAML, or .TOML files hugo uses
  - Hugo indexes /data and is accessible through templates
7. /resources
  - Generated files by hugo
8. /themes
  - Holds themes used by hugo
  - Theme lookup order is defined in config.toml file
  - Book theme is the base its added as a git submodule
