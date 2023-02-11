from collections import deque

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    f=l_input()
    return n,f

WHITE = 0
GRAY = 1
BLACK = 2
status = None
def bfs(u, nList):
    global status

    queue = deque()
    queue.append(u)
    while len(queue) > 0:
        u = queue.popleft()
        for v in nList[u]:
            if status[v] == WHITE:
                queue.append(v)
                status[v] = GRAY
        status[u] = BLACK
    return

def main(n,f):
    global status

    f.insert(0, 0)
    nList = []
    for _ in range(n+1):
        nList.append([])
    for i in range(1, n+1):
        j = f[i]
        nList[i].append(j)
        nList[j].append(i)

    status = [WHITE] * (n+1)
    count = 0
    for i in range(1, n+1):
        if status[i] == WHITE:
            bfs(i, nList)
            count += 1

    MOD = 998244353
    ans = pow(2, count, MOD) - 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,f=readinput()
    ans=main(n,f)
    printans(ans)
