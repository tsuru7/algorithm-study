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
    return n

def solve(n):
    ans=[str(n)+':']
    x = n
    while x > 0 and x % 2 == 0:
        ans.append(str(2))
        x //= 2
    i = 3
    while i*i <= n:
        while x > 0 and x % i == 0:
            ans.append(str(i))
            x //= i
        i += 2
    if x > 1:
        ans.append(str(x))
    return ' '.join(ans)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
