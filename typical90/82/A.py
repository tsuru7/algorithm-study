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
    l,r=m_input()
    return l,r

def solve(l,r):
    MOD = 10**9+7
    inv2 = pow(2, MOD-2, MOD)

    l_keta = len(str(l))
    r_keta = len(str(r))

    if l_keta == r_keta:
        keta_cnt = r - l + 1
        m = (((l+r))*keta_cnt*inv2) % MOD
        ans = m*l_keta % MOD
        return ans

    l_keta_cnt = 10**l_keta - l
    r_keta_cnt = r - 10**(r_keta-1) + 1

    # print(f'l_keta: {l_keta}, r_keta: {r_keta}')

    ans=0
    l_start = l
    l_end = 10**l_keta-1
    m = (((l_start+l_end) ) *l_keta_cnt*inv2) % MOD
    ans += m*l_keta % MOD
    ans %= MOD

    for keta in range(l_keta+1, r_keta):
        keta_start = 10**(keta-1)
        keta_end = 10**keta-1
        keta_cnt = keta_end - keta_start + 1
        m = (((keta_start+keta_end) ) * keta_cnt*inv2) % MOD
        ans += m*keta % MOD
        ans %= MOD

    r_start = 10**(r_keta-1)
    r_end = r
    m = (((r_start+r_end) ) * r_keta_cnt*inv2) % MOD
    ans += m * r_keta % MOD
    ans %= MOD

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    l,r=readinput()
    ans=solve(l,r)
    printans(ans)
