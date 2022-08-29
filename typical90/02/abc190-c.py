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
    n,m=m_input()
    abList = [l_input() for _ in range(m)]
    k=i_input()
    cdList = [l_input() for _ in range(k)]
    return n,m,abList,k,cdList

def solve(n,m,abList,k,cdList):
    ALL = 2**k
    ans=0
    for x in range(ALL):
        dishes = [0 for _ in range(n)]
        for bit in range(k):
            c, d = cdList[bit]
            c -= 1
            d -= 1
            b_ = 1<<bit
            if x & b_ == 0:
                dishes[c] += 1
            else:
                dishes[d] += 1
        satisfied = 0
        for a, b in abList:
            a -= 1
            b -= 1
            if dishes[a] > 0 and dishes[b] > 0:
                satisfied += 1
        ans = max(ans, satisfied)   
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,abList,k,cdList=readinput()
    ans=solve(n,m,abList,k,cdList)
    printans(ans)
