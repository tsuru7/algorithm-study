def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n, m = m_input()
    a=l_input()
    b=l_input()
    return n,m,a,b

def main(n,m,a,b):
    a.sort()
    b.sort()
    ia = 0
    for num in b:
        if ia >=n:
            return 'NO'
        while num > a[ia]:
            ia += 1
            if ia >= n:
                return 'NO'
        ia += 1
    return 'YES' 

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a,b=readinput()
    ans=main(n,m,a,b)
    printans(ans)
