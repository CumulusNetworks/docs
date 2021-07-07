#!/usr/bin/env python3
'''
This script will use the DocRaptor (www.docraptor.com) API to generate the PDFs of the user docs.

This is done by passing specific URLs to DocRaptor to download and render.
Because of this, we must run the PDF creation _after_ we deploy the updated changes.

This script is also responsible for building .xls files of all the release notes using the same docraptor API.
'''

import sys
import time
import os
import os.path
import errno
import docraptor

# Are we generating test or production PDFs?
TEST = False

# Validate that the amplify CLI is passing the right parameters
if len(sys.argv) != 5:
    print("Please provide arguments in the following order <DOCRAPTOR_API_KEY> <BASE_URL> <HTTP_AUTH_NAME> <HTTP_AUTH_PASS>.")
    print(F"Received {len(sys.argv)} arguments: {sys.argv}")
    exit(1)

# build_pdfs.py <DOCRAPTOR_API_KEY> <BASE_URL> <HTTP_AUTH_NAME> <HTTP_AUTH_PASS>
token = sys.argv[1]
# Deal with the user adding and ending URL slash or not. Don't make them remember.
if sys.argv[2].endswith("/"):
    base_url = sys.argv[2]
else:
    base_url = sys.argv[2] + "/"
http_user = sys.argv[3]
http_pass = sys.argv[4]
doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = str(token)

# Taken from https://stackoverflow.com/a/600612/119527
def mkdir_p(path):
    '''
    Generate a given path with all required parent folder
    '''
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def safe_open_w(path):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    mkdir_p(os.path.dirname(path))
    return open(path, 'wb')

def request_pdf(product):
    '''
    Make the HTTP request to build the PDF.

    product - one of "Linux" or "NetQ".

    Returns:
    Doc Raptor API "AsyncDoc" object
    '''
    # Based on API example: https://github.com/DocRaptor/docraptor-python/blob/master/examples/async.py
    # This _must_ be an async request. The filesizes of CL and NetQ are unlikely return before timeout.
    print("Sending Cumulus {} PDF creation request".format(product))
    pdf_request = doc_api.create_async_doc({
        "document_url": base_url + "{}/pdf/".format(product.lower()),
        "document_type": "pdf",
        "test": TEST,
        "javascript": True,
        "prince_options": {
            "http_user": http_user,
            "http_password": http_pass
        }
    })

    return pdf_request

def get_dir_list():
    '''
    Get a list of directories to place PDF content into.
    This ignores all CL versions before 37 and all netq versions before 24

    Returns a list of directory names, assuming the "content" folder as a parent
    '''
    full_dir_list = os.listdir('content')
    old_releases = ["cumulus-linux-37", "cumulus-netq-24"]  # Older versions that have a single release we care about
    return_dirs = []
    for directory in full_dir_list:
        if directory in old_releases:
            return_dirs.append(directory)
        else:
            split_dir = directory.split("-")
            if len(split_dir) == 3:
                if split_dir[1] == "linux" and split_dir[2][0] == "4":
                    return_dirs.append(directory)
                elif split_dir[1] == "netq" and split_dir[2][0] == "3":
                    return_dirs.append(directory)

    return return_dirs

def get_xls_files():
    '''
    Generate XLS files from docraptor.
    The process is simpler than PDF process so it is a self-contained method that directly downloads and writes the xls files.
    '''
    dir_list = get_dir_list()
    for directory in dir_list:
        for file in os.listdir("content/" + directory):
            if file.endswith(".xml"):
                print("Converting {}/rn.xml to xls".format(directory))
                create_response = doc_api.create_doc({
                    "test": TEST,                                                   # test documents are free but watermarked
                    "document_url": "{}{}/{}".format(base_url, directory, file),
                    "name": "{}-{}".format(directory, file),                        # help you find a document later
                    "document_type": "xls",                                         # pdf or xls or xlsx
                    "prince_options": {
                        "http_user": http_user,
                        "http_password": http_pass
                    }
                })
                xls_file = file.replace(".xml", ".xls")
                destination_file = "content/{}/{}".format(directory, xls_file)
                print("Writing {} to {}\n".format(file, destination_file))
                file = open(destination_file, "wb")
                file.write(create_response)
                file.close
try:

    # dir_list = get_dir_list()
    # pdf_requests = {}

    # # Get the list of directories we need to build PDFs for
    # # map each directory to docraptor request object
    # for directory in dir_list:
    #     pdf_requests[directory] = request_pdf(directory)

    # Request and download the XLS files
    print("Downloading XLS files...")
    get_xls_files()

    # print("Checking PDF status...", end="")
    # # It takes some time to gerate the pdf files, so loop forever
    # while True:

    #     for directory in dir_list:
    #         status = doc_api.get_async_doc_status(pdf_requests[directory].status_id)

    #         if status.status == "failed":
    #             print("\n{} PDF creation failed. Error response:".format(directory))
    #             print(status)
    #             exit(1)

    #         elif status.status == "completed":
    #             print("\nPDF generation for {} completed, downloading.\n".format(directory))
    #             doc_response = doc_api.get_async_doc(status.download_id)

    #             # write the file to the version folder, for example
    #             # content/cumulus-linux-37/cumulus-linux-37.pdf
    #             download_dir = "content/{}/{}.pdf".format(directory, directory)

    #             with safe_open_w(download_dir) as f:
    #                 f.write(doc_response)
    #             print("PDF written to {}".format(download_dir))

    #             # Now that we have the PDF of that release, remove it from the directory list
    #             dir_list.remove(directory)

    #             # If there are no directories left in the list then we have all the PDFs
    #             if len(dir_list) == 0:
    #                 print("All PDFs generated. Exiting")
    #                 exit(0)
    #             else:
    #                 print("Still waiting on PDFs {}.\n".format(", ".join(dir_list)))

    #         else:
    #             print(".", end="")
    #             #Flush the stdout buffer to print growing "..." for waiting message
    #             sys.stdout.flush()
    #     time.sleep(1)

except docraptor.rest.ApiException as error:
    print(error)
    exit(1)
