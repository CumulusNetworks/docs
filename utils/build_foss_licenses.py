#!/usr/bin/env python3
'''
This script will pull the collection of release note JSON files.

The script will parse and markdown sanatize the JSON.

And write markdown files for hugo to render into the respective product and version directories.

This will also write the XML files that are used to generate xls files for the release notes. 
'''

import json
from operator import itemgetter, attrgetter
import requests 
import re

def product_string(product):
    '''
    Take in the product short hand and return the product name.

    product - one of "cl" or "netq"
    '''
    if product == "cl":
        return "Cumulus Linux"
    elif product == "netq":
        return "Cumulus NetQ"
    else:
        print("Unknown product {}".format(product))
        exit(1)

def version_string(version):
    ''' 
    Take in the semver product version and return just the major.minor

    version - product version string, like 3.0.0 or 4.1.4
    Return
     3.0 
     4.1
    '''

    return version[:version.rfind(".")]

def get_hugo_folder(product, version):
    '''
    Take in a product like "cl" and version string like "4.0.0" 

    Returns
    Hugo /content directory name, for example cumulus-linux-40
    '''
    folder_ver = version_string(version).replace(".", "")

    if product == "cl":
        return "cumulus-linux-{}".format(folder_ver)
    elif product == "netq":
        return "cumulus-netq-{}".format(folder_ver)
    else:
        print("ERROR: Unknown product {}".format(product))
        exit(1)

def sanatize_rn_for_markdown(string):
    '''
    Strip any special or problematic characters from the a string. 
    This (generally) will be used on the release note text to strip characters that break markdown.

    string - The string to sanatize
    '''

    # # Remove HTML tags
    # TAG_RE = re.compile(r'<[^>]+>')
    # output_string = TAG_RE.sub('', string)
    output_string = string.replace("<p>", "")
    output_string = output_string.replace("</p>", "")
    
    output_string = output_string.replace("`", "'")

    output_string = output_string.replace("\r\n", "<br />")
    output_string = output_string.replace("\n", "")
    
    output_string = output_string.replace("&lt;", "<")
    output_string = output_string.replace("&gt;", ">")

    output_string = output_string.replace("<tt>", "`")
    output_string = output_string.replace("</tt>", "`")

    #CM-21678
    output_string = output_string.replace('<div class=\"preformatted\" style=\"border-width: 1px;\"><div class=\"preformattedContent panelContent\"><pre>', "<br /><pre>")
    output_string = output_string.replace("</pre></div></div>", "</pre><br />")

    # Remove line returns and replace them with HTML breaks
    output_string = output_string.replace("\r", "")
    #output_string = output_string.replace("\n\n", "<br />")
    #output_string = output_string.replace("\n", "<br />")

    
    # Escape pipe characters
    output_string = output_string.replace("|", "\|")

    #Replace @ characters to prevent auto email link creation 
    output_string = output_string.replace("@", "&#64;")
    output_string = output_string.replace("[", "&#91;")
    output_string = output_string.replace("]", "&#93;")
    

    return output_string

def build_foss_license_markdown(csv_file, version, product):
    '''
    Builds a list of lines that contain the entire formatted release notes in markdown table format.

    json_file - the json output to parse and build release notes from
    version - a full version string, i.e., 3.7.11
    product - a product_string() output, i.e., Cumulus Linux
    '''
    output = []
    header = True
    f = open(csv_file, "r")
    for line in f:
        split_line = line.split(",")
        if header:
            output.append("| {} | {} | {} |\n".format(split_line[0], split_line[1].strip(), split_line[2].strip()))
        else:
            output.append("| [{}]({}) | {} | {} |\n".format(split_line[0], split_line[0], split_line[1].strip(), split_line[2].strip()))
        if header:
            output.append("|---	        |---	        |---	    |\n")
            header = False
    
    output.append("\n")
    
    return output

def build_markdown_header(product, version):
    '''
    Produce the hugo front matter for the release note file
    
    product - the product_string output, i.e., "Cumulus Linux"
    version - the Major.Minor release version, i.e., "4.0"
    '''
    output = []

    output.append("---\n")
    output.append("title: {} {} Open Source Packages\n".format(product, version))
    output.append("author: Cumulus Networks\n")
    output.append("weight: -30\n")
    output.append("product: {}\n".format(product))
    output.append("version: \"{}\"\n".format(version))
    output.append("toc: 1\n")
    output.append("draft: True\n")
    output.append("bookhidden: True\n")
    output.append("---\n")
    output.append("\n\n")
    
    return output

def write_foss_licenses(output, product, version, minor=False):
    '''
    Write the RN output to the file for a given version.

    output - a list of lines to write
    type - xls or md
    version - the version to write to in hugo directory syntax. For example, cumulus-linux-40
    '''
    directory = get_hugo_folder(product, version)

    with open("content/{}/foss/_index.md".format(directory), "w") as out_file:
        for line in output:
            out_file.write(line)

def build_foss_license_markdown_files(product, version_list):
    
    # Sort the lists based on semver, most recent first.
    # I don't know what this does but that's what Stackoverflow is for
    # https://stackoverflow.com/a/2574090
    version_list.sort(key=lambda s: list(map(int, s.split('.'))), reverse=True)

    # We need to map major.minors to full release list, 
    # { 3.7: [3.7.1, 3.7.2, 3.7.3...]
    major_minor = {}

    for version in version_list:
        if version_string(version) in major_minor:
            major_minor[version_string(version)].append(version)
        else:
            major_minor[version_string(version)] = [version]
    
    # Now we have a map of majors.minors to ordered list of maintenance releases
    # loop over every major and build the RN page for that major 
    for major in major_minor.keys():        
        version_output = []
        
        # We only want to generate the frontmatter once per minor
        version_output.extend(build_markdown_header(product_string(product), major))    
        hugo_dir = get_hugo_folder(product, version)

        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            print("Building markdown for {} {}\n".format(product_string(product), version))
            version_output.append("## {} Open Source Software Licenses \n".format(version))
            hugo_dir = get_hugo_folder(product, version)

            version_output.extend(build_foss_license_markdown("utils/FOSS-4.1.0.csv", version, product_string(product)))

        # The version_output now contains the RNs for all maintenance releases in order. 
        # Write out the markdown file.
        write_foss_licenses(version_output, product, version)


def main():

    # products = {
    #     "cl":  ["3.7.1", "3.7.2", "3.7.3", "3.7.4", "3.7.5", "3.7.6", "3.7.7", "3.7.8", "3.7.9", "3.7.10", "3.7.11", "3.7.12", "4.0.0", "4.1.0"],
    #     "netq": ["2.4.0", "2.4.1"]
    # }
    
    products = {
        "cl": ["4.1.0"]
    }

    for product in products:
        build_foss_license_markdown_files(product, products[product])

    exit(0)


if __name__ == "__main__":
    main()