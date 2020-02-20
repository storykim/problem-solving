l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
d1 = (a-1)//c + 1
d2 = (b-1)//d + 1
print(l-max(d1, d2))
