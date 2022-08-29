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
    slist = []
    for _ in range(3):
        slist.append(input())
    t = input()
    return slist, t

def main(slist, t):
    ans=''
    for ti in t:
        i = int(ti)-1
        ans += slist[i]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    slist, t=readinput()
    ans=main(slist, t)
    printans(ans)
