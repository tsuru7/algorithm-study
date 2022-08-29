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
    p=l_input()
    return p

def main(p):
    ans=''
    for i in range(26):
        c = chr(p[i]-1 + ord('a'))
        ans += c
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    p=readinput()
    ans=main(p)
    printans(ans)
