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
    s,t=m_input()
    return s,t

def main(s,t):
    ans=0
    for a in range(101):
        for b in range(101):
            for c in range(101):
                if a+b+c > s:
                    continue
                if a*b*c > t:
                    continue
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s,t=readinput()
    ans=main(s,t)
    printans(ans)
