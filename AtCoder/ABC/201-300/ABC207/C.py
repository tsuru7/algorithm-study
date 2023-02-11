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
    term = []
    for _ in range(n):
        t, l, r = m_input()
        if t == 1:
            term.append((l, r))
        elif t == 2:
            term.append((l, r-0.1))
        elif t == 3:
            term.append((l+0.1, r))
        else:
            term.append((l+0.1, r-0.1))
    return n,term

def main(n,term):
    ans=0
    for i in range(n-1):
        li = term[i][0]
        ri = term[i][1]
        for j in range(i+1, n):
            lj = term[j][0]
            rj = term[j][1]
            if ri < lj or rj < li:
                continue
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,term=readinput()
    ans=main(n,term)
    printans(ans)
