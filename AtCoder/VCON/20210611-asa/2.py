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
    words = input().split()
    return n,words

def main(n,words):
    words[n-1] = words[n-1][:-1]
    ans=0
    for word in words:
        if word in ('TAKAHASHIKUN', 'Takahashikun', 'takahashikun'):
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,words=readinput()
    ans=main(n,words)
    printans(ans)
