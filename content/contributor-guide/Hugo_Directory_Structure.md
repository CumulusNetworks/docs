---
title: Hugo Directory Structure
author: Daniel Cawley
weight: 20
siteSlug: contributor-guide
---

When you clone the Cumulus Networks docs repository, it contains a number of
directories. The following directories are where your contributions will go:

- /content
  - This directory contains all of the Markdown files for all the pages and their
    enclosing folders.
  - Its arrangement determines the structure and hierarchy of the final site.
  - If you are modifying any content, all of your contributions will be made to the
    files located here.
- /static
  - Holds any static files like images and PDFs.
  - If you are adding an image or PDF, put it in the appropriate directory here.
  - This directory gets published to the site at /.

{{% notice warning %}}
Modifying files in any other directory will have significant impact on the overall
appearance and functioning of the site, so please [file a bug](https://github.com/CumulusNetworks/docs/issues/new)
to request changes to the site.
{{% /notice %}}