###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###


# This class originally relied on a class library to create inheritance. We can do this all in Python.
# 
class Node:
    nodeCount = 0
    
    def __init__(self) -> None:
        self.depth = 0
        self.id = self.nodeCount
        self.nodeCount += 1
        self.childText = "[[UNEXPANDED]]"
        
    def setParent(self, parent):
        pass
        
    def expand(self):
        pass
        
    def expandChildren(self):
        pass
        
    def createChildrenFromSections(self, sections):
        pass
        
    
class RootNode(Node):
    def __init__(self, grammar, rawRule) -> None:
        super().__init__()
        self.grammar = grammar
        self.parsedRule = tracery.parseRule(rawRule) # TODO
        
    def expand(self):
        pass
        
class TagNode(Node):
    def __init__(self, parent, parsedTag) -> None:
        super().__init__()
        # Complicated. There is some verification first.
    
    def expand(self):
        pass
        
    def toLabel(self):
        pass
        
    def toString(self):
        pass
        
class TextNode(Node):
    self.isLeaf = True
    
    def __init__(self, parent, text) -> None:
        super().__init__()
        self.setParent(parent)
        self.text = text
        self.finalText = text
        
    def expand(self):        
        pass
        
    def toLabel(self):
        pass
        
        
# Immediately returns root node.