from inline import text_to_textnodes
from blocks import markdown_to_blocks, block_to_block_type
from textnode import TextNode, TextType
from htmlnode import ParentNode

def markdown_to_html_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_block_node(block, block_type)
        block_nodes.append(block_node)
    div_node = ParentNode("div", block_nodes)
    return div_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            header_type = get_header_type(block)
            if header_type == "h1":
                return get_header_text(block)
    raise Exception("no title (header 1 in md syntax) found")

def text_to_children(text):
    leaf_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        leaf_node = text_node.text_node_to_html_node()
        leaf_nodes.append(leaf_node)
    return leaf_nodes

def get_header_type(block):
    parts = block.split(" ", 1)
    return "h"+str(len(parts[0]))

def get_header_text(block):
    parts = block.split(" ", 1)
    return parts[1]

def list_block_to_block_nodes(block, tag):
    list_nodes = []
    lines = block.split("\n")
    for line in lines:
        ### removes list syntax
        temp = line.split(" ", 1)
        text = temp[1]

        leaf_nodes = text_to_children(text)

        list_node = ParentNode("li", leaf_nodes)

        list_nodes.append(list_node)
    block_node = ParentNode(tag, list_nodes)
    return block_node
        

def block_to_block_node(block, block_type):
    match(block_type):
        case ("paragraph"):
            leaf_nodes = text_to_children(block)
            return ParentNode("p", leaf_nodes)
        case ("heading"):
            header_type = get_header_type(block)
            header_content = get_header_text(block)
            leaf_nodes = text_to_children(header_content)
            return ParentNode(header_type, leaf_nodes)
        case ("code"):
            ### misnomer it stips the string up until the first space (inclusive) from the left
            leaf_nodes = text_to_children(block)
            return ParentNode("code", leaf_nodes)
        case ("quote"):
            text = get_header_text(block)
            leaf_nodes = text_to_children(text)
            return ParentNode("blockquote", leaf_nodes)
        case ("unordered_list"):
            return list_block_to_block_nodes(block, "ul")
            #block_node = ParentNode("ul", list_nodes)
        case ("ordered_list"):
            return list_block_to_block_nodes(block, "ol")
            #block_node = ParentNode("ol", list_nodes)
        case _:
            raise Exception("no valid block_type")

    
