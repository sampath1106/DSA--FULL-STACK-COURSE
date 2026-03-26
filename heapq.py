#heapq pakage operations
import heapq
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,30)
heapq.heappush(heap,40)
print(heap)
x=heapq.heappop(heap)
print("Removed",x)
print("Remaining heap",heap)
y=heapq.heappop(heap)
print("Removed",y)
print("Remaining heap",heap)