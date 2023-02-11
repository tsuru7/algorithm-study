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
    s = [input() for _ in range(4)]
    return s

def main(s):
    count = [0]*4
    compare = ['H', '2B', '3B', 'HR']
    for i in range(4):
        for j in range(4):
            if s[i] == compare[j]:
                count[j] += 1
                if count[j] > 1:
                    return 'No'
    return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
