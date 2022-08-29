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

def readinput():
    s = input()
    return s

def main(s):
    t = deque()
    rev = False
    for c in s:
        if c == 'R':
            rev = not rev
        else:
            if rev:
                t.appendleft(c)
                if len(t) >= 2 and t[0] == t[1]:
                    t.popleft()
                    t.popleft()
            else:
                t.append(c)
                if len(t) >= 2 and t[-2] == t[-1]:
                    t.pop()
                    t.pop()
    if rev:
        return ''.join(t)[::-1]
    else:
        return ''.join(t)

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
