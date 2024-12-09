import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.NORMAL)
        node6 = TextNode("This is a text node", TextType.NORMAL)
        node7 = TextNode("This is a text node", TextType.BOLD, None)
        node8 = TextNode("This is another text node", TextType.BOLD)
        self.assertEqual(node, node2)        
        self.assertEqual(node3, node4)
        self.assertEqual(node5, node6)
        self.assertEqual(node, node7)
        self.assertNotEqual(node, node8)
        self.assertNotEqual(node, node3)

    def test_text_node_to_html_node(self):
        empty_node_wot = TextNode("", None)
        empty_node_wt = TextNode("", TextType.BOLD)
        n_node = TextNode("normal", TextType.NORMAL)
        b_node = TextNode("bold", TextType.BOLD)
        i_node = TextNode("italic", TextType.ITALIC)
        c_node = TextNode("code", TextType.CODE)
        l_node_wl = TextNode("Visit Google", TextType.LINK, "https://www.google.com")
        l_node_wol = TextNode("Visit nothing", TextType.LINK, "")
        l_node_wn = TextNode("Visit nothing", TextType.LINK)
        f_node_wl = TextNode("an apple", TextType.IMAGE, "https://upload.wikimedia.org/wikipedia/commons/f/f4/Honeycrisp.jpg")
        f_node_wol = TextNode("nothing", TextType.IMAGE, "")
        f_node_wn = TextNode("nothing", TextType.IMAGE)
        
        self.assertEqual(empty_node_wt.text_node_to_html_node().to_html() , "<b></b>")
        self.assertEqual(n_node.text_node_to_html_node().to_html(), "normal")
        self.assertEqual(b_node.text_node_to_html_node().to_html(), "<b>bold</b>")
        self.assertEqual(i_node.text_node_to_html_node().to_html(), "<i>italic</i>")
        self.assertEqual(c_node.text_node_to_html_node().to_html(), "<code>code</code>")
        self.assertEqual(l_node_wl.text_node_to_html_node().to_html(), '<a href="https://www.google.com">Visit Google</a>')
        self.assertEqual(l_node_wol.text_node_to_html_node().to_html(), '<a href="">Visit nothing</a>')
        self.assertEqual(l_node_wn.text_node_to_html_node().to_html(), '<a href="">Visit nothing</a>')
        self.assertEqual(f_node_wl.text_node_to_html_node().to_html(), '<img src="https://upload.wikimedia.org/wikipedia/commons/f/f4/Honeycrisp.jpg" alt="an apple">')
        self.assertEqual(f_node_wol.text_node_to_html_node().to_html(), '<img src="" alt="nothing">')
        self.assertEqual(f_node_wn.text_node_to_html_node().to_html(), '<img src="" alt="nothing">')

        with self.assertRaises(Exception):
            empty_node_wot.text_node_to_html_node()


if __name__ == "__main__":
    unittest.main()