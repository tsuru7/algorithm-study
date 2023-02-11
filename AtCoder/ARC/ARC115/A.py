def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n, m = m_input()
    sList = []
    for _ in range(n):
        sList.append(input())
    return n,m,sList

def main(n,m,sList):
    count_e = 0
    count_o = 0
    for s in sList:
        count = 0
        for c in s:
            if c == '1':
                count += 1
        if count % 2 == 0:
            count_e += 1
        else:
            count_o += 1
    ans = count_e * count_o
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,sList=readinput()
    ans=main(n,m,sList)
    printans(ans)
