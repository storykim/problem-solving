_, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
def choice(l, last_idx, stack):
    if len(stack) == m:
        for elem in stack:
            print(elem, end=' ')
        print()
        return

    for idx in range(last_idx, len(l)):
        stack.append(l[idx])
        choice(l, idx, stack)
        stack.pop()

choice(l, 0, [])
