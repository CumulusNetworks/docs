import glob
import sys
from markdownify import markdownify

html_files = glob.glob('public' + '/**/*.html', recursive=True)

if("--url-replace" in sys.argv):
    amp_url_replace = sys.argv[sys.argv.index("--url-replace") + 1]

for file in html_files:

    f = open(file, 'r')
    file_contents = f.read()
    md_output = markdownify(file_contents)

    edited_markdown=md_output.replace(amp_url_replace, '](https://docs.nvidia.com').replace('](/networking-ethernet-software', '](https://docs.nvidia.com/networking-ethernet-software')
    
    with open(file + ".md", "a") as new_md_file:
        print(edited_markdown, file=new_md_file)