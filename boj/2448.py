n = int(input())
m = [[' '] * (n*2 -1) for _ in range(n)]

size_map = {}
for i in range(11):
    size_map[3*2**i] = i+1

def draw(i, j, size):
    if size == 1:
        m[i][j] = '*'
        m[i+1][j-1] = '*'
        m[i+1][j+1] = '*'
        for k in range(-2,3):
            m[i+2][j+k] = '*'
    else:
        draw(i, j, size-1)
        draw(i + 3*2**(size-2), j - 3*2**(size-2), size-1)
        draw(i + 3*2**(size-2), j + 3*2**(size-2), size-1)

draw(0, n-1, size_map[n])

for line in m:
    print(''.join(line))
