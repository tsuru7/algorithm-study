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
    n,c=m_input()
    queries = [l_input() for _ in range(n)]
    return n,c,queries

def solve(n,c,queries):
    ans = [0 for _ in range(n)]
    for bit in range(30):
        func = [0, 1]
        x = (c & 1<<bit)>>bit
        for i, [t, a] in enumerate(queries):
            abit = (a & 1<<bit)>>bit
            if t == 1:
                func = [func[0]&abit, func[1]&abit]
            elif t == 2:
                func = [func[0]|abit, func[1]|abit]
            else:
                func = [func[0]^abit, func[1]^abit]
            x = func[x]
            ans[i] |= x<<bit


    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,c,queries=readinput()
    ans=solve(n,c,queries)
    printans(ans)
