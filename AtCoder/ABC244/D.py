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
    s = input().split()
    t = input().split()
    return s,t

def solve(s,t):
    if t == s or t == [s[1], s[2], s[0]] or t == [s[2], s[0], s[1]]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,t=readinput()
    ans=solve(s,t)
    printans(ans)
