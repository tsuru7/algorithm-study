import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    r,c,d=m_input()
    amap = []
    for _ in range(r):
        amap.append(l_input())
    return r,c,d,amap

def main(r,c,d,amap):
    targets = []
    for row in range(r):
        for col in range(c):
            targets.append((amap[row][col], row, col))
    targets.sort(reverse=True)
    for price, row, col in targets:
        dist = row+col
        if dist > d:
            continue
        if dist % 2 != d %2:
            continue
        return price

def printans(ans):
    print(ans)

if __name__=='__main__':
    r,c,d,amap=readinput()
    ans=main(r,c,d,amap)
    printans(ans)
