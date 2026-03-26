#claculate number of node:
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def countnodes(root):
    if not root:
        return 0
    return 1+ countnodes(root.left)+countnodes(root.right)
root=node(int(input("enter root:")))
root.left=node(int(input("enter left:")))
root.right=node(int(input("enter right:")))
root.left.left=node(int(input("enter left:")))
root.left.right=node(int(input("enter left:")))
print("number of nodes i n a tree:",countnodes(root))