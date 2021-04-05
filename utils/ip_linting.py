#!/usr/bin/env python3
'''
This script attempts to validate IPv4 and IPv6 addresses and ensure they are private or multicast addresses.

The checks can be disabled in a file by using <!-- vale off --> and <!-- vale on --> flags
'''
import glob
import ipaddress
import os
import re
import sys

DEBUG = False

def check_ipv4(line):
    '''
    Given a string, validate if an IPv4 address exists, and if so, validate it.

    Using IPAddress.is_private is a much larger net than just doc prefixes,
    but we'll live for simplicity's sake. Valid "is_private" addresses:
    https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml

    Returns:
        String of the error if one exists
    '''
    # Use regex to find potential IPv4 addresses and let the ipaddress module do the actual validation
    for m in re.finditer(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line):
        try:
            ip = ipaddress.IPv4Address(m.group())
            if not (ip.is_multicast or ip.is_private):
                return "{} is not a private or documentation prefix. Contributing guidelines: https://docs.cumulusnetworks.com/contributor-guide/Resources/Writing-Guidelines/#ip-addresses".format(ip)
        except:
            return "{} is an invalid IPv4 Address".format(m.group())
    return None

def v6_regex_exceptions(line):
    '''
    Compare a given line to a known set of IPv6 address exceptions.

    These are strings that resemble IPv6 addresses, like timestamps (23:22:11) or MAC addresses.

    Returns:
        True if the string contains an IPv6 address exception
        False if it does not
    '''
    # mac_address has the format <hex><hex>:<hex><hex>:<hex><hex>:<hex><hex>:<hex><hex>:<hex><hex>
    # example: 44:38:39:00:00:04
    mac_address = r"[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]"

    # timestamps have the format of a 24h clock (<0-24>:<0-59>:<0-59>)
    # example: 01:02:36
    timestamp = r"([0-1][0-9]|2[0-4])\:[0-5][0-9]\:[0-5][0-9]"

    # syslog messages have the format Dec 15 01:02:36
    # example: Dec 15 01:02:36
    syslog = r"\w\w\w \d{1,2} ([0-1][0-9]|2[0-4])\:[0-5][0-9]\:[0-5][0-9]"

    # The detailed output of "ip -d link show" with a bridge includes a MAC that trims 0s.
    # If the string "bridge_id" is found in the line, skip it.
    # example: vlan_filtering 0 vlan_protocol 802.1Q bridge_id 8000.0:0:0:0:0:0 designated_root 8000.0:0:0:0:0:0
    bridge_detail = "bridge_id"

    # Ebtables will trim 0s off of MAC addresses. Look for something like a mac, but surrounded by the -s or -d and -i or -j flags
    # example: -p ! 802_1Q -s 0:2:0:0:0:2 -i swp2 -j ACCEPT , pcnt = 1 -- bcnt = 421
    ebtables = r"\-[sd] [0-9a-f]{1,2}\:[0-9a-f]{1,2}\:[0-9a-f]{1,2}\:[0-9a-f]{1,2}\:[0-9a-f]{1,2}\:[0-9a-f]{1,2} -[ij]"

    if re.search(mac_address, line):
        return True
    if re.search(timestamp, line, re.IGNORECASE):
        return True
    if re.search(syslog, line, re.IGNORECASE):
        return True
    if line.find(bridge_detail) > 0:
        return True
    if re.search(ebtables, line, re.IGNORECASE):
        return True

    return False

