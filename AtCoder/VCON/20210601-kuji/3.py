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
    h=l_input()
    return n,h

def main(n,h):
    ans=0
    for x in range(100):
        water = False
        for i in range(n):
            if h[i] > 0 and water == False:
                water = True
                ans += 1
                h[i] -= 1
                # print(f'x: {x}, i: {i}')
            elif h[i] > 0 and water == True:
                h[i] -= 1
            elif h[i] == 0:
                water = False
        # print(f'h: {h}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,h=readinput()
    ans=main(n,h)
    printans(ans)
