from sys import stdin
input = stdin.readline

board = [list(map(int, input().split())) for _ in range(3)]

n = int(input())
for _ in range(n):
    num = int(input())
    for i in range(3):
        for j in range(3):
            if board[i][j] == num:
                board[i][j] = True
                break

# check bingo
bingo_count = 0
for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] == True:
        bingo_count += 1
    elif board[0][i] == board[1][i] == board[2][i] == True:
        bingo_count += 1

if board[0][0] == board[1][1] == board[2][2] == True:
    bingo_count += 1
if board[0][2] == board[1][1] == board[2][0] == True:
    bingo_count += 1

print('Yes' if bingo_count else 'No')
