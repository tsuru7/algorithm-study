import sys
sys.setrecursionlimit(10**6)
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
    k=i_input()
    return k

def bfs(k):
    queue = deque()
    queue.append(0)
    count = 0
    while len(queue) > 0:
        # print(f'count: {count}, queue: {queue}')
        u = queue.popleft()
        if u == 0:
            for i in range(1, 10):
                queue.append(i)
                count += 1
                if count == k:
                    return i
        else:
            d = u % 10
            if d-1 >= 0:
                queue.append(u*10+d-1)
                count += 1
                if count == k:
                    return u*10+d-1

            queue.append(u*10+d)
            count += 1
            if count == k:
                return u*10+d

            if d+1 <= 9:
                queue.append(u*10+d+1)
                count += 1
                if count == k:
                    return u*10+d+1

def solve(k):
    ans = bfs(k)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    k=readinput()
    ans=solve(k)
    printans(ans)
