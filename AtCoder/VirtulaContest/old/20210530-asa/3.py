import sys
sys.setrecursionlimit(10**5)
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
    n,m=m_input()
    sclist = []
    for _ in range(m):
        sclist.append(l_input())
    return n,m,sclist

def main(n,m,sclist):
    dist = [-1]*(n+1)
    for s, c in sclist:
        if dist[s] != -1 and dist[s] != c:
            return -1
        else:
            dist[s] = c
    if n > 1 and dist[1] == 0:
        return -1
    # print(dist)
    ans=''
    for i in range(1, n+1):
        if i == 1 and dist[i] == -1 and n != 1:
            ans += '1'
            continue
        if dist[i] != -1:
            ans += str(dist[i])
        else:
            ans += '0'

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,sclist=readinput()
    ans=main(n,m,sclist)
    printans(ans)
