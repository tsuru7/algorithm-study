def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n,q=m_input()
    a=l_input()
    txy = []
    for _ in range(q):
        txy.append(l_input())
    return n,a,q,txy

def main(n,a,q,txy):
    cumsum = [0]*n
    cumsum[0] = a[0]
    for i in range(1, n):
        cumsum[i] = cumsum[i-1]^a[i]
    ans = []
    # print(a)
    # print(cumsum)
    b = [0]*n
    for t, x, y in txy:
        if t == 1:
            # for i in range(x-1, n):
            #     cumsum[i] = cumsum[i]^y
            b[x-1] = b[x-1]^y
        else:
            temp = cumsum[y-1]
            if x > 1:
                temp = temp^cumsum[x-2]
            for i in range(x-1, y):
                temp = temp^b[i]
            ans.append(temp)
        # print(cumsum, b)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,a,q,txy=readinput()
    ans=main(n,a,q,txy)
    printans(ans)
