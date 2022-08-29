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
    a=l_input()
    b=l_input()
    return n,a,b

def main(n,a,b):
    sum_a = sum(a)
    sum_b = sum(b)
    if sum_a < sum_b:
        return -1

    fusoku = 0
    ans = 0
    yobun = [0]*n
    for i in range(n):
        yobun[i] = a[i] - b[i]
        if yobun[i] < 0:
            fusoku += -yobun[i]
            ans += 1
    if ans == 0:
        return 0
    yobun.sort(reverse=True)
    for i in range(n):
        fusoku -= yobun[i]
        ans += 1
        if fusoku <= 0:
            return ans
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    printans(ans)
