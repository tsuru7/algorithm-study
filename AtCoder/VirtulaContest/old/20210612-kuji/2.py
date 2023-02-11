import sys
sys.setrecursionlimit(10**5)
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
    slist = []
    for _ in range(n):
        slist.append(input())
    return n,slist

def main(n,slist):
    group0 = set()
    group1 = set()
    for s in slist:
        if s[0] == '!':
            group1.add(s[1:])
        else:
            group0.add(s)
    group2 = group0.intersection(group1)
    if len(group2) == 0:
        return 'satisfiable'
    else:
        return list(group2)[0]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,slist=readinput()
    ans=main(n,slist)
    printans(ans)
