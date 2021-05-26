---
title: Make a Larger Contribution
author: Cumulus Networks
weight: 20
---
So you have more extensive comments or want to provide new content? Then there is a bit more that you need to understand to provide feedback of this type.

You need to set up a local environment for the documentation, perform your edits or create your new content there, and then submit it all through a pull request against the CumulusNetworks/docs repository on GitHub.

To get started:

- [Install Hugo](#install-hugo)
- [Clone the Docs Repository](#clone-the-cumulus-documentation-repository)
- [Run the Local Server](#run-the-local-server)

## Install Hugo

The first step is to install Hugo:

1. Go to *https://github.com/gohugoio/hugo/releases/tag/v0.82.0*.

2. Select the relevant **extended** package based on your operating system:
    - hugo_extended_0.82.0_Linux-64bit.deb
    - hugo_extended_0.82.0_Linux-64bit.tar.gz
    - hugo_extended_0.82.0_macOS-64bit.tar.gz
    - hugo_extended_0.82.0_Windows-64bit.zip

{{%notice note%}}
You must use the **extended** version of Hugo to support our use of SCSS stylesheets.
{{% /notice %}}

3. Decompress and install Hugo from the download.

4. Verify Hugo is installed and running.
    
    From a terminal window, run `hugo version`:

    ```
    <computer>:<username>$ hugo version
    hugo v0.82.0-9D960784+extended linux/amd64 BuildDate=2021-03-21T17:28:04Z VendorInfo=gohugoio
    ```

## Clone the Documentation Repository

The next step is to obtain a local copy of the Cumulus Networks Documentation Repository:

1. Create a directory where you want to store the documentation files.

2. Navigate to *https://github.com/CumulusNetworks/docs*.

3. Make sure the **Branch** is on *stage*, and then click **Clone or download**.

    {{<figure src="/images/old_doc_images/contrib-gde-clone-docs-repo.png" width="700">}}

4. Copy the HTTPS URL.

5. Return to your directory in the terminal window and type `git clone`.

6. Paste in the URL, and press **Enter**.

    ```
    <computer>:<cndocs-repo> <username>$ git clone https://github.com/CumulusNetworks/docs.git
    ```

When it is done cloning, your directory should have a copy of all of the source files.

## Run the Local Server

And the final setup step is to validate that you can view your local copy of the documentation repository using Hugo:

1. From your terminal window, navigate to the `docs` subdirectory.

2. Start the hugo server by running `hugo server --baseURL localhost:1313`.

    You should see output similar to this:

    ```
    <computer>:docs <username>$ hugo server
    Building sites...

                       |  EN
    -------------------+-------
      Pages            |  769
      Paginator pages  |    0
      Non-page files   | 2003
      Static files     | 1925
      Processed images |    0
      Aliases          |    0
      Sitemaps         |    1
      Cleaned          |    0
    
    Built in 6294 ms   
    Watching for changes in /Users/<username>/<cndocs-repo>/docs/{content,data,static,themes}
    Watching for config changes in /Users/<username>/<cndocs-repo>docs/config.toml
    Environment: "development"
    Serving pages from memory
    Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
    Web Server is available at //localhost:1313/ (bind address 127.0.0.1)
    Press Ctrl+C to stop
    ```

3. In the address field of a web browser, enter *http://localhost:1313*.

    When you make and then save changes to the source Markdown files, the updates are shown here.

    {{%notice tip%}}
If the page does not appear to be updating, you may need to stop the Hugo server (press Ctrl+c) and restart it using `hugo server --baseURL localhost:1313 --gc` to rebuild the site without using cached data.
    {{%/notice%}}

You are now ready to edit the documentation or create a new topic. Refer to [Adding New Content](Adding_New_Content).
