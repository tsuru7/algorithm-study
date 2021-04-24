def readinput():
    k=int(input())
    return k

def makeLunlun(k):
    lunlun = [[str(i) for i in range(1, 10)]]
    count = len(lunlun[-1])
    while count < k:
        tmp = []
        for l in lunlun[-1]:
            n = int(l[-1])
            if n == 0:
                pass
                # tmp.append(l+'9')
            else:
                tmp.append(l+str(n-1))
            tmp.append(l+str(n))
            if n == 9:
                pass
                # tmp.append(l+'0')
            else:
                tmp.append(l+str(n+1))
        lunlun.append(tmp)
        count += len(tmp)
    tmp = []
    for l in lunlun:
        for ll in l:
            tmp.append(int(ll))
    return sorted(tmp)

def isLunlun(n):
    s = str(n)
    if len(s) == 1:
        return True
    for i in range(1, len(s)):
        if abs(int(s[i-1])-int(s[i])) <= 1:
            continue
        else:
            return False
    return True

def main2(k):
    count = 0
    i = 1
    while True:
        if isLunlun(i):
            count += 1
            if count == k:
                return i
        i += 1

    # lunlun = makeLunlun(k)
    # return lunlun[k-1]

def main(k):
    lunlun = makeLunlun(k)
    return lunlun[k-1]

def main3(k):
    from collections import deque
    queue = deque([i for i in range(1,10)])
    count = 0
    while True:
        v = queue.popleft()
        count += 1
        if count == k:
            return v
        q, r = divmod(v, 10)
        if r != 0:
            queue.append(v*10+r-1)
        queue.append(v*10+r)
        if r != 9:
            queue.append(v*10+r+1)
            

if __name__=='__main__':
    k=readinput()
    ans=main3(k)
    print(ans)
    # print(main2(k))