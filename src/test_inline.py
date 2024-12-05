import unittest

from inline import split_nodes_delimiter, get_texts_and_texttypes

from textnode import TextNode, TextType

class TestInline(unittest.TestCase):
    def test_split_notes_delimiter(self):
        node1 = TextNode("", TextType.NORMAL)
        node2 = TextNode("This is just raw text.", TextType.NORMAL)
        node3 = TextNode("Raw text with **bold content** and more stuff.", TextType.NORMAL)
        node4 = TextNode("Raw text and *italic*.", TextType.NORMAL)
        node5 = TextNode("Raw text with **bold content at the end.**", TextType.NORMAL)
        node6 = TextNode("Raw text and *italic* and **bold**.", TextType.NORMAL)
        node7 = TextNode("`Some code` at the beginning and raw stuff.", TextType.NORMAL)
        node8 = TextNode("**Only bold stuff**", TextType.NORMAL)
        node9 = TextNode("Empty `` code.", TextType.NORMAL)
        node10 = TextNode("Wrong bold ** syntax", TextType.NORMAL)
        node11 = TextNode("Wrong italic * syntax.", TextType.NORMAL)
        node12 = TextNode("Wrong code ` syntax.", TextType.NORMAL)
        node13 = TextNode("* Unordered list item 1.", TextType.NORMAL)
        node14 = TextNode("This is BOLD Type.", TextType.BOLD)        
        
        old_texts1 = [node2, node3]

        self.assertEqual(
            get_texts_and_texttypes(split_nodes_delimiter(old_texts1, "*", TextType.BOLD)), [
                    ("1: This is just raw text.", TextType.NORMAL), 
                    ("2: Raw text with ", TextType.NORMAL), 
                    ("bold content", TextType.BOLD), 
                    ("and more stuff.", TextType.NORMAL)
                ]
            )
    