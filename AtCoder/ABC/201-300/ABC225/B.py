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
    n=i_input()
    ab = []
    for _ in range(n-1):
        a, b = m_input()
        a -= 1
        b -= 1
        ab.append([a,b])
    return n,ab

def main(n,ab):
    apex = [0]*n
    for a, b in ab:
        apex[a] += 1
        apex[b] += 1
    root = 0
    leaf = 0
    for i in range(n):
        if apex[i] == 1:
            leaf += 1
        elif apex[i] == n-1:
            root += 1
    if root == 1 and leaf == n-1:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,ab=readinput()
    ans=main(n,ab)
    printans(ans)
