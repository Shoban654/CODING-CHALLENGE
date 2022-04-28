class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class tree:
    def insert(self,root,value):
        if root==None:
            return Node(value)
        else:
            if value<root.value:
                if root.left==None:
                    root.left=Node(value)
                else:
                    self.insert(root.left,value)
            else:
                if root.right==None:
                    root.right=Node(value)
                else:
                    self.insert(root.right,value)
            
                    
                    
def serialize(root):
    s=[]
    def serializeeee(root):
        if not root:
            s.append('_')
        else:
            s.append(str(root.data))
            serialize(root.left)
            serialize(root.right)
        return s
        
        
        
if __name__ == '__main__':
    numbers=[int(n) for n in input().split(',')]
    root=Node(None)
    Tree = tree()
    for n in numbers:
        root=Tree.insert(root,n)
    s1=serialize(Tree.root)
    print(s1)