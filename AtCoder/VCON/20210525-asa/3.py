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
    a = []
    for _ in range(n):
        a.append(i_input())
    return n,a

def main(n,a):
    a.insert(0,0)
    count = 0
    i = 1
    while count < n:
        i = a[i]
        count += 1
        if i == 2:
            return count

    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
