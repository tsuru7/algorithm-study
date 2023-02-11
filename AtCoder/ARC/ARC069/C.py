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
    n, m = m_input()
    return n,m

def main(n,m):
    if n > m//2:
        return m//2
    ans = n
    m -= 2*n
    ans += m // 4
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m=readinput()
    ans=main(n,m)
    printans(ans)
