import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from string import ascii_letters
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
    words = []
    for _ in range(n):
        words.append(input())
    return n,words

def main(n,words):
    prefix_dict = dict()
    suffix_dict = dict()
    for x in ascii_letters:
        for y in ascii_letters:
            for z in ascii_letters:
                prefix = suffix = x+y+z
                prefix_dict[prefix] = 0
                suffix_dict[suffix] = 0

    for word in words:
        prefix = word[:3]
        suffix = word[-3:]
        prefix_dict[prefix] += 1
        suffix_dict[suffix] += 1
    
    


    ans=0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,words=readinput()
    ans=main(n,words)
    printans(ans)
