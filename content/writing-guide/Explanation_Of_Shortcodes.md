---
title: Explanation of Shortcodes
author: Daniel Cawley
weight: 14
siteSlug: Writing_Guide
---

## Hugo Shortcodes

Markdown is designed for speed and simplicity, therefore limited in authoring
and customizing rendered content. Rather than insert raw HTML into markdown,
Hugo provides Shortcodes, predefined templates callable from markdown content.

Hugo provides some built-in shortcodes, for some standard use cases.
The Hugo documentation for built-in shortcodes is located [here](https://gohugo.io/content-management/shortcodes/)
Included in this theme is a set of custom shortcodes, built for documentation.
Use of these shortcodes are explained below

## Adding Links and References

There is multiple options for adding hyperlinks into markdown built with Hugo.
The easiest is with inline markdown.

[External Link](https://docs.cumulusnetworks.com)

[In-Page Anchor](#adding-images)

[Internal Absolute Reference](/Cumulus_Linux/Installation_Management/Upgrading_Cumulus_Linux)

[Internal Relative Reference](../Adding_New_Content)

Hugo provides default shortcodes for internal references, ref and relref. However these shortcodes
inconsistently open in new tabs so I have provided a custom shortcode `pageref` shown below.

{{< pageref "Cumulus_Linux_35" "Installation Management" >}}

This shortcode takes two paramters, the first is the siteSlug, which is defined in
the page front matter, and is the name of the subdirectory in /content or /content/version

It will render an internal link with the title

## Adding Images

With markdown and Hugo there are multiple options for adding Images, the first
is a static reference.

All files added to the /static folder are served to the site root path. An image
added to the /static/images/uploads subdirectory, for example PTPExample.png, will have
accessible at http://localhost:1313/images/uploads/PTPExample.png

These static images can be added in multiple ways. The first is with vanilla
markdown, and is similar to the link syntax.

![Example Image](/images/uploads/PTPExample.png)

There is also a basic img shortcode added, shown below.

{{< img src = "/images/uploads/PTPExample.png" >}}

Images added with the two above methods do not allow resizing or captioning of
elements.

Hugo also provides a shortcode which allows use of the HTML `<figure>` element,
which wraps around the `<img>` tag and adds functionality of embedded
images and elements.

Figure parameters include

| Parameter     |   Description |
| :---------    |  :----------- |
| `src`    |   URL of image to be displayed |
| `link`   |   URL of hyperlink destination |
| `alt` | Alternative text if image can't be displayed |
| `title` | Image Title |
| `caption`| Image Caption |
| `height` | height attribute of image |
| `width` | width attribute of image |

**Example**

{{<figure src="/images/uploads/PTPExample.png" alt="PTPExample.png" caption="PTP Example" height="200px" >}}
