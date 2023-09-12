---
title: Markdown Guide
author: NVIDIA
weight: 210
---
This topic provides additional Markdown usage guidelines and more detail about selected Markdown editing capabilities already covered in the {{< link title="Make a Larger Contribution" >}} topic.

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
| \[Display Text\](\<site-address\>) | \[Cumulus docs\](http://docs.cumulusnetworks.com) |

{{% notice note %}}
Do not use traditional markdown links to link between pages in the documentation. Use the custom `link` shortcode to to link between internal documentation pages.
{{% /notice %}} 


### In-page Anchor

This type of link is used to reference content in another section within the same file.

| Inline Markdown | Example |
| -------------------- | ---------- |
| \[Display Text\](#\<section-title\>/) | \[Hugo Shortcodes\](#hugo-shortcodes) |

{{%notice note%}}
The \<section-title\> must be in all lower case, and dashes must be used to replace any spaces, regardless of the formatting of the actual title.
{{%/notice%}}

## Image References

In general, Cumulus uses the *img* and *figure*  shortcodes to reference static images; however, you can also use inline Markdown.

\!\[Reference Text\](/path)

Note that the reference text is not displayed.

For example, this Markdown renders the following images:

![Trace Request Small]{{<img src="/images/old_doc_images/sch-trace-request-small-card.png" >}}

![EVPN Arch](/images/cumulus-linux/evpn-basic-clos.png)

## Tables

Creating tables in Markdown is very easy. Use three or more hyphens (---) to create each column header and pipes (|) to separate each column. While optional, Cumulus uses pipes on either end of a table row as well. 

For example, this Markdown renders the following table:

{{<figure src="/images/old_doc_images/contrib-gde-table-mkdn.png" width="250">}}

| heading | description |
| ---------  | ----------- |
| text        | text   |
| text        | text   |

### Align Content

Colons can be used to align column content.

For example, this Markdown renders the following table:

{{<figure src="/images/old_doc_images/contrib-gde-table-alignment.png" width="300">}}

| Tables | Are | Fun |
| ------ |:---:| ---:|
| col 1 | is left-aligned | $1 |
| col 2 | is centered | $12 |
| col 3 | is right-aligned | $1600 |

### Use Inline Styles

You can also use inline Markdown to format your text if needed.

For example, this Markdown renders the following table:

{{<figure src="/images/old_doc_images/contrib-gde-table-style.png" width="300">}}

| Use | Inline | Markdown |
| --- | --- | --- |
| *Italics* | `Commands` | **Bold** |
