import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    n,q,x=m_input()
    w = l_input()
    queries = [i_input() for _ in range(q)]
    return n,q,x,w,queries

def solve(n,q,x,w,queries):
    boxes = []
    calced = [False for _ in range(n)]
    w_all = sum(w)
    cumsum = [0]
    for i in range(2*n):
        j = i % n
        cumsum.append(cumsum[-1]+w[j])
    # print(f'w: {w}, w_all: {w_all}')
    # print(f'cumsum: {cumsum}')
    head = 0
    chain = []
    while not calced[head]:
        npoteto = (x // w_all) * n
        res = x % w_all
        idx = bisect_left(cumsum, cumsum[head]+res)
        npoteto += idx - head
        # print(f'head: {head}, res: {res}, idx: {idx}, npoteto: {npoteto}')
        boxes.append(npoteto)
        calced[head] = True
        chain.append(head)
        head = idx % n
    else:
        inloop = head
    idx = 0
    while chain[idx] != inloop:
        idx += 1
    loop_head = idx
    loop_len = len(chain) - loop_head
    # print(f'boxes: {boxes}')
    # print(f'before_loop: {before_loop}, loop_len: {loop_len}')
    ans=[]
    for k in queries:
        k -= 1
        if k < loop_head:
            ans.append(boxes[k])
        else:
            k -= loop_head
            ans.append(boxes[k % loop_len + loop_head])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,x,w,queries=readinput()
    ans=solve(n,q,x,w,queries)
    printans(ans)
