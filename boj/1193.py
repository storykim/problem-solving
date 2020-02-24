x = int(input())

i = 1
while True:
    if i*(i-1)//2 <x<= i*(i+1)//2:
        break
    i += 1

# sum of denominator and numerator is i+1
k = x - i*(i-1)//2 # k th number
if i % 2:
    # denominator starts from i, numerator starts from 1
    den = i+1-k
    num = k
else:
    den = k
    num = i+1-k
print('%d/%d' % (den, num))
