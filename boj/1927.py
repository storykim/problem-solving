import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    q = int(input())
    if q == 0:
        if heap:
            elem = heapq.heappop(heap)
            print(elem)
        else:
            print(0)
    else:
        heapq.heappush(heap, q)
