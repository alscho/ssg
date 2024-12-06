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
        node6 = TextNode("Raw text and *italic* and **bold**", TextType.NORMAL)
        node7 = TextNode("`Some code` at the beginning and raw stuff.", TextType.NORMAL)
        node8 = TextNode("**Only bold stuff**", TextType.NORMAL)
        node9 = TextNode("Empty `` code.", TextType.NORMAL)
        node10 = TextNode("Wrong bold ** syntax", TextType.NORMAL)
        node11 = TextNode("Wrong italic * syntax.", TextType.NORMAL)
        node12 = TextNode("Wrong `code` ` syntax.", TextType.NORMAL)
        node13 = TextNode("* Unordered list item 1.", TextType.NORMAL)
        node14 = TextNode("This is BOLD Type.", TextType.BOLD)   
        node15 = TextNode("Really ******BOLD******", TextType.NORMAL)     
        node16 = TextNode("Is this bold**Is this bold**", TextType.NORMAL)     

        old_nodes1 = [node2]
        old_nodes2 = [node3]
        old_nodes3 = [node4]
        old_nodes4 = [node5]
        old_nodes5 = [node6]
        old_nodes6 = [node7]
        old_nodes7 = [node8]
        old_nodes8 = [node9]
        old_nodes9 = [node14]
        old_nodes10 = [node1]
        old_nodes11 = [node1, node2, node3]
        old_nodes12 = [node10]
        old_nodes13 = [node11]
        old_nodes14 = [node12]
        old_nodes15 = [node13]
        old_nodes16 = [node15]
        old_nodes17 = [node16]

        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes1, "**", TextType.BOLD)), [("This is just raw text.", TextType.NORMAL)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes2, "**", TextType.BOLD)), [("Raw text with ", TextType.NORMAL), ("bold content", TextType.BOLD), (" and more stuff.", TextType.NORMAL)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes3, "*", TextType.ITALIC)), [("Raw text and ", TextType.NORMAL), ("italic", TextType.ITALIC), (".", TextType.NORMAL)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes4, "**", TextType.BOLD)), [("Raw text with ", TextType.NORMAL), ("bold content at the end.", TextType.BOLD)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes5, "**", TextType.BOLD)), [("Raw text and *italic* and ", TextType.NORMAL), ("bold", TextType.BOLD)])
        ### test for italic before bold: should remove bold delimiter and give sequence of TextType.ITALIC
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes5, "*", TextType.ITALIC)), [("Raw text and ", TextType.NORMAL), ("italic", TextType.ITALIC), (" and ", TextType.ITALIC), ("bold", TextType.ITALIC)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes6, "`", TextType.CODE)), [("Some code", TextType.CODE), (" at the beginning and raw stuff.", TextType.NORMAL)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes7, "**", TextType.BOLD)), [("Only bold stuff", TextType.BOLD)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes8, "`", TextType.CODE)), [("Empty ", TextType.NORMAL), (" code.", TextType.NORMAL)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes9, "`", TextType.CODE)), [("This is BOLD Type.", TextType.BOLD)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes10, "`", TextType.CODE)), [])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes11, "**", TextType.BOLD)), [("This is just raw text.", TextType.NORMAL), ("Raw text with ", TextType.NORMAL), ("bold content", TextType.BOLD), (" and more stuff.", TextType.NORMAL)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes15, "*", TextType.ITALIC)), [("* Unordered list item 1.", TextType.NORMAL)])
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes16, "**", TextType.BOLD)), [("Really ", TextType.NORMAL), ("BOLD", TextType.BOLD)])
        ### bug with exactly matching strings like "is this bold**is this bold**" --> [(is this bold, TextType.BOLD), (is this bold, TextType.BOLD)]
        self.assertEqual(get_texts_and_texttypes(split_nodes_delimiter(old_nodes17, "**", TextType.BOLD)), [("Is this bold", TextType.BOLD), ("Is this bold", TextType.BOLD)])

        with self.assertRaises(Exception):
            get_texts_and_texttypes(split_nodes_delimiter(old_nodes12, "**", TextType.BOLD))
        with self.assertRaises(Exception):
            get_texts_and_texttypes(split_nodes_delimiter(old_nodes13, "*", TextType.ITALIC))
        with self.assertRaises(Exception):
            get_texts_and_texttypes(split_nodes_delimiter(old_nodes14, "`", TextType.CODE))  