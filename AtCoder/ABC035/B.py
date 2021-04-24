s = input()
t = int(input())

x = 0
y = 0

count = 0
for c in s:
    if c == 'U':
        y += 1
    elif c == 'D':
        y -= 1
    elif c == 'L':
        x -= 1
    elif c == 'R':
        x += 1
    elif c == '?':
        count += 1

if t == 1:
    print(abs(x)+abs(y)+count)
elif t == 2:
    dist = abs(x)+abs(y)
    if count <= dist:
        print(dist-count)
    else:
        print((count - dist)%2)
