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
    h1,w1=m_input()
    amat = [l_input() for _ in range(h1)]
    h2, w2 = m_input()
    bmat = [l_input() for _ in range(h2)]
    return h1,w1,h2,w2,amat,bmat

def bitcount(x):
    binx = bin(x)[2:]
    return binx.count('1')

def bitposition(x):
    binx = bin(x)[2:][::-1]
    ans = []
    for i, b in enumerate(binx):
        if b == '1':
            ans.append(i)
    return ans

def next_pos(now, pos):
    now += 1
    while now in pos:
        now += 1
    return now

def solve(h1,w1,h2,w2,amat,bmat):
    if h1 < h2 or w1 < w2:
        return 'No'
    hdiff = h1-h2
    wdiff = w1-w2
    hALL = 2**h1
    wALL = 2**w1

    # print(f'hALL: {hALL}, wALL: {wALL}, hdiff: {hdiff}, wdiff: {wdiff}')

    for hbit in range(hALL):
        if bitcount(hbit) != hdiff:
            continue
        hdiff_pos = bitposition(hbit)
        for wbit in range(wALL):
            if bitcount(wbit) != wdiff:
                continue
            wdiff_pos = bitposition(wbit)

            # print(f'hbit: {bin(hbit)}, wbit: {bin(wbit)}')
            # print(f'hdiff_pos: {hdiff_pos}, wdiff_pos: {wdiff_pos}')

            match = True
            row1 = -1
            for row in range(h2):
                row1 = next_pos(row1, hdiff_pos)
                col1 = -1
                for col in range(w2):
                    col1 = next_pos(col1, wdiff_pos)
                    if amat[row1][col1] != bmat[row][col]:
                        match = False
            if match:
                return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    h1,w1,h2,w2,amat,bmat=readinput()
    ans=solve(h1,w1,h2,w2,amat,bmat)
    printans(ans)
