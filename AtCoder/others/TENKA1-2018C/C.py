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
    n=i_input()
    a = []
    for _ in range(n):
        a.append(i_input())
    return n,a

def main(n,a):
    ans = 0
    a.sort(reverse=True)
    if n % 2 == 0:
        for i in range(n//2-1):
            ans += 2*a[i]
        ans += a[n//2-1]
        ans -= a[n//2]
        for i in range(n//2+1, n):
            ans -= 2*a[i]
    else:
        ans1 = 0
        for i in range((n-1)//2):
            ans1 += 2*a[i]
            # print(f'i1: {i}')
        ans1 -= a[(n-1)//2]
        # print(f'i2: {(n-1)//2}')
        ans1 -= a[(n-1)//2+1]
        # print(f'i2: {(n-1)//2+1}')
        for i in range((n-1)//2+2, n):
            ans1 -= 2*a[i]
            # print(f'i3: {i}')

        ans2 = 0
        for i in range((n-1)//2-1):
            ans2 += 2*a[i]
            # print(f'i1: {i}')
        ans2 += a[(n-1)//2-1]
        # print(f'i2: {(n-1)//2-1}')
        ans2 += a[(n-1)//2]
        # print(f'i2: {(n-1)//2}')
        for i in range((n-1)//2+1, n):
            ans2 -= 2*a[i]
            # print(f'i3: {i}')
        ans = max(ans1, ans2)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans = main(n, a)
    printans(ans)
