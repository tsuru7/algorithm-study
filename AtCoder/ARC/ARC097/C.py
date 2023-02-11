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
    s = input()
    k=i_input()
    return s, k

def main(s, k):
    substr = set()
    for i in range(len(s)):
        for j in range(k):
            substr.add(s[i:i+j+1])
    ans = list(substr)
    ans.sort()
    return ans[k-1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    s, k=readinput()
    ans=main(s, k)
    printans(ans)
