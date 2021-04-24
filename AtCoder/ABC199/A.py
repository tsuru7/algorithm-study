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
    a,b,c=m_input()
    return a,b,c

def main(a,b,c):
    if a**2+b**2 < c**2:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c=readinput()
    ans=main(a,b,c)
    printans(ans)
