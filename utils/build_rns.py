#!/usr/bin/env python3
'''
This script will pull the collection of release note JSON files.

The script will parse and markdown sanatize the JSON.

And write markdown files for hugo to render into the respective product and version directories.

This will also write the XML files that are used to generate xls files for the release notes.
'''

from operator import itemgetter
import re
import requests
from distutils.version import LooseVersion

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

def rn_location(product, version):
    '''
    Deals with the fact sometimes we move the location of RNs.
    All the exception cases of what product+version for the rn file location should live here.

    Takes in a product_string() and version_string()

    Returns:
    string path of rn file location
    '''
    directory = get_hugo_folder(product, version)

    # NetQ moved the location of the RN file in 3.2 and later.
    if product == "netq" and version_string(version) in ["2.4", "3.0", "3.1"]:
        return "content/{}/More-Documents/rn.md".format(directory)
    else:
        return "content/{}/Whats-New/rn.md".format(directory)

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

def add_code_markdown(input_string, tag_to_replace):
    '''
    Replaces a generic tag with a <pre></pre> code block.
    This should be used for matching tags that do not indicate an open or close.

    For example:
    {noformat}
    this is some code
    {noformat}

    The requirement of a pair prevents a simple string.replace()

    Inputs:
        input_string - The string to search and replace on
        tag_to_replace - String representation of what to replace (e.g., "{noformat}")
    Returns:
        Updated string with the given tag replaced with open/closing <pre> tags
    '''
    matches = re.finditer(tag_to_replace, input_string)

    close_noformat = False
    for match in matches:
        if close_noformat:
            tag = "</pre>"
            close_noformat = False
        else:
            tag = "<pre>"
            close_noformat = True

        input_string = input_string.replace(tag_to_replace, tag, 1)

    return input_string

def sanatize_rn_for_markdown(string):
    '''
    Strip any special or problematic characters from the a string.
    This (generally) will be used on the release note text to strip characters that break markdown.

    string - The string to sanatize
    '''

    # # Remove HTML tags
    output_string = string.replace("<p>", "")
    output_string = output_string.replace("</p>", "")

    output_string = output_string.replace("`", "'")

    # Fix code blocks
    output_string = add_code_markdown(output_string, "{noformat}")
    output_string = add_code_markdown(output_string, "{code}")

    # Replace and clean up line returns
    output_string = output_string.replace("\r\n", "<br />")
    output_string = output_string.replace("\n ", "<br />")
    output_string = output_string.replace(".\n", "<br />")
    output_string = output_string.replace("\n", "")

    output_string = output_string.replace("&lt;", "<")
    output_string = output_string.replace("&gt;", ">")

    output_string = output_string.replace("<tt>", "`")
    output_string = output_string.replace("</tt>", "`")

    #Replace @ characters to prevent auto email link creation
    output_string = output_string.replace("@", "&#64;")
    output_string = output_string.replace("[", "&#91;")
    output_string = output_string.replace("]", "&#93;")

    #CM-21678
    output_string = output_string.replace('<div class=\"preformatted\" style=\"border-width: 1px;\"><div class=\"preformattedContent panelContent\"><pre>', "<br /><pre>")
    output_string = output_string.replace('<div class=\"code panel\" style=\"border-width: 1px;\"><div class=\"codeContent panelContent\">', '<br /><pre>')
    output_string = output_string.replace('<pre class=\"code-java\">', "")
    output_string = output_string.replace('<span class=\"code-keyword\">', "")
    output_string = output_string.replace("</span>", "")
    output_string = output_string.replace("</pre>\n</div></div>", "</pre><br />")

    # This is later due to other cleanups needing to run first
    output_string = output_string.replace("\r", "")

    # Escape pipe characters
    output_string = output_string.replace("|", "\|")

    # NetQ-5774 Fix. The use of "<>" in a string inside a code (<pre>) block disappears
    output_string = output_string.replace("<ipaddr>", "\<ipaddr\>")

    # NETQ-7489 Fix. Similar to above
    output_string = output_string.replace("<cloud-appliance-IP-address>", "\<cloud-appliance-IP-address\>")
    output_string = output_string.replace("<default/mgmt>", "\<default/mgmt\>")
    output_string = output_string.replace("<customer-premise>", "\<customer-premise\>")
    output_string = output_string.replace("<customer-email-address>", "\<customer-email-address\>")
    output_string = output_string.replace("<password>", "\<password\>")
    output_string = output_string.replace("<opid-here>", "\<opid-here\>")

    # Special Linux command, CM-29033
    output_string = output_string.replace("&amp;&amp;", "&&")

    # Formatting due to JIRA to Redmine migration
    output_string = output_string.replace("{{", "<code>")
    output_string = output_string.replace("}}", "</code>")

    return output_string

