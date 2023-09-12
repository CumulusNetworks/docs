---
title: Make a Larger Contribution
author: NVIDIA
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

## Conform to House Style with Vale

The documentation uses {{<exlink url="https://docs.errata.ai/vale/about" text="Vale">}} as a linting tool to keep the writing consistent. Think of it as an AI editor you invoke at the command line.

### Install Vale

To get started, {{<exlink url="https://docs.errata.ai/vale/install" text="install Vale">}}. Run the following command in a terminal:

{{<tabs "Install Vale">}}

{{<tab "MacOS or Linux">}}

```
$ brew install vale
```

{{</tab>}}
 
{{<tab "Windows">}}

```
> choco install vale
```

{{</tab>}}

{{<tab "Docker">}}

```
$ docker pull jdkato/vale
```

{{</tab>}}

{{</tabs>}}

{{%notice note%}}

You need {{<exlink url="https://docs.brew.sh/Installation" text="homebrew">}} to install on MacOS or Linux, and {{<exlink url="https://docs.chocolatey.org/en-us/" text="choco">}} to install on Windows.

{{%/notice%}}

### Run Vale

Before you run Vale, pull the latest version from the stage branch, then make sure your local checkout has the `/utils/.vale` folder.

Run Vale from the root of your local checkout:

    $ vale --glob='!*{foss,rn}.md'  --config utils/.vale/.vale.ini content/cumulus-linux-43
 
The command above uses the following arguments and options: 

- The `--glob` regular expression instructs Vale to ignore the `foss.md` and `rn.md` files; Vale does not check the release notes or t the Cumulus Linux open source software license page.
- The `--config utils/.vale/vale.ini` tells Vale where to find its configuration file.
- The `content/cumulus-linux-43` is the folder Vale is going to check. Vale recurses through every folder below it, so if you run it on the top level `content` folder, it checks every single page for every version and product.
 
Vale returns output like the followings sample:

```
pete$ vale --glob='!*{foss,rn}.md'  --config utils/.vale/.vale.ini content/cumulus-netq-40
...
 content/cumulus-netq-40/Manage-Configuration/Provision-Network-and-Devices/Switch-Lifecycle-Management/CL-Upgrade-LCM.md
 219:104  error  'Mellanox' should reference     NVIDIA.Branding 
                 NVIDIA Networking or NVIDIA                     
                 Spectrum                                        

 content/cumulus-netq-40/Get-Started/NetQ-Basics/NetQ-Components.md
 35:60  warning  'bare metal' is the house       NVIDIA.WordStyles    
                 style of 'bare-metal'                                
 99:9   warning  '-' should use title            NVIDIA.HeadingTitles 
                 caps-style capitalization.     

 content/cumulus-netq-40/Validate-Operations/_index.md
 120:328  warning  Possible future tense ??  NVIDIA.FutureTense 
...
✖ 1 error, 408 warnings and 0 suggestions in 131 files.
pete$
```

The Vale output breaks down as follows:

- Name of and path to the file with the issue.
- The location of the issue in the Markdown file. For example, *35:60* means line 35, cursor position 60.
- The severity of the issue, which is one of *error*, *warning* or *suggestion*.
- The error message itself.
- The Vale configuration file that references the rule. For example, *NVIDIA.WordStyles* is the WordStyles.yml file in the `utils/.vale/NVIDIA` directory.
 
### Ignore Errors

Occasionally, Vale may flag something as an error, when it is actually a false positive. If the word choice or spelling is a valid reason to violate the rules, you can disable the Vale check for that text. For example, the NVIDIA Vale style guide states that there should not be any punctuation in a title, but that does not work for version numbers, as in the following example:

```  
## For Servers Running Ubuntu 16.04 or 18.04
 
Run the following command to view the NetQ Agent version.
```

Vale returns the following error when it checks that heading:

```
21:33  warning  '.' should use title            NVIDIA.HeadingTitles
                 caps-style capitalization.
```

To avoid the error, you can disable Vale for that heading in the source file. Wrap the whole paragraph in `<!-- vale off -->` and `<!-- vale on -->` tags:

```
<!-- vale off -->
## For Servers Running Ubuntu 16.04 or 18.04
<!-- vale on -->
Run the following command to view the NetQ Agent version.
```

The `<!-- vale on -->` tag must be on its own line in order to reenable Vale checking; otherwise, Vale ignores the rest of the file.

Vale currently has a bug where it does not properly ignore a hyphen (-) in a title. If you wrote a heading with a hyphen and see this error, disable Vale and add a comment so we can find it later. For example:

```
<!-- vale off -->
<!-- vale.ai Issue #253 -->
### Any-source Multicast Routing (ASM)
<!-- vale on -->
```

### Expand the Checks

Feel free to suggest modifications for anything in the `.vale` folder, or submit your own pull request.

## Troubleshooting Hugo

### Large Changes

If Hugo is currently running and a large volume of changes are made, for example, changing branches, Hugo may not always detect the changes. Stop and restart Hugo to see the new changes.

### Hugo pipe failed Error

When launching Hugo it may fail and produce a traceback similar to the following:

