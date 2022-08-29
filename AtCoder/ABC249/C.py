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
    n,k=m_input()
    slist = [ input() for _ in range(n) ]
    return n,k,slist

def solve(n,k,slist):
    countlist = [ [0]*26 for _ in range(n) ]
    for i, s in enumerate(slist):
        for c in s:
            idx = ord(c) - ord('a')
            countlist[i][idx] += 1
    
    # bit全探索
    ans=0
    for i in range(1, 2**n):
        acc = [0]*26
        bit = 1
        for b in range(n):
            if i & bit == bit:
                for j in range(26):
                    acc[j] += countlist[b][j]
            bit *= 2
        temp = 0
        for j in range(26):
            if acc[j] == k:
                temp += 1
        ans = max(ans, temp)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,slist=readinput()
    ans=solve(n,k,slist)
    printans(ans)
