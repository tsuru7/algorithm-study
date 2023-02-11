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
    s=input()
    return s

def solve(s):
    pins = dict()
    pins[7] = 1
    pins[4] = 2
    pins[2] = 3
    pins[8] = 3
    pins[1] = 4
    pins[5] = 4
    pins[3] = 5
    pins[9] = 5
    pins[6] = 6
    pins[10] = 7

    if s[0] == '1':
        return 'No'
    columns = [0 for _ in range(8)]
    for i in range(10):
        c = s[i]
        if c == '1':
            columns[pins[i+1]] += 1
    # print(f'columns: {columns}')
    col1 = 1
    while col1 < 8 and columns[col1] == 0:
        col1 += 1
    if col1 == 8:
        return 'No'

    col2 = col1 + 1
    while col2 < 8 and columns[col2] > 0:
        col2 += 1
    if col2 == 8:
        return 'No'
    
    col3 = col2 + 1
    while col3 < 8 and columns[col3] == 0:
        col3 += 1
    if col3 == 8:
        return 'No'
    else:
        return 'Yes'

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=solve(s)
    printans(ans)
