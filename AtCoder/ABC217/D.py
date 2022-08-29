import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left
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
    l,q=m_input()
    queries = []
    for _ in range(q):
        queries.append(l_input())
    return l,q,queries

#ノードクラスの定義
class Node:
    def __init__(self, data): #コンストラクタ
        self.data = data #ノードがもつ数値
        self.left = None #左エッジ
        self.right = None #右エッジ

def main(l,q,queries):
    root = Node(0)
    root.right = Node(l)
    ans=[]
    # print(f'wood: {wood}')
    for c, x in queries:
        # print(f'c: {c}, x: {x}')
        i = bisect_left(wood, x)
        if c == 2:
            l = wood[i-1]
            r = wood[i]
            ans.append(r-l)
        else:
            wood.insert(i, x)
            # wood = wood[:i] + [x] + wood[i:]

        # print(f'wood: {wood}')

    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    l,q,queries=readinput()
    ans=main(l,q,queries)
    printans(ans)
