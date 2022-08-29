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
    h,w,n=m_input()
    ab = []
    for _ in range(n):
        ab.append(l_input())
    return h,w,n,ab

def main(h,w,n,ab):
    row = dict()
    for i in range(n):
        a, b = ab[i]
        if a in row.keys():
            row[a].append((b, i+1))
        else:
            row[a] = [(b, i+1)]
    row_list = list(row.items())
    row_list.sort()

    # print(f'row_list: {row_list}')

    cols = dict()
    for row_ in range(len(row_list)):
        _, l = row_list[row_]
        for b, idx in l:
            if b in cols.keys():
                cols[b].append((idx, row_+1))
            else:
                cols[b] = [(idx, row_+1)]
    cols_list = list(cols.items())
    cols_list.sort()

    # print(f'cols_list: {cols_list}')

    ans = [None]*n
    for col_ in range(len(cols_list)):
        # print(f'cols_list[col_]: {cols_list[col_]}')
        _, l = cols_list[col_]
        for idx, row in l:
            # print(f'idx: {idx}, row: {row}')
            ans[idx-1] = (col_+1, row)
            # print(f'ans: {ans}')

    return ans

def printans(ans):
    for a in ans:
        print(' '.join(map(str, a)))

if __name__=='__main__':
    h,w,n,ab=readinput()
    ans=main(h,w,n,ab)
    printans(ans)
