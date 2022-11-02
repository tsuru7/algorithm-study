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
    a,b=m_input()
    return a,b

def f0(x):
    ans = 0
    keta = 0
    while keta < 42:
        num_one = (x+1)//2**(keta+1) * 2**keta
        num_one += max((x+1)%2**(keta+1)-2**keta, 0)
        if num_one % 2 == 1:
            ans += 2**keta
        keta += 1
    return ans

def f00(x):
    num_pair = (x+1) // 2
    if (x+1) % 2 == 0:
        if num_pair % 2 == 0:
            return 0
        else:
            return 1
    else:
        if num_pair % 2 == 0:
            return x
        else:
            return 1^x

def solve(a,b):
    if a == 0:
        return f00(b)
    
    return f00(b)^f00(a-1)

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=solve(a,b)
    printans(ans)
