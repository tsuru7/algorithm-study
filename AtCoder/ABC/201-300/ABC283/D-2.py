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
        print(*args, file=sys.stderr)

def readinput():
    s = input()
    return s

def solve(s):
    stack = []
    n = len(s)
    box = set()
    stack.append(set())
    for i in range(n):
        si = s[i]
        if si == '(':
            stack.append(set())
        elif 'a' <= si <= 'z':
            if si in box:
                return 'No'
            box.add(si)
            stack[-1].add(si)
        elif si == ')':
            box = box - stack[-1]
            stack.pop()
        # print(si, stack)
    # if len(stack) > 1:
    #     return 'No'
    # else:
    #     return 'Yes'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
