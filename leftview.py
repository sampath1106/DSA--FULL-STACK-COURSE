'''left view of a tree'''
from collections  import deque
class node:
    def __init__(self,val):
        self.val= val
        self.left=None
        self.right=None
def build_tree(arr):
    if not arr:
        return None
    nodes=[node(x) for x in arr]
    for i in range(len(arr)):
        if 2*i+1< len(arr):
            nodes[i].left=nodes[2*i+1]
        if 2*i+2< len(arr):
            nodes[i].right=nodes[2*i+2]
    return nodes[0]
def left_view(root):
    q=deque([root])
    while q:
        n=len(q)
        for i in range(n):
            node=q.popleft()
            if i==0:
                print(node.val, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

n=int(input("enter  number nodes:"))
arr=list(map(int,input("enter node:").split()))
root= build_tree(arr)
print("left view:",left_view(root))