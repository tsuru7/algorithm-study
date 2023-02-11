def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    return n

def main(n):
    x = 1
    ans = 10**5+1
    while x*x <= n:
        for y in range(1, n+1):
            if x*y > n:
                break
            ans = min(ans, abs(x-y)+n-x*y)
        x += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    printans(ans)
