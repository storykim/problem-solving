s = input()

# 4n + 1
n = len(s)
draw = ''

for i in range(n):
    if i % 3 == 2:
        draw += '..*.'
    else:
        draw += '..#.'
draw += '.'

second = ''
for i in range(n):
    if i % 3 == 2:
        second += '.*.*'
    else:
        second += '.#.#'
second += '.'

mid = ''
for i in range(n):
    if i % 3 == 2 or (i >= 3 and i % 3 == 0):
        mid += '*.%s.' % (s[i])
    else:
        mid += '#.%s.' % (s[i])
if n % 3 == 0:
    mid += '*'
else:
    mid += '#'
print(draw)
print(second)
print(mid)
print(second)
print(draw)
