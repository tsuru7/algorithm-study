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
    s=l_input()
    return n,s

def main(n,s):
    candidates = set()
    for a in range(1, 144):
        for b in range(1, 144):
            candidates.add(4*a*b + 3*a + 3*b)
    ans=0
    for si in s:
        if si not in candidates:
            ans += 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    printans(ans)
