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
    aa = []
    for i in range(n):
        aa.append((a[i], i+1))
    aa.sort(reverse=True, key=lambda x: x[0])
    ans=[]
    for _, i in aa:
        ans.append(i)
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
