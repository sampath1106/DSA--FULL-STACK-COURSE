#write a code  to find the sum of longest subarray//////////<=k using slidding window with 2 pointer method?
arr=list(map(int,input("element:").split()))
k=int(input("enter slide size k:"))
slow=0
sum=0
maxlen=0
for fast in range(len(arr)):
    sum+=arr[fast]
    while sum>k:
        sum-=arr[slow]
        slow+=1
    maxlen=max(maxlen,fast-slow+1)
print("Maxlength:",maxlen)
