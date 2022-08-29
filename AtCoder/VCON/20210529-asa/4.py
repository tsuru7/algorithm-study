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
    d=l_input()
    return n,d

def main(n,d):
    MOD = 998244353
    layer = [0]*n
    if d[0] != 0:
        return 0
    max_layer = 0
    for i in range(n):
        layer[d[i]] += 1
        max_layer = max(max_layer, d[i])
    if layer[0] > 1:
        return 0
    ans=1
    for l in range(1, max_layer+1):
        if layer[l] == 0:
            return 0
        ans = (ans * pow(layer[l-1], layer[l], MOD)) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d=readinput()
    ans=main(n,d)
    printans(ans)
