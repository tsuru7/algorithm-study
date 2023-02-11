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
    s = input()
    return s

def main(s):
    t = deque()
    toggle = False
    for c in s:
        if c == 'R':
            toggle = not toggle
        else:
            if toggle:
                if len(t) > 0 and c == t[0]:
                    t.popleft()
                else:
                    t.appendleft(c)
            else:
                if len(t) > 0 and c == t[-1]:
                    t.pop()
                else:
                    t.append(c)
    t = ''.join(list(t))
    if toggle:
        t = t[::-1]
    return t

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
