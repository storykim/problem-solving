def is_pal(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

while True:
    s = input()
    if s == '0':
        break
    print('yes' if is_pal(s) else 'no')
