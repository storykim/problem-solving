t = input()
p = input()

def preprocessing(p):
    prep = [0] * len(p)
    begin = 1
    correct = 0
    while begin + correct < len(p):
        if p[begin+correct] != p[correct]:
            if correct == 0:
                begin += 1
            else:
                begin += correct - prep[correct-1]
                correct = prep[correct-1]
        else:
            correct += 1
            prep[begin+correct-1] = correct
    return prep

prep = preprocessing(p)

result = []
begin = 0
correct = 0

while begin + correct < len(t):
    if t[begin+correct] == p[correct]:
        correct += 1
        if correct == len(p):
            result.append(begin+1)
            begin += correct - prep[correct-1]
            correct = prep[correct-1]
    else:
        if correct == 0:
            begin += 1
        else:
            begin += correct - prep[correct-1]
            correct = prep[correct-1]

print(len(result))
for elem in result:
    print(elem, end=' ')

