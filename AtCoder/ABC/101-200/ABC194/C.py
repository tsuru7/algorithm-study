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
    a.insert(0,0)
    s = [0]*(n+1)
    s2 = [0]*(n+1)
    s[1] = a[1]
    s2[1] = a[1]*a[1]
    for i in range(2, n+1):
        s[i] = s[i-1] + a[i]
        s2[i] = s2[i-1] + a[i]*a[i]
    # print(a,s,s2)
    sum = 0
    for i in range(2, n+1):
        sum += a[i]*a[i]*(i-1) - 2*a[i]*s[i-1] + s2[i-1] 
    return sum

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
