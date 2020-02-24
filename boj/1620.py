import sys
input = sys.stdin.readline
name_to_id = {}
id_to_name = {}

n, m = map(int, input().split())
for i in range(n):
    s = input().strip()
    name_to_id[s] = i+1
    id_to_name[i+1] = s

for _ in range(m):
    query = input().strip()
    if query.isdigit():
        print(id_to_name[int(query)])
    else:
        print(name_to_id[query])

