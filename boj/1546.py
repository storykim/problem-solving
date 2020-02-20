import sys
_ = sys.stdin.readline()
l = list(map(int, sys.stdin.readline().split()))
print(sum(l) / len(l) * 100 / max(l))
