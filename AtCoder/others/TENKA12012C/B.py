import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s=input()
    return s

def next_card(s, i):
    mark = s[i]
    if s[i+1] in ('2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A'):
        num = s[i+1]
        return mark, num, i+2
    if i+2 < len(s) and s[i+2] == '0':
        num = '10'
        return mark, num, i+3
    else:
        num = '1'
        return mark, num, i+2

def make_royal(s, m):
    sute = []
    mochi = []
    i = 0
    while i < len(s):
        mark, num, i = next_card(s, i)
        if mark != m:
            sute.append(mark+num)
        elif num not in ('10', 'J', 'Q', 'K', 'A'):
            sute.append(mark+num)
        else:
            mochi.append(mark+num)
            if len(mochi) == 5:
                break
    return sute


def main(s):
    sute = []
    for m in ['S', 'H', 'D', 'C']:
        sute.append(make_royal(s, m))
    minsute = 52
    minsute_i = 0
    for i, t in enumerate(sute):
        if minsute > len(t):
            minsute = len(t)
            minsute_i = i
    return ''.join(sute[minsute_i])

def printans(ans):
    if len(ans) == 0:
        print(0)
    else:
        print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
