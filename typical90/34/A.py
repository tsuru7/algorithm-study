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
    n,k=m_input()
    a=l_input()
    return n,k,a

def solve(n,k,a):
    head = 0
    tail = 0
    numdict = dict()
    numdict[a[0]] = 1
    maxlen = 1
    while True:
        while len(numdict) <= k:
            maxlen = max(maxlen, head-tail+1)
            head += 1
            if head >= n:
                break
            if a[head] in numdict:
                numdict[a[head]] += 1
            else:
                numdict[a[head]] = 1
            # print(f'head: {head}')
        while len(numdict) > k:
            numdict[a[tail]] -= 1
            if numdict[a[tail]] == 0:
                numdict.pop(a[tail])
            tail += 1
            if tail >= head:
                break
            # print(f'tail: {tail}')
        
        if head >= n:
            return maxlen

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
