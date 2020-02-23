import sys
import collections
input = sys.stdin.readline
t = int(input())

def check_order(m, priorities):
    c = collections.Counter(priorities)
    tasks = collections.deque(enumerate(priorities))
    
    while tasks:
        task = tasks.popleft()
        if task[1] == max(c):
            c[task[1]] -= 1
            if c[task[1]] == 0:
                del c[task[1]]
            if task[0] == m:
                print(len(priorities) - len(tasks))
                return
        else:
            tasks.append(task)

for _ in range(t):
    n, m = map(int, input().split())
    priorites = list(map(int, input().split()))
    check_order(m, priorites)
    
    
