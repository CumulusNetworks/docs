---
title: Links and References
author: Daniel Cawley
weight: 14
siteSlug: contributor-guide
version: 1.0
---

## Hugo Shortcodes

Markdown is designed for speed and simplicity, thus it is limited in authoring
and customizing rendered content. Rather than insert raw HTML into Markdown,
Hugo provides [*shortcodes*](https://gohugo.io/content-management/shortcodes/),
predefined templates referenced from Markdown content.

Hugo provides some built-in shortcodes for some standard use cases. In addition,
the Cumulus Networks documentation theme has its own set of custom shortcodes,
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

Hugo provides default shortcodes for internal references,
[*ref* and *relref*](https://gohugo.io/content-management/shortcodes/#ref-and-relref).
However, these shortcodes inconsistently open in new tabs, so we created a custom
shortcode called `pageref`:

{{&lt; pageref "Cumulus_Linux_37" "Installation Management" >}}

This shortcode takes two parameters:

- The _siteSlug_, which is defined in the page's [front matter](Adding_New_Content/#front-matter);
  it is the name of the subdirectory in /content or /content/version, like _cumulus-linux_.
- The page title, which is also defined in the page's front matter.

This shortcode renders an internal link with the title of the page as the link text, like this:

{{< pageref "cumulus-linux" "Buffer and Queue Management" >}}

## Adding Images

Markdown and Hugo both offer multiple options for adding images.

### Static References

The first method is a static reference. All files added to the `/static`
folder are served to the site root path. An image added to the
`/static/images/cumulus-linux` subdirectory &mdash; for example `voice-vlan.png`
&mdash; is accessible at http://localhost:1313/images/cumulus-linux/voice-vlan.png.

These static images can be added in one of two ways. The first is with vanilla
Markdown, and is similar to the link syntax. The following Markdown syntax:

```
![Example Image](/images/cumulus-linux/voice-vlan.png)
```

Renders this image:

![Example Image](/images/cumulus-linux/voice-vlan.png)

You can also use the `img` shortcode, shown below.

<pre>{{&lt; img src = "/images/uploads/PTPExample.png" >}}</pre>

Images added with either of the two methods above do not allow for resizing or
captioning.

### HTML figure Tag

Hugo also provides a shortcode that provides for the use of the HTML `<figure>`
element, which wraps around the `<img>` tag and adds the functionality of embedded
images and elements.

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

<pre>{{&lt;figure src="/images/uploads/NetQAgentLogFormat.png" alt="NetQAgentLogFormat.png" caption="NetQ Agent log format" height="50px" >}}</pre>

Renders this image with a caption:

{{<figure src="/images/uploads/NetQAgentLogFormat.png" alt="NetQAgentLogFormat.png" caption="NetQ Agent log format" height="50px" >}}
