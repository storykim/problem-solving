n = int(input())
l = set()
for _ in range(n):
    l.add(input())
l = list(l)
def compare(a):
    return len(a), a
l.sort(key=compare)
for elem in l:
    print(elem)
