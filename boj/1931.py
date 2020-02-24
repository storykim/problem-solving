import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key=lambda elem: (elem[1], elem[0]))
last_end = -1
count = 0

for meet in meetings:
    if meet[0] >= last_end:
        last_end = meet[1]
        count += 1
print(count)
