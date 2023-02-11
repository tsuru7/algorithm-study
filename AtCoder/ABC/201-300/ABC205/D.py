import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from bisect import bisect_left
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
    a=l_input()
    klist = []
    for _ in range(q):
        klist.append(i_input())
    return n,q,a,klist

def main(n,q,a,klist):
    prevs = []
    for i in range(n):
        v = a[i]
        prevs.append(a[i] - (i+1))

    # print(f'prevs: {prevs}')

    ans=[]
    for k in klist:
        i = bisect_left(prevs, k)
        if i == n:
            v = k-prevs[n-1] + a[n-1]
        else:
            v = a[i] - (prevs[i]-k+1)
        ans.append(v)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,q,a,klist=readinput()
    ans=main(n,q,a,klist)
    printans(ans)
