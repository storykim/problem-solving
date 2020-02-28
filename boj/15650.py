import itertools

def p_list(l):
    for elem in l:
        print(elem, end=' ')
    print('')

n, m = map(int,input().split())
l = range(1, n+1)

for combination in itertools.combinations(l, m):
    p_list(combination)
