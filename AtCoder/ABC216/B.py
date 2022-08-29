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
    names = []
    n=i_input()
    for _ in range(n):
        s, t = input().split()
        names.append([s,t])
    return n,names

def main(n,names):
    for i in range(n-1):
        si, ti = names[i]
        for j in range(i+1, n):
            sj, tj = names[j]
            if si == sj and ti == tj:
                return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,names=readinput()
    ans=main(n,names)
    printans(ans)
