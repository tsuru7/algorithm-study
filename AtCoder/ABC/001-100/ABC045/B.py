def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    sa = input()
    sb = input()
    sc = input()
    return sa, sb, sc

def main(sa, sb, sc):
    ia = 0
    ib = 0
    ic = 0
    now = 'a'
    while True:
        if now == 'a':
            if ia == len(sa):
                return 'A'
            else:
                now = sa[ia]
                ia += 1
        elif now == 'b':
            if ib == len(sb):
                return 'B'
            else:
                now = sb[ib]
                ib += 1
        elif now == 'c':
            if ic == len(sc):
                return 'C'
            else:
                now = sc[ic]
                ic += 1

def printans(ans):
    print(ans)

if __name__=='__main__':
    sa, sb, sc=readinput()
    ans=main(sa, sb, sc)
    printans(ans)
