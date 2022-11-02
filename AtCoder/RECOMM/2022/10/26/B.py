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
    conds = [l_input() for _ in range(n)]
    return n,conds

def solve(n,conds):
    for cx in range(101):
        for cy in range(101):
            h = 0
            match = True
            for xi, yi, hi in conds:
                if hi > 0:
                    tmp = hi + abs(cx-xi) + abs(cy-yi)
                    # print(f'cx: {cx}, cy: {cy}, xi: {xi}, yi: {yi}, hi: {hi}, tmp: {tmp}')
                    if h > 0:
                        if tmp != h:
                            match = False
                            break
                    else:
                        h = tmp
            if not match:
                continue
            for xi, yi, hi in conds:
                if hi == 0:
                    if h > abs(cx-xi) + abs(cy-yi):
                        match = False
                        break
            if match:
                return cx, cy, h



def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,conds=readinput()
    ans=solve(n,conds)
    printans(ans)
