import sys
sys.setrecursionlimit(10**5)
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
    s = input()
    return n,k,s

def main(n,k,s):
    flips = [0]*n
    pre = s[0]
    flips[0] = 0
    for i in range(1, n):
        if s[i] != pre:
            flips[i] = flips[i-1]+1
            pre = s[i]
        else:
            flips[i] = flips[i-1]
    left = -1
    right = 0
    while flips[right] <= (2*k-2) and right < n:
        right += 1
    ans = right - left - 1
    while left < n:
        left += 1
        while left+1 < n and flips[left+1] == flips[left]:
            left += 1
        right = min(right+1, n-1)
        while right+1 < n and flips[right+1] == flips[right]:
            right += 1
        right += 1
        ans = max(ans, right -left - 1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,s=readinput()
    ans=main(n,k,s)
    printans(ans)
