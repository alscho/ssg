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
        return f"HTMLNode(<{self.tag}>, '{value}', {children}, {props})"
 
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("no value found, all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        