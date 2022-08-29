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
    l=input()
    return l

def solve(l):
    MOD = 10**9+7
    nbit = len(l)
    ans=3**(nbit-1)
    # print(f'nbit: {nbit}, ans: {ans}')
    x = 1<<(nbit-1)
    # print(f'x: {x}')
    while x <= int(l, 2):
        count = 0
        for i in range(nbit):
            bit = 1<<i
            if x & bit > 0:
                count += 1
        ans += pow(2, count, MOD)
        # print(f'x: {x}, count: {count}, ans: {ans}')
        x += 1

    return ans % MOD

def printans(ans):
    print(ans)

if __name__=='__main__':
    l=readinput()
    ans=solve(l)
    printans(ans)
