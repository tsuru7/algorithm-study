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
    n, s = input().split()
    n = int(n)
    return n,s

def main(n,s):
    ans=0
    for i in range(n):
        count_a = 0
        count_t = 0
        count_c = 0
        count_g = 0
        for j in range(i,n):
            c = s[j]
            if c == 'A':
                count_a += 1
            elif c == 'T':
                count_t += 1
            elif c == 'C':
                count_c += 1
            elif c == 'G':
                count_g += 1
            if count_a == count_t and count_c == count_g:
                ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    printans(ans)
