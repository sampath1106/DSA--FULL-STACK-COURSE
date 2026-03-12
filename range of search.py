#wirte a code to performe binary search in range and print"alogrthm


arr=list(map(int,input("enter anumber:").split()))
target=int(input("target:"))
low=0
high=len(arr)
while low<=high:
    mid=(low+high)//2
    print("Range:",low, "to",high)
    if arr[mid]==target:
        print("element found at index:",mid)
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
else:
        print("element not found!!!")
