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
    d=i_input()
    n = i_input()
    m = i_input()
    shops = [ i_input() for i in range(n-1) ]
    shops.insert(0, 0)
    shops.append(d)
    orders = [ i_input() for _ in range(m) ]
    return n,m,shops,orders

def solve(n,m,shops,orders):
    ans=0
    shops.sort()
    for order in orders:
        ac = 0
        wa = len(shops)-1
        while wa - ac > 1:
            wj = (ac+wa)//2
            if shops[wj] <= order:
                ac = wj
            else:
                wa = wj
        ans += min(order-shops[ac], shops[wa]-order)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,shops,orders=readinput()
    ans=solve(n,m,shops,orders)
    printans(ans)
