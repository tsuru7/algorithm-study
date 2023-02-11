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
    n,x=m_input()
    a=l_input()
    return n,x,a

def main(n,x,a):
    ans = 0
    bit = 1
    for i in range(n):
        if x & bit == bit:
            ans += a[i]
        bit *= 2
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,a=readinput()
    ans=main(n,x,a)
    printans(ans)
