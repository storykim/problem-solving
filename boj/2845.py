L, P = map(int, input().split())
num = L*P
gap = [elem - num for elem in list(map(int, input().split()))]

print("%d %d %d %d %d" % (gap[0], gap[1], gap[2], gap[3], gap[4]))
