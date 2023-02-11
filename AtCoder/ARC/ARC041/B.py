def readinput():
    n, m = map(int, input().split())
    bmap = []
    for _ in range(n):
        bmap.append(list(map(int, list(input()))))
    return n, m, bmap

def main(n, m, bmap):
    amap = []
    for _ in range(n):
        amap.append([0 for i in range(m)])
    for i in range(1, n-1):
        for j in range(1, m-1):
            c = bmap[i-1][j]
            bmap[i-1][j] -= c
            bmap[i+1][j] -= c
            bmap[i][j-1] -= c
            bmap[i][j+1] -= c
            amap[i][j] = c
    return amap

def printans(ans):
    # print(ans)
    for l in ans:
        print(''.join(map(str, l)))

if __name__ == '__main__':
    n, m, bmap = readinput()
    ans = main(n, m, bmap)
    printans(ans)
