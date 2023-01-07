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
    n,m=m_input()
    a=l_input()
    return n,m,a

def solve(n,m,a):
    b = [i for i in range(n+1)]
    ones = []
    for i in range(m):
        ai = a[i]
        if b[ai] == 1:
            ones.append(b[ai+1])
        elif b[ai+1] == 1:
            ones.append(b[ai])
        else:
            ones.append(1)
        b[ai], b[ai+1] = b[ai+1], b[ai]

    # print(f'b: {b}')

    pos = [0 for _ in range(n+1)]
    for i in range(n+1):
        pos[b[i]] = i

    # print(f'pos: {pos}')

    ans=[]
    for i in range(m):
        num = ones[i]
        ans.append(pos[num])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
