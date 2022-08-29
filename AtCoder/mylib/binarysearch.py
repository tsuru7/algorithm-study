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
    n,k=m_input()
    a=l_input()
    return n,k,a

def judge(i, a, k):
    if k <= a[i]:
        return True
    else:
        return False

def main(n,k,a):
    ng = -1
    ok = n
    while ok - ng > 1:
        now = (ng+ok)//2
        if judge(now, a, k):
            ok = now
        else:
            ng = now
    if ok == n:
        return -1
    else:
        return ok

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    printans(ans)
