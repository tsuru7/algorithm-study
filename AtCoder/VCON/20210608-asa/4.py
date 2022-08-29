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
    a,b=m_input()
    return a,b

def g(a):
    ans = []
    for i in range(1, 41):
        if a >= 2**i:
            num1 = (a//2**i)*(2**(i-1)) + (a%(2**i)) - (2**(i-1)-1)
        else:
            num1 = 0
        ans.append(num1)
    return ans

def main(a,b):
    ans=0
    num1_a = g(a)
    num1_b = g(b)
    print(f'num1_a: {num1_a}, num1_b: {num1_b}')
    for i in range(1, 41):
        if (num1_a[i-1]-num1_b[i-1]) % 2 == 1:
           ans += 2**(i-1) 
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    printans(ans)
