import sys
input = sys.stdin.readline

n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

for i in range(n):
    visited = [0] * n
    stack = [i]
    while stack:
        node = stack.pop()
        for idx, connected in enumerate(mat[node]):
            if not connected:
                continue

            if not visited[idx]:
                visited[idx] = 1
                stack.append(idx)

    for elem in visited:
        print(elem, end=' ')
    print('')
