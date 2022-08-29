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
    s = input()
    q=i_input()
    queries = [ l_input() for _ in range(q) ]
    return s,q,queries

def solve(s,q,queries):
    ans=[]
    for t, k in queries:
        k -= 1
        count = 0
        residues = []
        while True:
            if count == t:
                break
            if k & 1 == 1:
                residues.append(1)
            else:
                residues.append(0)
            k >>= 1
            count += 1
        print(f'k: {k}, t: {t}, count: {count}, ans: {ans}')
        c = s[k] 
        n = ord(c) - ord('A')
        for x in residues[::-1]:
            if x == 0:
                n = (n+1) % 3
            else:
                n = (n-1) % 3
        c = chr(ord('A')+n)
        ans.append(c)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    s,q,queries=readinput()
    ans=solve(s,q,queries)
    printans(ans)
