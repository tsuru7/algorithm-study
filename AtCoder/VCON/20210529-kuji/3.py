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
    a=l_input()
    return n,a

def main(n,a):
    two = 0
    four = 0
    odd = 0
    for i in range(n):
        if a[i] % 2 != 0:
            odd += 1
        elif a[i] % 4 == 0:
            four += 1
        else:
            two += 1
    if two + four == n:
        return 'Yes'
    elif n % 2 == 0 and odd <= four:
        return 'Yes'
    elif n % 2 == 1:
        if odd == (n+1)//2 and four == (n-1)//2:
            return 'Yes'
        elif odd < (n+1)//2 and odd <= four:
            return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
