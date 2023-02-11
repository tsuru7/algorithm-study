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
    n,k=m_input()
    d=l_input()
    return n,k,d

def main(n,k,d):
    dislike = set(d)
    like = set(list(range(10)))
    like -= dislike
    like = sorted(list(like))
    # print(f'like: {like}')
    for n4 in like:
        for n3 in like:
            for n2 in like:
                for n1 in like:
                    tmp = n1 + n2*10 + n3*100 + n4*1000
                    if tmp >= n:
                        return tmp

    for n5 in like:
        for n4 in like:
            for n3 in like:
                for n2 in like:
                    for n1 in like:
                        tmp = n1 + n2*10 + n3*100 + n4*1000 + n5*10000
                        if tmp >= n:
                            return tmp
    

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,d=readinput()
    ans=main(n,k,d)
    printans(ans)
