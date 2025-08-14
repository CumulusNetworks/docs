import glob
import sys
from markdownify import markdownify

html_files = glob.glob('public' + '/**/*.html', recursive=True)


for file in html_files:

    f = open(file, 'r')
    file_contents = f.read()
    md_output = markdownify(file_contents)
    
    with open(file + ".md", "a") as new_md_file:
        print(md_output, file=new_md_file)