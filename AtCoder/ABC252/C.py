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
    slist = [ input() for _ in range(n) ]
    return n,slist

def solve(n,slist):
    numbers = [ [0]*10 for _ in range(10) ]
    for s in slist:
        for i, c in enumerate(s):
            n = int(c)
            numbers[n][i] += 1

    # print(*numbers, sep='\n')
    ans=INFTY
    for n in range(10):
        maxn = 0
        maxi = 0
        for i in range(10):
            if maxn <= numbers[n][i]:
                maxn = numbers[n][i]
                maxi = i
        ans = min(ans, (maxn-1)*10+maxi)
        # print(f'n: {n}, maxn: {maxn}, maxi: {maxi}, ans: {ans}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,slist=readinput()
    ans=solve(n,slist)
    printans(ans)
