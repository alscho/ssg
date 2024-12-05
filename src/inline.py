from textnode import TextNode, TextType

def split_nodes_delimiter(old_notes, delimiter, text_type):
    new_nodes = []
    for note in old_notes:
        if delimiter in note.text and note.text_type == TextType.NORMAL:
            new_text = ""
            prev_delimiter = False
            for i in range(0, len(note)):
                c = note[i]
                if c == delimiter and not prev_delimiter and len(new_text):
                    new_node = TextNode(new_text, TextType.NORMAL)
                    new_nodes.append(new_node)
                    new_text = ""
                    prev_delimiter = True
                elif c == delimiter and prev_delimiter:
                    new_node = TextNode(new_text, text_type)
                    new_nodes.append(new_node)
                    new_text = ""
                    prev_delimiter = False
                elif i == len(note) - 1 and len(new_text):
                    if prev_delimiter == True:
                        raise Exception(f"invalid markdown syntax: closing '{delimiter}' missing")
                    new_node = TextNode(new_text+c, TextType.NORMAL)
                    new_nodes.append(new_node)
                    #new_text = ""
                    prev_delimiter = False
                else:
                    new_text += c
        else:
            new_nodes.append(note)
    return new_nodes

def get_texts_and_texttypes(text_nodes):
    attributes = []
    for node in text_nodes:
        attributes.append(node.get_text_and_texttype())
    return attributes

                

