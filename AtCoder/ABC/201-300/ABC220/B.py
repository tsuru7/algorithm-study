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
    k=i_input()
    a,b=m_input()
    return k,a,b

def main(k,a,b):
    xa = 0
    digit = 0
    while a > 0:
        xa += (a % 10)*k**digit
        a = a // 10
        digit += 1
        # print(f'a: {a}, xa: {xa}')
    xb = 0
    digit = 0
    while b > 0:
        xb += (b % 10)*k**digit
        b = b // 10
        digit += 1
    # print(f'b: {b}, xb: {xb}')
    ans=xa*xb
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    k,a,b=readinput()
    ans=main(k,a,b)
    printans(ans)
