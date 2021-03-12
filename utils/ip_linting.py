#!/usr/bin/env python3
import ipaddress
import re
import glob
import os
import sys

DEBUG = False


def check_ipv4(line):
    '''
    Look at a string and see if an IPv4 address exists, and if so, validate it.

    Using IPAddress.is_private is a much larger net than just doc prefixes,
    but we'll live for simplicity's sake. Valid "is_private" addresses:
    https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml

    Returns:
        String of the error if one exists
    '''
    for m in re.finditer(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line):
        try:
            ip = ipaddress.IPv4Address(m.group())
            if not (ip.is_multicast or ip.is_private):
                return "{} is not a private or documentation prefix. Contributing guidelines: https://docs.cumulusnetworks.com/contributor-guide/Resources/Writing-Guidelines/#ip-addresses".format(ip)
        except:
            return "{} is an invalid IPv4 Address".format(m.group())
    return

def v6_regex_exceptions(line):
    # mac_address has the format <hex><hex>:<hex><hex>:<hex><hex>:<hex><hex>:<hex><hex>:<hex><hex>
    # example: 44:38:39:00:00:04
    mac_address = r"[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]"

    # v6 linklocal has the format fe80::<hex><hex><hex><hex>:<hex><hex><hex><hex>:<hex><hex><hex><hex>:<hex><hex><hex><hex>
    # example: fe80::4638:39ff:fe00:4
    v6_lla = r"[fe80\:\:[0-9a-f]{1,4}\:[0-9a-f]{1,4}\:[0-9a-f]{1,4}\:[0-9a-f]{1,4}\:"

    # timestamps have the format of a 24h clock (<0-24>:<0-59>:<0-59>)
    # example: 01:02:36
    timestamp = r"([0-1][0-9]|2[0-4])\:[0-5][0-9]\:[0-5][0-9]"

    # syslog messages have the format Dec 15 01:02:36
    # example: Dec 15 01:02:36
    syslog = r"\w\w\w \d{1,2} ([0-1][0-9]|2[0-4])\:[0-5][0-9]\:[0-5][0-9]"

    if re.search(mac_address, line):
        return True
    if re.search(v6_lla, line, re.IGNORECASE):
        return True
    if re.search(timestamp, line, re.IGNORECASE):
        return True
    if re.search(syslog, line, re.IGNORECASE):
        return True

    return False
def check_ipv6(line):
    '''
    Look at a string and see if an IPv6 address exists, and if so, validate it.

    Returns:
        String of the error if one exists
    '''

    # Trying to match a v6 address contained in a string via regex is not easy.
    # As a result we are doing some fast and loose matching. It is entirely possible
    # some false positives slip past, but this is better than nothing.


    # regex on v6 is terrible. nothing is reliable.
    # instead be sloppy and look for <1-4 hex>:<1-4 hex> OR <1-4 hex>::
    # take that match and let the ipaddress module do the heavy lifting.
    v6_regex = r"[0-9a-f]{1,4}\:[0-9a-f]{1,4}\:|[0-9a-f]{1,4}\:\:"

    for m in re.finditer(v6_regex, line.lower()):
        # We think we have a v6 address in the string, but there are a number of corner cases we need to validate
        if v6_regex_exceptions(line):
            return
        try:
            ip = ipaddress.IPv6Address(m.group())
            if not (ip.is_multicast or ip.is_private):
                return "{} is not a private or documentation prefix. Contributing guidelines: https://docs.cumulusnetworks.com/contributor-guide/Resources/Writing-Guidelines/#ip-addresses".format(ip)
        except:
            # Becuase of how the regex match works we may have only "2001:db8" to build an address from.
            # this triggers an exception.
            # Check if we have something that smells like a doc prefix, if yes, move on.
            # If no, then maybe it's an actual error
            if m.group() == "2001:db8:" or m.group() == "2001:0db8:":
                return
            return "{} does not appear to contain a private or documentation prefix.".format(line)
    return

def main():
    """
    Main function.
    """
    skip_files = ["weights", "pdf", "foss", "rn"]

    if DEBUG:
        print("Fetching markdown files")
    for md_file in glob.glob("./content/cumulus-linux-43/**/*.md", recursive=True):
    # for md_file in glob.glob("./content/cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/_index.md"):
        if DEBUG:
            print("file: {}".format(md_file))
        if os.path.split(md_file)[1][:-3] in skip_files:
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

    sys.exit(1)


if __name__ == "__main__":
    main()


