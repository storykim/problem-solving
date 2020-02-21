n = int(input())
p = []

def convert(s):
    return int(s)/100.

for _ in range(n):
    p.append(list(map(convert, input().split())))


state = [-1.] * (1<<n)
MAX_STATE = (1<<n) - 1

def solve(idx, cur_state):
    if cur_state == MAX_STATE:
        return 1.

    if state[cur_state] >= 0.:
        return state[cur_state]

    prob = 0.
    for i in range(n):
        if cur_state & (1<<i):
            continue
        prob = max(prob, p[i][idx] * solve(idx+1, cur_state | (1<<i)))
    state[cur_state] = prob
    return prob

print(solve(0, 0) * 100)
