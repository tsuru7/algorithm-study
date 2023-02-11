import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations

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
    sList = [list(input()) for _ in range(3)]
    return sList

def solve(sList):
    count = [0 for _ in range(26)]
    for i in range(3):
        for c in sList[i]:
            count[ord(c)-ord('a')] += 1
    nchar = 0
    chars = []
    for i in range(26):
        if count[i] > 0:
            chars.append(chr(i+ord('a')))
            nchar += 1
    if nchar > 10:
        return 'UNSOLVABLE'
    for p in permutations(range(10), nchar):
        xtbl = dict()
        for idx, d in enumerate(p):
            xtbl[chars[idx]] = str(d)
        tList = []
        for i in range(3):
            tmp = ['' for _ in range(len(sList[i]))]
            for j, c in enumerate(sList[i]):
                tmp[j] = xtbl[c]
            tList.append(''.join(tmp))
        n1 = int(tList[0])
        n2 = int(tList[1])
        n3 = int(tList[2])
        if tList[0][0] == '0' or tList[1][0] == '0' or tList[2][0] == '0':
            continue
        if n1 + n2 == n3 and n1 > 0 and n2 > 0 and n3 > 0:
            return (n1, n2, n3)
    return 'UNSOLVABLE'

def printans(ans):
    if type(ans) is tuple:
        print(*ans, sep='\n')
    else:
        print(ans)

if __name__=='__main__':
    sList=readinput()
    ans=solve(sList)
    printans(ans)
