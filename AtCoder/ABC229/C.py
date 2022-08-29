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
    n,w=m_input()
    ablist = []
    for _ in range(n):
        ablist.append(l_input())
    return n,w,ablist

def main(n,w,ablist):
    ablist.sort(key=lambda x: x[0], reverse=True)
    weight = 0
    delicious = 0
    for i in range(n):
        ai, bi = ablist[i]
        if weight + bi <= w:
            delicious += ai*bi
            weight += bi
        else:
            rest = w - weight
            weight += rest
            delicious += ai*rest
    return delicious

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,w,ablist=readinput()
    ans=main(n,w,ablist)
    printans(ans)
