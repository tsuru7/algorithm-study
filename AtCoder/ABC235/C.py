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
    n,q=m_input()
    a=l_input()
    queries = [ l_input() for _ in range(q) ]
    return n,q,a,queries

def solve(n,q,a,queries):
    counter = dict()
    for i in range(n):
        ai = a[i]
        if ai not in counter:
            counter[ai] = [i+1]
        else:
            counter[ai].append(i+1)
    ans=[]
    for x, k in queries:
        if x not in counter:
            ans.append(-1)
        else:
            # print(f'x: {x}, k: {k}, counter[x]: {counter[x]}')
            if len(counter[x]) < k:
                ans.append(-1)
            else:
                ans.append(counter[x][k-1])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
