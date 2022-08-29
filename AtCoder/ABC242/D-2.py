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
    s = input()
    q=i_input()
    queries = [ l_input() for _ in range(q) ]
    return s, q, queries

def f(t, k, s):
    if t == 0:
        return ord(s[k]) - ord('A')
    if k == 0:
        c = ord(s[0]) - ord('A')
        c += t
        c %= 3
        return c
    if k % 2 == 0:
        c = f(t-1, k//2, s) + 1
    else:
        c = f(t-1, (k-1)//2, s) - 1
    c %= 3
    return c

def solve(s, q, queries):
    ans=[]
    for t, k in queries:
        k -= 1
        ans.append(chr(f(t, k, s)+ord('A')))
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    s, q, queries=readinput()
    ans=solve(s, q, queries)
    printans(ans)
