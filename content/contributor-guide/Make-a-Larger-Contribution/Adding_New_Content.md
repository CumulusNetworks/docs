---
title: Add New Content
author: NVIDIA
weight: 100
---
Now that you have installed Hugo, cloned the GitHub repository, and run the local server,
you can add new content to the Docs site. If you came here first without performing these setup tasks, refer to {{% link title="Make a Larger Contribution" %}} and then return here.

You can submit new paragraphs, images, sections and whole topics for inclusion into the documentation. The first step is to understand how the documentation is organized so you can add information in the proper place. Secondly, you need to be, or become, familiar with editing in Markdown format. The basics are included here. To learn more, refer to  {{% link title="Resources" %}}.

## Documentation Site Structure

You can view the documentation site structure through your file manager or through a text-based editor. We use [VS Code](https://code.visualstudio.com/) to develop the documentation, but you may use any text editor of your choice.

There are two directories in the Cumulus Networks documentation site that are particularly important for authoring new content:

- **content/**: Contains product documentation directories and files
- **static/images/**: Contains referenced images

The other directories are primarily used to generate the website, but if you are interested in knowing what they contain and their purpose, refer to {{% link title="Hugo Constructs" %}}.

## Add a New Page

New pages are added into the `/content` directory using `hugo new` which relies on Hugo archetypes; Markdown templates which contain the needed front matter (meta data) and default values. They are specific to each product and create a new .md (Markdown) file.

1. If `hugo server` is currently running, press Ctrl+c to quit the docs server in your terminal window.

2. Add the page:

    - To add a new page, named `test_post`, to Cumulus Linux 4.1, run `hugo new cumulus-linux-41/test_post.md`.
    - To add a new page, named `test_post` to Cumulus NetQ 3.0, run `hugo new cumulus-netq-30/test_post.md`.
    - To add a file within a subtopic, include the full path to the location. For example, run `hugo new cumulus-linux-41/Layer-2/test_post.md`.

    {{% notice tip %}}
Don't forget to use the `.md` file extension.
    {{% /notice %}}

3.  Change the front matter `title` to reflect the new content.
    {{% notice tip %}}
For more detail about the front matter parameters, refer to the {{% link title="Hugo Constructs" %}}.
    {{% /notice %}}

4.  Change the `weight` value to determine the order of the page in the left hand menu. Lower values are listed higher in the section list.

5. Change the `toc` value to match the file directory depth. Your page's `toc` value should be 1 greater than the `toc` of the `_index.md` file in the same directory.

6. Add your content.

You can also create new pages by copying and pasting an existing file from within some editors. Just be sure to supply a new name for the file and a new title. Some editors let you drag and drop the newly created page within the directory tree in the event that you placed it incorrectly.

{{% notice note %}}
A unqiue page `title` is required to ensure the `link` shortcode works correctly.
{{% /notice %}}

## Add a New Section

In Hugo terminology, a section is the same as a folder. Hugo defines sections by their location within the `/content` folder, and the name of the .md file. Adding a section is as simple as adding a new subdirectory, and creating a `_index.md` file within that subdirectory. This can be done using the `hugo new` command.

For example, to create a new section "Test Section," at `/content/cumulus-linux-41/`, run `hugo new cumulus-linux-41/Test_Section/_index.md`.

To create a section under another section (nested section), include the full path to the location. For example, run `hugo new cumulus-linux-41/Layer-2/Test_Section/_index.md`.

You can also create new sections by copying and pasting an existing folder from within some editors. Just be sure to supply a new name for the section. Some editors let you drag and drop the newly created section within the directory tree in the event that you placed it incorrectly.

## Edit Content

These guidelines cover the most common formatting tasks you will encounter during your new content creation. For more details about these items and other formatting issues, refer to the {{< link title="Markdown Guide" >}}.

### Add Text

To add or modify text in an existing file:

1. Open the Docs directory in your text editor.

    This example shows the Docs directory in VS Code:
    {{<figure src="/images/old_doc_images/contrib-gde-docs-dir.png" width="500">}}

2. Expand the *content* directory to find the product of interest.

    {{<figure src="/images/old_doc_images/contrib-gde-content-dir.png" width="500">}}

3. Expand the product directory and any subdirectories to find the file that contains the text you want to change or where you want to add additional text.

4. Open the relevant file and add or modify the desired text.

    {{<figure src="/images/old_doc_images/contrib-gde-edit-text.png" width="700">}}

### Add a Heading

If you want to add a new section within a document, then you can add a new header and then enter the text. To create the correct level of header, use two pound signs (#) for a second-level heading (the file title is the only first-level heading) or three pound signs for a third-level heading.

For example: `## New Topic` or `### New Subtopic`

{{%notice tip%}}
If possible, do not use special characters, such as dashes and parentheses, in the titles as these can be problematic to creating links or references to these topics.
{{%/notice%}}

{{%notice note%}}
For more detail about writing with Markdown, refer to the [Markdown Guide](../../Resources/Markdown_Guide/) in the Resources section of this guide.
{{%/notice%}}

### Add Inline Style to Text

It is common to emphasize important text, such as a field name in the UI (bold), a directory or file name (italic), and commands (computer font). These are handled as follows:

- Use a single asterisk (*) on either side of a word or phrase to italicize the text.
- Use two asterisks (**) on either side of a word or phrase to bold the text.
- Use one tick (`) on either side of a command to display the command in a computer font.

For example, this markdown will render the following formatted text.

{{<figure src="/images/old_doc_images/contrib-gde-italic-bold-cmd.png">}}

*This text will be italicized in the rendered site.*

The word *italics* will be italicized in the rendered site.

**This text will be bold in the rendered site.**

The word **bold** will be bolded in the rendered site.

The `net show bgp` command will be rendered in special font, and highlighted.

### Add a Note

You can add a note to a file with the notice shortcodes. We support four types of notes: Tip, Note, Info, and Warning.  Refer to the [Markdown Guide](../../Resources/Markdown_Guide) for additional details about when to use each type and placement.

This example shows how to add a note:

1. On a new line, enter the notice shortcode.

2. On the next line, enter the text for the note.

3. Complete the note by adding  end notice to the line after the note text.

This shows an example note:

{{<figure src="/images/old_doc_images/contrib-gde-note-shtcode-ex.png">}}

### Add a List

A *bulleted* list is created using a dash (-) at the beginning of each item. This renders with a filled circle as the bullet. You can also create second-level bullets by simply tabbing in and then using a dash. Second-level bullets render with an open circle for the bullets.

For example, this markdown renders the following bulleted list.

{{<figure src="/images/old_doc_images/contrib-gde-bullet-format.png">}}

- First-level bullet
- First-level bullet
    - Second-level bullet
    - Second-level bullet
- First-level bullet

A *numbered* list is created using numbers at the beginning of each item. You can increase your numbering or always use one (1). You can create second-level items by simply tabbing in and then using the one. First-level items render as 1, 2, 3, and so forth. Second-level items render as a, b, c, and so forth.

For example, either of these markdown examples render the following numbered list.

{{<figure src="/images/old_doc_images/contrib-gde-list-ex.png">}}

1. First-level item or step
2. First-level item or step
  1. Second-level item or sub-step
  2. Second-level item or sub-step
3. First-level item or step

### Add an Image

If you have an image or figure (in SVG or PNG file format) that you want to add:

1. Copy or save the file into *static/images* for the associated product.

    For example, if you are editing a Cumulus Linux file, use *static/images/cumulus-linux*. For a Cumulus NetQ file, use *static/images/netq/*.

2. In the file text, add the image or figure reference using the figure or img shortcode:

    {{<figure src="/images/old_doc_images/contrib-gde-fig-shtcode.png">}}

    Optionally scale the image by adding the `width` option. Width value is defined in pixels.

    For example:
    {{<figure src="/images/old_doc_images/contrib-gde-fig-shtcode-ex.png">}}

    {{%notice tip%}}
The figure shortcode places the figure on a new line. The img shortcode places the image inline with the text (unless it is too wide to do so).
    {{%/notice%}}

### Add a Code Block

A code block is used when you want to present two or more lines of code. To create the highlighted box and set the font accordingly, insert three ticks (`) on a separate line before the code, and a second set of three ticks on a new line after the code.

For example, this markdown renders the following code block.

{{<figure src="/images/old_doc_images/contrib-gde-codeblk-ex.png">}}

```
cumulus@switch:~$ netq check bgp
bgp check result summary:

Checked nodes       : 8
Total nodes         : 8
Rotten nodes        : 0
Failed nodes        : 0
Warning nodes       : 0

Additional summary:
Total Sessions      : 30
Failed Sessions     : 0

Session Establishment Test   : passed
Address Families Test        : passed
Router ID Test               : passed
```
### Add a Link
#### External Links
For external links standard markdown link syntax can be used. The link text is placed in brackets `[]`, followed by the full URL in parenthesis `()`. For example `[Link to Cumulus](https://www.cumulusnetworks.com)` generates the link [Link to Cumulus](https://docs.nvidia.com/networking-ethernet-software/). 

{{% notice note %}}
Do not put a space between the brackets and parenthesis.
{{% /notice %}}

#### Across Products
To link betwen products use the Hugo built-in `ref` function with standard Markdown links. Using the same syntax for External links with brackets `[]` and parenthesis `()`. 

To properly generate the URL of the linked page the `ref` code takes in the path of the file to link. For example, to link to the Cumulus Linux 4.3 page on NTP:  

`[NTP]({{</* ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time"*/>}})`

To link to the latest release of a product, for example `/cumulus-linux` or `/cumulus-netq`, do not link directly but use the `kb_link` shortcode and provide the parameter `latest` along with the file path of the page. For example, to link to the latest Cumulus Linux NTP page

`{{</* kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP"*/>}}`

The value `latest` supports `cl`, `netq` or `sonic`. 
For root pages (`_index.md`) the `_index.md` filename must be included.

#### Within a Product
To preserve portability of pages, a [Hugo shortcode](https://gohugo.io/content-management/shortcodes/#what-a-shortcode-is) is used for all pages within the same section.

The `link` shortcode is used with the `title` argument. Use the `Title` value in the front matter of the page being linked. For example, to link to the "Give Simple Feedback" chapter use the shortcode `{{</* link title="Give Simple Feedback" */>}}`. By default the link title is the link text used. The text can be specified with the `text` attribute. For example, `{{</* link title="Give Simple Feedback" text="How to give feedback"*/>}}` generates the link {{< link title="Give Simple Feedback" text="How to give feedback" >}}.



