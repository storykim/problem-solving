a = int(input())
b = int(input())
c = int(input())
n = str(a*b*c)
arr = [0] * 10
for digit in n:
    arr[int(digit)] += 1
for elem in arr:
    print(elem)
