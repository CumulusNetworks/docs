#!/usr/bin/env python3
'''
This script will use the DocRaptor (www.docraptor.com) API to generate the PDFs of the user docs.

This is done by passing specific URLs to DocRaptor to download and render. 
Because of this, we must run the PDF creation _after_ we deploy the updated changes.
'''
import requests
import sys
import time
import docraptor
import os, os.path
import errno

TEST = True

if len(sys.argv) != 5:
    print("Please provide arguments in the following order <DOCRAPTOR_API_KEY> <BASE_URL> <HTTP_AUTH_NAME> <HTTP_AUTH_PASS>.")
    print(F"Received {len(sys.argv)} arguments: {sys.argv}" )
    exit(1)

# build_pdfs.py <DOCRAPTOR_API_KEY> <BASE_URL> <HTTP_AUTH_NAME> <HTTP_AUTH_PASS> 
token = sys.argv[1]
base_url = sys.argv[2]
http_user = sys.argv[3]
http_pass = sys.argv[4]
pdf_dir = "static/pdfs"

# this key works for test documents
docraptor.configuration.username = str(token)
# docraptor.configuration.debug = True
doc_api = docraptor.DocApi()

# Taken from https://stackoverflow.com/a/600612/119527
def mkdir_p(path):
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
        "document_url": base_url + "cumulus-{}/pdf/".format(product.lower()),
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
    full_dir_list = os.listdir('content')
    old_releases = ["cumulus-linux-37", "cumulus-netq-24"]  # Older versions that have a single release we care about
    return_dirs = []

    for directory in full_dir_list:
        if directory in old_releases:
            return_dirs.append(directory)
        else:
            split_dir = directory.split("-")
            if len(split_dir) == 3:
                if split_dir[0] == "cumulus" and split_dir[2][0] == "4":
                    return_dirs.append(directory)
                elif split_dir[0] == "netq" and split_dir[3][0] == "3":
                    return_dirs.append(directory)

    return return_dirs

def get_xls_files():
    dir_list = get_dir_list()
    for directory in dir_list:
        for file in os.listdir("content/" + directory):
            if file.endswith(".xml"):
                print("Converting {} to xls".format(file))
                create_response = doc_api.create_doc({
                    "test": TEST,                                                   # test documents are free but watermarked
                    "document_url": "{}{}/{}".format(base_url, directory, file),
                    "name": "{}-{}".format(directory, file),                                 # help you find a document later
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
    netq_request = request_pdf("NetQ")
    cl_request = request_pdf("Linux")
    
    first_loop = True
    download_cl = False
    download_netq = False
    download_xls = False
    
    print("Downloading XLS files...")
    get_xls_files()

    while True:
        if(first_loop):
            print("Checking PDF status...", end="")
        else:
            print(".", end="")
        
        # API calls to create both NetQ and CL docs in parallel
        netq_status_response = doc_api.get_async_doc_status(netq_request.status_id)
        cl_status_response = doc_api.get_async_doc_status(cl_request.status_id)
        
        # If we've already downloaded NetQ but are waiting on CL,
        # Then just skip over the netq checking.
        if not download_netq:
            if netq_status_response.status == "completed":

                print("\nNetQ PDF successfully created. Downloading...")
                doc_response = doc_api.get_async_doc(netq_status_response.download_id)
                with safe_open_w(pdf_dir + "/cumulus-netq.pdf") as f:
                    f.write(doc_response)
                # file = open(pdf_dir + "/cumulus-netq.pdf", "wb")
                # file.write(doc_response)
                # file.close
                print(F"Wrote PDF to {pdf_dir}/cumulus-netq.pdf")
                download_netq = True
                
                # If aren't sure if CL is already done, let's keep waiting.
                if not download_cl:
                    print("Continuing to wait for CL PDF...", end="")
            elif netq_status_response.status == "failed":
                print("\nCL PDF creation failed. Error response:")
                print(netq_status_response)
                exit(1)

        # Just like NetQ, if we have already downloaded CL but are waiting on NetQ
        # Skip all the CL checking.
        if not download_cl:
            if cl_status_response.status == "completed":
                print("\nCumulus Linux PDF successfully created. Downloading...")
                doc_response = doc_api.get_async_doc(cl_status_response.download_id)
                with safe_open_w(pdf_dir + "/cumulus-linux.pdf") as f:
                    f.write(doc_response)
                # file = open(pdf_dir + "/cumulus-linux.pdf", "wb")
                # file.write(doc_response)
                # file.close
                print(F"Wrote PDF to {pdf_dir}/cumulus-linux.pdf")
                download_cl = True

                # If we are not sure that netq is done yet, keep waiting.
                if not download_netq:
                    print("Continuing to wait for NetQ PDF...", end="")
            elif cl_status_response.status == "failed":
                print("\nCL PDF creation failed. Error response:")
                print(cl_status_response)
                exit(1)

        # If we've downloaded both PDFs then let's exit.
        if download_netq and download_cl:
            print("\nBoth PDF files successfully downloaded. Exiting.")
            exit(0)
        else:
            #Flush the stdout buffer to print growing "..." for waiting message
            sys.stdout.flush()
            first_loop = False
            time.sleep(1)

except docraptor.rest.ApiException as error:
    print(error)
    print(error.message)
    print(error.code)
    print(error.response_body)
    exit(1)
