s = set()
_, m = map(int, input().split())
l = sorted(list(map(int, input().split())))

def search(l, stack):
    if len(stack) == m:
        s.add(tuple(stack))
        return
    
    for i in range(len(l)):
        stack.append(l[i])
        search(l[:i] + l[i+1:], stack)
        stack.pop()

search(l, [])
for seq in sorted(list(s)):
    for elem in seq:
        print(elem, end=' ')
    print()
