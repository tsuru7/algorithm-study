import sys
INFTY = sys.maxsize

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    xy = []
    for _ in range(n):
        xy.append(l_input())
    return n,xy

def main(n,xy):
    z = [0]*n
    w = [0]*n
    minz = INFTY
    maxz = -INFTY
    minw = INFTY
    maxw = -INFTY
    for i in range(n):
        x, y = xy[i]
        z[i] = x + y
        w[i] = x - y
        if maxz < z[i]:
            maxz = z[i]
        if minz > z[i]:
            minz = z[i]
        if maxw < w[i]:
            maxw = w[i]
        if minw > w[i]:
            minw = w[i]
    return max(maxz - minz, maxw - minw)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xy=readinput()
    ans=main(n,xy)
    printans(ans)
