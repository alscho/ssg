from page import generate_page
from files import replace_dest_with_src_copy

def main():
    copy_src = "static"
    copy_dest = "public"

    markdown_src = "content/index.md"
    template_src = "template.html"
    html_dest = "public"

    replace_dest_with_src_copy(copy_src, copy_dest)

    generate_page(markdown_src, template_src, html_dest)

main()