```
Start building sites …

                   |  EN
-------------------+-------
  Pages            | 1736
  Paginator pages  |    0
  Non-page files   | 6722
  Static files     | 1685
  Processed images |    0
  Aliases          |    0
  Sitemaps         |    1
  Cleaned          |    0

Built in 18957 ms
Watching for changes in /git/docs/{content,static,themes}
Watching for config changes in /git/docs/config.yml
fatal error: pipe failed
```

{{<expand "Traceback Output">}}

```
goroutine 1 [running]:
runtime.throw(0x5a04840, 0xb)
	/usr/local/go/src/runtime/panic.go:1117 +0x72 fp=0xc03cc51890 sp=0xc03cc51860 pc=0x40394f2
runtime.sigNoteSetup(0x6c9b140)
	/usr/local/go/src/runtime/os_darwin.go:98 +0xc5 fp=0xc03cc518b8 sp=0xc03cc51890 pc=0x40359e5
os/signal.signal_enable(0x2fa5a6e100000002)
	/usr/local/go/src/runtime/sigqueue.go:228 +0xa5 fp=0xc03cc518d8 sp=0xc03cc518b8 pc=0x406f7e5
os/signal.enableSignal(...)
	/usr/local/go/src/os/signal/signal_unix.go:49
os/signal.Notify.func1(0x2)
	/usr/local/go/src/os/signal/signal.go:145 +0x88 fp=0xc03cc518f8 sp=0xc03cc518d8 pc=0x5426108
os/signal.Notify(0xc048ce3da0, 0xc03cc51b38, 0x2, 0x2)
	/usr/local/go/src/os/signal/signal.go:165 +0x185 fp=0xc03cc51970 sp=0xc03cc518f8 pc=0x5425b25
github.com/gohugoio/hugo/commands.(*commandeer).serve(0xc000030a80, 0xc0008e7d40, 0x1f2, 0x200)
	/root/project/hugo/commands/server.go:494 +0x629 fp=0xc03cc51b68 sp=0xc03cc51970 pc=0x5459e49
github.com/gohugoio/hugo/commands.(*serverCmd).server(0xc0008e7d40, 0xc000612580, 0xc000152b20, 0x0, 0x2, 0x0, 0x0)
	/root/project/hugo/commands/server.go:272 +0x2c5 fp=0xc03cc51cb0 sp=0xc03cc51b68 pc=0x5458605
github.com/gohugoio/hugo/commands.(*serverCmd).server-fm(0xc000612580, 0xc000152b20, 0x0, 0x2, 0x0, 0x0)
	/root/project/hugo/commands/server.go:131 +0x5b fp=0xc03cc51cf8 sp=0xc03cc51cb0 pc=0x546685b
github.com/spf13/cobra.(*Command).execute(0xc000612580, 0xc000152ae0, 0x2, 0x2, 0xc000612580, 0xc000152ae0)
	/go/pkg/mod/github.com/spf13/cobra@v1.1.1/command.go:850 +0x472 fp=0xc03cc51db8 sp=0xc03cc51cf8 pc=0x41d3c52
github.com/spf13/cobra.(*Command).ExecuteC(0xc000359340, 0xc0002bde40, 0x5, 0x6)
	/go/pkg/mod/github.com/spf13/cobra@v1.1.1/command.go:958 +0x375 fp=0xc03cc51e98 sp=0xc03cc51db8 pc=0x41d47d5
github.com/gohugoio/hugo/commands.Execute(0xc000128010, 0x3, 0x3, 0x4007c85, 0xc00009e058, 0x546a730, 0x0)
	/root/project/hugo/commands/hugo.go:87 +0xb9 fp=0xc03cc51f28 sp=0xc03cc51e98 pc=0x5445019
main.main()
	/root/project/hugo/main.go:23 +0x76 fp=0xc03cc51f88 sp=0xc03cc51f28 pc=0x546a096
runtime.main()
	/usr/local/go/src/runtime/proc.go:225 +0x256 fp=0xc03cc51fe0 sp=0xc03cc51f88 pc=0x403bd16
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1371 +0x1 fp=0xc03cc51fe8 sp=0xc03cc51fe0 pc=0x40735a1

goroutine 20 [select]:
go.opencensus.io/stats/view.(*worker).start(0xc0000a8880)
	/go/pkg/mod/go.opencensus.io@v0.22.5/stats/view/worker.go:276 +0xcd
created by go.opencensus.io/stats/view.init.0
	/go/pkg/mod/go.opencensus.io@v0.22.5/stats/view/worker.go:34 +0x68

goroutine 2003 [syscall]:
syscall.syscall6(0x424e440, 0x8, 0x0, 0x0, 0xc000064e88, 0xa, 0x6c9ac00, 0x0, 0x0, 0x0)
	/usr/local/go/src/runtime/sys_darwin.go:41 +0x2e
golang.org/x/sys/unix.kevent(0x8, 0x0, 0x0, 0xc000064e88, 0xa, 0x6c9ac00, 0x0, 0x0, 0x0)
	/go/pkg/mod/golang.org/x/sys@v0.0.0-20210104204734-6f8348627aad/unix/zsyscall_darwin_amd64.go:275 +0xa5
golang.org/x/sys/unix.Kevent(0x8, 0x0, 0x0, 0x0, 0xc000064e88, 0xa, 0xa, 0x6c9ac00, 0x0, 0x0, ...)
	/go/pkg/mod/golang.org/x/sys@v0.0.0-20210104204734-6f8348627aad/unix/syscall_bsd.go:428 +0x71
github.com/fsnotify/fsnotify.read(0x8, 0xc000064e88, 0xa, 0xa, 0x6c9ac00, 0xc000064e88, 0x0, 0xa, 0x0, 0x0)
	/go/pkg/mod/github.com/fsnotify/fsnotify@v1.4.9/kqueue.go:511 +0x6e
github.com/fsnotify/fsnotify.(*Watcher).readEvents(0xc046ae2960)
	/go/pkg/mod/github.com/fsnotify/fsnotify@v1.4.9/kqueue.go:274 +0x81b
created by github.com/fsnotify/fsnotify.NewWatcher
	/go/pkg/mod/github.com/fsnotify/fsnotify@v1.4.9/kqueue.go:62 +0x199

goroutine 2004 [select]:
github.com/gohugoio/hugo/watcher.(*Batcher).run(0xc04640fea0)
	/root/project/hugo/watcher/batcher.go:53 +0x129
created by github.com/gohugoio/hugo/watcher.New
	/root/project/hugo/watcher/batcher.go:42 +0x13b

goroutine 2005 [select]:
github.com/gohugoio/hugo/livereload.(*hub).run(0x6c5c4e0)
	/root/project/hugo/livereload/hub.go:39 +0xfd
created by github.com/gohugoio/hugo/livereload.Initialize
	/root/project/hugo/livereload/livereload.go:99 +0x45

goroutine 1976 [select]:
github.com/gohugoio/hugo/commands.(*commandeer).newWatcher.func1(0xc04640fea0, 0xc000030a80, 0xc0457a79a0, 0xc044930a80)
	/root/project/hugo/commands/hugo.go:853 +0xc5
created by github.com/gohugoio/hugo/commands.(*commandeer).newWatcher
	/root/project/hugo/commands/hugo.go:851 +0x2ce
```

