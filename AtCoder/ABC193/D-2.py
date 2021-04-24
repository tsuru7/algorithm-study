def readinput():
    k=int(input())
    s = input()
    t = input()
    return k, s, t

def main(k, s, t):
    taka = [0]*10
    aoki = [0]*10
    nokori = [k]*10
    for i in range(4):
        c = int(s[i])
        taka[c] += 1
        nokori[c] -= 1
    for i in range(4):
        c = int(t[i])
        aoki[c] += 1
        nokori[c] -= 1
    # print(taka)
    # print(aoki)
    # print(nokori)

    takaTen = [0]*10
    for i in range(1, 10):
        ten = 0
        for j in range(1, 10):
            num = taka[j]
            if i == j:
                num += 1
            ten += j * 10**num
        takaTen[i] = ten

    aokiTen = [0]*10
    for i in range(1, 10):
        ten = 0
        for j in range(1, 10):
            num = aoki[j]
            if i == j:
                num += 1
            ten += j * 10**num
        aokiTen[i] = ten

    count = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if takaTen[i] > aokiTen[j]:
                if i == j:
                    if nokori[i] < 2:
                        continue
                    else:
                        count += nokori[i]*(nokori[i]-1)
                else:
                    count += nokori[i]*nokori[j]
    ans = count / ((9*k-8)*(9*k-9))
    return ans

def printq(q):
    for l in q:
        print(l)

def checkq(q):
    sum = 0
    for i in range(1, 10):
        for j in range(1, 10):
            sum += q[i][j]
    print(sum)

def printans(ans):
    print(ans)

if __name__=='__main__':
    k, s, t=readinput()
    ans=main(k, s, t)
    printans(ans)
