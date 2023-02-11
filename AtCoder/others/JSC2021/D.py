import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,p=m_input()
    return n,p

def main(n,p):
    MOD = 10**9+7
    ans = ((p-1) * pow(p-2, n-1, MOD))%MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
