#write a code to reverse an array s using 2 pointer apporch?
arr=list(map(int,input("element:").split()))
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print("reversed array:",arr)
