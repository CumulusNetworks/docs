import glob
import sys
from markdownify import markdownify
from bs4 import BeautifulSoup
import re
from datetime import datetime

html_files = glob.glob('public' + '/**/*.html', recursive=True)



if("--url-replace" in sys.argv):
    amp_url_replace = sys.argv[sys.argv.index("--url-replace") + 1]

for file in html_files:
    url_source = ""
    doc_title = ""
    published_time = "Published Time: " + datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT") + "\n\n"
    url_relpath = match = re.search(r'public/(.*?)/index\.html', file)
    markdown_content = "Markdown Content: \n"
    if url_relpath:
        relpath = match.group(1)
        url_source = "URL Source: https://docs.nvidia.com/networking-ethernet-software/" + relpath + "/" + "\n\n"

    with open(file) as page:
        soup = BeautifulSoup(page.read())
        doc_title_tag = soup.find('title')
        if doc_title_tag:
            doc_title = "Title: " + doc_title_tag.get_text() + "\n\n"



    f = open(file, 'r')
    file_contents = f.read()
    md_output = markdownify(file_contents)

    edited_markdown=md_output.replace(amp_url_replace, '](https://docs.nvidia.com').replace('](/networking-ethernet-software', '](https://docs.nvidia.com/networking-ethernet-software')
    
    
    with open(file + ".md", "a") as new_md_file:
        print(doc_title + url_source + published_time + edited_markdown, file=new_md_file)
