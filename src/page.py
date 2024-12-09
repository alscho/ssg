import os
from markdown import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):

    ##### hardcoded
    placeholders = {"title": "{{ Title }}", "content": "{{ Content }}"}
    html_name = "index.html"
    #####

    html_path = os.path.join(dest_path, html_name)

    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
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

    os.makedirs(dest_path, exist_ok = True)

    print(f"Created destination filepath if neccesary.")

    with open(html_path, "w+") as f:
        f.write(html_page)
    
    print(f"Page '{html_page}' created from '{from_path}' using '{template_path}'.\n")

def read_savely(path):
    with open(path) as f:
        return f.read()

