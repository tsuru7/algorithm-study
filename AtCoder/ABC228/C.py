import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right
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
    pmat = []
    for _ in range(n):
        pmat.append(l_input())
    return n,k,pmat

def main(n,k,pmat):
    sum3 = [0]*n
    MAXPOINT = 900
    dist = [0]*(MAXPOINT+1)
    for i in range(n):
        plist = pmat[i]
        sum3[i] = sum(plist)
        dist[sum3[i]] += 1
    cumsum = [0]*(MAXPOINT+1)
    cumsum[0] = dist[0]
    for i in range(MAXPOINT):
        cumsum[i+1] = cumsum[i]+dist[i+1]

    ans=[]
    for i in range(n):
        point = sum3[i]
        maxpoint = point+300
        # minpoint = point-300
        if maxpoint > MAXPOINT:
            hirank = 1
        else:
            hirank = n - cumsum[maxpoint] + 1
        # if minpoint < 0:
        #     lorank = n
        # else:
        #     lorank = n - cumsum[minpoint]
        # if hirank <= k <= lorank:
        if hirank <= k:
            ans.append('Yes')
        else:
            ans.append('No')

    return ans

def main2(n,k,pmat):
    sum3 = [0]*n
    for i in range(n):
        plist = pmat[i]
        sum3[i] = sum(plist)
    sum33 = sum3.copy()
    sum33.sort()
    ans = []
    for i in range(n):
        point = sum3[i]
        lo = bisect_right(sum33, point-300)
        hi = bisect_right(sum33, point+300)
        hirank = hi - n + 1
        lorank = n - lo
        print(f'lo: {lo}, hi: {hi}, lorank: {lorank}, hirank: {hirank}')
        if hirank <= k <= lorank:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans

        

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,k,pmat=readinput()
    ans=main(n,k,pmat)
    printans(ans)
