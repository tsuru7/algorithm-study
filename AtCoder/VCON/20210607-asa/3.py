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
    q=i_input()
    qlist = []
    for _ in range(q):
        tmp = input().split()
        if len(tmp) == 1:
            qlist.append([int(tmp[0])])
        else:
            qlist.append([int(tmp[0]), int(tmp[1]), tmp[2]])
    return s,q,qlist

def main(s,q,qlist):
    ans = deque(s)
    flip = False
    for tmp in qlist:
        if len(tmp) == 1:
            flip = not flip
        else:
            t, f, c = tmp
            if (flip and f == 1) or (not flip and f == 2):
                ans.append(c)
            else:
                ans.appendleft(c)
    ans = ''.join(ans)
    if flip:
        ans = ans[::-1]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,q,qlist=readinput()
    ans=main(s,q,qlist)
    printans(ans)
