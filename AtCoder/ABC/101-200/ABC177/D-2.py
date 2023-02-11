def readinput():
    n, m = map(int, input().split())
    nList = []
    for _ in range(n+1):
        nList.append([])
    pairs = set()
    for _ in range(m):
        a, b = map(int, input().split())
        if (a, b) in pairs or (b, a) in pairs:
            continue
        nList[a].append(b)
        nList[b].append(a)
        pairs.add((a, b))
        
    return n, nList

def main(n, nList):
    color = [0]*(n+1)
    maxcolor = 1
    for i in range(1, n+1):
        used = set()
        if color[i] == 0:
            color[i] = 1
        used.add(color[i])
        whiteList = []
        for next in nList[i]:
            if color[next] != 0:
                used.add(color[next])
            else:
                whiteList.append(next)
        icolor = 1
        for next in whiteList:
            while icolor in used:
                icolor += 1
            color[next] = icolor
            used.add(icolor)
            icolor += 1
        maxcolor = max(maxcolor, icolor-1)
    return maxcolor

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, nList = readinput()
    ans = main(n, nList)
    printans(ans)
