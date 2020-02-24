n = int(input())
l = sorted(list(map(int, input().split())))
time = 0
for i, elem in enumerate(l):
    time += elem * (len(l) - i)
print(time)
