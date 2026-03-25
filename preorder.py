#postorder traversal of a tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    if root:
        print(root.data,end=" ")
        inorder(root.left)
        inorder(root.right)
        
root=node(int(input("enter root:")))
root.left=node(int(input("enter left:")))
root.right=node(int(input("enter right:")))
print("Inorder Traversal:", inorder(root))