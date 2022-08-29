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
    n,d,h=m_input()
    dh = []
    for _ in range(n):
        dh.append(l_input())
    return n,d,h,dh

def main(n,d,h,dh):
    maxb = 0
    for di, hi in dh:
        b = h-d*(h-hi)/(d-di)
        maxb = max(maxb, b)
    return maxb

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,d,h,dh=readinput()
    ans=main(n,d,h,dh)
    printans(ans)
