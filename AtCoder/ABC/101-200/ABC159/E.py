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

def rowcounts(col, pos, smap):
    h = len(smap)
    i = 0
    ans = []
    count = 0
    for row in range(h):
        if row > pos[i]:
            ans.append(count)
            i += 1
            count = 0
        if smap[row][col] == '1':
            count += 1
    else:
        ans.append(count)
    # print(f'col: {col}, pos: {pos}, ans: {ans}')
    return ans

def judge(x, h, w, k, smap):
    '''x回のカットで条件を満たせるか判定する'''

    hALL = 2**(h-1)
    mincut = INFTY
    for i in range(hALL):
        pos = bitpos(i) + [h-1]
        cut = len(pos)-1
        pieces = [0 for _ in range(h)]
        for col in range(w):
            tmp = rowcounts(col, pos, smap)
            if max(tmp) > k:
                # print(f'max(tmp): {max(tmp)}')
                mincut = INFTY
                break
            for i, cnt in enumerate(tmp):
                pieces[i] += cnt
            if max(pieces) > k:
                cut += 1
                pieces = tmp
            # print(f'pieces: {pieces}, cut: {cut}')
        mincut = min(mincut, cut)
        # print(f'mincut: {mincut}, cut: {cut}')
    # print(f'mincut: {mincut}, x: {x}')
    return mincut <= x
        

def solve(h,w,k,smap):
    ac = h*w
    wa = -1
    while ac - wa > 1:
        wj = (ac+wa)//2
        # wj回のカットで条件を満たせるか判定する
        if judge(wj, h, w, k, smap):
            ac = wj
        else:
            wa = wj
        # print(f'wa: {wa}, ac: {ac}')
    return ac

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,k,smap=readinput()
    ans=solve(h,w,k,smap)
    printans(ans)
