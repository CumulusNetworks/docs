#!/usr/bin/env python3

import json
from operator import itemgetter, attrgetter
import requests 
import re

def get_json(product, version, json_file):
    ''' 
    Downloads the json file for a given product/version from the cloudfront bucket.
    Also sort based on "ticket" value.

    product - either "cl" or "netq"
    version - the specific version of file to download. For example, "3.2.1" or "4.1.1"
    json_file - either "fixed" or "affects"
    '''

    session = requests.Session()
    url = "https://d2whzysjlaya8k.cloudfront.net/{}/{}/{}.json".format(product, version, json_file)
    response = session.get(url)
    if response.status_code != 200:
        print('Unable to download {}. \nReceived response {}'.format(url, response.status_code))
        exit(1)
    
    return sorted(response.json(), key=itemgetter("ticket"), reverse=True)

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

def build_rn_markdown(json_file, version, product, file_type):
    '''
    Builds a list of lines that contain the entire formatted release notes in markdown table format.

    json_file - the json output to parse and build release notes from
    version - a full version string, i.e., 3.7.11
    product - a product_string() output, i.e., Cumulus Linux
    file_type - one of "affects" or "fixed"
    '''
    output = []

    if(file_type == "affects"):
        output.append("### Open issues in {}".format(version))
        output.append("\n")
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
        output.append("\n")
        output.append("|  Bug ID 	|   Description	|   Affects	|   Fixed in release	|")
        output.append("\n")
        output.append("|---	        |---	        |---	    |---	                |")
        output.append("\n")
    else:
        output.append("### Fixed issues in {}".format(version))
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
        output.append("\n")
        output.append("|  Bug ID 	|   Description	|   Affects	|")
        output.append("\n")
        output.append("|---	        |---	        |---	    |")
        output.append("\n")

    for bug in json_file:
        if(file_type == "affects"):
            output.append("| " + bug["ticket"] + " | " + sanatize_rn(bug["release_notes_text"]) + " | " + ", ".join(bug["affects_versions"]) + " | " + ", ".join(bug["fixed_versions"]) + "|")
        else:
            output.append("| " + bug["ticket"] + " | " + sanatize_rn(bug["release_notes_text"]) + " | " + ", ".join(bug["affects_versions"]) + " | " + "|")

        output.append("\n")
    
    # output.append("</div>")
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
    output.append("title: {} {} Release Notes\n".format(product, version))
    output.append("author: Cumulus Networks\n")
    output.append("weight: -30\n")
    output.append("cascade:\n")
    output.append("    product: {}\n".format(product_string))
    output.append("    version: \"{}\"\n".format(version_string))
    output.append("toc: 1\n")
    output.append("---\n")
    output.append("\n\n")
    
    return output

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

def write_rns(release_note_markdown, product, version):
    '''
    Write the RN output to the file for a given version.

    release_note_markdown - a list of lines to write
    version - the version to write to in hugo directory syntax. For example, cumulus-linux-40
    '''
    directory = get_hugo_folder(product, version)
    with open("content/{}/rn.md".format(get_hugo_folder(product, version)), "w") as out_file:
        for line in release_note_markdown:
            out_file.write(line)

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

def build_rn_files(product, version_list):
    
    files = ["affects", "fixed"] # Order matters. This order determines the order rendered on the RN page.


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
        
        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            print("Building {} {}\n".format(product_string(product), version))
            version_output.append("## {} Release Notes\n".format(version))

            # once for affects, once for fixed.
            for rn_file in files:
                version_output.extend(
                    build_rn_markdown(get_json(product, version, rn_file), version, product_string(product), rn_file))

        # The version_output now contains the RNs for all maintenance releases in order. 
        # Write out the markdown file.
        write_rns(version_output, product, version)


def main():

    products = {
        "cl":  ["3.7.1", "3.7.2", "3.7.3", "3.7.4", "3.7.5", "3.7.6", "3.7.7", "3.7.8", "3.7.9", "3.7.10", "3.7.11", "3.7.12", "4.0.0", "4.1.0"],
        "netq": ["2.4.0", "2.4.1"]
    }
    
    for product in products:
        build_rn_files(product, products[product])


    exit(0)


if __name__ == "__main__":
    main()