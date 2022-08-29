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
    s=input()
    return s

def main(s):
    i = 0
    count = 0
    while i < len(s):
        if i+3 < len(s) and s[i:i+4] == 'ZONe':
            count += 1
            i += 4
        else:
            i += 1
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
