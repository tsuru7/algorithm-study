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
    p=l_input()
    return n,p

def main(n,p):
    p.insert(0,0)
    ans=0
    for i in range(2, n+1)[::-1]:
        # print(f'i: {i}, p[i]: {p[i]}')
        if p[i] == i:
            p[i-1], p[i] = p[i], p[i-1]
            ans += 1
    if p[1] == 1:
        ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
