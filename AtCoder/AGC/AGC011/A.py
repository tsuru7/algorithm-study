from collections import deque

def readinput():
    n, c, k = map(int, input().split())
    tList = []
    for _ in range(n):
        tList.append(int(input()))
    return n, c, k, tList

def main(n, c, k, tList):
    tList.sort()
    nbus = 1
    nperson = 1
    t0 = tList[0]
    for i in range(1, n):
        t = tList[i]
        if t <= t0 + k:
            nperson += 1
            if nperson > c:
                nbus += 1
                nperson = 1
                t0 = t
        else:
            nbus += 1
            nperson = 1
            t0 = t
    return nbus

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n, c, k, t = readinput()
    ans = main(n, c, k, t)
    printans(ans)
