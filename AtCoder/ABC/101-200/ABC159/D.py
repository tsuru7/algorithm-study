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
    n=i_input()
    a=l_input()
    return n,a

def solve(n,a):
    counter = Counter(a)
    all = 0
    for k, v in counter.items():
        all += v*(v-1)//2
    ans=[]
    for i in range(n):
        ai = a[i]
        v = counter[ai]
        tmp = all - v*(v-1)//2 + (v-1)*(v-2)//2
        ans.append(tmp)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
