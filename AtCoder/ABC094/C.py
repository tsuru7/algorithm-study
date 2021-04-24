def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    x=l_input()
    return n,x

def main(n,x):
    xs = sorted(x)
    med1 = xs[n//2-1]
    med2 = xs[n//2]
    ans = []
    for i in range(n):
        if x[i] <= med1:
            ans.append(med2)
        else:
            ans.append(med1)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,x=readinput()
    ans=main(n,x)
    printans(ans)
