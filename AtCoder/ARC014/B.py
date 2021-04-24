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
    n=i_input()
    words = []
    for _ in range(n):
        words.append(input())
    return n,words

def main(n,words):
    used = set()
    word1 = words[0]
    used.add(word1)
    for i in range(1, n):
        word2 = words[i]
        if (word2 in used) or (word1[-1] != word2[0]):
            if i % 2 == 0:
                return 'LOSE'
            else:
                return 'WIN'
        word1 = word2
        used.add(word2)
    return 'DRAW'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,words=readinput()
    ans=main(n,words)
    printans(ans)
