import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations
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
    p=l_input()
    q=l_input()
    return n,p,q

def main(n,p,q):
    perm_list = list(permutations(range(1, n+1)))
    for i, perm in enumerate(perm_list):
        if list(perm) == p:
            a = i
        if list(perm) == q:
            b = i
    ans=abs(a-b)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p,q=readinput()
    ans=main(n,p,q)
    printans(ans)
