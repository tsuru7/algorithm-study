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
    l=l_input()
    return n,l

def main(n,l):
    ans=0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                l1 = l[i]
                l2 = l[j]
                l3 = l[k]
                maxl = max(l1, l2, l3)
                suml = l1+l2+l3
                if 2*maxl >= suml:
                    continue
                if l1 == l2 or l2 == l3 or l3 == l1:
                    continue
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l=readinput()
    ans=main(n,l)
    printans(ans)
