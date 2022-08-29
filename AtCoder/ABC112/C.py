import sys
sys.setrecursionlimit(10**6)
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
    n=i_input()
    xyh = []
    for _ in range(n):
        xyh.append(l_input())
    return n,xyh

def getH(x, y, h, cx, cy):
    return h + abs(x-cx) + abs(y-cy)


def main(n,xyh):

    for cx in range(0, 101):
        for cy in range(0, 101):
            H = INFTY
            found = False
            for i in range(n):
                xi, yi, hi = xyh[i]
                if hi == 0:
                    continue
                Hi = getH(xi, yi, hi, cx, cy)
                if H == INFTY:
                    H = Hi
                elif H == Hi:
                    continue
                else:
                    break
            else:
                found = True
            
            if not found:
                continue

            found = False
            for i in range(n):
                xi, yi, hi = xyh[i]
                if hi > 0:
                    continue
                if max(0, H - abs(xi-cx) - abs(yi-cy)) == 0:
                    continue
                else:
                    break
            else:
                found = True

            if found:
                return cx, cy, H
    

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__=='__main__':
    n,xyh=readinput()
    ans=main(n,xyh)
    printans(ans)
