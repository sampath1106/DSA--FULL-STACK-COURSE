def linear(n):
    if n==0:
        return 0
    return n+linear(n-1)
n=int(input("enter a number:"))
print("sum:",linear(n))