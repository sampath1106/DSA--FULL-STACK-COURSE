#write a code iN a 2 -d matrix in a sprial pattern clock wise direction using divide-and -conqer apporch?

n=int(input("enter a  size:"))
matrix= [[0]*n for _ in range(n)]
print(matrix)
num=1
top=0
bottom=n-1
left=0
right=n-1
while top<=bottom and left<=right:
    for i in range(left,right+1):
        matrix[top][i]=num
        num+=1
    top+=1
    for i in range(top,bottom+1):
        matrix[i][right]=num
        num+=1
    right-=1
    for i in range(right,left-1,-1):
        matrix[bottom][i]=num
        num+=1
    bottom-=1
    for i in range(bottom,top-1,-1):
        matrix[i][left]=num
        num+=1
    left+=1
for row in matrix:
    print(*row)
