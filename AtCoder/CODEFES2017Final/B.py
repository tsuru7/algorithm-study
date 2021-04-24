s = input()
counta=0
countb=0
countc=0
for c in s:
    if c=='a':
        counta+=1
    elif c=='b':
        countb+=1
    elif c=='c':
        countc+=1

maxcount = max([counta, countb, countc])
mincount = min([counta, countb, countc])
medcount = counta+countb+countc-maxcount-mincount
if maxcount - mincount > 1:
    print('NO')
else:
    print('YES')
