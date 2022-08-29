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

def num_ones(x):
    x += 1
    ans = [0]*40
    for bit in range(40):
        base0 = 2**bit
        base1 = base0*2
        num = (x//base1)*base0 + max(0, x % base1 - base0)
        ans[bit] = num
    return ans

def main(a,b):
    if a == 0:
        bin_a = [0]*40
    else:
        bin_a = num_ones(a-1)
    if b == 0:
        bin_b = [0]*40
    else:
        bin_b = num_ones(b)
    # print(f'bin_a: {bin_a}')
    # print(f'bin_b: {bin_b}')
    ans=0
    for bit in range(40)[::-1]:
        ans *= 2
        if (bin_b[bit] - bin_a[bit]) % 2 != 0:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    printans(ans)
