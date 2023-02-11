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
    longest = max(l)
    sumedge = sum(l)
    if longest < sumedge - longest:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,l=readinput()
    ans=main(n,l)
    printans(ans)
