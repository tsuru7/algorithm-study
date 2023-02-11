import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,m=m_input()
    a=l_input()
    return n,m,a

def main(n,m,a):
    dist = [ [] for _ in range(n)]
    for idx, v in enumerate(a):
        dist[v].append(idx)
    # print(dist)
    for v in range(n):
        if len(dist[v]) == 0:
            return v
        pre = -1
        dist[v].append(n)
        # print(dist[v])
        for now in dist[v]:
            if now-1 - pre >= m:
                return v
            pre = now
    return n

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    printans(ans)
