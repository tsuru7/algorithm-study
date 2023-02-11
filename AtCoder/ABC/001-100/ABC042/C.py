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
    d=input().split()
    return n,k,d

def main(n,k,d):
    d = set(d)
    for p in range(100000):
        s = set(list(str(p)))
        if len(s & d) > 0:
            continue
        if p >= n:
            return p
        


def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,d=readinput()
    ans=main(n,k,d)
    printans(ans)
