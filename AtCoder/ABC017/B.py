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
    x = input()
    return x

def main(x):
    while len(x) > 0:
        if x[-1] == 'o' or x[-1] == 'k' or x[-1] == 'u':
            x = x[:-1]
        elif len(x) > 1 and x[-2:] == 'ch':
            x = x[:-2]
        else:
            return 'NO'
    return 'YES'

def printans(ans):
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    printans(ans)
