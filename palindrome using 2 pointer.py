#write a code to check palidrome by using two pointer

s=input("enter a string:")
left=0
right=len(s)-1
isPD=True
while left<right:
    if s[left]!=s[right]:
        isPD=False
        break
    left+=1
    right-=1
if isPD:
    print(s,"is a palindrome:")
else:
    print(s,"is not a  palindrome:")
