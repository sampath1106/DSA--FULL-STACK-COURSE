value=list(map(int,input("enter a value in a BST pattern:").split()))
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,value):
    if root is None:
        return node(value)
    if value<root.data:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root
def inorder(root):
    if root:
        print(root.data,end=" ")#pre ordre
        inorder(root.left)
        inorder(root.right)
        #print(root.data,end=" ")#in ordre
        #inorder(root.right)
        #print(root.data,end=" ")#post order
root=None
for v in value:
    root=insert(root,v)
print("inorder travels:", inorder (root))
    
