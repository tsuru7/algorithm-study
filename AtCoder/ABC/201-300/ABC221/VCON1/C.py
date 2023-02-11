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
    s = str(n)
    m = len(s)
    ALL = 2**m
    ans = 0
    for x in range(1, ALL-1):
        grp1 = []
        grp2 = []
        for j in range(m):
            bit = 1<<j
            if x & bit > 0:
                grp1.append(int(s[j]))
            else:
                grp2.append(int(s[j]))
        grp1.sort(reverse=True)
        grp2.sort(reverse=True)
        if grp1[0] == 0 or grp2[0] == 0:
            continue
        num1 = 0
        for n in grp1:
            num1 *= 10
            num1 += n
        num2 = 0
        for n in grp2:
            num2 *= 10
            num2 += n
        ans = max(ans, num1*num2)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
