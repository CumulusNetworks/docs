#!/usr/bin/env python3
'''
This script will pull the collection of release note JSON files.

The script will parse and markdown sanatize the JSON.

And write markdown files for hugo to render into the respective product and version directories.

This will also write the XML files that are used to generate xls files for the release notes.
'''

import tarfile
import os
from os import listdir
import requests

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

    if version.count(".") == 1:
        return version

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

def format_license_string(license_string):
    '''
    Modify the license string to work around any special characters for HTML, markdown or CSS needs.

    license_string - string to format

    Returns:
    Formatted string that can be placed into a markdown page
    '''

    # Remove extra white space
    modified_string = license_string.strip()
    # Replace * character with HTML escape to not mess up markdown
    modified_string = modified_string.replace("*", "&#42;")
    # Add a space after license semi-colon to allow CSS to auto line break.
    modified_string = modified_string.replace(";", "; ")

    return modified_string

def build_foss_license_markdown(csv_file, version):
    '''
    Builds a list of lines that contain the entire formatted foss licenses in markdown table format.

    json_file - the json output to parse and build foss licenses from
    version - a full version string, i.e., 3.7.11
    product - a product_string() output, i.e., Cumulus Linux
    '''
    output = []
    header = True
    f = open(csv_file, "r")
    for line in f:
        split_line = line.split(",")
        license_string = format_license_string(split_line[2])

        if header:
            output.append("| {} | {} | {} |\n".format(split_line[0], split_line[1].strip(), license_string))
        else:
            output.append("| [{}](/cumulus-linux-{}/Whats-New/licenses/{}.txt) | {} | {} |\n".format(split_line[0], version_string(version).replace(".", ""), split_line[0], split_line[1].strip(), license_string))
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
    output.append("draft: true\n")
    output.append("pdfhidden: True\n")
    output.append("---\n")
    output.append("\n\n")

    return output

def read_markdown_header(product, version):
    '''
    To allow for the modification of front matter within the release note files
    we will read in the existing front matter and use that instead of generating it manually.

    This will rely on a valid YAML closing "---" line as a delimiter

    product - the product_string output, i.e., "Cumulus Linux"
    version - the Major.Minor release version, i.e., "4.0"

    Returns a list of strings that are the existing front matter.
    '''
    directory = get_hugo_folder(product, version)

    if product == "cl":
        input_file = "content/{}/Whats-New/foss.md".format(directory)
    elif product == "netq":
        input_file = "content/{}/More-Documents/foss.md".format(directory)

    look_for_end_of_header = True
    header_lines = []
    with open(input_file, "r") as in_file:
        # skip the first line, it should be just a yaml header of "---"
        header_lines.append(in_file.readline())
        while look_for_end_of_header:
            current_line = in_file.readline()
            if current_line.strip("\n") == "---":
                look_for_end_of_header = False
                break
            header_lines.append(current_line)

        header_lines.append("---\n")
    return header_lines

def write_foss_licenses(output, product, version):
    '''
    Write the RN output to the file for a given version.

    output - a list of lines to write
    type - xls or md
    version - the version to write to in hugo directory syntax. For example, cumulus-linux-40
    '''
    directory = get_hugo_folder(product, version)

    with open("content/{}/Whats-New/foss.md".format(directory), "w") as out_file:
        for line in output:
            out_file.write(line)

def build_foss_license_markdown_files(product, version_list):
    '''
    Build the markdown file for every version in the version_list

    version_list - a list of product versions like [3.7.2, 3.8.1, 3.9.0, 4.0.0]. Order does not matter.
    '''

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
        #version_output.extend(build_markdown_header(product_string(product), major))
        version_output.extend(read_markdown_header(product, major))

        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            print("Building markdown for {} {}\n".format(product_string(product), version))
            version_output.append("## {} Open Source Software Licenses \n".format(version))

            version_output.extend(build_foss_license_markdown("content/cumulus-linux-{}/Whats-New/licenses/FOSS-{}.csv".format(version_string(version).replace(".", ""), version), version))

        # The version_output now contains the RNs for all maintenance releases in order.
        # Write out the markdown file.
        write_foss_licenses(version_output, product, version)

def process_foss_tar(version):
    '''
    Download the tar file containing the foss licenses.

    version - the version to capture foss tar files for
    '''

    url = "https://d2whzysjlaya8k.cloudfront.net/cl/{}/FOSS-{}.tgz".format(version, version)

    response = requests.get(url, stream=True)

    if response.status_code != 200:
        print('Unable to download {} \nReceived response {}'.format(url, response.status_code))
        exit(1)

    with open("temp.tgz", "wb") as f:
        f.write(response.raw.read())
    license_dir = "content/cumulus-linux-{}/Whats-New/licenses/".format(version_string(version).replace(".", ""))
    tar = tarfile.open("temp.tgz")
    tar.extractall(path=license_dir)

    for file in listdir(license_dir):
        if file.endswith(".csv") or file.endswith(".txt"):
            continue
        os.rename("{}{}".format(license_dir, file), "{}{}.txt".format(license_dir, file))

    os.remove("temp.tgz")

    return "{}/FOSS-{}.csv".format(license_dir, version)

def main():
    '''
    Main function
    '''
    products = {
        "cl": ["3.7.12", "4.1.0", "4.1.1", "4.1.2"]
    }

    cvs_file_list = []
    for product in products:
        for value in products[product]:
            cvs_file_list.append(process_foss_tar(value))

        build_foss_license_markdown_files(product, products[product])

        for file in cvs_file_list:
            os.remove(file)

    exit(0)


if __name__ == "__main__":
    main()
