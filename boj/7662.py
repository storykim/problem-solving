import heapq
import collections
import sys
input = sys.stdin.readline

# Init
def solve():
    min_heap = []
    max_heap = []

    deleted_from_min = collections.defaultdict(int)
    deleted_from_max = collections.defaultdict(int)

    k = int(input())
    for _ in range(k):
        query, param = input().split()
        param = int(param)

        if query == 'I':
            heapq.heappush(min_heap, param)
            heapq.heappush(max_heap, -param)
        elif param == 1:
            # delete from max_heap
            if max_heap:
                item = -heapq.heappop(max_heap)
                empty = False
                while item in deleted_from_min:
                    deleted_from_min[item] -= 1
                    if deleted_from_min[item] == 0:
                        del deleted_from_min[item]

                    if not max_heap:
                        empty = True
                        break
                    item = -heapq.heappop(max_heap)

                if not empty:
                    deleted_from_max[item] += 1
        else:
            #delete from min_heap
            if min_heap:
                item = heapq.heappop(min_heap)
                empty = False
                while item in deleted_from_max:
                    deleted_from_max[item] -= 1
                    if deleted_from_max[item] == 0:
                        del deleted_from_max[item]

                    if not min_heap:
                        empty = True
                        break
                    item = heapq.heappop(min_heap)

                if not empty:
                    deleted_from_min[item] += 1

    def finalize():
        if not min_heap:
            print('EMPTY')
            return

        while max_heap and -max_heap[0] in deleted_from_min:
            item = -heapq.heappop(max_heap)
            deleted_from_min[item] -= 1
            if deleted_from_min[item] == 0:
                del deleted_from_min[item]
        if not max_heap:
            print('EMPTY')
            return

        while min_heap and min_heap[0] in deleted_from_max:
            item = heapq.heappop(min_heap)
            deleted_from_max[item] -= 1
            if deleted_from_max[item] == 0:
                del deleted_from_max[item]

        print(-max_heap[0], min_heap[0])
    finalize()

t = int(input())
for _ in range(t):
    solve()
