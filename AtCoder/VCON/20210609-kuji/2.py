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
    t=i_input()
    nlist = []
    for _ in range(t):
        nlist.append(i_input())
    return t,nlist

def main(t,nlist):
    ans = []
    for n in nlist:
        if n % 2 == 1:
            ans.append('Odd')
        elif n % 4 == 0:
            ans.append('Even')
        else:
            ans.append('Same')
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    t,nlist=readinput()
    ans=main(t,nlist)
    printans(ans)
