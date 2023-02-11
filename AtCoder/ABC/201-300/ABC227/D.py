import sys
sys.setrecursionlimit(10**6)
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
    ac = 0
    wa = INFTY
    while wa - ac > 1:
        p = (wa+ac)//2
        if judge(p, k, a):
            ac = p
        else:
            wa = p
    ans=ac
    return ans

def judge(p, k, a):
    sum = 0
    for i in range(len(a)):
        sum += min(p, a[i])
    if sum < k*p:
        return False
    else:
        return True


def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=main(n,k,a)
    printans(ans)
