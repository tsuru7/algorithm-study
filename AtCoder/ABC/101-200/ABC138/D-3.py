from collections import deque

def readinput():
    n, q = map(int, input().split())
    nList = []
    for _ in range(n+1):
        nList.append([])
    for _ in range(n-1):
        a, b = map(int, input().split())
        nList[a].append(b)
        nList[b].append(a)
    px = []
    for _ in range(q):
        px.append(list(map(int, input().split())))
    return n, q, nList, px

WHITE = 0
GRAY = 1
BLACK = 2
status = None
next = None
def dfs(u, nList, counter):
    global status
    global next

    stack = deque()
    stack.append(u)
    status[u] = GRAY
    while len(stack) > 0:
        # print(f'stack: {stack}')
        u = stack[-1]
        if next[u] >= len(nList[u]):
            v = -1
        else:
            v = nList[u][next[u]]
            next[u] += 1
        if v != -1:
            if status[v] == WHITE:
                status[v] = GRAY
                counter[v] += counter[u]
                stack.append(v)
        else:
            stack.pop()
            status[u] = BLACK
    return counter[1:]
   

def main(n, q, nList, px):
    global status
    global next

    counter = [0]*(n+1)
    for p, x in px:
        counter[p] += x
    
    status = [WHITE] * (n+1)
    next = [0] * (n+1)

    # print(nList)

    counter = dfs(1, nList, counter)

    return counter

def printans(ans):
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    n, q, nList, px = readinput()
    ans = main(n, q, nList, px)
    printans(ans)
