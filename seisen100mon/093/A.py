import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from copy import deepcopy

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
    h,w,k=m_input()
    cmap = [list(map(int, list(input()))) for _ in range(h)]
    return h,w,k,cmap

def scan_line(line, k):
    '''lineをスキャンして、k個以上の同じ数字の並びを検出する
    返り値　[(start, end, number), ...]
    
    '''
    # print(f'[scan_line] line: {line}, k: {k}')
    ans = []
    w = len(line)
    seq = False
    hit = False
    head = -1
    tail = -1
    for col in range(1, w):
        if line[col-1] > 0 and line[col-1] == line[col]:
            if not seq:
                seq = True
                head = col-1
                tail = col
            else:
                tail += 1
            if tail - head + 1 >= k:
                hit = True
        else:
            if hit:
                ans.append((head, tail, line[col-1]))
                hit = False
            seq = False
    else:
        if hit:
            ans.append((head, tail, line[col-1]))
    # print(f'[scan_line] ans: {ans}')
    # print()
    return ans



def judge(h, w, k, cmap):
    total = 0
    for row in range(h):
        hitList = scan_line(cmap[row], k)
        for head, tail, number in hitList:
            total += (tail - head + 1)*number
            for col in range(head, tail+1):
                cmap[row][col] = 0
    return total

def dropstone(h, w, cmap):
    for col in range(w):
        zeros = 0
        for row in range(h)[::-1]:
            if cmap[row][col] == 0:
                zeros += 1
            else:
                cmap[row+zeros][col] = cmap[row][col]
                if zeros > 0:
                    cmap[row][col] = 0
    return


def game(h, w, k, cmap):
    point = 0
    i = 0
    dropstone(h, w, cmap)
    # print(*cmap, sep='\n')
    tmp = judge(h, w, k, cmap)
    while tmp > 0:
        point += tmp*2**i
        dropstone(h, w, cmap)
        # print(*cmap, sep='\n')
        tmp = judge(h, w, k, cmap)
        i += 1
    return point

def solve(h,w,k,cmap):
    if k == 1:
        sum = 0
        cmin = INFTY
        for row in range(h):
            sum += sum(cmap[row])
            cmin = min(cmin, min(cmap[row]))
        return sum-cmin       

    ans=0
    for row in range(h):
        for col in range(w):
            tmp = deepcopy(cmap)
            tmp[row][col] = 0
            ans = max(ans, game(h, w, k, tmp))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,k,cmap=readinput()
    ans=solve(h,w,k,cmap)
    printans(ans)

    # line = [0, 1, 1, 2, 2, 0, 2, 4, 4, 2, 2, 2, 2]
    # ans = scan_line(line, 2)
    # print(ans)