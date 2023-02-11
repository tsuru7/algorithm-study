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
    return n,k

def main(n,k):
    # sum == 3 
    m = 3
    count = 1
    if k == count:
        return (1,1,1)
    while True:
        k -= count
        m += 1
        count = count*(m-1)//(m-3)
        if  k <= count:
            break 
    
    l = 1
    while True:
        count = m-l-1
        if k <= count:
            return (l, k, m-l-k)
        else:
            k -= count
            l += 1

def printans(ans):
    print(' '.join(map(str,ans)))

if __name__=='__main__':
    n,k=readinput()
    ans=main(n,k)
    printans(ans)
