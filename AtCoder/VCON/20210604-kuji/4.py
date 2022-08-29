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
    a,b,k=m_input()
    return a,b,k

def main(a,b,k):
    c = [[0]*60 for _ in range(60)]
    c[1][0] = 1
    c[1][1] = 1
    for i in range(2, 60):
        for j in range(i+1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1] + c[i-1][j]

    ans=''
    for i in range(a+b):
        if a == 0:
            ans += 'b'*b
            return ans
        if b == 0:
            ans += 'a'*a
            return ans
            
        cc = c[a+b-1][a-1]
        if k <= cc:
            ans += 'a'
            a -= 1
        else:
            k -= cc
            ans += 'b'
            b -= 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,k=readinput()
    ans=main(a,b,k)
    printans(ans)
