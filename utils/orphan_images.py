#!/usr/bin/env python3
import sys
import os
import pathlib
import typing
import glob
import mmap

def get_all_images():
    directories = ["/Volumes/RAMDisk/static", "/Volumes/RAMDisk/themes"]
    file_types = ["[pP][nN][gG]", "[jJ][pP][gG]", "[sS][vV][gG]", "[gG][iI][fF]"]
    raw_file_set = set()
    file_map = {}
    for type in file_types:
        for directory in directories:
            for file in glob.glob(directory + "/**/*." + type, recursive=True):
                raw_file_set.add(file)

    for file in raw_file_set:
        path_parts = file.split("/")
        # if "baseline" in path_parts[len(path_parts) - 1].lower():
        #     print(file)
        file_map[path_parts[len(path_parts) - 1].lower()] = file

    return file_map

def get_used_images():
    image_names = set()

    for path in glob.glob("/Volumes/RAMDisk/public/**/*.html", recursive=True):
        skip_files = ["pdf/index.html", "foss/index.html", "licenses"]
        skip_file_found = False
        for skip in skip_files:
            if skip in path:
                skip_file_found = True

        if skip_file_found:
            continue

        with open(path, mode="r") as in_file:
            with mmap.mmap(in_file.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:

                for line in iter(mmap_obj.readline, b""):
                    file_types_bytes = [b".jpg", b".jpeg", b".png", b".svg", b".gif"]
                    file_types_str = [".jpg", ".jpeg", ".png", ".svg", ".gif"]

                    # My parsing is bad. Some of the filenames end in extra junk
                    # It's easier to keep a list of known junk rather than improve the parser
                    bad_stuff = [");", "&quot;", "')><", ");"]

                    # Does the string contain any of our filetypes (in bytes)?
                    if any(x in line.lower() for x in file_types_bytes):
                        # Skip the icons. files
                        if line.find(b"icons.cumulusnetworks") != -1:
                            continue

                        # decode the line and split the words
                        for word in line.decode("utf-8").split():

                            # Does the word contain our filetypes (as string)?
                            if any(x in word.lower() for x in file_types_str):
                                # Split the word based on file path
                                split_word = word.split("/")

                                # Look at each part of the file path
                                for part in split_word:
                                    # See if this part of the path has our filetype in it
                                    if any(x in part for x in file_types_str):
                                        # Remove quotes
                                        temp_string = part.replace("\"", "")

                                        # Remove known junk
                                        for bad_string in bad_stuff:
                                            temp_string = temp_string.replace(bad_string, "")
                                        image_names.add(temp_string.lower())
    return image_names

def main():
    all_images = get_all_images()
    used_images = get_used_images()
    all_image_names = set(all_images.keys())


    print(len(used_images))
    print(len(all_images))

    max_length = 30
    for k in all_images.keys():
        if len(k) > max_length:
            max_length = len(k)

    for image in used_images:
        # print(image)
        # Confirm that all used_images were found locally
        if image not in all_images:
            print("Couldn't find {}".format(image))

        all_image_names.remove(image)

    index = len("/Volumes/RAMDisk/")
    for image in all_image_names:
        #print("{} {}".format(image.ljust(max_length), all_images[image]))
        print("Deleting {}".format(all_images[image][index:]))
        os.unlink(all_images[image][index:])


    # used_images = set()

    # directory = "./public/"
    # png = directory + "/**/*.png"
    # jpg = directory + "/**/*.jpg"
    # svg = directory + "/**/*.svg"
    # types = [png, jpg, svg]
    # files = []
    # file_map = {}
    # for type in types:
    #     for file in glob.glob(type, recursive=True):
    #         path = file.split("/")
    #         files.append(path[len(path) - 1])
    #         file_map[path[len(path) - 1]] = file
    # all_images = set(files)

    # for path in glob.glob("public/**/*.html", recursive=True):
    #     if "pdf/index.html" in path:
    #         continue
    #     with open(path, "r") as in_file:
    #         soup = BeautifulSoup(in_file, 'html.parser')

    #         for link in soup.find_all("img"):
    #             if not link.get("src"):
    #                 continue
    #             path = link.get("src").split("/")
    #             used_images.add(path[len(path) - 1])

    # unused_images = all_images.difference(used_images)


    # content_types = ["./content/**/*.png", "./content/**/*.jpg", "./content/**/*.svg"]
    # content_files = []
    # content_file_map = {}
    # for type in content_types:
    #     for file in glob.glob(type, recursive=True):
    #         path = file.split("/")
    #         content_files.append(path[len(path) - 1])
    #         content_file_map[path[len(path) - 1]] = file

    # for image in unused_images:
    #     if image not in content_file_map:
    #         print("Couldn't find {}".format(image))
    #         continue
    #     print("Deleting {}".format(content_file_map[image]))
    #     os.unlink(content_file_map[image])

    # #print(used_images.difference(all_images))
    # print("")
    # print("{} used images".format(len(used_images)))
    # print("{} images total".format(len(all_images)))


if __name__ == "__main__":
    main()
