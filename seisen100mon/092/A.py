import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import Counter

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
    queries = []
    h=i_input()
    while h > 0:
        queries.append((h, [l_input() for _ in range(h)]))
        h=i_input()
    return queries

def judge_discard(row):
    counter = Counter(row)
    mc = counter.most_common(1)
    num, cnt = mc[0]
    if cnt < 3 or num == 0:
        return False, row, 0
    if cnt == 5:
        return True, [0 for _ in range(5)], 5*num

    tmp = 0
    for col in range(3):
        if row[col] == row[col+1] == row[col+2]:
            tmp += 1
    cnt = tmp+2
    if cnt == 4:
        if row[0] == num:
            return True, [0 for _ in range(4)] + [row[4]], 4*num
        else:
            return True, [row[0]] + [0 for _ in range(4)], 4*num
    else:
        for col in range(3):
            if row[col] == row[col+1] == row[col+2]:
                return True, row[:col] + [0 for _ in range(3)] + row[col+3:], 3*num
    return False, row, 0

def solve(queries):
    ans=[]
    for h, amap in queries:
        point = 0
        while True:
            # print(*amap)
            # print(f'point: {point}')
            # print()
            # 判定
            match = False
            for row in range(h):
                _match, amap[row], _point = judge_discard(amap[row])
                # print(f'match: {match}, amap[row]: {amap[row]}')
                point += _point
                match |= _match

            if not match:
                break
            # 下詰め
            for col in range(5):
                drop = 0
                for row in range(h)[::-1]:
                    if amap[row][col] == 0:
                        drop += 1
                    else:
                        if drop > 0:
                            amap[row+drop][col] = amap[row][col]
                            amap[row][col] = 0
        ans.append(point)

    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    queries=readinput()
    ans=solve(queries)
    printans(ans)
