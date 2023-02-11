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
    h,w=m_input()
    smap = []
    for _ in range(h):
        smap.append(input())
    return h,w,smap

def main(h,w,smap):
    MOD = 998244353
    ans=1
    for k in range(2, h+w+1):
        count_red = 0
        count_blue = 0
        count_dot = 0
        for i in range(1, k):
            j = k - i
            if i > h or j > w:
                continue
            if smap[i-1][j-1] == 'R':
                count_red += 1
            elif smap[i-1][j-1] == 'B':
                count_blue += 1
            else:
                count_dot += 1
        if count_red > 0 and count_blue > 0:
            ans *= 0
        elif count_red == 0 and count_blue == 0:
            ans *= 2
            ans = ans % MOD
        else:
            pass
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,smap=readinput()
    ans=main(h,w,smap)
    printans(ans)
