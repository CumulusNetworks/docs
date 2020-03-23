#!/usr/bin/env python3
'''
This script will pull the collection of release note JSON files.

The script will parse and markdown sanatize the JSON.

And write markdown files for hugo to render into the respective product and version directories.
'''

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
        output.append("|  Issue ID 	|   Description	|   Affects	|   Fixed |")
        output.append("\n")
        output.append("|---	        |---	        |---	    |---	                |")
        output.append("\n")
    else:
        output.append("### Fixed issues in {}".format(version))
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
        output.append("\n")
        output.append("|  Issue ID 	|   Description	|   Affects	|")
        output.append("\n")
        output.append("|---	        |---	        |---	    |")
        output.append("\n")

    for bug in json_file:
        if(file_type == "affects"):
            output.append("| <a name=\"" + bug["ticket"] + "\"></a> [" + bug["ticket"] + "](#" + bug["ticket"] + ") <a name=\"" + bug["ticket"] + "\"></a> | " + sanatize_rn_for_markdown(bug["release_notes_text"]) + " | " + ", ".join(bug["affects_versions"]) + " | " + ", ".join(bug["fixed_versions"]) + "|")
        else:
            output.append("| <a name=\"" + bug["ticket"] + "\"></a> [" + bug["ticket"] + "](#" + bug["ticket"] + ") | " + sanatize_rn_for_markdown(bug["release_notes_text"]) + " | " + ", ".join(bug["affects_versions"]) + " | " + "|")

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
    output.append("product: {}\n".format(product))
    output.append("version: \"{}\"\n".format(version))
    output.append("toc: 1\n")
    output.append("draft: True\n")
    output.append("---\n")
    output.append("\n\n")
    
    return output

def write_rns(output, file_type, product, version, minor=False):
    '''
    Write the RN output to the file for a given version.

    output - a list of lines to write
    type - xls or md
    version - the version to write to in hugo directory syntax. For example, cumulus-linux-40
    '''
    directory = get_hugo_folder(product, version)
    if file_type not in ["xls", "md"]:
        print("Incorrect filetype. Can not write release notes.")
        exit(1)

    if minor:
        minor_version = version
    else:
        minor_version = ""

    with open("content/{}/rn{}.{}".format(directory, minor_version, file_type), "w") as out_file:
        for line in output:
            out_file.write(line)

def build_rn_markdown_files(product, version_list):
    
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
            print("Building markdown for {} {}\n".format(product_string(product), version))
            version_output.append("## {} Release Notes\n".format(version))

            # once for affects, once for fixed.
            for rn_file in files:
                version_output.extend(
                    build_rn_markdown(get_json(product, version, rn_file), version, product_string(product), rn_file))

        # The version_output now contains the RNs for all maintenance releases in order. 
        # Write out the markdown file.
        write_rns(version_output, "md", product, version)

def build_rn_xls(json_file, version, product, file_type):
    '''
    Builds a list of lines that contain the entire formatted release notes in html table format.

    json_file - the json output to parse and build release notes from
    version - a full version string, i.e., 3.7.11
    product - a product_string() output, i.e., Cumulus Linux
    file_type - one of "affects" or "fixed"
    '''
    output = []
    if(file_type == "affects"):
        output.append("<table name=\"Open Issues in {}\">\n".format(version))
    else:
        output.append("<table name=\"Fixed issues in {}\">\n".format(version))
    output.append("<tr>\n")
    output.append("<th> Issue ID </th>\n")
    output.append("<th> Description </th>\n")
    output.append("<th> Affects </th>\n")
    if(file_type == "affects"):
        output.append("<th> Fixed </th>\n")
    output.append("</tr>\n")
    for bug in json_file:
        output.append("<tr>\n")
        output.append("<td>{}</td>\n".format(bug["ticket"]))
        output.append("<td>{}</td>\n".format(bug["release_notes_text"]))
        output.append("<td>{}</td>\n".format(bug["affects_versions"]))
        if(file_type == "affects"):
            output.append("<td>{}</td>\n".format(bug["fixed_versions"]))
        output.append("<tr>\n")
    output.append("</table>\n")

    return output

def build_rn_xls_files(product, version_list):
    files = ["affects", "fixed"]

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

        # all_versions_xls is the combined table of all minors within a major in a single xls file.
        all_versions_xls = []

        all_versions_xls.append("<tables>")
        
        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            print("Building xls for {} {}\n".format(product_string(product), version))
            
            # one_version_output is the table output for a single release
            one_version_output = []

            # once for affects, once for fixed.
            for rn_file in files:
                rn_output = build_rn_xls(get_json(product, version, rn_file), version, product_string(product), rn_file)
                one_version_output.extend(rn_output)
                all_versions_xls.extend(rn_output)
            
            write_rns(one_version_output, "xls", product, version, minor=True)

        # The one_version_output now contains the RNs for all maintenance releases in order. 
        # Write out the markdown file.
        all_versions_xls.append("</tables>")
        write_rns(all_versions_xls, "xls", product, version)
    
def main():

    products = {
        "cl":  ["3.7.1", "3.7.2", "3.7.3", "3.7.4", "3.7.5", "3.7.6", "3.7.7", "3.7.8", "3.7.9", "3.7.10", "3.7.11", "3.7.12", "4.0.0", "4.1.0"],
        "netq": ["2.4.0", "2.4.1"]
    }
    
    for product in products:
        build_rn_markdown_files(product, products[product])
        build_rn_xls_files(product, products[product])

    exit(0)


if __name__ == "__main__":
    main()