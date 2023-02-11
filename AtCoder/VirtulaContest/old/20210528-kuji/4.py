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
    k=i_input()
    return k

def main(k):
    if k % 2 == 0:
        return -1
    if k == 7:
        return 1
    if k == 1:
        return 1
    r = 7 % k
    sumr = 7 % k
    amari = [7 % k]
    for i in range(2, k+1):
        r = (10*r) % k
        amari.append(r)
        sumr += r
        # print(f'i: {i}, r: {r}, sumr: {sumr}, amari: {amari}')
        if sumr % k == 0:
            return i
    return -1

def printans(ans):
    print(ans)

if __name__=='__main__':
    k=readinput()
    ans=main(k)
    printans(ans)
