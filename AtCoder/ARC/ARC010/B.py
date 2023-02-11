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
    n=i_input()
    yasumi = []
    for _ in range(n):
        yasumi.append(list(map(int, input().split('/'))))
    return n,yasumi

def set_firstdays_2012():
    firstdays = [0]*12

    firstdays[0] = 0
    firstdays[1] = firstdays[0] + 31
    firstdays[2] = firstdays[1] + 29
    firstdays[3] = firstdays[2] + 31
    firstdays[4] = firstdays[3] + 30
    firstdays[5] = firstdays[4] + 31
    firstdays[6] = firstdays[5] + 30
    firstdays[7] = firstdays[6] + 31
    firstdays[8] = firstdays[7] + 31
    firstdays[9] = firstdays[8] + 30
    firstdays[10] = firstdays[9] + 31
    firstdays[11] = firstdays[10] + 30


    return firstdays

def set_yasumi(kyujitsu, doy):
    if not kyujitsu[doy]:
        kyujitsu[doy] = True
    else:
        while doy < 366 and kyujitsu[doy]:
            doy += 1
        if doy == 366:
            pass
        else:
            kyujitsu[doy] = True
    return kyujitsu


def main(n,yasumi):
    kyujitsu = [False]*366
    # Sun. and Sat.
    for i in range(0, 366, 7):
        kyujitsu[i] = True
        if i+6 < 366:
            kyujitsu[i+6] = True
    firstdays = set_firstdays_2012()

    # print(firstdays)

    yasumi.sort()
    # print(yasumi)

    for m, d in yasumi:
        m -= 1
        d -= 1
        dayofyear = firstdays[m]+d
        kyujitsu = set_yasumi(kyujitsu, dayofyear)

    # printdays(kyujitsu, firstdays)

    ans=0
    renkyu = False
    count = 0
    for d in range(366):
        if renkyu and kyujitsu[d]:
            count += 1
        elif kyujitsu[d]:
            renkyu = True
            count = 1
        elif renkyu:
            renkyu = False
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,yasumi=readinput()
    ans=main(n,yasumi)
    printans(ans)
