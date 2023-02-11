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
    x,y,z,k=m_input()
    a=l_input()
    b=l_input()
    c=l_input()
    return x,y,z,k,a,b,c

def main(x,y,z,k,a,b,c):
    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i]+b[j])
    ab.sort(reverse=True)
    abc = []
    for i in range(min(x*y, k)):
        for j in range(z):
            abc.append(ab[i]+c[j])
    abc.sort(reverse=True)
    ans=abc[:k]
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    x,y,z,k,a,b,c=readinput()
    ans=main(x,y,z,k,a,b,c)
    printans(ans)
