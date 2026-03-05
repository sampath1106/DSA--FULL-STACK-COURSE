#writw a code to decet a dupicate using index array jumping (floyd's  algo concept)
arr=list(map(int,input("elements:").split()))
slow=arr[0]
fast=arr[0]
while True:
    slow=arr[slow]
    fast=arr[arr[fast]]
    if slow==fast:
        break
slow=arr[0]
while slow!=fast:
    slow=arr[slow]
    fast=arr[fast]
    print("Duplicate:",slow) 
        
