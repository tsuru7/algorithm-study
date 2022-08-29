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
    n,k=m_input()
    ablist = []
    for _ in range(n):
        ablist.append(l_input())
    return n,k,ablist

def main(n,k,ablist):
    ablist.sort(key=lambda x:x[0])
    wallet = k
    now = 0
    for a, b in ablist:
        wallet -= (a-now)
        if wallet < 0:
            return a+wallet
        wallet += b
        now = a
    ans = now + wallet
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,ablist=readinput()
    ans=main(n,k,ablist)
    printans(ans)
