import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        node5 = LeafNode("img", "", {"src": "https://commons.wikimedia.org/wiki/File:Honeycrisp.jpg", "alt": "an apple"})
        self.assertEqual(node1.to_html(), "<b>bold test</b>")
        self.assertEqual(node2.to_html(), "this is raw text")
        self.assertEqual(node3.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(node5.to_html(), '<img src="https://commons.wikimedia.org/wiki/File:Honeycrisp.jpg" alt="an apple">')
        with self.assertRaises(ValueError):
            node4.to_html()       

class TestParentNode(unittest.TestCase):
    def test_value(self):
        child = LeafNode(None, "child")
        node = ParentNode("p", [child])
        self.assertEqual(node.value, None)
    
    def test_to_html(self):
        leaf1 = LeafNode("b", "bold text")
        leaf2 = LeafNode("i", "italic text")
        leaf3 = LeafNode("a", "Click this", {"href": "https://www.google.com"})
        leaf4 = LeafNode(None, "normal text")
        
        parent1 = ParentNode("h1", [leaf1, leaf2])
        parent2 = ParentNode("h2", [leaf3])
        parent3 = ParentNode("h3", [parent1, parent2, leaf3, leaf4])
        parent4 = ParentNode("TEST", [leaf1], {"test": "it out baby"})
        parent5 = ParentNode(None, [leaf1])
        parent6 = ParentNode("h6", [])
        parent7 = ParentNode("h7", None)

        self.assertEqual(parent1.to_html(), "<h1><b>bold text</b><i>italic text</i></h1>")
        self.assertEqual(parent2.to_html(), '<h2><a href="https://www.google.com">Click this</a></h2>')
        self.assertEqual(parent3.to_html(), '<h3><h1><b>bold text</b><i>italic text</i></h1><h2><a href="https://www.google.com">Click this</a></h2><a href="https://www.google.com">Click this</a>normal text</h3>')
        self.assertEqual(parent4.to_html(), '<TEST test="it out baby"><b>bold text</b></TEST>')
        
        with self.assertRaises(ValueError):
            parent5.to_html() 
        with self.assertRaises(ValueError):
            parent6.to_html()
        with self.assertRaises(ValueError):
            parent7.to_html()        

if __name__ == "__main__":
    unittest.main()