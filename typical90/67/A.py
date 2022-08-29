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
    n,k=m_input()
    return n,k

def nine(x):
    if x == 0:
        return '0'
    ans = ''
    while x > 0:
        r = x % 9
        ans += str(r)
        x //= 9
    return ans[::-1]

def solve(n,k):
    strn = str(n)
    for _ in range(k):
        strn = nine(int(strn, 8))
        strn = strn.replace('8', '5')

    return strn

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
