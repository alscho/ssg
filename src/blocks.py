import re

def block_to_block_type(block):
    if len(block) < 2:
        return "paragraph"
    if block[:3] == "```" and block[-3:] == "```":
        return "code"
    if ("\n" not in block) and ("# " in block[:min(len(block), 7)]):
        return "heading"
    lines = block.split("\n")
    is_quote = True
    is_unordered_list = True
    is_ordered_list = True
    for i in range(0, len(lines)):
        line = lines[i]
        if len(line) < 2 or line[0:2] != "> ":
            is_quote = False
        if len(line) < 2 or (line[0:2] != "* " and line[0:2] != "- "):
            is_unordered_list = False
        if len(line) < 3 or line[0:3] != f"{i+1}. ":
            is_ordered_list = False
    if is_quote == True:
        return "quote"
    if is_ordered_list == True:
        return "ordered_list"
    if is_unordered_list == True:
        return "unordered_list"
    
    return "paragraph"


### takes in perfectly formatted markdown
def markdown_to_blocks(markdown):
    blocks = []
    temps = markdown.split("\n\n")
    for block in temps:
        if block != "":
            temp = block.strip()
            blocks.append(temp)
    return blocks
