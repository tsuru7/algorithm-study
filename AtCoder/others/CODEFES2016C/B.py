from heapq import heappush, heappop, heapify

def readinput():
    k, t = map(int, input().split())
    a = list(map(int, input().split()))
    return k, t, a

def main(k, t, a):
    
    hq = []
    for i in range(t):
        heappush(hq, -a[i])
    while len(hq) > 1:
        # print(hq)
        x = heappop(hq) + 1
        y = heappop(hq) + 1
        if x != 0:
            heappush(hq, x)
        if y != 0:
            heappush(hq, y)
    if len(hq) == 1:
        return -hq[0] - 1
    if len(hq) == 0:
        return 0

def main2(k, t, a):
    a.sort(reverse=True)
    ans = a[0] - 1
    ans = max(ans - (k-a[0]), 0)
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    k, t, a = readinput()
    ans = main2(k, t, a)
    printans(ans)
