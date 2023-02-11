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
    n=i_input()
    a=l_input()
    b=l_input()
    c=l_input()
    return n,a,b,c

def main(n,a,b,c):
    new_b = [b[cj-1] for cj in c]
    counter_nb = Counter(new_b)
    counter_a = Counter(a)
    ans=0
    for ai, nai in counter_a.items():
        if ai in counter_nb:
            ans += nai * counter_nb[ai]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=main(n,a,b,c)
    printans(ans)
