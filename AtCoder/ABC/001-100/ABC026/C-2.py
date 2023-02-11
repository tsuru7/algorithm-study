import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import deque
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
    graph = [[] for _ in range(n+1)]
    buka = [[] for _ in range(n+1)]
    depth = [0]*(n+1)
    depth[1] = 0
    for i in range(2, n+1):
        b = i_input()
        graph[i].append(b)
        graph[b].append(i)
        buka[b].append(i)
        depth[i] = depth[b]+1
    return n,graph,buka,depth

def main(n,graph,buka,depth):
    # print(buka)
    dp = [0]*(n+1)
    dmax = max(depth)
    group = [[] for _ in range(dmax+1)]
    for member in range(1, n+1):
        group[depth[member]].append(member)
    # print(group)
    # for member in group[dmax]:
    #     dp[member] = 1
    for d in range(0,dmax+1)[::-1]:
        for member in group[d]:
            if len(buka[member]) == 0:
                dp[member] = 1
            else:
                max_sarary = 0
                min_sarary = INFTY
                for buk in buka[member]:
                    max_sarary = max(max_sarary, dp[buk])
                    min_sarary = min(min_sarary, dp[buk])
                dp[member] = max_sarary + min_sarary + 1
            # print(f'member: {member}, sarary: {dp[member]}')
    return dp[1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,graph,buka,depth=readinput()
    ans=main(n,graph,buka,depth)
    printans(ans)
