import sys
input = sys.stdin.readline
n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))

m1 = 0
z = 0
p1 = 0
def add_global(color):
    global m1, z, p1
    if color == 1:
        p1 += 1
    elif color == 0:
        z += 1
    else:
        m1 += 1

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
        hl = length//3
        diff = [0, hl, 2*hl]
        for dx in diff:
            for dy in diff:
                check(x+dx, y+dy, hl)

check(0,0, n)
print(m1)
print(z)
print(p1)
