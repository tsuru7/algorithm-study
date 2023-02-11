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
    s = input()
    k = i_input()
    return n,s,k

def main(n,s,k):
    ans=''
    for c in s:
        if c == s[k-1]:
            ans += c
        else:
            ans += '*'
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s,k=readinput()
    ans=main(n,s,k)
    printans(ans)
