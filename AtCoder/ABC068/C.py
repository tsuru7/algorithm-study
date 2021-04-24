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
    n,m=m_input()
    ab = []
    for _ in range(m):
        ab.append(l_input())
    return n,m,ab

def main(n,m,ab):
    nlist = [ [] for _ in range(n)]
    for a, b in ab:
        nlist[a-1].append(b-1)
        nlist[b-1].append(a-1)
    for i in range(1, n-1):
        if 0 in nlist[i] and n-1 in nlist[i]:
            return 'POSSIBLE'
    return 'IMPOSSIBLE'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,ab=readinput()
    ans=main(n,m,ab)
    printans(ans)
