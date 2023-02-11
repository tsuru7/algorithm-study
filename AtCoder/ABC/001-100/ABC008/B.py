from collections import Counter

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    sList = []
    for _ in range(n):
        sList.append(input())
    return n,sList

def main(n,sList):
    candidates = Counter(sList)
    ans, count = candidates.most_common(1)[0]
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,sList=readinput()
    ans=main(n,sList)
    printans(ans)
