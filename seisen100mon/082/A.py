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
    queries = []
    n=i_input()
    while n > 0:
        table = []
        for _ in range(n):
            table.append(input().split())
        queries.append(table)
        n = i_input()
    return queries

def sec(t):
    ans = 0
    hms = t.split(':')
    ans += int(hms[0])*60*60
    ans += int(hms[1])*60
    ans += int(hms[2])
    return ans

def solve(queries):
    ans=[]
    for table in queries:
        time = [0 for _ in range(24*60*60)]
        for s, t in table:
            time[sec(s)] += 1
            time[sec(t)] -= 1
        for t in range(1, 24*60*60):
            time[t] += time[t-1]
        ans.append(max(time))

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    queries=readinput()
    ans=solve(queries)
    printans(ans)
