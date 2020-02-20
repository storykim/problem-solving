t = int(input())
for _ in range(t):
    score = 0
    streak = 0

    s = input()
    for c in s:
        if c == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)

