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
    n,k=m_input()
    c=l_input()
    return n,k,c

def main(n,k,c):
    count = Counter(c[:k])
    ans=len(count)
    i = 1
    while i+k-1 < n:
        ci = c[i-1]
        count[ci] -= 1
        if count[ci] == 0:
            count.pop(ci)
        ci = c[i+k-1]
        if ci not in count:
            count[ci] = 1
        else:
            count[ci] += 1
        ans = max(ans, len(count))
        i += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,c=readinput()
    ans=main(n,k,c)
    printans(ans)
