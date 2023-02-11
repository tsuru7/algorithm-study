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
    t = input()
    return s,t

def solve(s,t):
    offset = (ord(t[0]) - ord(s[0])) % 26
    for i in range(1, len(s)):
        if ord(t[i]) - ord('a') == (ord(s[i]) - ord('a') + offset) % 26:
            continue
        else:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,t=readinput()
    ans=solve(s,t)
    printans(ans)
