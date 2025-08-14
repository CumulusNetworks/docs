import glob
import sys
from markdownify import markdownify
from bs4 import BeautifulSoup
import re
from datetime import datetime

url_pattern = re.compile(r'public/(.*?)/index\.html')

html_files = glob.glob('public' + '/**/*.html', recursive=True)

if "--url-replace" in sys.argv:
    amp_url_replace = sys.argv[sys.argv.index("--url-replace") + 1]

for file in html_files:
    url_source = ""
    doc_title = ""
    published_time = "Published Time: " + datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT") + "\n\n"
    

    with open(file, 'r') as f:
        file_contents = f.read()
    

    soup = BeautifulSoup(file_contents, 'html.parser')
    doc_title_tag = soup.find('title')
    
    if doc_title_tag:
        doc_title = "Title: " + doc_title_tag.get_text() + "\n\n"
    

    match = url_pattern.search(file)
    if match:
        relpath = match.group(1)
        url_source = "URL Source: https://docs.nvidia.com/networking-ethernet-software/" + relpath + "/" + "\n\n"


    md_output = markdownify(file_contents)
    edited_markdown = md_output.replace(amp_url_replace, '](https://docs.nvidia.com').replace('](/networking-ethernet-software', '](https://docs.nvidia.com/networking-ethernet-software')
    

    with open(file + ".md", "a") as new_md_file:
        combined_content = doc_title + url_source + published_time + edited_markdown
        new_md_file.write(combined_content)