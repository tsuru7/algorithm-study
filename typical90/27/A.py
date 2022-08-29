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
    sList = [input() for _ in range(n)]
    return n,sList

def solve(n,sList):
    member = set()
    ans=[]
    for i in range(n):
        si = sList[i]
        if si in member:
            continue
        member.add(si)
        ans.append(i+1)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,sList=readinput()
    ans=solve(n,sList)
    printans(ans)
