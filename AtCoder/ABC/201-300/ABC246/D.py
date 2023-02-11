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
    return n

def func(a, b):
    return (a+b)*(a**2+b**2)

def judge(a, b, n):
    if func(a, b) >= n:
        return True
    else:
        return False

def solve(n):
    # bmax を見つける
    b = 0
    while b**3 < n:
        b += 1
    bmax = b
    # print(f'bmax: {bmax}')
    ans = INFTY
    for bi in range(bmax+1)[::-1]:
        al = 0
        ar = bi
        if func(ar, bi) < n:
            break
        while ar - al > 0:
            # print(f'al: {al}, ar: {ar}')
            # print(f'ar: {ar}, bi: {bi}, judge: {judge(ar, bi, n)}')
            am = (al+ar)//2
            # print(f'am: {am}, bi: {bi}, judge: {judge(am, bi, n)}')
            if judge(am, bi, n):
                ar = am 
            else:
                al = am + 1
        ans = min(ans, func(ar, bi))
        # print(f'ans: {ans}, ar: {ar}, bi: {bi}, func: {func(ar,bi)}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
