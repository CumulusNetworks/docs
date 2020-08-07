---
title: vi for Beginners
author: Cumulus Networks
weight: 58
toc: 4
---

Many new Linux administrators find the `vi` editor complex and daunting.
It is not as user friendly as other editors that they may have used
before, but with a little practice, `vi` can be a powerful tool for
managing files.

This article is not intended to make you a master of `vi`. Instead, it
tries to get you comfortable with the editor so that you can learn the
more advanced tools as you need them.

## Background

`vi` was originally called the \"VIsual editor\" because it allowed the
entire file to be seen on screen at once. It was first developed in a
world without function keys and a mouse. Administrators had just the
basic keyboard keys and so had to make the most of what they had to work
with. Every key has a function within `vi`, but how do you separate the
text from the commands?

## Modes

`vi` has two modes: *command* and *input*.

Command mode is the default when you first opens a file. In this mode,
your keystrokes perform different actions within the editor. Be careful,
however -- in order to extend the number of possible commands, `vi` is
case sensitive, so the upper- and lowercase letters almost always have
different behaviors. Certain characters -- most notably the colon (:)
and forward slash (/) -- activate an in-application command line for
multi-character commands.

Input mode allows text to be entered in the file. You activate this mode
with a set of command mode characters. A status bar at the bottom of the
screen indicates which input mode is in use. The \<esc\> key exits input
mode and returns the editor to command mode.

## Movement

Although you can use arrow keys to move through a file in modern
incarnations of `vi`, part of the editor\'s strength is that you never
need to move your hands from the home keys. This means less wasted
movement and better efficiency.

The simple movement keys are h, j, k, and l.

| Command | Action       | Mnemonic                                                              |
|---------|--------------|-----------------------------------------------------------------------|
| h       | cursor left  | Key is at left of the group on the keyboard                           |
| j       | cursor down  | "Jump down"                                                           |
| k       | cursor up    | "Kick up"                                                             |
| l       | Cursor right | (lowercase letter l) Key is at the right of the group on the keyboard |

Many administrators only use these four keys to navigate their files.
Once comfortable with the basic movements, the next step is to learn how
to move more efficiently.

| Command | Action                                         |
|---------|------------------------------------------------|
| 0       | (zero) Go to the **front** of the current line |
| $       | Go to the **end** of the current line          |
| w       | Advance a single **word**                      |
| b       | Go **back** a single word                      |
| G       | Go to the **last line** of the file            |

## Managing Text

Multiple commands start input mode, depending on where and how the text
is placed in the file.

| Command | Action                                                         |
|---------|----------------------------------------------------------------|
| i       | **Insert** text before the current cursor position             |
| a       | **Append** text after the current cursor position              |
| I       | (uppercase I) **Insert** text at the front of the current line |
| A       | **Append** text at the end of the current line                 |
| r       | **Replace** the letter at the current cursor position          |
| R       | **Replace** individual characters as the administrator types   |
| o       | (lowercase letter o) **Open** a line below for adding text     |
| O       | (uppercase letter O) **Open** a line above for adding text     |

To manipulate text, the major commands are x (character delete or
\"strike out\"), d (delete), y (copy or \"yank\"), and p (paste). The y
and d commands require additional characters to indicate the amount of
text to copy or delete. Prepending a number will repeat an action that
number of times.

| Command | Action                                                          |
|---------|-----------------------------------------------------------------|
| x       | **Delete** the character after the cursor position              |
| dw      | **Delete** an entire word                                       |
| dd      | **Delete** an entire line                                       |
| yw      | **Yank** an entire word                                         |
| yy      | **Yank** an entire line                                         |
| y$      | **Yank** to the end of the current line                         |
| p       | **Paste** copied or deleted text after current cursor position  |
| P       | **Paste** copied or deleted text before current cursor position |
| 4dw     | **Delete** the next four words                                  |
| u       | **Undo** the last action                                        |
| U       | **Undo** all changes since you last entered the current line    |
| .       | **Repeat** the last action                                      |

## Closing a File

Like an text editor, `vi` allows you multiple ways to exit a file, with
and without saving. Some of the files require the : character which
allows you to see the commands you type on screen.

| Command             | Action                                                                |
|---------------------|-----------------------------------------------------------------------|
| :q                  | **Quit** a file (will prompt if a save is needed)                     |
| :q!                 | **Quit** a file forcefully (discards unsaved changes)                 |
| :w                  | **Write** (save) the file                                             |
| :w &lt;filename&gt; | **Write** the file and rename to &lt;filename&gt;                     |
| :w!                 | **Write** forcefully (overrides read-only files that you own)         |
| :wq                 | **Write** file, then **quit**                                         |
| zz                  | **Write** file, then **quit** (also called "putting the file to bed") |
