import sys
sys.setrecursionlimit(10**5)
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
    n,m=m_input()
    name = input()
    kit = input()
    return n,m,name,kit

def main(n,m,name,kit):
    name_c = Counter(name)
    kit_c = Counter(kit)
    ans=0
    for k, v in name_c.items():
        if k in kit_c:
            n = kit_c[k]
            q, r = divmod(v, n)
            if r == 0:
                need = q
            else:
                need = q+1
            ans = max(ans, need)
        else:
            return -1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,name,kit=readinput()
    ans=main(n,m,name,kit)
    printans(ans)
