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
    if n == 1:
        if a[0] == k:
            return 'Yes'
        else:
            return 'No'

    m = n//2
    head = a[:m]
    tail = a[m:]
    ALLh = 2**(len(head))
    ALLt = 2**(len(tail))
    candih = set()
    candit = set()
    for i in range(ALLh):
        tmp = 0
        for j in range(len(head)):
            b = 1<<j
            if i & b > 0:
                tmp += head[j]
        candih.add(tmp)
    for i in range(ALLt):
        tmp = 0
        for j in range(len(tail)):
            b = 1 << j
            if i & b > 0:
                tmp += tail[j]
        candit.add(tmp)
    for x in candih:
        if k - x in candit:
            return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
