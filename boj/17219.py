import sys
input = sys.stdin.readline
password_dict = {}
n, m = map(int, input().split())
for _ in range(n):
    site, pw = input().strip().split()
    password_dict[site] = pw
for _ in range(m):
    print(password_dict[input().strip()])
