def readinput():
    x, y, a, b, c = map(int, input().split())
    plist = list(map(int, input().split()))
    qlist = list(map(int, input().split()))
    rlist = list(map(int, input().split()))
    return x, y, a, b, c, plist, qlist, rlist

def main(x, y, a, b, c, plist, qlist, rlist):
    plist = sorted(plist, reverse=True)[:x]
    qlist = sorted(qlist, reverse=True)[:y]
    apples = sorted(plist + qlist + rlist, reverse=True)
    sum = 0
    for i in range(x+y):
        sum += apples[i]
    return sum

def printans(ans):
    print(ans)

if __name__ == '__main__':
    x, y, a, b, c, plist, qlist, rlist = readinput()
    ans = main(x, y, a, b, c, plist, qlist, rlist)
    printans(ans)
