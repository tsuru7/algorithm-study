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
    return n

def solve(n):
    s = bin(n)[2:]
    s = s[::-1]
    ones = []
    for i in range(len(s)):
        if s[i] == '1':
            ones.append(i)
    m = len(ones)
    ALL = 2**m
    ans=[]
    for x in range(ALL):
        tmp = 0
        for j in range(m):
            if x & 1<<j > 0:
                tmp += 1<<ones[j]
        ans.append(tmp)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
