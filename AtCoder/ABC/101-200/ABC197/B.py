def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    h, w, x, y=m_input()
    smap = []
    for _ in range(h):
        smap.append(input())
    return h, w, x, y, smap

def main(h, w, x, y, smap):
    # print(x, y)
    count = 1
    for i in range(x-2, -1, -1):
        if smap[i][y-1] == '.':
            count += 1
        else:
            break
    # print(f'count(1): {count}')
    for i in range(x, h):
        if smap[i][y-1] == '.':
            count += 1
        else:
            break
    # print(f'count(2): {count}')
    for j in range(y-2, -1, -1):
        if smap[x-1][j] == '.':
            count += 1
        else:
            break
    # print(f'count(3): {count}')
    for j in range(y, w):
        # print(j, y, h)
        if smap[x-1][j] == '.':
            count += 1
        else:
            break
    # print(f'count(4): {count}')

    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    h, w, x, y, smap=readinput()
    ans=main(h, w, x, y, smap)
    printans(ans)
