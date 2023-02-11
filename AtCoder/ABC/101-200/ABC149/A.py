import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s, t = input().split()
    return s, t

def main(s, t):
    return t+s

def printans(ans):
    print(ans)

if __name__=='__main__':
    s, t=readinput()
    ans=main(s, t)
    printans(ans)
