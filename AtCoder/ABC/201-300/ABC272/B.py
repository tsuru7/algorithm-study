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
    members = [l_input() for _ in range(m)]
    return n,m,members

def solve(n,m,members):
    atendee = [[False for _ in range(n)] for _ in range(m)]
    for party, member in enumerate(members):
        for mm in member[1:]:
            atendee[party][mm-1] = True

    # print(*atendee, sep='\n')

    ans=True
    for i in range(n):
        for j in range(i+1, n):
            meet = False
            for party in range(m):
                # print(f'i: {i}, j: {j}, party: {party}')
                if atendee[party][i] and atendee[party][j]:
                    meet = True
                    break
            ans = ans and meet
    if ans:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,members=readinput()
    ans=solve(n,m,members)
    printans(ans)
