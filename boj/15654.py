import itertools

def p_list(l):
    for elem in l:
        print(elem, end=' ')
    print('')

n, m = map(int,input().split())
l = sorted(list(map(int, input().split())))

for combination in itertools.permutations(l, m):
    p_list(combination)
