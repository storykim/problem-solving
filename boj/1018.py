r, c = map(int, input().split())

board = []
for _ in range(r):
    board.append(input())

def count_required_coloring(i, j):
    # odd : B, even : W
    count = 0
    for di in range(8):
        for dj in range(8):
            if (di+dj)%2:
                count += 0 if board[i+di][j+dj] == 'W' else 1
            else:
                count += 0 if board[i+di][j+dj] == 'B' else 1

    return min(count, 64-count)

def solve():
    ret = float('inf')
    for i in range(r-7):
        for j in range(c-7):
            ret = min(ret, count_required_coloring(i,j))
    print(ret)

solve()
