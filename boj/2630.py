import sys
input = sys.stdin.readline
n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))

blue = 0
white = 0
def add_global(color):
    global blue, white
    if color == 1:
        blue += 1
    else:
        white += 1

def check(x, y, length):
    color = m[x][y]
    # Check all
    ok = True
    for dx in range(length):
        for dy in range(length):
            if m[x+dx][y+dy] != color:
                ok = False
                break
        if not ok:
            break

    if ok:
        add_global(color)
    else:
        hl = length//2
        check(x, y, hl)
        check(x + hl, y, hl)
        check(x, y+hl, hl)
        check(x+hl, y+hl, hl)

check(0,0, n)
print(white)
print(blue)
