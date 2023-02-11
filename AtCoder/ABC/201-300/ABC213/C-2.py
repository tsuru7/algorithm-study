import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import Counter
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
    h,w,n=m_input()
    alist = []
    blist = []
    ab = []
    for _ in range(n):
        a, b = m_input()
        alist.append(a)
        blist.append(b)
        ab.append((a, b))
    return h,w,n,ab,alist,blist

def main(h,w,n,ab,alist,blist):
    counter_A = Counter(alist)
    counter_B = Counter(blist)
    idx_A = dict()
    for i, key in enumerate(sorted(counter_A.keys())):
        idx_A[key] = i+1
    idx_B = dict()
    for i, key in enumerate(sorted(counter_B.keys())):
        idx_B[key] = i+1
    ans = []
    for a, b in ab:
        ans.append((idx_A[a], idx_B[b]))
    return ans

def printans(ans):
    for a in ans:
        print(' '.join(map(str, a)))

if __name__=='__main__':
    h,w,n,ab,alist,blist=readinput()
    ans=main(h,w,n,ab,alist,blist)
    printans(ans)
