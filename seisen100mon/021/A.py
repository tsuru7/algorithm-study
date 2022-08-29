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
    n=i_input()
    hslist = [ l_input() for _ in range(n) ]
    return n,hslist

def judge(x, hslist):
    times = []
    for h, s in hslist:
        t = (x - h)//s
        times.append(t)
    times.sort()
    # print(f'times: {times}')
    for i, t in enumerate(times):
        if t < i:
            return False
    return True

def solve(n,hslist):
    ans=0
    wa = 0
    ac = INFTY
    while ac - wa > 1:
        wj = (ac+wa)//2
        if judge(wj, hslist):
            # print('judge: True')
            ac = wj
        else:
            # print('judge: False')
            wa = wj
    ans = ac

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,hslist=readinput()
    ans=solve(n,hslist)
    printans(ans)
