import sys
sys.setrecursionlimit(10**5)
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
    n=i_input()
    hlist = []
    for _ in range(n):
        hlist.append(i_input())
    return n,hlist

def get_s(t, hlist):
    if t == 0:
        return t
    s = t - 1
    while s >= 0 and hlist[s] < hlist[s+1]:
        s -= 1
    else:
        s += 1
    return s

def get_u(t, hist):
    n = len(hlist)
    if t == n - 1:
        return t
    u = t + 1
    while u <= n-1 and hlist[u-1] > hlist[u]:
        u += 1
    else:
        u -= 1
    return u

def main(n,hlist):
    if n == 1:
        return 1
    ans = 0
    if hlist[0] > hlist[1]:
        s = 0
        t = 0
        u = get_u(0, hlist)
        tmp = u - s + 1
        ans = max(ans, tmp)
        # print(f's: {s}, t: {t}, u: {u}, tmp: {tmp}')
    for t in range(1, n-1):
        if hlist[t-1] < hlist[t] > hlist[t+1]:
            s = get_s(t, hlist)
            u = get_u(t, hlist)
            tmp = u - s + 1
            ans = max(ans, tmp)
            # print(f's: {s}, t: {t}, u: {u}, tmp: {tmp}')
    if hlist[n-2] < hlist[n-1]:
        s = get_s(n-1, hlist)
        t = n-1
        u = n-1
        tmp = u - s  + 1
        ans = max(ans, tmp)
        # print(f's: {s}, t: {t}, u: {u}, tmp: {tmp}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,hlist=readinput()
    ans=main(n,hlist)
    printans(ans)
