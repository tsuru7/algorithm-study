s = int(input())
q = s // 10**9
r = s % 10**9
if r == 0:
    h = q
    x = 0
else:
    h = q + 1
    x = 10**9 - r
print('{} {} {} {} {} {}'.format(10**9, h, 10**9 - x, 0, 0, h - 1))
