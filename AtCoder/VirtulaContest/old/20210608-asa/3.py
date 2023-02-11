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
    m = i_input()
    return m

def main(m):
    if m < 100:
        return '00'
    elif m <= 5000:
        return ('0'+str(m//100))[-2:]
    elif m <= 30000:
        return str(m//1000+50)
    elif m <= 70000:
        return str((m//1000-30)//5+80)
    else:
        return '89'

def printans(ans):
    print(ans)

if __name__=='__main__':
    m=readinput()
    ans=main(m)
    printans(ans)
