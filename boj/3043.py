N = int(input())
x_pos = []
y_pos = []

for i in range(N):
    x, y = map(int, input().split())
    x, y = x-1, y-1

    x_pos.append((x, i+1))
    y_pos.append((y, i+1))

x_pos.sort()
y_pos.sort()

total = 0

up = []
down = []
left = []
right = []
for idx, (x, id) in enumerate(x_pos):
    diff = idx - x
    if diff < 0:
        # move to up
        up += ['%d U' % (id)] * abs(diff)
    else:
        down += ['%d D' % (id)] * abs(diff)
    total += abs(diff)

for idx, (y, id) in enumerate(y_pos):
    diff = idx - y
    if diff < 0:
        # move to left
        left += ['%d L' % (id)] * abs(diff)
    else:
        right += ['%d R' % (id)] * abs(diff)
    total += abs(diff)
print(total)
# NOTE : reverse down and right
output = up + down[::-1] + left + right[::-1]
for elem in output:
    print(elem)
