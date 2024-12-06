from textnode import TextNode, TextType

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

    
def get_texts_and_texttypes(text_nodes):
    attributes = []
    for node in text_nodes:
        attributes.append(node.get_text_and_texttype())
    return attributes

                

