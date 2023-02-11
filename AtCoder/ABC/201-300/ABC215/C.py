import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations
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
    s, k = input().split()
    k = int(k)
    return s,k

def main(s,k):
    plist = sorted(list(set(list(permutations(s)))))
    ans=''.join(plist[k-1])
    # print(plist)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,k=readinput()
    ans=main(s,k)
    printans(ans)
