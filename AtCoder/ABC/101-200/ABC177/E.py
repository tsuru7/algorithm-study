from math import gcd

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def main(n,a):
    a.sort()
    setwise = True
    x = gcd(a[0], a[1])
    i = 2
    while i < n:
        x = gcd(x, a[i])
        i += 1
    if x != 1:
        setwise = False
        # print('case1', x)
    
    val = [0]*(10**6+1)
    pairwise = True
    e_count = 0
    for i in range(n):
        if a[i] % 2 == 0:
            e_count += 1
        val[a[i]] += 1
        if val[a[i]] > 1 and a[i] != 1:
            pairwise = False
            # print('case2')
            break
    if e_count > 1:
        pairwise = False
        # print('case3')
    
    if pairwise == True:
        for i in range(3, 10**6+1, 2):
            count = 0
            x = i
            while x <= 10**6:
                if val[x] > 0:
                    count += 1
                x += i
            if count > 1:
                pairwise = False
                # print('case4')
                break


    if pairwise == True:
        return 'pairwise coprime'
    elif setwise == True:
        return 'setwise coprime'
    else:
        return 'not coprime'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