def sanatize_rn_for_xls(string):
    '''
    Strip any special or problematic characters from the a string.
    This (generally) will be used on the release note text to strip characters that break markdown.

    string - The string to sanatize
    '''

    # # Remove HTML tags
    # TAG_RE = re.compile(r'<[^>]+>')
    # output_string = TAG_RE.sub('', string)
    output_string = string.replace("<p>", "\015")
    output_string = output_string.replace("</p>", "")
    output_string = output_string.replace("<br>", "\015")
    output_string = output_string.replace("<br />", "\015")

    output_string = output_string.replace("&", "&amp;")
    output_string = output_string.replace("`", "&apos;")
    output_string = output_string.replace("\\<", "&lt;")
    output_string = output_string.replace("\\>", "&gt;")
    output_string = output_string.replace("<", "&lt;")
    output_string = output_string.replace(">", "&gt;")

    output_string = output_string.replace("&lt;tt&gt;", "")
    output_string = output_string.replace("&lt;/tt&gt;", "")

    output_string = output_string.replace("&lt;pre&gt;", "")
    output_string = output_string.replace("&lt;/pre&gt;", "")
    output_string = output_string.replace("&lt;pre class=\"code-java\"&gt;", "")

    output_string = output_string.replace('&lt;div class=\"code panel\" style=\"border-width: 1px;\"&gt;&lt;div class=\"codeContent panelContent\"&gt;', "")
    output_string = output_string.replace('&lt;div class=\"preformatted\" style=\"border-width: 1px;\"&gt;&lt;div class=\"preformattedContent panelContent\"&gt;', "")
    output_string = output_string.replace("&lt;/div&gt;", "")
    output_string = output_string.replace("&lt;span class=\"code-keyword\"&gt;", "")
    output_string = output_string.replace("&lt;/span&gt;", "")

    # NetQ-5774 Fix. The use of "<>" in a string inside a code (<pre>) block disappears
    output_string = output_string.replace("&lt;ipaddr&gt;", "[ipaddr]")

    output_string = output_string.replace("{noformat}", "")
    return output_string

