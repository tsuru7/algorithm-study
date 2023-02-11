def readinput():
    n, h = map(int, input().split())
    aList = []
    bList = []
    for _ in range(n):
        a, b = map(int, input().split())
        aList.append(a)
        bList.append(b)
    return n, h, aList, bList

def main(n, h, aList, bList):
    amax = max(aList)
    bList.sort(reverse=True)
    count = 0
    i = 0
    while h > 0 and i < len(bList) and bList[i] >= amax:
        h -= bList[i]
        count += 1
        i += 1

    if h <= 0:
        return count

    hit = h // amax
    if h % amax != 0:
        hit += 1
    
    count += hit

    return count

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, h, aList, bList = readinput()
    ans = main(n, h, aList, bList)
    printans(ans)
