import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop

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
    c = l_input()
    q = i_input()
    queries = [ input().split() for _ in range(q) ]
    return n,c,q,queries

def solve(n,c,q,queries):
    c.insert(0,0)
    min_even = INFTY
    for i in range(2, n+1, 2):
        if min_even > c[i]:
            min_even = c[i]
    min_odd = INFTY
    for i in range(1, n+1, 2):
        if min_odd > c[i]:
            min_odd = c[i]
    # print(f'min_even: {min_even}, min_odd: {min_odd}')
    n_odd = (n+1)//2
    matome_o = 0
    matome_e = 0
    ans=0
    for query in queries:
        # print(f'query: {query}')
        # print(*c)
        if query[0] == '1':
            x = int(query[1])
            a = int(query[2])
            if x % 2 == 0:
                if c[x] - matome_e < a:
                    continue
            else:
                if c[x] - matome_o < a:
                    continue
            c[x] -= a
            ans += a
            if x % 2 == 0:
                if c[x] < min_even:
                    min_even = c[x]
            else:
                if c[x] < min_odd:
                    min_odd = c[x]
        elif query[0] == '2':
            a = int(query[1])
            if min_odd - matome_o < a:
                continue
            ans += a * n_odd
            matome_o += a
            # print(f'ans: {ans}, matome_o: {matome_o}')
        else:
            a = int(query[1])
            if min_odd - matome_o < a or min_even - matome_e < a:
                continue
            ans += a * n
            matome_o += a
            matome_e += a
            # print(f'ans: {ans}, matome_o: {matome_o}, matome_e: {matome_e}')

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,c,q,queries=readinput()
    ans=solve(n,c,q,queries)
    printans(ans)
