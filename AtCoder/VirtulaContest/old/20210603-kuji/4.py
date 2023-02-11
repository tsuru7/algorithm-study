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
    return s

def main(s):
    n = len(s)
    ans=0
    for i in range(2**(n-1)):
        term = s[0]
        sum = 0
        b = 1
        for j in range(n-1):
            if i & b == b:
                sum += int(term)
                term = s[j+1]
            else:
                term += s[j+1]
            b *= 2
        sum += int(term)
        ans += sum
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
