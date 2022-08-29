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
    relations = [ [] for _ in range(n) ]
    for i in range(m):
        x, y = m_input()
        x -= 1
        y -= 1
        relations[x].append(y)
    return n,m,relations

def solve(n,m,relations):
    ans=0
    for bit in range(2**n):
        # b = 1
        party = []
        for i in range(n):
            b = 1 << i
            if bit & b == b:
                party.append(i)
            # b <<= 1
        flag = True
        for p in party:
            for q in party:
                if p == q:
                    continue
                if (p < q and q in relations[p]) or (q < p and p in relations[q]):
                    continue
                else:
                    flag = False
        if flag:
            ans = max(ans, len(party))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,relations=readinput()
    ans=solve(n,m,relations)
    printans(ans)
