import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,x=m_input()
    return n,x

def get_niku(l):
    return pow(2,l+1)-1

def main(n,x):
    niku = 0
    level = n
    l = 1
    r = pow(2,n+2)-3
    while level >= 0:
        # print(level, l, r)
        m = (l+r)//2
        if x == m:
            return niku+get_niku(level-1)+1
        elif x == l:
            return niku
        elif x == r:
            return niku+get_niku(level)
        elif x > m:
            niku += get_niku(level-1)+1
            l = m+1
            r = r-1
        elif x < m:
            r = m-1
            l = l+1
        level -= 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x=readinput()
    ans=main(n,x)
    printans(ans)
