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
    l,r=m_input()
    s = input()
    return l,r,s

def main(l,r,s):
    l -= 1
    r -= 1

    ans=s[:l] + s[l:r+1][::-1] + s[r+1:]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    l,r,s=readinput()
    ans=main(l,r,s)
    printans(ans)
