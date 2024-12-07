import re

from textnode import TextNode, TextType

def extract_markdown_links(text):
    images = []
    to_process = re.findall(r"[^\!]\[.*?\]\(.*?\)", text)
    
    for item in to_process:
        ### strips outer markdown syntax
        item = item[2:-1]
        ### strips inner markdown syntax
        anc, src = item.split("](")
        
        images.append((anc, src))
    return images

def extract_markdown_images(text):
    images = []
    to_process = re.findall(r"\!\[.*?\]\(.*?\)", text)
    
    for item in to_process:
        ### strips outer markdown syntax
        item = item[2:-1]
        ### strips inner markdown syntax
        alt, src = item.split("](")

        images.append((alt, src))
    return images

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        ### don't extract out of other types
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        raw_text = [old_node.text]
        links = extract_markdown_links(raw_text[0])
        ### no links in the node
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        
        ### repeat until all links have been dealt with
        while len(links) > 0:
            ### updates links list for next iteration
            lk = links.pop(0)
            link = f"[{lk[0]}]({lk[1]})"
            ### first element is a text node, second element is the rest of the old_node - to be processed next iteration
            raw_text = raw_text[0].split(link)
            ### raw_text contains leftover string for next iteration 
            node_text = raw_text.pop(0)
            ### removes implicitly all empty NORMAL nodes which .split() produces
            if node_text != "":
                new_node = TextNode(node_text, TextType.NORMAL)
                new_nodes.append(new_node)
            alt, src = lk
            new_node = TextNode(alt, TextType.LINK, src)
            new_nodes.append(new_node)

        ### last bit of string gets added (or omitted if empty)
        node_text = raw_text.pop(0)
        if node_text != "":
            new_node = TextNode(node_text, TextType.NORMAL)
            new_nodes.append(new_node)
    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        ### don't extract out of other types
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        raw_text = [old_node.text]
        images = extract_markdown_images(raw_text[0])
        ### no images in the node
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        ### repeat until all images have been dealt with
        while len(images) > 0:
            ### updates images list for next iteration
            img = images.pop(0)
            image = f"![{img[0]}]({img[1]})"
            ### first element is a text node, second element is the rest of the old_node - to be processed next iteration
            raw_text = raw_text[0].split(image)
            ### raw_text contains leftover string for next iteration 
            node_text = raw_text.pop(0)
            ### removes implicitly all empty NORMAL nodes which .split() produces
            if node_text != "":
                new_node = TextNode(node_text, TextType.NORMAL)
                new_nodes.append(new_node)
            alt, src = img
            new_node = TextNode(alt, TextType.IMAGE, src)
            new_nodes.append(new_node)

        ### last bit of string gets added (or omitted if empty)
        node_text = raw_text.pop(0)
        if node_text != "":
            new_node = TextNode(node_text, TextType.NORMAL)
            new_nodes.append(new_node)
    return new_nodes


### works on list of text LINES
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        
        ### skips entirely empty entries, same effect as adding empty text_type.NORMAL
        if old_node.text == "":
            continue
        ### not NORMAL texts won't be further processed
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        ### checks if old_note is an unordered list item
        if old_node.text[0] == "*" and old_node.text.count("*") == 1:
            new_nodes.append(old_node)
            continue
        ### checks if closing delimiter is missing
        if old_node.text.count(delimiter) % 2 == 1:
            raise Exception(f"invalid markdown syntax: uneven amount of {delimiter}, maybe close it?")
            continue

        ### valid texts to process regularly
        texts = old_node.text.split(f"{delimiter}")
        
        for text in texts:
            ### type 0: empty texts get thrown out
            if text == "":
                continue
            ### type 1: enclosed in delimiter --> text_type
            if f"{delimiter}{text}{delimiter}" in old_node.text:
                new_node = TextNode(text, text_type)
                new_nodes.append(new_node)
            ### type 2: raw text --> TextType.NORMAL
            else:
                new_node = TextNode(text, TextType.NORMAL)
                new_nodes.append(new_node)
    return new_nodes

def get_texts_and_texttypes_and_urls(text_nodes):
    attributes = []
    for node in text_nodes:
        attributes.append(node.get_text_and_texttype_and_url())
    return attributes

def get_texts_and_texttypes(text_nodes):
    attributes = []
    for node in text_nodes:
        attributes.append(node.get_text_and_texttype())
    return attributes

                