def build_rn_markdown(json_file, version, file_type):
    '''
    Builds a list of lines that contain the entire formatted release notes in markdown table format.

    json_file - the json output to parse and build release notes from
    version - a full version string, i.e., 3.7.11
    product - a product_string() output, i.e., Cumulus Linux
    file_type - one of "affects" or "fixed"
    '''
    output = []

    if file_type == "affects":
        output.append("### Open Issues in {}".format(version))
        output.append("\n")
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
        output.append("\n")
        output.append("|  Issue ID 	|   Description	|   Affects	|   Fixed |")
        output.append("\n")
        output.append("|---	        |---	        |---	    |---	                |")
        output.append("\n")
    else:
        output.append("### Fixed Issues in {}".format(version))
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
        output.append("\n")
        output.append("|  Issue ID 	|   Description	|   Affects	|")
        output.append("\n")
        output.append("|---	        |---	        |---	    |")
        output.append("\n")

    '''
    Generic JSON format is
    {
        "ticket": "2556037",
        "jira_ticket": "CM-33012",
        "affects_versions": [
        "3.7.9-4.2.0"
        ],
        "release_notes_text": "After you add an interface to the bridge, an OSPF session flap can occur.\r\n\r\n"
    }
    '''
    for bug in json_file:
        '''
        With the conversion from Jira to Redmine the JSON file is now inconsistent.
        "ticket" may be a Jira CM or Redmine issue number.
        The filed "jira_ticket" is the Jira CM number, but not every issue has a mapped Jira ticket.
        '''
        if "jira_ticket" in bug and not bug["jira_ticket"] == "":
                issue_id_string = "| <a name=\"" + bug["ticket"] + "\"></a> [" + bug["ticket"] + "](#" + bug["ticket"] + ") <a name=\"" + bug["ticket"] + "\"></a> <br />" + bug["jira_ticket"] + " | "
        else:
            issue_id_string = "| <a name=\"" + bug["ticket"] + "\"></a> [" + bug["ticket"] + "](#" + bug["ticket"] + ") <a name=\"" + bug["ticket"] + "\"></a> <br /> | "

        if file_type == "affects":
            output.append(issue_id_string + sanatize_rn_for_markdown(bug["release_notes_text"]) + " | " + ", ".join(bug["affects_versions"]) + " | " + ", ".join(bug["fixed_versions"]) + "|")
        else:
            output.append(issue_id_string + sanatize_rn_for_markdown(bug["release_notes_text"]) + " | " + ", ".join(bug["affects_versions"]) + " | " + "|")

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
    if product == "Cumulus Linux":
        weight = "-30"
    elif product == "Cumulus NetQ":
        weight = "30"
    output = []

    output.append("---\n")
    output.append("title: NVIDIA {} {} Release Notes\n".format(product, version))
    output.append("author: Cumulus Networks\n")
    output.append("weight: {}\n".format(weight))
    output.append("product: {}\n".format(product))
    output.append("version: \"{}\"\n".format(version))
    output.append("toc: 1\n")
    output.append("type: rn\n")
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

    input_file = rn_location(product, version)

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

def write_rns(output, file_type, product, version):
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

    # DocRaptor requires the file to be an .xml file
    # but calling it xml when we are building xls is confusing
    if file_type == "xls":
        file_type = "xml"
        # this keeps the .xml file at the root of the version.
        # Moving it into the product specific folder makes generating xls much more complicated.
        output_file = "content/{}/rn.{}".format(directory, file_type)

    else:
        output_file = rn_location(product, version)

    with open(output_file, "w+") as out_file:
        for line in output:
            out_file.write(line)


def build_rn_markdown_files(product, version_list):
    '''
    Build the contents of the markdown files for each version's release notes.
    This includes making the call to write the output to a file.

    This takes place for every version provided in version_list.

    product - The product to to generate markdown down. One of ['cl', 'netq']
    version_list - a list of all x.y.z release numbers to build release notes for
    '''
    files = ["affects", "fixed"] # Order matters. This order determines the order rendered on the RN page.

    # Sort the lists based on semver, most recent first.
    # I don't know what this does but that's what Stackoverflow is for
    # https://stackoverflow.com/a/2574090
    #version_list.sort(key=lambda s: list(map(int, s.split('.'))), reverse=True)
    version_list.sort(key=LooseVersion, reverse=True)
    # We need to map major.minors to full release list,
    # { 3.7: [3.7.1, 3.7.2, 3.7.3...]
    major_minor = {}

    for version in version_list:
    #### Temporarily skip NetQ 4.8.0 until Redmine updates complete - Nov 11 2023
    #   if version == "4.6.0":
    #       continue
    #    if version == "4.8.0":
    #        continue
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
        try:
            version_output.extend(read_markdown_header(product, major))
        except FileNotFoundError:
            version_output.extend(build_markdown_header(product_string(product), major))
        hugo_dir = get_hugo_folder(product, major)
        version_output.append("{{{{<rn_xls_link dir=\"{}\" >}}}}\n".format(hugo_dir))


        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            if version == "4.1.2":
                continue
            print("Building markdown for {} {}\n".format(product_string(product), version))
            version_output.append("## {} Release Notes\n".format(version))

            # once for affects, once for fixed.
            for rn_file in files:
                version_output.extend(
                    build_rn_markdown(get_json(product, version, rn_file), version, rn_file))

        # The version_output now contains the RNs for all maintenance releases in order.
        # Write out the markdown file.
        write_rns(version_output, "md", product, version)

