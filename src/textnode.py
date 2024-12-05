from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def text_node_to_html_node(text_node):
        match (text_node.text_type):
            case (TextType.NORMAL):
                text_node = LeafNode(None, text_node.text)
                return text_node
            case (TextType.BOLD):
                text_node = LeafNode("b", text_node.text)
                return text_node
            case (TextType.ITALIC):
                text_node = LeafNode("i", text_node.text)
                return text_node
            case (TextType.CODE):
                text_node = LeafNode("code", text_node.text)
                return text_node
            case (TextType.LINK):
                if text_node.url == None:
                    props = {"href": ""}
                else:
                    props = {"href": text_node.url}
                text_node = LeafNode("a", text_node.text, props)
                return text_node
            case (TextType.IMAGE):
                if text_node.url == None:
                    props = {"src": "", "alt": text_node.text}
                else:
                    props = {"src": text_node.url, "alt": text_node.text}
                text_node = LeafNode("img", "", props)
                return text_node
            case _:
                raise Exception("no valid text type")


    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"