n = int(input())
s = input()
nw = 0
nb = 0
nw_left = 0
nb_right = 0
for c in s:
    if c == '.':
        nw += 1
    else:
        nb += 1

leftb = 0
rightw = nw
minchg = nw
for c in s:
    if c == '#':
        leftb += 1
    else:
        rightw -= 1
    minchg = min(minchg, leftb + rightw)

print(minchg)

