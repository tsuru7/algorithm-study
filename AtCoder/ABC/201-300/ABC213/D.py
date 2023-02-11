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
    n=i_input()
    nList = []
    for _ in range(n):
        nList.append([])
    for _ in range(n-1):
        a,b=m_input()
        a -= 1
        b -= 1
        nList[a].append(b)
        nList[b].append(a)
    return n,nList

def dfs(u, nList, visited, visit_list):
    visit_list.append(u+1)
    visited[u] = True
    leaf = True
    for v in sorted(nList[u]):
        if visited[v]:
            continue
        else:
            leaf = False
            dfs(v, nList, visited, visit_list)
            visit_list.append(u+1)
    # if not leaf:
    #     visit_list.append(u+1)
    return

def main(n,nList):
    visited = [False]*n
    visit_list = []
    dfs(0, nList, visited, visit_list)
    return visit_list

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__=='__main__':
    n,nList=readinput()
    ans=main(n,nList)
    printans(ans)
