import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate

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
    m,n=m_input()
    k=i_input()
    smap = [input() for _ in range(m)]
    areas = [l_input() for _ in range(k)]
    return n,m,k,smap,areas

def solve(n,m,k,smap,areas):
    jmap = [[int(smap[row][col]=='J') for col in range(n)] for row in range(m)]
    omap = [[int(smap[row][col]=='O') for col in range(n)] for row in range(m)]
    imap = [[int(smap[row][col]=='I') for col in range(n)] for row in range(m)]
    # print(f'jmap: {jmap}')
    jcum = [[0]+list(accumulate(jmap[row])) for row in range(m)]
    ocum = [[0]+list(accumulate(omap[row])) for row in range(m)]
    icum = [[0]+list(accumulate(imap[row])) for row in range(m)]
    jcumt = list(zip(*jcum))
    icumt = list(zip(*icum))
    ocumt = list(zip(*ocum))
    # print(f'jcumt: {jcumt}')
    jcum2t = [[0]+list(accumulate(jcumt[col])) for col in range(n+1)]
    ocum2t = [[0]+list(accumulate(ocumt[col])) for col in range(n+1)]
    icum2t = [[0]+list(accumulate(icumt[col])) for col in range(n+1)]
    jcum2 = list(zip(*jcum2t))
    ocum2 = list(zip(*ocum2t))
    icum2 = list(zip(*icum2t))
    # print(f'jcum2: {jcum2}')

    ans=[]
    for a, b, c, d in areas:
        tmp = [0,0,0]
        tmp[0] += jcum2[c][d]-jcum2[a-1][d]-jcum2[c][b-1]+jcum2[a-1][b-1]
        tmp[1] += ocum2[c][d]-ocum2[a-1][d]-ocum2[c][b-1]+ocum2[a-1][b-1]
        tmp[2] += icum2[c][d]-icum2[a-1][d]-icum2[c][b-1]+icum2[a-1][b-1]
        ans.append(tmp)
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,m,k,smap,areas=readinput()
    ans=solve(n,m,k,smap,areas)
    printans(ans)
