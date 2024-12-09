import re
import unittest

from blocks import markdown_to_blocks, block_to_block_type

class TestBlocks(unittest.TestCase):
    def test_block_to_block_type(self):
        tests = [
            ["### heading", "heading"],
            ["####### too much hashtags", "paragraph"],
            ["#notheader", "paragraph"],
            ["Just a paragraph", "paragraph"],
            ["```code is code\nand other stuff```", "code"],
            ["> quote\n> quote\n> quote", "quote"],
            ["> quote\n not quote", "paragraph"],
            ["* 1\n* 2\n* 3\n* 4", "unordered_list"],
            ["** paragraph", "paragraph"],
            ["*paragraph", "paragraph"],
            ["1. ordered list\n2. list\n3. works", "ordered_list"],
            ["1. not\n2. an\n3.ordered list", "paragraph"],
            ["", "paragraph"],
            ["something\n\n\nsomething", "paragraph"]
        ]
        for i in range(0, len(tests)):
            self.assertEqual(block_to_block_type(tests[i][0]), tests[i][1])

    def test_markdown_to_blocks(self):
        markdown1 = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        tests = [
            [markdown1, ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]],
            ["", []],
            ["   This is just a sentence.\n", ["This is just a sentence."]],
            ["Lots of newlines\n\n\n\n\n\n\n\n\n\nWhat now?", ["Lots of newlines", "What now?"]]

        ]
        for i in range(0, len(tests)):    
            self.assertEqual(markdown_to_blocks(tests[i][0]), tests[i][1])