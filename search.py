#search function in a tree:
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def search(root,key):
    if not root:
        return False
    if root.data==key:
        return True
    return search(root.left,key) or search(root.right,key)
root=node(int(input("enter root:")))
root.left=node(int(input("enter left:")))
root.right=node(int(input("enter right:")))
root.left.left=node(int(input("enter left:")))
root.left.right=node(int(input("enter left:")))

key=int(input("enter a value of search:"))
if search(root,key):
    print("value found:")
else:
    print("not found")
