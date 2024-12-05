from textnode import TextNode, TextType

def main():
    dummy = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(dummy)

main()