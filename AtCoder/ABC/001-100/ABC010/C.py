from math import sqrt

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    xa, ya, xb, yb, t, v = m_input()
    n=i_input()
    xy = []
    for _ in range(n):
        xy.append(l_input())
    return xa, ya, xb, yb, t, v, n, xy

def main(xa, ya, xb, yb, t, v, n, xy):
    for x, y in xy:
        dist = sqrt((x-xa)**2+(y-ya)**2) + sqrt((x-xb)**2+(y-yb)**2)
        if dist > t*v:
            continue
        else:
            return 'YES'
    return 'NO'

def printans(ans):
    print(ans)

if __name__=='__main__':
    xa, ya, xb, yb, t, v, n, xy=readinput()
    ans=main(xa, ya, xb, yb, t, v, n, xy)
    printans(ans)
