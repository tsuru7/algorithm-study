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
    n=i_input()
    dice = []
    for _ in range(n):
        dice.append(l_input())
    return n,dice

def main(n,dice):
    count = 0
    pre = False
    for d1, d2 in dice:
        if d1 == d2:
            if pre:
                count += 1
                if count >= 3:
                    return 'Yes'
            else:
                pre = True
                count = 1
        else:
            pre = False
            count = 0
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,dice=readinput()
    ans=main(n,dice)
    printans(ans)
