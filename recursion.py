def direct(n):
    if n==0:
        return
    print(n)
    direct(n-1)
n=int(input("enter a number :"))
direct(n)
#write a code in even and odd using indirect recussion  function ?
def is_even(n):
    id