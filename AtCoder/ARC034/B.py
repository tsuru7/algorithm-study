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
    return n

def f(x):
    s = str(x)
    ans = 0
    for c in s:
        ans += int(c)
    return ans

def main(n):
    ans=[]
    for i in range(1, 154):
        x = n - i
        if x <= 0:
            continue
        if x + f(x) == n:
            ans.append(x)
    ans.sort()
    return ans

def printans(ans):
    print(len(ans))
    for a in ans:
        print(a)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
