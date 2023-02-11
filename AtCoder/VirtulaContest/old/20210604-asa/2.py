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
    s = input()
    return s

def main(s):
    counter = Counter(s)
    ans = []
    for c in 'ABCDEF':
        ans.append(counter[c])
    return ans

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
