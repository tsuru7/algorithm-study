from collections import Counter
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
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    MOD = 10**9+7
    counter = Counter(a)
    # print(counter)
    nheight = len(list(counter.keys()))
    ans = 1
    for i in range(1, nheight+1):
        ans = (ans * i)%MOD
    return ans+2

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
