s = input()
ret = 0

l = s.split('-')
flag = True

def eval_plus_expr(expr):
    l = expr.split('+')
    return sum(map(int, l))

for elem in l:
    if flag:
        ret += eval_plus_expr(elem)
        flag = False
    else:
        ret -= eval_plus_expr(elem)

print(ret)

