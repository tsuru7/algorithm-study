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

def main(s):
    words = set()
    for i in range(3):
        for j in range(3):
            if j == i:
                continue
            for k in range(3):
                if k == j or k == i:
                    continue
                word = s[i]+s[j]+s[k]
                words.add(word)

    ans=len(words)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
