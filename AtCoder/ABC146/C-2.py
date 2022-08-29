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
    a,b,x=m_input()
    return a,b,x

def judge(i, a, b, x):
    if a*i+b*len(str(i)) <= x:
        return True
    else:
        return False

def main(a,b,x):
    ok = 0
    ng = 10**9+1
    while ng - ok > 1:
        now = (ok+ng)//2
        if judge(now, a, b, x):
            ok = now
        else:
            ng = now
    return ok

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,x=readinput()
    ans=main(a,b,x)
    printans(ans)
