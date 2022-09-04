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
    w=i_input()
    return w

def main(w):
    ans=[]
    for i in range(1, 100):
        ans.append(i)
        ans.append(i*100)
        ans.append(i*10000)
    ans.append(1000000)
    return ans

def printans(ans):
    print(len(ans))
    print(*ans)

if __name__=='__main__':
    w=readinput()
    ans=main(w)
    printans(ans)
