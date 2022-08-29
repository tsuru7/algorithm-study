import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = True
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n=i_input()
    return n

def main(n):
    favorites = set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            r = i
            m = n//r-1
            if r < m:
                favorites.add(m)
            r = n//i
            m = n//r-1
            if r < m:
                favorites.add(m)
        i += 1
    
    # printd(favorites)
    ans=0
    for m in list(favorites):
        ans += m

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
