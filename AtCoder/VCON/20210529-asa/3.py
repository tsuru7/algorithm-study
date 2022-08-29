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
    a=l_input()
    return n,a

def main(n,a):
    MOD = 10**9+7
    a.sort()
    b = [a[0]]
    for i in range(1, n):
        v = a[i]-a[i-1]
        if v > 0:
            b.append(v)
    ans=1
    for v in b:
        if v == 0:
            continue
        ans = (ans*(v+1))%MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
