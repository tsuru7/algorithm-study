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
    n = input()
    k=i_input()
    return n,k

def solve(n,k):
    l = len(n)
    dpsm = [[0 for _ in range(l+1)] for _ in range(k+1)]
    dpeq = [[0 for _ in range(l+1)] for _ in range(k+1)]
    # dpsm[j: 1..k][i: 1..l]
    # dpeq[j: 1..k][i: 1..l]
    # i 桁目までみたとき、0 でない数字が 1..k 個となる数字の個数
    # i 桁目までみたとき、N より小さい場合を dpsm、 N と等しい場合を dpeq に保存する
    di = int(n[0])
    # 0 桁目までみたとき、0 でない数が 0 個になる個数は 1 個
    dpeq[0][0] = 1
    # 1 桁目以降
    for i in range(l):
        di = int(n[i])
        # smaller -> smaller
        for d in range(10):
            if d != 0:
                for j in range(k):
                    dpsm[j+1][i+1] += dpsm[j][i]
            else:
                for j in range(k+1):
                    dpsm[j][i+1] += dpsm[j][i]
        # equal -> smaller
        for d in range(di):
            if d != 0:
                for j in range(k):
                    dpsm[j+1][i+1] += dpeq[j][i]
            else:
                for j in range(k+1):
                    dpsm[j][i+1] += dpeq[j][i]
        # equal -> equal
        if di != 0:
            for j in range(k):
                dpeq[j+1][i+1] += dpeq[j][i]
        else:
            for j in range(k+1):
                dpeq[j][i+1] += dpeq[j][i]
    # print(dp[equal])
    # print(dp[smaller])
    return dpeq[k][l] + dpsm[k][l]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
