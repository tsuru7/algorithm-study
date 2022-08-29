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
    k,n=m_input()
    a=l_input()
    return k,n,a

def main(k,n,a):
    a.append(a[0]+k)
    dist = [0]*n
    for i in range(n):
        dist[i] = a[i+1]-a[i]
    ans = k - max(dist)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    k,n,a=readinput()
    ans=main(k,n,a)
    printans(ans)
