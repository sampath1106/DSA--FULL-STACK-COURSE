#write a code to search  an element using 2 pointer one way  and print the element ?
arr=list(map(int,input("elements:").split()))
slow=0
fast=0
while fast<len(arr)and fast+1<len(arr):
    slow+=1
    fast+=2
print("Middle element:",arr[slow])
