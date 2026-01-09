#!/usr/bin/env python3
'''
Edits html NVIDIA doc pdf HTML files to enable a more user-friendly experience.
'''
from bs4 import BeautifulSoup
import sys
import os
from os import path
from urllib.parse import urlparse

def rewrite_urls(soup, product):
    """
    Modifies links that point into the product content, but ONLY if they
    contain a non-empty fragment (#something). External links and links
    without fragments are left untouched.

    soup - BeautifulSoup object to modify
    product - Product string, e.g., "cumulus-linux-42"

    Returns a modified BeautifulSoup object
    """
    for link in soup.find_all("a", href=True):
        href = link["href"].strip()

        # Skip obvious external or special schemes
        if href.startswith(("http://", "https://", "mailto:", "tel:")):
            continue

        parsed = urlparse(href)

        # Only touch links that target the product path
        if product not in parsed.path:
            continue

        # Only rewrite when there is a NON-empty fragment (i.e., #something)
        # urlparse puts the fragment (text after "#") in parsed.fragment
        if not parsed.fragment:
            # This covers cases like "...#", or no "#" at all => skip
            continue

        # Rewrite to a local anchor: "#fragment"
        link["href"] = f"#{parsed.fragment}"

    return soup

def expand_details(soup):
    '''
    Expands all "summary" sections of an HTML page

    soup - BeautifulSoup object to modify

    Returns BeautifulSoup object
    '''
    for div in soup.find_all("div", {"class": "expand-content"}):
        div["style"] = ""

    return soup

def get_folder_list(hugo_dir):
    '''
    Get a list of generated Hugo folders that have a pdf file to modify.
    Assumes that Hugo docs are built into public/networking-ethernet-software

    Returns a list of paths rooted at the repo url
    '''
    path_list = []
    for folder in os.listdir(hugo_dir):
        if path.exists(hugo_dir + folder + "/pdf/index.html"):
            path_list.append(hugo_dir + folder + "/pdf/index.html")

    return path_list

def get_product(path):
    '''
    Determine the product component of a path to a PDF HTML page.

    path - the string path to the PDF file.

    Returns a string of just the component.
    '''
    start_index = len(path)
    path = path[start_index:path.find("/pdf")]

    return path

def main():
    """
    Main function to modify static HTML files
    """

    if len(sys.argv) < 2:
        hugo_dir = "public/networking-ethernet-software/"
    else:
        # Deal with the user not adding an ending "/"
        if sys.argv[1].endswith("/"):
            hugo_dir = sys.argv[1]
        else:
            hugo_dir = sys.argv[1] + "/"

    if not os.path.exists(hugo_dir):
        print("Unable to locate local directory " + hugo_dir)
        exit(1)

    for path in get_folder_list(hugo_dir):
        with open(path, "r") as in_file:
            soup = BeautifulSoup(in_file, 'html.parser')

        product = get_product(path)
        print("Modifying " + path)
        soup = rewrite_urls(soup, product)
        soup = expand_details(soup)

        with open(path, "w") as in_file:
            in_file.write(str(soup))

if __name__ == "__main__":
    main()



