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
    a=l_input()
    return a

def main(a):
    a1, a2, a3 = a
    ans=INFTY
    ans = min(ans, abs(a2-a1)+abs(a3-a2))  # 1, 2, 3
    ans = min(ans, abs(a3-a1)+abs(a2-a3))  # 1, 3, 2
    ans = min(ans, abs(a1-a2)+abs(a3-a1))  # 2, 1, 3
    ans = min(ans, abs(a3-a2)+abs(a1-a3))  # 2, 3, 1
    ans = min(ans, abs(a1-a3)+abs(a2-a1))  # 3, 1, 2
    ans = min(ans, abs(a2-a3)+abs(a1-a2))  # 3, 2, 1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a=readinput()
    ans=main(a)
    printans(ans)
