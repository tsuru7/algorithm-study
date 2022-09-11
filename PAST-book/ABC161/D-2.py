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
    k=i_input()
    return k

def dfs(prevlist, k):
    lunlun = []
    for num in prevlist:
        last = num[-1]
        if last != '0':
            prevnum = chr(ord(last)-1)
            lunlun.append(num+prevnum)
        lunlun.append(num+last)
        if last != '9':
            nextnum = chr(ord(last)+1)
            lunlun.append(num+nextnum)
    if k < len(lunlun):
        return lunlun[k-1]
    k -= len(lunlun)
    return dfs(lunlun, k)

def solve(k):
    lunlun = [str(i) for i in range(1, 10)]
    if k < len(lunlun):
        return lunlun[k-1]
    k -= len(lunlun)
    ans = dfs(lunlun, k)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    k=readinput()
    ans=solve(k)
    printans(ans)
