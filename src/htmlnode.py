class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented yet")
    
    def props_to_html(self):
        l_props = ""
        if self.props:
            for k in self.props:
                #l_props += f" {k.strip('"')}={self.props[k]}"
                l_props += f' {k}="{self.props[k]}"'                
        return l_props
        
    def __repr__(self):
        return f"HTMLNode(<{self.tag}>, '{self.value}', {self.children}, {self.props})"
 
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("no value found, all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("parent node has to have a tag")
        if self.children == None or len(self.children) == 0:
            raise ValueError("parent node has to have at least one child")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
