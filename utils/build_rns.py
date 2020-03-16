#!/usr/bin/env python3

import json
import re
import sys

json_dir = "data/rn_json"

def get_json(version, json_file):
    ''' 
    Open a given json file and return the loaded json.

    version - the folder name of the version to look for. For example cumulus-linux-40
    json_file - the filename of the json file to load
    '''

    with open(json_dir + "/" +  version + "/" + json_file) as file:
        loaded_json = json.load(file)
    
    return loaded_json

def sanatize_rn(string):
    '''
    Strip any special or problematic characters from the a string. 
    This (generally) will be used on the release note text to strip characters that break markdown.

    string - The string to sanatize
    '''

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
    '''
    Builds a list of lines that contain the entire formatted release notes in markdown table format.

    json_file - the loaded json output to parse and build release notes from
    fixed - If "true" we are building the "Fixed Issues" RNs. If "false" we are building the "Open Issues" RNs.
    '''
    output = []
    if(fixed):
        output.append("## Open issues in {{% version %}}")
        output.append("\n")
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
        output.append("\n")
        output.append("|  Bug ID 	|   Description	|   Affects	|   Fixed in release	|")
        output.append("\n")
        output.append("|---	        |---	        |---	    |---	                |")
        output.append("\n")
    else:
        output.append("## Fixed issues in {{% version %}}")
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
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
    
    # output.append("</div>")
    output.append("\n")

    return output

def write_rns(release_note_markdown, version):
    '''
    Write the RN output to the file for a given version.

    release_note_markdown - a list of lines to write
    version - the version to write to in hugo directory syntax. For example, cumulus-linux-40
    '''
    with open("content/" + version + "/rn.md", "a") as out_file:
        for line in release_note_markdown:
            out_file.write(line)

def main():
    # if len(sys.argv) != 2:
    #     print("Please provide the content folder name of the release to build release notes for. For example \n\t $ python build_rns.py cumulus-linux-41")
    # exit(1)

    version = "cumulus-linux-41" #sys.argv[1]
    affects_filename = "cl_release_note_affects.json"
    fixed_filename = "cl_release_note_fixed.json"

    open_output = build_rns(get_json(version, affects_filename))
    fixed_output = build_rns(get_json(version, fixed_filename), fixed=False)
    open_output.extend(fixed_output)

    write_rns(open_output, version)

if __name__ == "__main__":
    main()