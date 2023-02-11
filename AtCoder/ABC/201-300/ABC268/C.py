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
    p=l_input()
    return n,p

def solve(n,p):
    deli = [0 for _ in range(n)]
    for i in range(n):
        j = (p[i] - i) % n
        deli[j] += 1
    sum = deli[0]+deli[1]+deli[2]
    ans = sum
    for i in range(n):
        sum -= deli[i]
        sum += deli[(i+3)%n]
        ans = max(ans, sum)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=solve(n,p)
    printans(ans)
