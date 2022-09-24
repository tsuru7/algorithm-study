# ABC161-D
# https://atcoder.jp/contests/ABC161/tasks/ABC161_D
 
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
    k=i_input()
    return k

def dfs(pres, k):
    now = []
    for pre in pres:
        lastd = pre % 10
        if lastd-1 >= 0:
            now.append(pre*10+lastd-1)
        now.append(pre*10+lastd)
        if lastd+1 <= 9:
            now.append(pre*10+lastd+1)
    # print(f'k: {k}, now: {now}')
    if len(now) > k:
        return now[k]
    return dfs(now, k-len(now))

def solve(k):
    k -= 1
    now = [i for i in range(1, 10)]
    if k < 10:
        return now[k]
    ans=dfs(now, k-len(now))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    k=readinput()
    ans=solve(k)
    printans(ans)
