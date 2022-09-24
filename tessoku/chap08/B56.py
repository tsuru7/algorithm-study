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

def solve(n,q,s,queries):
    t = s[::-1]
    # print(f't: {t}')
    MOD = 10**9+7
    pow100 = [1 for _ in range(n+1)]
    for i in range(1, n+1):
        pow100[i] = (pow100[i-1]*100) % MOD

    # hash_s[i] = b^(i-1) *s[0] + b^(i-2) *s[1] + ... + b^1 * s[i-2] + b^0 * s[i-1]
    # hash_t[i] = b^(i-1) *t[0] + b^(i-2) *t[1] + ... + b^1 * t[i-2] + b^0 * t[i-1]
    # hash_s[r]

    hash_s = [0 for _ in range(n+1)]
    hash_t = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        hash_s[i] = hash_s[i-1]*100 + ord(s[i-1]) - ord('a')
        hash_s[i] %= MOD
        hash_t[i] = hash_t[i-1]*100 + ord(t[i-1]) - ord('a')
        hash_t[i] %= MOD

    # print(f'hash_s: {hash_s}')
    # print(f'hash_t: {hash_t}')

    ans=[]
    for l, r in queries:
        # sのl文字目からr文字目
        # tのn-r+1文字目からn-l+1文字目が対応
        # print(f'l: {l}, r: {r}, n-r+1: {n-r+1}, n-l+1: {n-l+1}')
        # print(f's[l-1:r]: {s[l-1:r]}, t[n-r:n-l+1]: {t[n-r:n-l+1]}')
        hash1 = hash_s[r] - pow100[r-l+1]*hash_s[l-1]
        hash1 %= MOD
        hash2 = hash_t[n-l+1] - pow100[r-l+1]*hash_t[n-r]
        hash2 %= MOD
        # print(f'hash1: {hash1}, hash2: {hash2}')
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
