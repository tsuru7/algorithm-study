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
    ablist = [ l_input() for _ in range(n) ]
    return n,ablist

def solve(n,ablist):
    a = []
    b = []
    sum = 0
    for ai, bi in ablist:
        a.append(ai)
        b.append(bi)
        sum += abs(ai-bi)
    a.sort()
    b.sort()
    mid = n//2
    # print(f'a: {a}')
    # print(f'b: {b}')
    # print(f'amid: {a[mid]}, bmid: {b[mid]}')
    for i in range(n):
        sum += abs(a[i] - a[mid])
        sum += abs(b[i] - b[mid])
    return sum

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,ablist=readinput()
    ans=solve(n,ablist)
    printans(ans)
