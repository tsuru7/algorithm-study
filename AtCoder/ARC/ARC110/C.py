import sys
sys.setrecursionlimit(10**5)
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
    p=l_input()
    return n,p

def main(n,p):
    offsets = [0]*(n+1)
    nplus = 0
    nminus = 0
    for i in range(1, n+1):
        offsets[i] = i - p[i-1]
        if offsets[i] > 0:
            nplus += offsets[i]
        elif offsets[i] == 0:
            return [-1]
    if nplus != n-1:
        return [-1]
    
    ans = []
    for i in range(1, n+1):
        if offsets[i] > 0:
            for j in range(offsets[i]):
                ans.append(i-j-1)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
