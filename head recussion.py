#wirte a code  to print  n natural numbers using head recussion?
def head(n):
    if n==0:
        return 0
    head(n-1)
    print(n)
n=int(input("enter a number:"))
head(n)
