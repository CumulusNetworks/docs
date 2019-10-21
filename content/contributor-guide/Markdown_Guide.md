---
title: Markdown Guide
author: Daniel Cawley
weight: 15
siteSlug: contributor-guide
version: 1.0
---

This guide is a rehash of what you can find in the original
[Markdown documentation](https://daringfireball.net/projects/markdown/syntax).

## Heading Styles

Here are the heading styles:

```
## Second Level Header (always start with a second level header)

### Third Level Header (always put after a second level header)

#### Fourth Level Header (use this level sparingly; consider reorganizing the content if possible)
```

The template adds the title in a first level header by default; start all content
with second level headers (## Header).

## Numbered and Bulleted Lists

- The - character signifies a bulleted list
- Round bullets are enabled by default
- The * character may also be used; Cumulus Networks uses - as the default style
  - Nested lists are supported
  - They will render with a,b,c
    - Only second level nesting currently supported
  - As in paragraphs, you can continue to add text onto the next line in
    Markdown
- A new line followed by a - signifies a new list item

1. Numbered lists are supported as well.
2. They're very simple and self explanatory.
   1. Nested lists also supported.
   2. Will display as a, b, c.
3. A nested bulleted list displays differently:
   - Bullets
   - Are displayed

## Inline Styling

Use two asterisks to bold the enclosed text:

**This text will be bold (strong) in the rendered html**

Use one asterisk to italicize the enclosed text:

*This text will be italicized in the rendered text*

You can use underscores instead of asterisks. However, the Cumulus Networks
standard is to use asterisks.

You can use the tilde (~) character to strike through the text:

~~This text has a strikethrough~~

### Code Blocks and Syntax

Use three backticks before and after the enclosed text to signify a code block
(also known as a *code fence*). Use this for code blocks containing multiple
lines of code.

    ```
    Formatter.prototype.removeSideandTopBar = function(){
    $ = this.$
    $("div[id = 'ht-loader']").remove()
    $('#ht-headerbar').remove()
    $('#ht-sidebar').remove()
    $('#ht-breadcrumb').remove()
    $('#ht-sidebar-dragbar').remove()
    $("div[class = 'section section-1']").has('p.expand-control-text').remove()
    }
    ```

Alternately, you can indent code samples with 4 spaces to begin a code block:

```
    Formatter.prototype.removeSideandTopBar = function(){
    $ = this.$
    $("div[id = 'ht-loader']").remove()
    $('#ht-headerbar').remove()
    $('#ht-sidebar').remove()
    $('#ht-breadcrumb').remove()
    $('#ht-sidebar-dragbar').remove()
    $("div[class = 'section section-1']").has('p.expand-control-text').remove()
    }
```

Inline code can be added with single backticks. For example:

> Run `git checkout -b dev` to add a new branch

### Syntax Highlighting

Coming soon!
