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
    n,x=m_input()
    lmap = []
    for _ in range(n):
        l = l_input()
        lmap.append((l[0], l[1:]))
    return n,x,lmap

def countup(n, lind, llen):
    for i in range(n):
        lind[i] += 1
        if lind[i] <= llen[i]:
            return lind
        lind[i] = 0
    return None
    
def main(n,x,lmap):
    llen = [ lmap[i][0]-1 for i in range(n) ]
    lnum = [ lmap[i][1] for i in range(n) ]
    lind = [0]*n
    # print(f'llen: {llen}')
    # print(f'lnum: {lnum}')
    # print(f'lind: {lind}')
    ans=0
    while lind is not None:
        prod = 1
        for i in range(n):
            prod *= lnum[i][lind[i]]
        if prod == x:
            ans += 1
        lind = countup(n, lind, llen)
        # print(f'lind: {lind}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,lmap=readinput()
    ans=main(n,x,lmap)
    printans(ans)