def check_ipv6(line):
    '''
    Look at a string and see if an IPv6 address exists, and if so, validate it.

    Returns:
        String of the error if one exists
    '''

    # regex on v6 is terrible. nothing is reliable.
    # instead be sloppy and look for <1-4 hex>:<1-4 hex> OR <1-4 hex>::
    # take that match and let the ipaddress module do the heavy lifting.
    v6_regex = r"[0-9a-f]{1,4}\:[0-9a-f]{1,4}\:|[0-9a-f]{1,4}\:\:"

    # change the line to lowercase to avoid capital hex characters
    line = line.lower()

    # We we find a candidate IPv6 address based on regex we will capture the start and end index
    # This is to avoid having the regex match a substring of the v6 address accidentally.
    address_index_ranges = []

    # Get all the regex matches in the line.
    for m in re.finditer(v6_regex, line):
        # Get the index of the first character of the v6 address in the string
        address_beginning_index = m.start()

        # Assume we have not determined this is a substring of an already found v6 address
        address_substring = False

        # Look at all the found index ranges and see if this address falls in that range.
        for index_range in address_index_ranges:
            if (index_range[0] <= address_beginning_index) and ( address_beginning_index <= index_range[1]):

                # The address falls within the range of an already identified address. This is a substring and should be ignored.
                address_substring = True

        if address_substring:
            continue

        # Look for the first non-hex and non-":" character and count that as the end of the address
        address_ending = re.search(r"[^0-9a-f\:]", line[m.start():])
        if address_ending:
            # The ending index is starting from the first character of the address, not the first of the line
            # Add the two indexes together to get the character in the line that ends the address
            address_ending_index = address_ending.start() + address_beginning_index
        else:
            # If we don't find the end of the address, use the end of line
            address_ending_index = len(line)

        # We have enough information to slice the line to get just the v6 address out of it
        v6_address = line[address_beginning_index:address_ending_index]
        address_index_ranges.append((address_beginning_index, address_ending_index))

        # # We think we have a v6 address in the string, but there are a number of corner cases we need to validate
        if v6_regex_exceptions(line):
            return

        try:
            ip = ipaddress.IPv6Address(v6_address)
            if not (ip.is_multicast or ip.is_private):
                return "{} is not a private or documentation prefix. Contributing guidelines: https://docs.cumulusnetworks.com/contributor-guide/Resources/Writing-Guidelines/#ip-addresses".format(ip)

        except ipaddress.AddressValueError as error:
            if DEBUG:
                print(line)
            return "{} does not appear to contain a private or documentation prefix. {}".format(v6_address, error)
    return

def check_files(directory, skip_list):
    '''
    Given a glob directory path, look at all the matching files.

    For each file, iterate over all lines in the file checking for valid v4 and v6 addresses.
    Any lines contained within
    <!-- vale off -->
    and
    <!-- vale on -->
    will be ignored.

    Any errors will be printed to stdout.

    Returns:
        True if errors are found
        False if no errors are found
    '''
    errors = []
    for md_file in glob.glob(directory, recursive=True):
        if DEBUG:
            print("file: {}".format(md_file))
        if os.path.split(md_file)[1][:-3] in skip_list:
            if DEBUG:
                print("skipping {}".format(os.path.split(md_file)[1][:-3]))
            continue
        errors = []
        line_num = 1
        check = True
        for line in open(md_file, 'r'):
            line = line.replace('\n', '').replace('\r', '')
            if line.lower() == "draft: true":
                break
            if line.lower().replace(' ', '') == "<!--valeoff-->":
                check = False
                line_num = line_num + 1
                continue
            if line.lower().replace(' ', '') == "<!--valeon-->":
                check = True
                line_num = line_num + 1
                continue
            if check:
                error_msg_v4 = check_ipv6(line)
                error_msg_v6 = check_ipv4(line)
                if error_msg_v6:
                    errors.append({line_num: error_msg_v6})
                if error_msg_v4:
                    errors.append({line_num: error_msg_v4})
            line_num = line_num + 1
        if errors:
            print("\033[4m{}\033[0m".format(md_file))
            for error in errors:
                for line_num, message in error.items():
                    print("{:<10d}{:>20s}".format(line_num, message))
            print("\n")

    return bool(errors)

def main(argv):
    """
    Main function.

    Pass in a list of directories to check as command line arguments.
    """

    # Validate that the amplify CLI is passing the right parameters
    if len(argv) < 2:
        print("Please provide a list of directories for checking")
        print(F"Received {len(argv)} arguments: {argv}")
        exit(1)

    errors = False
    skip_files = ["weights", "pdf", "foss", "rn"]

    if DEBUG:
        print("Fetching markdown files")

    for arg in argv[1:]:
        dir_string = arg + "/**/*.md"
        if not errors:
            errors = check_files(dir_string, skip_files)
        else:
            check_files(dir_string, skip_files)

    if errors:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
