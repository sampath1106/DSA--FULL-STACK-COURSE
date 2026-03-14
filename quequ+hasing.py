'''queue+hash'''
from collections import deque
stream=input("enter chars:")
freq={}
q=deque()
for ch in stream:
    freq[ch]=freq.get(ch,0)+1
    q.append(ch)
    print("\ n queue before enque",list(q))
    #repating chars remove
    while q and freq[q[0]]>1:
        removed= q.popleft()
        print("removed from queue:",removed)
    print("queue after removing cahr",list(q))
    if q:
        print("first non repeating.char:",q[0])
    else:
        print("first no repeating char-1:")
    
