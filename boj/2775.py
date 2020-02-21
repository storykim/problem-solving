t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    cur_floor = 0
    cur_people = range(1, n+1)
    prev_people = []
    while cur_floor != k:
        prev_people = cur_people
        cur_people = []
        for idx in range(len(prev_people)):
            if idx == 0:
                cur_people.append(1)
            else:
                cur_people.append(cur_people[-1] + prev_people[idx])
        cur_floor += 1
    print(cur_people[-1])
