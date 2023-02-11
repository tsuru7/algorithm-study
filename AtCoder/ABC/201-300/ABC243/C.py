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
    n=i_input()
    xylist = [ l_input() for _ in range(n) ]
    s = input()
    return n,xylist,s

def solve(n,xylist,s):
    l = dict()
    r = dict()
    for i in range(n):
        x, y = xylist[i]
        c = s[i]
        if c == 'L':
            if y not in l:
                l[y] = [x]
            else:
                l[y].append(x)
        else:
            if y not in r:
                r[y] = [x]
            else:
                r[y].append(x)

    for y, xlist_l in l.items():
        if y not in r:
            continue
        xlist_l.sort(reverse=True)
        xlist_r = r[y]
        xlist_r.sort()
        if xlist_r[0] < xlist_l[0]:
            return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xylist,s=readinput()
    ans=solve(n,xylist,s)
    printans(ans)
