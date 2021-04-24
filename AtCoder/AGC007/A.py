h, w = map(int, input().split())
aMap = []
for _ in range(h):
    aMap.append(input())

preridx = 0
for y in range(h):
    lidx = aMap[y].find('#')
    # if lidx == -1:
    #     print('Impossible')
    #     break
    ridx = aMap[y].find('.', lidx)
    if ridx == -1:
        ridx = w - 1
    else:
        if aMap[y].find('#', ridx) != -1:
            print('Impossible')
            break
        ridx -= 1
    # print(preridx, lidx, ridx)
    if lidx != preridx:
        print('Impossible')
        break

    preridx = ridx
else:
    if preridx < w -1:
        print('Impossible')
    else:
        print('Possible')
