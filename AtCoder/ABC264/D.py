import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

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

def solve(s):
    t = 'atcoder'
    s = list(s)
    ans=0
    for i, c in enumerate(t):
        pos = s.index(c)
        tmp = s.pop(pos)
        s.insert(i, tmp)
        ans += pos-i
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
