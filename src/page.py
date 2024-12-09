import os
import re
from markdown import markdown_to_html_node, extract_title

def generate_page_recursively(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        content_path = os.path.join(dir_path_content, content)
        #print(f"content_path: {content_path}")
        if os.path.isfile(content_path):
            #print(f"content_path: {content_path}")
            dest_path = str(os.path.join(dest_dir_path, content))
            dest_path = dest_path.replace(".md", ".html")
            #print(f"dest_path: {dest_path}")
            generate_page(content_path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_dir_path, content)
            generate_page_recursively(content_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):

    ##### hardcoded
    placeholders = {"title": "{{ Title }}", "content": "{{ Content }}"}
    #html_name = "index.html"
    #####

    #html_path = os.path.join(dest_path, html_name)

    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'.")
    
    from_file = read_savely(from_path)
    template_file = read_savely(template_path)
    
    print(f"Read in source and template.")

    html_content = markdown_to_html_node(from_file).to_html()
    html_title = extract_title(from_file)

    ### not pretty, but works. .replace() had issues
    temp1 = template_file.split(placeholders["title"])
    html_page = temp1[0]+html_title+temp1[1]
    temp2 = html_page.split(placeholders["content"])
    html_page = temp2[0]+html_content+temp2[1]

    print(f"Created *.html")

    ### not pretty, but works - drops the file name from dest_path
    temp3 = dest_path.rsplit("/", 1)
    dest_dir = temp3[0]
    #print(f"dest_dir: {dest_dir}")
    os.makedirs(dest_dir, exist_ok = True)

    print(f"Created destination filepath if neccesary.")

    with open(dest_path, "w+") as f:
        f.write(html_page)
    
    print(f"Page '{dest_path}' created from '{from_path}' using '{template_path}'.\n")

def read_savely(path):
    with open(path) as f:
        return f.read()

