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
    h,w,k=m_input()
    smap = [input() for _ in range(h)]
    return h,w,k,smap

def bitpos(x):
    ans = []
    xb = bin(x)[::-1]
    for i, c in enumerate(xb):
        if c == '1':
            ans.append(i)
    # print(f'bitpos x: {x}, pos: {ans}')
    return ans

def grouping(bitpos_, h):
    ans = [0 for _ in range(h)]
    group = 0
    now = 0
    for pos in bitpos_:
        for next in range(now, pos+1):
            ans[next] = group
        now = next+1
        group += 1
    else:
        for next in range(now, h):
            ans[next] = group
    return ans


def solve(h,w,k,smap):
    hALL = 2**(h-1)
    mincut = INFTY
    for x in range(hALL):
        cut = bin(x).count('1')
        groupmap = grouping(bitpos(x), h)
        # print(f'x: {bin(x)}, groupmap: {groupmap}')
        whites = [0 for _ in range(h)]
        for col in range(w):
            row_whites = [0 for _ in range(h)]
            for row in range(h):
                row_whites[groupmap[row]] += int(smap[row][col])
            if max(row_whites) > k:
                cut = INFTY
                break
            for idx, cnt in enumerate(row_whites):
                whites[idx] += cnt
            if max(whites) > k:
                cut += 1
                whites = row_whites
        mincut = min(mincut, cut)
    return mincut


def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,k,smap=readinput()
    ans=solve(h,w,k,smap)
    printans(ans)
