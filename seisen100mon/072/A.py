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
    w,h=m_input()
    return w,h

def solve(w,h):
    MOD = 10**9+7
    # (w+h)! // w!h!
    if w > h:
        w, h = h, w
    bunsi = h-1+1
    bunbo = 1
    ans=1
    for i in range(w-1):
        ans *= bunsi
        ans *= pow(bunbo, MOD-2, MOD)
        ans %= MOD
        # print(f'bunsi: {bunsi}, bunbo: {bunbo}, bunbo(MOD): {pow(bunbo, MOD-2, MOD)}, ans: {ans}')
        bunsi += 1
        bunbo += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    w,h=readinput()
    ans=solve(w,h)
    printans(ans)
