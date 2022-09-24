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
    hash = [0 for _ in range(n)]
    pow100 = [0 for _ in range(n+1)]
    MOD = 10**9+7
    # bi = 100**i mod MOD
    pow100[0] = 1
    for i in range(1, n+1):
        pow100[i] = pow100[i-1]*100
        pow100[i] %= MOD
    hash[0] = ord(s[0]) - ord('a')
    for i in range(1, n):
        hash[i] = hash[i-1]*100 + ord(s[i]) - ord('a')
        hash[i] %= MOD
    hash.insert(0, 0)
    # print(f'hash: {hash}')
    ans=[]
    for a,b,c,d in queries:
        hash_ab = hash[b] - pow100[b-a+1]*hash[a-1]
        hash_ab %= MOD
        hash_cd = hash[d] - pow100[d-c+1]*hash[c-1]
        hash_cd %= MOD
        # print(f'hash_ab: {hash_ab}, hash_cd: {hash_cd}')
        if hash_ab == hash_cd:
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
