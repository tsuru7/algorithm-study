import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import Counter
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
    t=i_input()
    slist = []
    for _ in range(t):
        slist.append(input())
    return t, slist

def main(t, slist):
    ans=[]
    for s in slist:
        if s > 'atcoder':
            ans.append(0)
            continue
        counter = Counter(s)
        if 'a' in counter.keys() and counter['a'] == len(s):
            ans.append(-1)
        elif s[0] > 'a':
            ans.append(0)
        else:
            for i in range(1, len(s)):
                if s[i] == 'a':
                    continue
                else:
                    if s[i] <= 't':
                        ans.append(i)
                    else:
                        ans.append(i-1)
                    break
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    t, slist=readinput()
    ans=main(t, slist)
    printans(ans)
