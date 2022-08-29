import sys
sys.setrecursionlimit(10**5)
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
    n,m=m_input()
    smap = []
    for _ in range(n):
        smap.append(input())
    return n,m,smap

def dist(node1, node2):
    row1, col1 = node1
    row2, col2 = node2
    return abs(row1-row2)+abs(col1-col2)

def main(n,m,smap):
    nlist = [[] for _ in range(11)]
    for row in range(n):
        for col in range(m):
            c = smap[row][col]
            if c == 'S':
                num = 0
            elif c == 'G':
                num = 10
            else:
                num = int(c)
            nlist[num].append((row, col))
    dp = [[INFTY]*m for _ in range(n)]
    s_row, s_col = nlist[0][0]
    dp[s_row][s_col] = 0
    for num in range(1, 11):
        for node_row, node_col in nlist[num]:
            for prev_row, prev_col in nlist[num-1]:
                dp[node_row][node_col] = min(dp[node_row][node_col], dp[prev_row][prev_col]+dist((node_row, node_col), (prev_row, prev_col)))
    g_row, g_col = nlist[10][0]
    return dp[g_row][g_col] if dp[g_row][g_col] < INFTY else -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,smap=readinput()
    ans=main(n,m,smap)
    printans(ans)
