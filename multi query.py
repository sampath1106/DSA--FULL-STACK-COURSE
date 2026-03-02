
n = int(input("enter a number of elements: " ))
arr=list(map(int, input("element:").split()))
prefix=[0]*n
prefix[0]=arr[0]
for i in range(1, n):
    prefix[i]=prefix[i-1]+arr[i]
q=int(input("enter number of quries:"))
for _ in range(q):
    l,r=map(int,input("emter l and r :").split())
    if l==0:
        print("sum=",prefix[r])
    else:
        print("sum:",prefix[r]-prefix[l-1])
    
