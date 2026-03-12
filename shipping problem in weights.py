#write a code  calculate the minmum capcity of ship wwhere you package with weight you have to ship them within d days
#find the minimum capacity  of the ship w r t days
#input:[1,2,3,4,5,6,7,8,9,10]
#d=5
#otput 15
#min capacity=max(w)=10
#max capacity=sum(w)=55
#i=min.capacity
#h=max.capacity

weight=list(map(int,input("enter a weight:").split()))
days=int(input("engter a  days :"))
low=max(weight)
high=sum(weight)
ans=high
while low<=high:
    mid=(low+high)//2
    d=1
    curr=0
    for w in weight:
        if curr+w>mid:
            d+=1
            curr=0
        curr+=w
    if d<=days:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print("min capacity:",ans)
