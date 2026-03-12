#find the squareroot(floor value) by bsr approch

n=int(input("entr a number:"))
low=0
high=n
ans=0
while  low<=high:
    mid=(low+high)//2
    if mid*mid<=n:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print("squareroot (floor value)",ans)
