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
    k,x=m_input()
    return k,x

def main(k,x):
    if 500*k >= x:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    k,x=readinput()
    ans=main(k,x)
    printans(ans)
