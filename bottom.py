'''top view of a tree'''
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
def bottom_view(root):
    if not (root):
        return
    q=deque([(root,0)])
    hd_map={}
    while q:
        node, hd=q.popleft()
        hd_map[hd]=node.val
        if node.left:
            q.append((node.left,hd-1))
        if node.right:
            q.append((node.right,hd+1))
    for key in sorted(hd_map):
        print(hd_map[key],end=" ")      

n=int(input("enter  number nodes:"))
arr=list(map(int,input("enter node:").split()))
root= build_tree(arr)
print(bottom_view(root))