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
    s = input()
    return s

def main(s):
    must = set()
    fumei = set()
    never = set()
    for i in range(10):
        if s[i] == 'o':
            must.add(i)
        elif s[i] == '?':
            fumei.add(i)
        else:
            never.add(i)
    m = len(must)
    f = len(fumei)
    if len(must) > 4:
        return 0
    # if len(never) > 7:
    #     return 0
    candidate = list(must)+list(fumei)
    # print(candidate)
    angou = ''
    count = 0
    for a in candidate:
        for b in candidate:
            for c in candidate:
                for d in candidate:
                    angou = str(a)+str(b)+str(c)+str(d)
                    for e in must:
                        if str(e) not in angou:
                            break
                    else:
                        count += 1

    return count

def printans(ans):
    print(ans)

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    printans(ans)
