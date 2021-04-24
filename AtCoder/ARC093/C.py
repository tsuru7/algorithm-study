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
    a.insert(0, 0)
    a.append(0)
    sum = 0
    for i in range(n+1):
        sum += abs(a[i]-a[i+1])
    ans = []
    for j in range(1, n+1):
        ans.append( sum - abs(a[j-1]-a[j]) - abs(a[j]-a[j+1]) + abs(a[j-1]-a[j+1]) )
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
