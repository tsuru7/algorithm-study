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
    d=i_input()
    n=i_input()
    atendee = [l_input() for _ in range(n)]
    return d,n,atendee

def solve(d,n,atendee):
    count = [0 for _ in range(d+2)]
    for l, r in atendee:
        count[l] += 1
        count[r+1] -= 1
    # print(f'count: {count}')
    ans=[]
    now = 0
    for i in range(d):
        now += count[i+1]
        ans.append(now)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    d,n,atendee=readinput()
    ans=solve(d,n,atendee)
    printans(ans)
