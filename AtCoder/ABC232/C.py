import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations
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
    n,m=m_input()
    takahashi = [ [] for _ in range(n) ]
    aoki = [ [] for _ in range(n) ]
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        takahashi[a].append(b)
        takahashi[b].append(a)
    for _ in range(m):
        a, b = m_input()
        a -= 1
        b -= 1
        aoki[a].append(b)
        aoki[b].append(a)
    return n,m,takahashi, aoki

def main(n,m,takahashi, aoki):
    takahashi_dict = dict()
    aoki_dict = dict()
    for i in range(n):
        takahashi_dict[i] = set(takahashi[i])
        aoki_dict[i] = set(aoki[i])
    if takahashi_dict == aoki_dict:
        return 'Yes'
    for p in permutations(range(n)):
        aoki_dict = dict()
        for i in range(n):
            pi = p[i]
            aoki_dict[pi] = set()
            for b in aoki[i]:
                aoki_dict[pi].add(p[b])
        if takahashi_dict == aoki_dict:
            return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,takahashi, aoki=readinput()
    ans=main(n,m,takahashi, aoki)
    printans(ans)
