arr=list(map(int,input("enter value:").split()))
key=int(input())
found=false
for i in range(len(arr)):
    if arr[i]==key:
        print("element  found in  index",i)
        foung=True
        break
if not found:
    print("element dosent exsists in array")