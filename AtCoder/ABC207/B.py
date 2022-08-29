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
    a,b,c,d=m_input()
    return a,b,c,d

def main(a,b,c,d):
    if d*c-b < 1:
        return -1
    
    ans=1
    while a > (d*c-b)*ans:
        ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,d=readinput()
    ans=main(a,b,c,d)
    printans(ans)
