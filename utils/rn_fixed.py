#!/usr/bin/env python3

import json
import re
from bs4 import BeautifulSoup

json_dir = "data/rn_json/"

def get_json(json_file):

    with open(json_dir + json_file) as file:
        loaded_json = json.load(file)
    
    return loaded_json

def sanatize_rn(string):
    
    # Replace code format with markdown

    # Remove HTML tags
    TAG_RE = re.compile(r'<[^>]+>')
    output_string = TAG_RE.sub('', string)

    # Remove line returns and replace them with HTML breaks
    output_string = output_string.replace("\r", "")
    output_string = output_string.replace("\n\n", "<br />")
    output_string = output_string.replace("\n", "<br />")

    # Escape pipe characters
    output_string = output_string.replace("|", "\|")

    #Replace @ characters to prevent auto email link creation 
    output_string = output_string.replace("@", "&#64;")

    return output_string
 

def build_rns(json_file, fixed=True):
    output = []
    if(fixed):
        output.append("## Open issues in 4.1")
        output.append("\n")
        output.append("|  Bug ID 	|   Description	|   Affects	|   Fixed in release	|")
        output.append("\n")
        output.append("|---	        |---	        |---	    |---	                |")
        output.append("\n")
    else:
        output.append("## Fixed issues in 4.1")
        output.append("\n")
        output.append("|  Bug ID 	|   Description	|   Affects	|")
        output.append("\n")
        output.append("|---	        |---	        |---	    |")
        output.append("\n")

    for bug in json_file:
        if(fixed):
            output.append("| " + bug["ticket"] + " | " + sanatize_rn(bug["release_notes_text"]) + " | " + ", ".join(bug["affects_versions"]) + " | " + ", ".join(bug["fixed_versions"]) + "|")
        else:
            output.append("| " + bug["ticket"] + " | " + sanatize_rn(bug["release_notes_text"]) + " | " + ", ".join(bug["affects_versions"]) + " | " + "|")

        output.append("\n")

    return output

def write_rns(release_note_markdown):
    with open("content/cumulus-linux-41/rn.md", "w") as out_file:
        header = """---
title: Cumulus Linux 4.1 Release Notes
author: Cumulus Networks
weight: -30
cascade:
    product: Cumulus Linux
    version: "4.1"
toc: 1
---
"""
        out_file.write(header + "\n")
        for line in release_note_markdown:
            out_file.write(line)

def main():
    open_output = build_rns(get_json("cl_release_note_affects.json"))
    fixed_output = build_rns(get_json("cl_release_note_fixed.json"), fixed=False)
    open_output.extend(fixed_output)

    write_rns(open_output)

if __name__ == "__main__":
    main()