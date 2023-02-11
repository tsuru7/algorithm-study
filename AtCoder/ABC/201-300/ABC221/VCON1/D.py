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
    abList = [l_input() for _ in range(n)]
    return n,abList

def solve(n,abList):
    logins = []
    for a, b in abList:
        logins.append((a, 1))
        logins.append((a+b, -1))
    logins.sort()
    days = [0 for _ in range(n+1)]
    pre = logins[0][0]
    count = 1
    for i in range(1, len(logins)):
        now, c = logins[i]
        days[count] += now-pre
        # print(f'count: {count}, days[count]: {days[count]}, pre: {pre}, now: {now}')
        pre = now
        count += c
    
    ans=days[1:]
    return ans

def printans(ans):
    print(*ans)

if __name__=='__main__':
    n,abList=readinput()
    ans=solve(n,abList)
    printans(ans)