{{</expand>}}

This is caused by operating system limits on the number of open files. The way to verify and adjust this depends on the operating system and version in use.

#### Mac OSX 10.4 Mojave and Later

To adjust the max file limits, you must change both the kernel settings and session ulimits.

```
sudo sysctl -w kern.maxfiles=65536
ulimit -n 65536 65536
```

{{%notice note%}}
The `ulimit` adjustment only lives for the life of that terminal window. If the window is closed or a new window is open, the `ulimit` command must be run again.
{{%/notice%}}

### Sparse Checkout

It is possible to only check out a portion of the docs repository to work on only the section you wish to contribute to. Git refers to this partial checkout as a *sparse checkout*.

A sparse checkout speeds up Hugo build times, limits the amount of local disk space that is used and can be a valid workaround for the Hugo `pipe failed` error message.

To create a sparse checkout:

1. Create the destination directory for the repo:

       mkdir docs

2. Enter the new directory and initialize it with Git:

   ```
   cd docs
   git init
   ```
3. Add the docs repo as a Git Remote:

       git remote add -f origin git@github.com:CumulusNetworks/docs.git

4. Configure this directory as a *sparse checkout*:

       git config core.sparseCheckout true

5. Configure Git to check out the mandatory docs files:

       echo "utils/" >> .git/info/sparse-checkout
       echo "config.toml" >> .git/info/sparse-checkout
       echo "build_trigger.txt" >> .git/info/sparse-checkout
       echo "themes/" >> .git/info/sparse-checkout
       echo ".vale" >> .git/info/sparse-checkout
       echo "config.yml" >> .git/info/sparse-checkout
       echo "static/mibs" >> .git/info/sparse-checkout

6. Add the content you wish to modify to the Git sparse checkout. This includes both the files in the `/content` directory as well as any relevant images in `/static/images` directory. For example, to make contributions or modifications to {{<kb_link url="knowledge-base/_index.md" text="Knowledge Base" >}} articles add both the `/content/knowledge-base` and `/static/images/knowledge-base` directories.

       echo "content/knowledge-base/` >> .git/info/sparse-checkout
       echo "static/images/knowledge-base/` >> .git/info/sparse-checkout

7. Checkout the appropriate branch:

       git checkout stage

8. Adjust the Hugo configuration to ignore link checking.

   If you plan to run Hugo locally, due to how the Hugo `ref` shortcode validates links it will cause Hugo to fail at runtime due to the sparse checkout. The Hugo configuration must be changed locally to only log Warnings and allow Hugo to start

       echo "\nrefLinksErrorLevel: WARNING" >> config.yml

9. Configure Git to ignore the `config.yml` file to prevent an accidental commit of this change:

       git update-index --assume-unchanged config.yml

10. Run Hugo. You can safely ignore `REF_NOT_FOUND` warnings.

        hugo server --baseURL localhost:1313

All other git operations including `git commit`, `git push` and `git checkout` work normally.
