---
title: Hugo Constructs
author: NVIDIA
weight: 200
---
Cumulus uses Hugo to create a static web site for our user documentation. This topic describes some of the features of Hugo that impact how our documentation is created and presented.

If you want to provide feedback or submit new content for inclusion in our documentation, please refer to the other topics in this document.

## Directory Structure

Hugo uses a [directory structure](https://gohugo.io/getting-started/directory-structure/) to support multilevel content, images, templates and the so forth. The highest-level directories include:

- archetypes
- content
- data
- resources
- static
- themes

Their roles and content are described here:

| Directory | Description |
| ----------- | -------------- |
| [archetypes](https://gohugo.io/content-management/archetypes/) | Contains template files for new content (.md files). Populates and adds default [front matter](https://gohugo.io/content-management/front-matter/). Works by calling `hugo new` to build the Markdown files. |
| [content](https://gohugo.io/content-management/page-bundles/) | Contains all of the sections and page resources built into the main site. The arrangement of this content determines the structure and hierarchy of the final site. |
| data | Contains JSON files that map images to pages from a previous version of the Cumulus documentation. These files are not user modified.|
| resources | Contains files generated by Hugo and are used as a cache to speed up page builds. These files are not user modified. |
| [static](https://gohugo.io/content-management/static-files/) | Contains all static files, including configuration files and user-created images. Any images files should be placed within the `/static` directory. |
| [themes](https://gohugo.io/hugo-modules/theme-components/) | Contains the document themes used to display the content in the published site. Cumulus uses the [Book theme](https://github.com/alex-shpak/hugo-book) as the base theme. A subdirectory, *layouts*, contains the go-html templates (.html files) that build pages from *content*. |

{{% notice warning %}}
Modifying files in any other directory will have significant impact on the overall appearance and functioning of the site, so please [file a bug](https://github.com/CumulusNetworks/docs/issues/new) to request changes to the site.
{{% /notice %}}

## Front Matter

Each page in Hugo contains a .YAML front matter header. For example.

```
---
title: 802.1X Interfaces
weight: 101
toc: 3
---
```

Hugo uses these parameters in the generation of the site. The Cumulus documentation team use these to set the order of display within a topic, display within a PDF and place the content with the correct product and release. When you create a new Markdown file, these values are provided. In this case, please provide a title and then let the documentation team modify any of the other parameters as needed.

## Graphical Content

Cumulus makes use of graphical content by placing static images in the */static/images/* directory. Images in this directory are accessible by the published site and well as the Hugo server used to display content locally.

Markdown is designed for speed and simplicity, therefore limited in authoring and customizing rendered content. Rather than insert raw HTML into markdown, Hugo provides *shortcodes*, or predefined templates, that can be called from Markdown content for situations where you need additional information or formatting capabilities.

Hugo provides several built-in shortcodes, of which a subset are useful for documentation. For reference, the full Hugo documentation for all of their built-in shortcodes is located [here](https://gohugo.io/content-management/shortcodes/). We use the built-in [*figure*](https://gohugo.io/content-management/shortcodes/#figure) shortcode.

{{%notice tip%}}
We do not use the *ref* and *relref* shortcodes for hyperlinks and references, but instead use a custom `link` shortcode.
{{%/notice%}}

### Image Shortcode

The *img*, or image, shortcode is a custom shortcode. It is used when you want to insert an icon or small image *inline* with your text. Note that you do not need to include the *static/* portion of the path to the file. Optionally, images can be scaled using the *width* and/or *height* parameters, specified in pixels. Using only *width* or *height* scales the image proportionally. Images that are too wide to be included inline are automatically presented on a new line. The basic shortcode is:

`{{</* img src="/path/" */>}}`

For example:  
`{{</* img src="/images/icons/export-button.png" width="80" */>}}`

`{{</* img src="/images/cumulus-linux/evpn-basic-clos.png" width="700" */>}}`

### Figure Shortcode

The *figure* shortcode is a built-in Hugo shortcode. It is used when you want to insert an image on a new line. This shortcode makes use of the HTML `<figure>` element, wrapping the `<img>` tag and providing more optional parameters to specify how the image is displayed. The basic shortcode is:

`{{</* figure src="/path/" */>}}`

The available parameters include:

| Parameter | Description |
| ------------  |  ------------- |
| src | URL of image to be displayed |
| link | URL of hyperlink destination |
| alt | Alternative text if image cannot be displayed |
| title | Image Title, placed above figure |
| caption| Image Caption, placed below figure |
| height | Height of image, in pixels |
| width | Width of image, in pixels |

For example:

`{{</* figure src="/images/netq/sch-trace-result-small-card.png" alt="Results of a scheduled trace shown in the small card" caption="Scheduled Trace Result" width="200px" */>}}`

`{{</* figure src = “/images/cumulus-linux/evpn-basic-clos.png" width="700" */>}}`