def build_rn_xls(json_file, version, file_type):
    '''
    This is a helper function to build_rn_xls_files().

    Given a maintenance version and file type it will generate an HTML table for that single combo.

    json_file - the json output to parse and build release notes from
    version - a full version string, i.e., 3.7.11
    product - a product_string() output, i.e., Cumulus Linux
    file_type - one of "affects" or "fixed"

    Returns: List of strings representing the HTML lines for that release note table.
    '''
    output = []
    if file_type == "affects":
        output.append("<table name=\"Open Issues in {}\">\n".format(version))
    else:
        output.append("<table name=\"Fixed Issues in {}\">\n".format(version))
    output.append("<tr>\n")
    output.append("<th> Issue ID </th>\n")
    output.append("<th> Description </th>\n")
    output.append("<th> Affects </th>\n")
    if file_type == "affects":
        output.append("<th> Fixed </th>\n")
    output.append("</tr>\n")
    for bug in json_file:
        rn_text = sanatize_rn_for_xls(bug["release_notes_text"])
        if bug["affects_versions"]:
            affects_versions = ", ".join(bug["affects_versions"])
        else:
            affects_versions = ""
        if file_type == "affects":
            if bug["fixed_versions"]:
                fixed_versions = ", ".join(bug["fixed_versions"])
            else:
                fixed_versions = ""

        output.append("<tr>\n")
        output.append("<td>{}</td>\n".format(bug["ticket"]))
        output.append("<td>{}</td>\n".format(rn_text))
        output.append("<td>{}</td>\n".format(affects_versions))
        if file_type == "affects":
            output.append("<td>{}</td>\n".format(fixed_versions))
        output.append("</tr>\n")
    output.append("</table>\n")

    return output

def build_rn_xls_files(product, version_list):
    '''
    This works in conjuction with build_rn_xls().

    This is responsible for putting together the entire HTML table.
    This includes putting all maintenance releases into a single table
    and building the tables for both "affects" and "fixed" notes.

    Whereas build_rn_xls() is only responsible for generating a table
    for a single table of (maintenance, [affects | fixed])

    This function will write the final file that can be consumed by DocRaptor to generate the xls file.
    '''
    files = ["affects", "fixed"]

    # Sort the lists based on semver, most recent first.
    # I don't know what this does but that's what Stackoverflow is for
    # https://stackoverflow.com/a/2574090
    #version_list.sort(key=lambda s: list(map(int, s.split('.'))), reverse=True)
    version_list.sort(key=LooseVersion, reverse=True)
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

        all_versions_xls.append("<tables>\n")

        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            print("Building xls for {} {}\n".format(product_string(product), version))

            # once for affects, once for fixed.
            for rn_file in files:
                rn_output = build_rn_xls(get_json(product, version, rn_file), version, rn_file)
                all_versions_xls.extend(rn_output)

        # The one_version_output now contains the RNs for all maintenance releases in order.
        # Write out the markdown file.
        all_versions_xls.append("</tables>")
        write_rns(all_versions_xls, "xls", product, version)

def get_products():
    '''
    Download the engineering provided JSON file detailing the list of products and releases.
    Expects the key "release_notes" to exist at the top level.
    Returns: a dict of product short name and versions. For example
    { "cl":  ["3.7.1", "3.7.2"], "netq": ["2.4.0", "2.4.1", "3.0.0", "3.1.0"] }
    '''
    session = requests.Session()
    url = "https://d2whzysjlaya8k.cloudfront.net/release_notes_and_license_list.json"
    response = session.get(url)
    if response.status_code != 200:
        print("Unable to download JSON releases file to determine products and versions for release notes.")
        print('Received response {} from {}'.format(response.status_code, url))
        exit(1)

    if not "release_notes" in response.json():
        print("Unable to find release notes within JSON releases file. JSON dump:")
        print(response.json())
        exit(1)

    return response.json()["release_notes"]

def main():
    """
    Main function.
    """

    print("Fetching product and version list")
    products = get_products()

    for product in products:
        build_rn_markdown_files(product, products[product])
        build_rn_xls_files(product, products[product])

    exit(0)


if __name__ == "__main__":
    main()
