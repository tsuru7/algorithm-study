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
    n=i_input()
    a=l_input()
    return n,a

def solve(n,a):
    nums = set()
    for i in range(n):
        nums.add(a[i])
    numslist = list(nums)
    numslist.sort()
    comp_dict = dict()
    for i, x in enumerate(numslist):
        comp_dict[x] = i+1
    b = [0 for _ in range(n)]
    for i in range(n):
        ai = a[i]
        bi = comp_dict[ai]
        b[i] = bi
    return b

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
