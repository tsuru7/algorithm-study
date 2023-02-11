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
    n,k=m_input()
    return n,k

def solve(n,k):
    '''
    N以下の整数の組(a, b)
    aをbで割った余りがK以上

    bを固定して考える
    bで割った余りがK以上ということから、bはK+1以上N以下ということがわかる
    a = b*Q + Rと書け、Rはb未満。RはK以上でもあるのでaはbの倍数+K以上b未満でN以下の数
    m = n//bとすると、(m-1)*(b-k) + (m*b + K+cがN以下になるようなcの個数)
    k = 0のときa = 0とならないように調整する
    これをbがK+1からNまでの和を取る
    '''

    ans=0
    for b in range(k+1, n+1):
        m = n//b
        ans += (m)*(b-k)
        if k == 0:
            ans -= 1
        # c = 0
        # while m*b+k+c <= n:
        #     ans += 1
        #     c += 1
        ans += max(0, n - m*b - k + 1)
        # print(f'b: {b}, m: {m}, ans: {ans}')
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k=readinput()
    ans=solve(n,k)
    printans(ans)
