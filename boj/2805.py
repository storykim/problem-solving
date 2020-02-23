import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

def check(h):
    result = 0
    for tree in trees:
        result += max(0, tree - h)
    return result >= m

# NOTE : tree range 제한되어 있으면 counter 사용
lo, hi = 0, 1000000000
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid + 1
    else:
        hi = mid
print(hi-1)

