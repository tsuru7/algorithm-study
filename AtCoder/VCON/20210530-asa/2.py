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
    n=i_input()
    return n

def main(n):
    seikai = 0
    for i in range(1, 10):
        for j in range(1, 10):
            seikai += i*j
    fusoku = seikai - n
    ans=[]
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == fusoku:
                ans.append(str(i)+' x '+str(j))
    return sorted(ans)

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
