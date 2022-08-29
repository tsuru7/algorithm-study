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
    n = i_input()
    s = input()
    t = input()
    return n, s, t

def main(n, s, t):
    p = deque()
    q = deque()
    for i in range(n):
        if s[i] == '1':
            p.append(i)
        if t[i] == '1':
            q.append(i)

    if len(p) < len(q):
        return -1
    ans = 0
    while len(p) >= len(q) and len(q) > 0:
        head_p = p[0]
        head_q = q[0]
        if head_p == head_q:
            p.popleft()
            q.popleft()
        elif head_p > head_q:
            ans += head_p - head_q
            p.popleft()
            q.popleft()
        else:
            if len(p) > 1:
                next_p = p[1]
                ans += next_p - head_p
                p.popleft()
                p.popleft()
            else:
                return -1
    else:
        # print(f'p: {p}, q: {q}')
        if len(q) == len(p) == 0:
            return ans
        elif len(q) > 0:
            return -1
        else:
            while len(p) > 1:
                head = p.popleft()
                next = p.popleft()
                ans += next - head
            else:
                if len(p) > 0:
                    return -1
                else:
                    return ans

   

def printans(ans):
    print(ans)

if __name__=='__main__':
    n, s, t=readinput()
    ans=main(n, s, t)
    printans(ans)
