import sys
l = [ int(line) for line in sys.stdin ]

def pre_to_post(start, end):
    # [start, end)
    if start >= end:
        return
    if start + 1 == end:
        print(l[start])
        return
    root = l[start]

    # search first elem larger than root
    lo = start + 1
    hi = end
    while lo < hi:
        mid = (lo + hi)//2
        if l[mid] > root:
            hi = mid
        else:
            lo = mid + 1
    pre_to_post(start + 1, hi)
    pre_to_post(hi, end)
    print(root)

pre_to_post(0, len(l))
