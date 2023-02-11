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
    n=i_input()
    return n

def solve(n):
    prob = [0 for _ in range(n)]
    prob[n-1] = 3.5
    for i in range(n-1)[::-1]:
        stop = 0
        cont = 0
        for j in range(1, 7):
            if j < prob[i+1]:
                cont += prob[i+1]
            else:
                stop += j
        prob[i] = (cont + stop)/6.0
    # print(f'prob: {prob}')
    return prob[0]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
