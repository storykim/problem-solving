from sys import stdin
input= stdin.readline

n = int(input())
if n == 1:
    print(int(input()))
else:
    prev = [int(input())]
    for _ in range(n-1):
        current_score = list(map(int, input().split()))
        cur = []

        for idx, score in enumerate(current_score):
            if idx == 0:
                cur.append(score + prev[idx])
            elif idx == len(current_score) - 1:
                cur.append(score + prev[idx-1])
            else:
                cur.append(score + max(prev[idx-1], prev[idx]))
        prev = cur

    print(max(prev))
