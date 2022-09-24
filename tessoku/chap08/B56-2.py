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
    n,q=m_input()
    s = input()
    queries = [l_input() for _ in range(q)]
    return n,q,s,queries

def prepare(s, b, MOD):
    '''
    英小文字からなる文字列 s のハッシュ値を b 進法(mod MOD)で計算するための準備

    返却値
    hash[i]: 1文字目からi文字目までの文字列のハッシュ値
    powb[i]: bのi乗

    '''

    n = len(s)
    powb = [1 for _ in range(n+1)]
    for i in range(1, n):
        powb[i] = (powb[i-1]*b) % MOD
    hash = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        si = s[i-1]
        hash[i] = hash[i-1]*b + ord(si) - ord('a')
        hash[i] %= MOD
    return powb, hash

def strhash(hash, powb, MOD, l, r):
    '''
    文字列 s の l 文字目から r 文字目までの部分文字列のハッシュ値を返す
    '''
    return (hash[r] - powb[r-l+1]*hash[l-1]) % MOD

def solve(n,q,s,queries):
    t = s[::-1]
    MOD = 10**9+7
    pow100, hash_s = prepare(s, 100, MOD)
    _, hash_t = prepare(t, 100, MOD)
    ans = []
    for l, r in queries:
        l2, r2 = n-r+1, n-l+1
        hash1 = strhash(hash_s, pow100, MOD, l, r)
        hash2 = strhash(hash_t, pow100, MOD, l2, r2)
        if hash1 == hash2:
            ans.append('Yes')
        else:
            ans.append('No')

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,s,queries=readinput()
    ans=solve(n,q,s,queries)
    printans(ans)
