import glob
import sys
from markdownify import markdownify

html_files = glob.glob('public' + '/**/*.html', recursive=True)


for file in html_files:

    f = open(file, 'r')
    file_contents = f.read()
    md_output = markdownify(file_contents)

    edited_markdown=md_output.replace('](https://stu-stage.d30wkbbasyrvu1.amplifyapp.com', '](https://docs.nvidia.com').replace('](/networking-ethernet-software', '](https://docs.nvidia.com')
    
    with open(file + ".md", "a") as new_md_file:
        print(edited_markdown, file=new_md_file)