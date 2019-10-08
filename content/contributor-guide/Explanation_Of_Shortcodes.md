---
title: Links and References
author: Daniel Cawley
weight: 14
siteSlug: contributor-guide
---

## Hugo Shortcodes

Markdown is designed for speed and simplicity, thus it is limited in authoring
and customizing rendered content. Rather than insert raw HTML into Markdown,
Hugo provides *shortcodes*, predefined templates callable from Markdown content.

Hugo provides some built-in shortcodes for some standard use cases. The Hugo
documentation for built-in shortcodes is located [here](https://gohugo.io/content-management/shortcodes/).

The Cumulus Networks documentation theme has its own set of custom shortcodes, 
built for documentation. These shortcodes are explained below.

## Adding Links and References

There are multiple options for adding hyperlinks into Markdown built with Hugo.
The easiest is with inline Markdown:

```
[External Link](https://docs.cumulusnetworks.com)
[In-Page Anchor](#adding-images)
[Internal Absolute Reference](/cumulus-linux/Installation_Management/Upgrading_Cumulus_Linux)
[Internal Relative Reference](../Adding_New_Content)
```

Hugo provides default shortcodes for internal references, *ref* and *relref*. 
However, these shortcodes inconsistently open in new tabs so we created a custom
shortcode called `pageref`:

{{&lt; pageref "Cumulus_Linux_35" "Installation Management" >}}

This shortcode takes two paramters: 

- The siteSlug, which is defined in the page's front matter; it is the name of
  the subdirectory in /content or /content/version.
- The page title, which is also defined in the page's front matter.

{{< pageref "cumulus-linux" "Buffer and Queue Management" >}}

This shortcode renders an internal link with the title of the page as the link text.

## Adding Images

Both Markdown and Hugo offer multiple options for adding images. 

The first is a static reference. All files added to the `/static` folder are 
served to the site root path. An image added to the 
`/static/images/uploads subdirectory` &mdash; for example PTPExample.png &mdash; 
is accessible at http://localhost:1313/images/uploads/PTPExample.png.

These static images can be added in multiple ways. The first is with vanilla
Markdown, and is similar to the link syntax.

```
![Example Image](/images/uploads/PTPExample.png)
```

There is also a basic img shortcode added, shown below.

<pre>{{&lt; img src = "https://s3-us-west-2.amazonaws.com/dev.docs.cumulusnetworks.com/images/uploads/PTPExample.png" >}}</pre>

Images added with either of the two methods above do not allow for resizing or
captioning.

Hugo also provides a shortcode that allows for the use of the HTML `<figure>` element,
which wraps around the `<img>` tag and adds the functionality of embedded images and elements.

Figure parameters include:

| Parameter     |   Description |
| :---------    |  :----------- |
| `src`    |   URL of image to be displayed |
| `link`   |   URL of hyperlink destination |
| `alt` | Alternative text if image can't be displayed |
| `title` | Image title |
| `caption`| Image caption |
| `height` | Height in pixels of the image |
| `width` | Width in pixels of the image |

For example, the following code:

<pre>{{&lt;figure src="https://s3-us-west-2.amazonaws.com/dev.docs.cumulusnetworks.com/images/uploads/NetQAgentLogFormat.png" alt="NetQAgentLogFormat.png" caption="NetQ Agent log format" height="50px" >}}</pre>

Renders this image with a caption:

{{<figure src="https://s3-us-west-2.amazonaws.com/dev.docs.cumulusnetworks.com/images/uploads/NetQAgentLogFormat.png" alt="NetQAgentLogFormat.png" caption="NetQ Agent log format" height="50px" >}}
