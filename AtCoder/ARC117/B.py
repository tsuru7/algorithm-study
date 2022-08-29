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
    heights = sorted(list(counter.keys()))
    steps = []
    prev = 0
    for height in heights:
        steps.append(height - prev)
        prev = height
    ans = 1
    for step in steps:
        ans = (ans * (step+1))%MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
