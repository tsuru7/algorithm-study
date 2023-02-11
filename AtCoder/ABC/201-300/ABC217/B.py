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
    s1 = input()
    s2 = input()
    s3 = input()
    return s1, s2, s3

def main(s1, s2, s3):
    three = set([s1, s2, s3])
    four = set(['ABC', 'ARC', 'AGC', 'AHC'])
    one = four - three
    return list(one)[0]

def printans(ans):
    print(ans)

if __name__=='__main__':
    s1, s2, s3=readinput()
    ans=main(s1, s2, s3)
    printans(ans)
