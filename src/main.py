from page import generate_page, generate_page_recursively
from files import replace_dest_with_src_copy

def main():
    copy_src = "static"
    copy_dest = "public"

    replace_dest_with_src_copy(copy_src, copy_dest)

    print("##############################\n")

    single = False

    if single:
        markdown_src = "content/index.md"
        template_src = "template.html"
        html_dest = "public/index.html"

        generate_page(markdown_src, template_src, html_dest)
    
    else:
        markdown_src = "content/"
        template_src = "template.html"
        html_dest = "public/"

        generate_page_recursively(markdown_src, template_src, html_dest)
        
main()