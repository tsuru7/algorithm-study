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
    n,k=m_input()
    a=l_input()
    return n,k,a

def main(n,k,a):
    aa = []
    for i in range(n):
        aa.append((a[i], i))
    aa.sort()
    all = k // n
    add = k % n
    ans=[]
    for i in range(n):
        ii = aa[i][1]
        if i < add:
            ans.append((all+1, ii))
        else:
            ans.append((all, ii))
    ans.sort(key=lambda x: x[1])
    return ans

def printans(ans):
    for a in ans:
        print(a[0])

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    printans(ans)
