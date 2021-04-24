import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s=input()
    return s

def main(s):
    s = s[::-1]
    even = 0
    odd = 0
    for i in range(len(s)):
        if i % 2 == 0:
            odd += int(s[i])
        else:
            even += int(s[i])
    return (even, odd)

def printans(ans):
    print(ans[0], ans[1])

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
