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
    n,l=m_input()
    k=i_input()
    a=l_input()
    return n,l,k,a

def judge(x, sabun, k):
    count = 0
    now = 0
    for delta in sabun:
        now += delta
        if now >= x:
            count += 1
            now = 0
    if count >= k+1:
        return True
    else:
        return False


def solve(n,l,k,a):
    a.insert(0, 0)
    sabun = [a[i+1]-a[i] for i in range(n)] + [l-a[n]]
    # print(f'sabun: {sabun}')
    ac = min(sabun)
    wa = l+1
    while wa - ac > 1:
        wj = (wa+ac)//2
        result = judge(wj, sabun, k)
        # print(f'wj: {wj}, result: {result}')
        if result:
            ac = wj
        else:
            wa = wj
        
    return ac

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l,k,a=readinput()
    ans=solve(n,l,k,a)
    printans(ans)
