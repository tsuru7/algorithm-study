import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
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

def solve(n):
    keta = len(str(n))
    r = [[0 for _ in range(10)] for _ in range(keta)]
    for i in range(keta):
        di = n % 10**(i+1) // 10**i
        # print(di)
        for j in range(10):
            if j < di:
                r[i][j] = n//10**(i+1)*10**i + 10**i
            elif j == di:
                r[i][j] = n//10**(i+1)*10**i + n % 10**i + 1
            else:
                r[i][j] = n//10**(i+1)*10**i
    # print(r)
    ans=0
    for i in range(keta):
        for j in range(10):
            ans += r[i][j]*j

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
