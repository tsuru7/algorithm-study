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
    f = []
    for _ in range(n):
        f.append(l_input())
    p = []
    for _ in range(n):
        p.append(l_input())
    return n,f,p

def main(n,f,p):
    ans=-INFTY
    for i in range(1, 2**10):
        b = 1
        open = [0]*n
        for j in range(10):
            if i & b == b:
                for store in range(n):
                    if f[store][j] == 1:
                        open[store] += 1
            b *= 2
        sales = 0
        for store in range(n):
            sales += p[store][open[store]]
        # print(f'i: {bin(i)}, sales: {sales}')
        ans = max(ans, sales)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,f,p=readinput()
    ans=main(n,f,p)
    printans(ans)
