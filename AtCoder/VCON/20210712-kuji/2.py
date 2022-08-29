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
    n=i_input()
    p=l_input()
    return n,p

def main(n,p):
    min_value = p[0]
    count = 1
    for i in range(1, n):
        min_value = min(min_value, p[i])
        if min_value >= p[i]:
            count += 1
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
