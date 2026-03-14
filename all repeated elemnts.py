#array +hashmap find gthe fist repeating element in array dta structure input:5 3 4 3 2 2

arr=list(map(int,input("element:").split()))
freq={}
for  num in arr:
    if num in freq:
        print("first repeating element:",num)
        #break
    freq[num]=1
else:
    print("no repeating elements:")
