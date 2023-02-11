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
    a=l_input()
    return n,a

def main(n,a):
    aa = []
    for i in range(n):
        aa.append(a[i] - (i+1))
    aa.sort()
    if n % 2 == 0:
        mid = n // 2
        b = aa[mid]
    else:
        mid = n // 2
        b = aa[mid]
    
    ans=0
    for i in range(n):
        ans += abs(aa[i]-b)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
