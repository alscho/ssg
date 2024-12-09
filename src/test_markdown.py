import unittest

from markdown import get_header_type, list_block_to_block_nodes, markdown_to_html_node, text_to_children, block_to_block_node, extract_title
from htmlnode import LeafNode, ParentNode, HTMLNode

class TestMarkdown(unittest.TestCase):
    def test_extract_title(self):
        tests_eq = [
            ["# title", "title"],
            ["# title2\n\nThis is a paragraph\n", "title2"],
            ["# title3\n\n## not a title\n### still not a title", "title3"]
        ]

        tests_raise = [
            ["", "## no title", "paragraph\n\n```code```\n\n### not a title"]
        ]

        for i in range(0, len(tests_eq)):
            self.assertEqual(extract_title(tests_eq[i][0]), tests_eq[i][1])
        
        with self.assertRaises(Exception):
            for j in range(0, len(tests_raise)):
                extract_title(tests_raise[j])

        

    def test_get_header_type(self):
        tests = [
            ["# header", "h1"],
            ["### header", "h3"],
            [" no header", "h0"],
            ["", "h0"],
            ["########### ", "h11"]
        ]
        for i in range(0, len(tests)):
            self.assertEqual(get_header_type(tests[i][0]), tests[i][1])

    def test_text_to_children(self):
        tests = [
            ["*header*", ["<i>header</i>"]],
            ["**bold**", ["<b>bold</b>"]],
            ["This is **bold** text with some *italic* and `code`.", ["This is ", "<b>bold</b>", " text with some ", "<i>italic</i>", " and ", "<code>code</code>", "."]],
            ["", []]
        ]
        for i in range(0, len(tests)):
            html_nodes = text_to_children(tests[i][0])
            for j in range(0, len(html_nodes)):
                node = html_nodes[j]
                self.assertEqual(node.to_html(), tests[i][1][j])

    def test_list_block_to_block_nodes(self):
        tests = [
            [("* item1\n* item2", "ul"), "<ul><li>item1</li><li>item2</li></ul>"],
            [("1. bla", "ol"), "<ol><li>bla</li></ol>"],
            [("1. bla\n2. blabla\n3. blablabla", "ol"), "<ol><li>bla</li><li>blabla</li><li>blablabla</li></ol>"]
        ]
        for i in range(0, len(tests)):
            self.assertEqual(list_block_to_block_nodes(tests[i][0][0], tests[i][0][1],).to_html(), tests[i][1])

    def test_block_to_block_node(self):
        tests = [
            [("### header", "heading"), "<h3>header</h3>"],
            [("##### headR", "heading"), "<h5>headR</h5>"],
            [("just some text", "paragraph"), "<p>just some text</p>"],
            [("some code", "code"), "<code>some code</code>"],
            [("nice quote", "quote"), "<blockquote>nice quote</blockquote>"],
            [("* item1\n* item2", "unordered_list"), "<ul><li>item1</li><li>item2</li></ul>"],
            [("1. item1\n2. item2", "ordered_list"), "<ol><li>item1</li><li>item2</li></ol>"],
            [("some code with **bold** and *italic*", "code"), "<code>some code with <b>bold</b> and <i>italic</i></code>"],
            [("text", "paragraph"), "<p>text</p>"]

        ]
        for i in range(0, len(tests)):
            block = tests[i][0][0]
            block_type = tests[i][0][1]
            to_check = tests[i][1]

            self.assertEqual(block_to_block_node(block, block_type).to_html(), to_check)



    def test_markdown_to_html_node(self):
        tests = [
            ["# heading\n\nparagraph with **bold** and *italic*.\n\n* 1\n* 2\n* 3", "<div><h1>heading</h1><p>paragraph with <b>bold</b> and <i>italic</i>.</p><ul><li>1</li><li>2</li><li>3</li></ul></div>"],
            ["text", "<div><p>text</p></div>"]
        ]
        for i in range(0, len(tests)):
            self.assertEqual(markdown_to_html_node(tests[i][0]).to_html(), tests[i][1])