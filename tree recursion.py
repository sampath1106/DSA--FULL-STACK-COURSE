def tree(n):
    if n<=1:
        return n
    return tree(n-1)+ tree(n-2)
n=int(input("enter a value:"))
print(tree(n))