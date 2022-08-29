import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import defaultdict

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
    h,w=m_input()
    pmat = [l_input() for _ in range(h)]
    return h,w,pmat

def solve(h,w,pmat):
    bitcount = lambda x: bin(x).count('1')
    hALL = 2**h
    ans=0
    for hbit in range(1, hALL):
        sameval = defaultdict(int)
        for col in range(w):
            tmpset = set()
            for row in range(h):
                if hbit & 1<<row > 0:
                    tmpset.add(pmat[row][col])
            if len(tmpset) == 1:
                value = list(tmpset)[0]
                sameval[value] += 1
        # print(f'sameval: {sameval}')
        if len(sameval) == 0:
            continue
        maxcount = max(sameval.values())
        ans = max(ans, maxcount*bitcount(hbit))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,pmat=readinput()
    ans=solve(h,w,pmat)
    printans(ans)
