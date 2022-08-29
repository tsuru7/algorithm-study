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
    ss = s[0]+s[1]
    tt = t[0]+t[1]
    for i in range(2, len(s)):
        si = s[i]
        if si == ss[-1] and si == ss[-2]:
            continue
        else:
            ss += si
    for i in range(2, len(t)):
        ti = t[i]
        if ti == tt[-1] and ti == tt[-2]:
            continue
        else:
            tt += ti
        
    if ss == tt:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,t=readinput()
    ans=solve(s,t)
    printans(ans)
