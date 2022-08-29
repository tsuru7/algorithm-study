import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import Counter
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
    counter = Counter(a)
    # print(f'counter: {counter}')
    ans=0
    for k, v in counter.items():
        ans += v*(n-v)
    return ans // 2

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
