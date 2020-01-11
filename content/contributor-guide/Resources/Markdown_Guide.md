---
title: Markdown Guide
author: Cumulus Networks
weight: 210
siteSlug: contributor-guide
---
This topic provides additional Markdown usage guidelines and more detail about selected Markdown editing capabilities already covered in the [Make a Larger Contribution](../../Make-a-Larger-Contribution/) topic.

## Inline Styling

Double tildas (~) can be used to display text with a line through it. 

For example, this Markdown will output the following text:

\~\~This text will have a strikethrough style\~\~

~~This text will have a strikethrough~~

## Links and References

There are multiple types of links and references that can be added to Markdown files built with Hugo. Each has an equivalent inline Markdown. All links and references are rendered as green text.

### External Link

This type of link is used to reference content outside of the documentation site, typically to another website.

| Inline Markdown | Example |
| -------------------- | ---------- |
| \[Display Text\](\<site-address\>) | \[Cumulus Forums\](http://forums.cumulusnetworks.com) |

### In-page Anchor

This type of link is used to reference content in another section within the same file.

| Inline Markdown | Example |
| -------------------- | ---------- |
| \[Display Text\](#\<section-title\>/) | \[Hugo Shortcodes\](#hugo-shortcodes) |

{{%notice note%}}
The \<section-title\> must be in all lower case, and dashes must be used to replace any spaces, regardless of the formatting of the actual title.
{{%/notice%}}

### Internal Absolute Reference

This type of link is used to reference content within the document site, but outside of the current file, using an exact directory path.

| Inline Markdown | Example |
| -------------------- | ---------- |
| \[Display Text\](/\<full-path\>/) | \[Routing\](/cumulus-linux/Layer-3/Routing/) |

Begin the path at the product-level directory. Be sure to start *and* end the path with a forward slash (/).

{{%notice note%}}
While this is type of reference is acceptable, we strongly recommend using the [Internal Relative Reference](#internal-relative-reference) instead. This simplifies the transition of documents into the *version* directory when they are no longer the newest available version.
{{%/notice%}}

### Internal Relative Reference

This type of link is used to reference content within the document site, but outside of the current file, using a relative directory path. This is the preferred type to be used for internal references.

| Inline Markdown | Example |
| -------------------- | ---------- |
| \[Display Text\](../\<section-title\>/) | \[Adding New Content\](../../Make-a-Larger-Contribution/Adding_New_Content/) |

Use ../ for each step up the tree, and then the section title names for each step down the tree to the file. Be sure to end the path with a forward slash (/).

## Image References

In general, Cumulus Networks uses the *img* and *figure*  shortcodes to reference static images; however, you can also use inline Markdown.

\!\[Reference Text\](/path)

Note that the reference text is not displayed.

For example, this Markdown renders the following images:

![Trace Request Small](/images/uploads/sch-trace-request-small-card.png)

![EVPN Arch](/images/cumulus-linux/evpn-basic-clos.png)

## Tables

Creating tables in Markdown is very easy. Use three or more hyphens (---) to create each column header and pipes (|) to separate each column. While optional, Cumulus uses pipes on either end of a table row as well. 

For example, this Markdown renders the following table:

{{<figure src="/images/uploads/contrib-gde-table-mkdn.png" width="250">}}

| heading | description |
| ---------  | ----------- |
| text        | text   |
| text        | text   |

### Align Content

Colons can be used to align column content.

For example, this Markdown renders the following table:

{{<figure src="/images/uploads/contrib-gde-table-alignment.png" width="300">}}

| Tables | Are | Fun |
| ------ |:---:| ---:|
| col 1 | is left-aligned | $1 |
| col 2 | is centered | $12 |
| col 3 | is right-aligned | $1600 |

### Use Inline Styles

You can also use inline Markdown to format your text if needed.

For example, this Markdown renders the following table:

{{<figure src="/images/uploads/contrib-gde-table-style.png" width="300">}}

| Use | Inline | Markdown |
| --- | --- | --- |
| *Italics* | `Commands` | **Bold** |
