"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.
"""



class node:
    def __init__(self, data, left=None, right=None)
        self.data=data
        self.left=left
        self.right=right
        

def leafnode(root):
    return root.left is None and root.right is None
    
    
def operators(ops, a, b)
    if ops=='+':
        return a+b
    
    elif ops=='-'
        return a-b
        
    elif ops=='*'
        return a*b
        
    elif ops=='/'
        return a/b
        
        

def arth_expression(root):
    if root is None:
        return 0
    
    if leafnode(root):
        return int(root.data)
        
    a=arth_expression(root.left)
    b=arth_expression(root.right)
    
    return operators(root.data, a, b)
    
    
    
print(arth_expression(root))
    
    