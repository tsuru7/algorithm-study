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
    return n

def make_standard(n):
    if n == 1:
        return ['a']
    ans = []
    sub = make_standard(n-1)
    for s in sub:
        counter = Counter(s)
        m = len(counter)
        for i in range(m+1):
            ans.append(s+chr(ord('a')+i))
    return ans


def main(n):
    return make_standard(n)

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
