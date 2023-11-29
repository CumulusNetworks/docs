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
import csv

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

    # The rfind here will drop the right most value. This means 3.7.14.2 returns "3.7.14".
    # But we only want "3.7"
    while version.count(".") > 1:
        version = version[:version.rfind(".")]

    return version

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

def build_foss_license_markdown(csv_file, version, product):
    '''
    Builds a list of lines that contain the entire formatted foss licenses in markdown table format.

    csv_file - the csv output to parse and build foss licenses from
    version - a full version string, i.e., 3.7.11
    product - a product_string() output, i.e., Cumulus Linux
    '''
    output = []
    header = True
    f = open(csv_file, "r")
    f_csv = csv.reader(f)
    for row in f_csv:
        license_string = format_license_string(row[2])
        if header:
            output.append("| {} | {} | {} |\n".format(row[0], row[1].strip(), license_string))
        else:
            if product == "cl":
                output.append("| {{{{<foss_file text=\"{}\" url=\"cumulus-linux-{}/Whats-New/licenses/{}.txt\" >}}}} | {} | {} |\n".format(row[0], version_string(version).replace(".", ""), row[0], row[1].strip(), license_string))
            if product == "netq":
                output.append("| {{{{<foss_file text=\"{}\" url=\"cumulus-netq-{}/Whats-New/licenses/{}.txt\" >}}}} | {} | {} |\n".format(row[0], version_string(version).replace(".", ""), row[0], row[1].strip(), license_string))
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
    output.append("pdfhidden: True\n")
    output.append("---\n")

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
        input_file = "content/{}/Whats-New/foss.md".format(directory)
    else:
        print("Unknown product {}. Exiting".format(product))
        exit(1)

    header_lines = []

    # If the foss.md file exists, read it in, otherwise return an empty header_lines
    if os.path.exists(input_file):
        with open(input_file, "r") as in_file:
            # skip the first line, it should be just a yaml header of "---"
            header_lines.append(in_file.readline())
            for line in in_file:
                current_line = line
                if current_line.strip("\n") == "---":
                    break
                header_lines.append(current_line)
            else:
                # There is no frontmatter yaml header
                return []
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
        markdown_header = read_markdown_header(product, major)
        if markdown_header == []:
            markdown_header = build_markdown_header(product_string(product), major)
        version_output.extend(markdown_header)

        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            print("Building markdown for {} {}\n".format(product_string(product), version))
            version_output.append("## {} Open Source Software Licenses \n".format(version))

            if product == "cl":
                version_output.extend(build_foss_license_markdown("content/cumulus-linux-{}/Whats-New/licenses/FOSS-{}.csv".format(version_string(version).replace(".", ""), version), version, product))

            if product == "netq":
                version_output.extend(build_foss_license_markdown("content/cumulus-netq-{}/Whats-New/licenses/FOSS-{}.csv".format(version_string(version).replace(".", ""), version), version, product))

        # The version_output now contains the RNs for all maintenance releases in order.
        # Write out the markdown file.
        write_foss_licenses(version_output, product, version)

def process_foss_tar(product, version):
    '''
    Download the tar file containing the foss licenses.

    product - either "cl" or "netq"
    version - the version to capture foss tar files for
    '''
    print("Downloading license file for {} {}".format(product_string(product), version))
    url = "https://d2whzysjlaya8k.cloudfront.net/{}/{}/FOSS-{}.tgz".format(product, version, version)

    response = requests.get(url, stream=True)

    if response.status_code != 200:
        print('Unable to download {} \nReceived response {}'.format(url, response.status_code))
        exit(1)

    with open("temp.tgz", "wb") as f:
        f.write(response.raw.read())

    if product == "cl":
        license_dir = "content/cumulus-linux-{}/Whats-New/licenses/".format(version_string(version).replace(".", ""))
        tared_folder = license_dir
    elif product == "netq":
        license_dir = "content/cumulus-netq-{}/Whats-New/licenses/".format(version_string(version).replace(".", ""))
        # NetQ licenses are put inside a folder /inside/ the tar.
        tared_folder = license_dir + "FOSS-{}/".format(version)
    else:
        print("Unknown product {}. Exiting".format(product))
        exit(1)

    tar = tarfile.open("temp.tgz")
    tar.extractall(path=license_dir)

    for file in listdir(tared_folder):
        if file.endswith(".csv") or file.endswith(".txt"):
            # Move from tared_folder to license_dir, if they are different, but do not change the file type
            os.rename("{}{}".format(tared_folder, file), "{}{}".format(license_dir, file))
            continue

        # Move from tared_folder to license_dir, if they are different. Always add .txt
        os.rename("{}{}".format(tared_folder, file), "{}{}.txt".format(license_dir, file))

    os.remove("temp.tgz")

    return "{}/FOSS-{}.csv".format(license_dir, version)

def get_products():
    '''
    Download the engineering provided JSON file detailing the list of products and releases.
    Expects the key "release_notes" to exist at the top level.
    Returns: a dict of product short name and versions. For example
    { "cl":  ["3.7.1", "3.7.2"], "netq": ["2.4.0", "3.0.0"] }
    '''
    # Some versions are included in the JSON file that don't have correct licenses
    # This is the list of versions to exclude from processing
    cl_exclude_list = ["3.7.12", "4.1.0", "4.1.1", "4.2.0", "4.3.0", "4.3.1", "4.3.2", "4.4.0", "4.4.1", "4.4.1", "4.4.2", "4.4.3", "4.4.4", "4.4.5", "5.0.1", "5.1.0", "5.2.0", "5.3.0", "5.3.1", "5.4.0", "5.5.0", "5.5.1", "5.6.0"]
    netq_exclude_list = ["4.1.0", "4.2.0", "4.3.0", "4.4.0", "4.5.0", "4.6.0", "4.7.0", "4.8.0"]

    session = requests.Session()
    url = "https://d2whzysjlaya8k.cloudfront.net/release_notes_and_license_list.json"
    response = session.get(url)
    if response.status_code != 200:
        print("Unable to download JSON releases file to determine products and versions for FOSS licenses.")
        print('Received response {} from {}'.format(response.status_code, url))
        exit(1)

    if not "licenses" in response.json():
        print("Unable to find licenses within JSON releases file. JSON dump:")
        print(response.json())
        exit(1)

    licenses = response.json()["licenses"]
    valid_cl_versions = []
    valid_netq_versions = []

    for version in licenses["cl"]:
        if version not in cl_exclude_list:
            valid_cl_versions.append(version)

    for version in licenses["netq"]:
        if version not in netq_exclude_list:
            valid_netq_versions.append(version)

    return {"cl": valid_cl_versions, "netq": valid_netq_versions}


def main():
    '''
    Main function
    '''
    print("Fetching product and version list")
    products = get_products()
    # products = {"netq": ["4.1.0-SNAPSHOT"]}
    cvs_file_list = []

    for product in products:
        for version in products[product]:
            cvs_file_list.append(process_foss_tar(product, version))

        build_foss_license_markdown_files(product, products[product])

    for file in cvs_file_list:
        print(file)
        os.remove(file)

    exit(0)


if __name__ == "__main__":
    main()
