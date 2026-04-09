n=int(input("enter number of items:"))
items=[]
for i in range(n):
    value=int(input(f"value of item {i+1}:"))
    weight=int(input(f"weight od item{i+1}:"))
    items.append((value,weight,value/weight))
capacity=int(input("enter capacity:"))
items.sort(key=lambda x:x[2], reverse=True)
total_value=0
for value,weight,ratio in items:
    if capacity>=weight:
        total_value+=value
        capacity -= weight
    else:
        total_value+=value*(capacity/weight)
        break
print("maximum value:",total_value)