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
    a=i_input()
    b = i_input()
    c = i_input()
    x = i_input()
    return a,b,c,x

def main(a,b,c,x):
    ans=0
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if 500*i + 100*j + 50*k == x:
                    ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,x=readinput()
    ans=main(a,b,c,x)
    printans(ans)
