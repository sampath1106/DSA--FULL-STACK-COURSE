#write a stackhasing for performing the evalutions of stack operations usig hash elements=6
'''1st=5
2nd=7
3rd=5
4th=7
5th=4
6th=5
before pop:
freq=[5,7,4]
freq=[5,7]
freq=[5]
after pop
freq=[5,7,4]
freq=[5,7]
freq=[]'''
from collections import defaultdict
freq=defaultdict(int)
stack=defaultdict(list)
max_freq=0
n=int(input("stack size:"))
for i in range(n):
    x=int(input("enter element:"))
    freq[x]+=1
    f=freq[x]
    stack[f].append(x)
    if f>max_freq:
        max_freq=f
print(" \n before pop :")
for i in stack:
    print("frequency",f,":",stack[f])
#pop operation
val=stack[max_freq].pop()
freq[val]=-1
print(" \n pop value:",val)
print(" \n after pop:")
for f in stack:
    
    print("frequency",f,":",stack[f])

