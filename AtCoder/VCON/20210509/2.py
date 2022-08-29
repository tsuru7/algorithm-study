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
    ab = []
    for _ in range(n):
        ab.append(l_input())
    return n,ab

def main(n,ab):
    ans=0
    for a, b in ab:
        ans += (a+b)*(b-a+1)//2
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    printans(ans)
