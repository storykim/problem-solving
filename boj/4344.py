t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))[1:]
    avg = sum(l) / len(l)
    cnt = 0
    for elem in l:
        if elem > avg: cnt += 1

    print("%.3f%%" % (cnt / len(l) * 100))
