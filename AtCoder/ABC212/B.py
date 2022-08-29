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
    s = input()
    return s

def next(passwd):
    if passwd == 9:
        return 0
    else:
        return passwd + 1

def main(s):
    passwd = []
    for i in range(4):
        passwd.append(int(s[i]))
    # print(passwd)
    if passwd[0] == passwd[1] and passwd[1] == passwd[2] and passwd[2] == passwd[3]:
        return 'Weak'
    elif (passwd[1] == next(passwd[0])) and (passwd[2] == next(passwd[1])) and (passwd[3] == next(passwd[2])):
        # print(passwd[1] == next(passwd[0]))
        return 'Weak'
    else:
        return 'Strong'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
