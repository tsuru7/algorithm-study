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
    h1, h2, h3, w1, w2, w3=m_input()
    return h1,h2,h3,w1,w2,w3

def solve(h1,h2,h3,w1,w2,w3):
    ans=0
    for a11 in range(1, 29):
        for a12 in range(1, 29):
            for a21 in range(1, 29):
                for a22 in range(1, 29):
                    a13 = h1 - a11 - a12
                    a23 = h2 - a21 - a22
                    a31 = w1 - a11 - a21
                    a32 = w2 - a12 - a22
                    if a13 <= 0 or a23 <= 0 or a31 <= 0 or a32 <= 0:
                        continue
                    a33 = h3 - a31 - a32
                    if a33 <= 0:
                        continue
                    if a33 == w3 - a13 - a23:
                        ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h1,h2,h3,w1,w2,w3=readinput()
    ans=solve(h1,h2,h3,w1,w2,w3)
    printans(ans)
