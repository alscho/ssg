import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_props_to_html1(self):
        children = ["child1", "child2", "child3"]
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("p", "this is content", children, props)
        html_props = node.props_to_html()
        self.assertEqual(html_props, ' href="https://www.google.com" target="_blank"')

    def test_props_to_html2(self):
        children = ["child1", "child2", "child3"]
        props = {}
        node = HTMLNode("p", "this is content", children, props)
        html_props = node.props_to_html()
        self.assertEqual(html_props, "")

    def test_props_to_html3(self):      
        node = HTMLNode()
        html_props = node.props_to_html()
        self.assertEqual(html_props, "")

class TestLeafNode(unittest.TestCase):
    def test_children(self):
        node = LeafNode("p", "value", {"href": "https://www.google.com"})
        self.assertEqual(node.children, None)

    def test_to_html(self):
        node1 = LeafNode("b", "bold test")
        node2 = LeafNode(None, "this is raw text")
        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node4 = LeafNode("p", None)
        self.assertEqual(node1.to_html(), "<b>bold test</b>")
        self.assertEqual(node2.to_html(), "this is raw text")
        self.assertEqual(node3.to_html(), '<a href="https://www.google.com">Click me!</a>')
        with self.assertRaises(ValueError):
            node4.to_html()       


if __name__ == "__main__":
    unittest.main()