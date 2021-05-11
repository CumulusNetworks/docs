#!/usr/bin/env python3
from bs4 import BeautifulSoup

pdf_file = "public/networking-ethernet-software/cumulus-linux-43/pdf/index.html"

def rewrite_urls(soup):
    for link in soup.find_all("a"):
        href = link.get("href")

        if not href:
            continue

        path_parts = href.split("/")

        if len(path_parts) < 2:
            continue

        product = "cumulus-linux-43"

        if product not in path_parts:
            continue

        if path_parts[len(path_parts) - 1] == "#":
            anchor = "#" + path_parts[len(path_parts) - 2]
        else:
            anchor = path_parts[len(path_parts) - 1]

        link["href"] = anchor

    return soup

def expand_details(soup):
    for div in soup.find_all("div", {"class": "expand-content"}):
        div["style"] = ""

    return soup

def write_soup(soup):
    with open(pdf_file, "w") as in_file:
        in_file.write(str(soup))

def main():
    """
    Main function.

    Pass in a list of directories to check as command line arguments.
    """

    with open(pdf_file, "r") as in_file:
        soup = BeautifulSoup(in_file, 'html.parser')

    print("Rewriting URLs")
    soup = rewrite_urls(soup)
    print("Expanding Details")
    soup = expand_details(soup)
    write_soup(soup)

if __name__ == "__main__":
    main()



