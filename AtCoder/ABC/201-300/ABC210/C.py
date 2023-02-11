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
    n,k=m_input()
    c=l_input()
    return n,k,c

def main(n,k,c):
    candies = {}
    for i in range(k):
        if c[i] in candies:
            candies[c[i]] += 1
        else:
            candies[c[i]] = 1
    # print(f'candies: {candies}')
    # print(len(candies))
    maxc = len(candies)
    for i in range(k,n):
        candies[c[i-k]] -= 1
        if candies[c[i-k]] == 0:
            del candies[c[i-k]]
        if c[i] in candies:
            candies[c[i]] += 1
        else:
            candies[c[i]] = 1
        maxc = max(maxc, len(candies))
    return maxc

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,c=readinput()
    ans=main(n,k,c)
    printans(ans)
