#claculate hight of tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(root):
    if not root:
        return 0
    return 1+max(height(root.left),height(root.right))
root=node(int(input("enter root:")))
root.left=node(int(input("enter left:")))
root.right=node(int(input("enter right:")))
root.left.left=node(int(input("enter left:")))
root.left.right=node(int(input("enter left:")))
print("height level of the tree:",height(root))