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
    a,b,k=m_input()
    return a,b,k

def decode(x, keta):
    tmp = bin(x)[2:]
    tmp = ('0'*keta + tmp)[-keta:]
    # print(f'tmp: {tmp}, keta: {keta}')
    ans = ''
    for c in tmp:
        if c == '0':
            ans += 'a'
        else:
            ans += 'b'
    return ans


def solve(a,b,k):
    ans = []
    keta = a+b
    ALL = 2**keta
    for x in range(ALL):
        if bin(x).count('1') != b:
            continue
        ans.append(x)
    ans.sort()
    # print(f'ans: {ans}')
    return decode(ans[k-1], keta)

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,k=readinput()
    ans=solve(a,b,k)
    printans(ans)
