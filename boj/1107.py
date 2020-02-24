def reachable(ch):
    s = str(ch)
    if s == '100': return True
    return not any( [ c in broken for c in s ])

target = int(input())
n = int(input())
broken = set(input().split()) if n else []

# NOTE : 100이랑 가까운 경우 핸들
one_by_one = abs(100 - target)
use_num = None
if reachable(target):
    use_num = len(str(target))
else:
    diff = 1
    while True:
        if target - diff >= 0 and reachable(target - diff):
            use_num = diff + len(str(target-diff))
            break
        elif reachable(target + diff):
            use_num = diff + len(str(target+diff))
            break
        diff += 1
print(min(one_by_one, use_num))
