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
    s = input()
    return s

def solve(s):
    stack = []
    n = len(s)
    box = set()
    setlist = [set()]
    idx = 0
    for i in range(n):
        si = s[i]
        if si == '(':
            idx += 1
            setlist.append(set())
        elif 'a' <= si <= 'z':
            if si in box:
                return 'No'
            box.add(si)
            setlist[idx].add(si)
        elif si == ')':
            box = box - setlist[idx]
            setlist.pop()
            idx -= 1
    return 'Yes'


def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
