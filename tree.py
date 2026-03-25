'''create a binary tree with user difine nodes where the root: 11 left ,12 right 13'''
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root_val=int(input("enter root value:"))
root=node(root_val)
left_val=int(input("enter left value:"))
root.left=node(left_val)
right_val=int(input("enter left value:"))
root.right=node(right_val)
print("\n Tree created succes")
print("Root:",root.data)
print("Left child",root.left.data)
print("right child",root.right.data)
