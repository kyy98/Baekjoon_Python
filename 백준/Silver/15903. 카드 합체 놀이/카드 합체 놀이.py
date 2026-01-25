import heapq
n, m = map(int, input().split())
heap = list(map(int, input().split()))

for _ in range(m):
    heapq.heapify(heap)
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    num = a+b
    heapq.heappush(heap, num)
    heapq.heappush(heap, num)

print(sum(heap))