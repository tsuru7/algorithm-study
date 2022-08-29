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
    n,k=m_input()
    a=l_input()
    f=l_input()
    return n,k,a,f

def judge(wj, a, f, k):
    n = len(a)
    tmp = 0
    for i in range(n):
        fi = f[i]
        ai = a[i]
        ki = max((ai*fi-wj+fi-1)//fi, 0)
        # print(f'ai: {ai}, fi: {fi}, ki: {ki}')
        tmp += ki
    # print(f'wj: {wj}, tmp: {tmp}, k: {k}, ans: {tmp<=k}')
    return tmp <= k

def solve(n,k,a,f):
    a.sort()
    f.sort(reverse=True)
    wa = -1
    ac = 10**12
    while ac - wa > 1:
        wj = (ac+wa)//2
        if judge(wj, a, f, k):
            ac = wj
        else:
            wa = wj
    return ac

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a,f=readinput()
    ans=solve(n,k,a,f)
    printans(ans)
