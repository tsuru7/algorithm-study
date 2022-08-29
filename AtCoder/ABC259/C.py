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
    ss = []
    ss.append([s[0], 1])
    for i in range(1, len(s)):
        si = s[i]
        ci, _ = ss[-1]
        if si == ci:
            ss[-1][1] += 1
        else:
            ss.append([si, 1])
    tt = []
    tt.append([t[0], 1])
    for i in range(1, len(t)):
        ti = t[i]
        ci, _ = tt[-1]
        if ti == ci:
            tt[-1][1] += 1
        else:
            tt.append([ti, 1])
    if len(ss) != len(tt):
        return 'No'
    for (si, sn), (ti, tn) in zip(ss, tt):
        if si != ti:
            return 'No'
        if sn == tn:
            continue
        if sn == 1 or tn == 1:
            return 'No'
        if tn < sn:
            return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,t=readinput()
    ans=solve(s,t)
    printans(ans)
