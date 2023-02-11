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
    n,q=m_input()
    lrlist = [ l_input() for _ in range(q) ]
    return n,q,lrlist

def solve(n,q,lrlist):
    # if q < n:
    #     return 'No'
    count = [0]*n
    for l, r in lrlist:
        l -= 1
        r -= 1
        count[l] += 1
        count[r] -= 1
    cumsum = count[0]
    i = 1
    while cumsum > 0 and i < n:
        cumsum += count[i]
        i += 1
    if i == n:
        return 'Yes'
    else:
        return 'No'

    ans=0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,q,lrlist=readinput()
    ans=solve(n,q,lrlist)
    printans(ans)
