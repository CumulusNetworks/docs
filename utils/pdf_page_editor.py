#!/usr/bin/env python3
from bs4 import BeautifulSoup
# import string
# import random

# global global_name_list
# global_name_list = set()

def rewrite_urls(soup):
    for link in soup.find_all("a"):
        href = link.get("href")

        if not href:
            continue

        path_parts = href.split("/")

        if len(path_parts) < 2:
            continue

        if path_parts[1] != "cumulus-linux-43":
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
    with open("public/networking-ethernet-software/cumulus-linux-43/pdf/index.html", "w") as in_file:
        in_file.write(str(soup))

# def generate_name():
#     # Generate a random tab name
#     new_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

#     # Ensure that tab names are globally unique
#     while new_name in global_name_list:
#         new_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

#     global_name_list.add(new_name)

#     return new_name


# def fix_tabs(soup):
#     tabs_to_books = BeautifulSoup("", "html.parser")

#     for book in soup.find_all("div", {"class": "book-tabs"}):
#         tab_labels = book.find_all("label")

#         for label in tab_labels:
#             new_book = BeautifulSoup("<div></div>", "html.parser")
#             new_book.div["class"] = "book-tabs"
#             tab = book.find_all(id=label["id"])

#             if not tab:
#                 continue

#             # tab[0] is <input>
#             # tab[1] is <label>
#             # tab[2] is <div class="book-tabs-content markdown-inner">
#             new_name = generate_name()
#             tab[0]["checked"] = "checked"
#             tab[0]["class"] = "hidden"
#             tab[0]["id"] = new_name
#             tab[0]["name"] = new_name
#             tab[0]["type"] = "radio"

#             tab[1]["for"] = new_name
#             tab[1]["name"] = new_name
#             tab[1]["id"] = new_name

#             tab[2]["id"] = new_name
#             # Check if there are books nested inside
#             child_tabs = tab[2].find_all("div", {"class": "book-tabs"})
#             if child_tabs:
#                 tab[2].div.insert(1,fix_tabs(tab[2]))

#             # Wrap the tab in a <div>
#             new_book.div.extend(tab)

#             #Place that div into the holder for the entire set
#             tabs_to_books.append(new_book)



#     return tabs_to_books

def main():
    """
    Main function.

    Pass in a list of directories to check as command line arguments.
    """

    with open("public/networking-ethernet-software/cumulus-linux-43/pdf/index.html", "r") as in_file:
        soup = BeautifulSoup(in_file, 'html.parser')

    # soup = fix_tabs(soup)
    # print(soup)
    soup = rewrite_urls(soup)
    soup = expand_details(soup)
    write_soup(soup)

if __name__ == "__main__":
    main()



