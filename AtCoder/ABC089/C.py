from collections import Counter
from itertools import combinations

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    name_heads = []
    for _ in range(n):
        name_heads.append(input()[0])
    return n, name_heads

def main(n,name_heads):
    counter = Counter(name_heads)
    combs = combinations('MARCH', 3)
    count = 0
    for comb in combs:
        temp = 1
        for c in comb:
            temp *= counter[c]
        count += temp
    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,name_heads=readinput()
    ans=main(n,name_heads)
    printans(ans)
