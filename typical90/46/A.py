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
    a=l_input()
    b=l_input()
    c=l_input()
    return n,a,b,c

def solve(n,a,b,c):
    a46 = [0 for _ in range(46)]
    b46 = [0 for _ in range(46)]
    c46 = [0 for _ in range(46)]
    for i in range(n):
        ai = a[i]
        bi = b[i]
        ci = c[i]
        a46[ai % 46] += 1
        b46[bi % 46] += 1
        c46[ci % 46] += 1
    ans=0
    for i in range(46):
        for j in range(46):
            k = (46 - i - j) % 46
            ans += a46[i]*b46[j]*c46[k]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b,c=readinput()
    ans=solve(n,a,b,c)
    printans(ans)
