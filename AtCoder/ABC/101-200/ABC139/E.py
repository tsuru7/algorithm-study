import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import combinations
from collections import defaultdict
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
    G = defaultdict(list)
    deg = defaultdict(int)
    for pair in combinations(range(n), 2):
        u, v = pair
        enc_pair = u*10000+v
        G[enc_pair] = []
        deg[enc_pair] = 0

    for u in range(n):
        l = l_input()
        pairs = []
        for v in l:
            v -= 1
            if u < v:
                pair = u*10000+v
            else:
                pair = v*10000+u
            pairs.append(pair)
        for i in range(len(pairs)-1):
            from_pair = pairs[i]
            to_pair = pairs[i+1]
            G[to_pair].append(from_pair)
            deg[from_pair] += 1
    return n,G,deg

def solve(n,G,deg):
    # print(f'G: {G}')
    # print(f'deg: {deg}')
    queue = deque()
    order = []
    for k, v in deg.items():
        if v == 0:
            queue.append(k)
    while len(queue) > 0:
        # print(f'queue: {queue}')
        u = queue.popleft()
        order.append(u)
        for v in G[u]:
            deg[v] -= 1
            if deg[v] == 0:
                queue.append(v)
    if len(order) < len(G):
        return -1
    order = order[::-1]
    ans=1
    count = dict()
    for pair in order:
        u, v = divmod(pair, 10000)
        if u in count or v in count:
            ans += 1
            count = dict()
        count[u] = 1
        count[v] = 1
    
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,G,deg=readinput()
    ans=solve(n,G,deg)
    printans(ans)
