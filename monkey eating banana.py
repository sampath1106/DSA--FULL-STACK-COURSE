'''"MONKEY EATING BANANNA "write a code to find the minimum speed of eating, so the monkey eats all  bananna in an hour h using bsr apporch'''
'''banana piles:3,6,7,11
h=8
3 >1hrs
6->2hrs
7->2hrs
11->2hrs
   8hrs
   4hrs'''

piles=list(map(int,input("enter piles:").split()))
h=int(input("hours:"))
low=1
high=max(piles)
ans=high
while low<=high:
    mid=(low+high)//2
    hours=0
    for p in piles:
        if p%mid==0:
            hours +=p//mid
        else:
            hours +=(p//mid)+1
    if hours<=h:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print("minimum eating speed:",ans)
