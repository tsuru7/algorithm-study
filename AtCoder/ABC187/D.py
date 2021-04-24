def readinput():
    n=int(input())
    abList = []
    for _ in range(n):
        a,b=map(int,input().split())
        abList.append((2*a+b,a))
    return n,abList

def main(n,abList):
    abList.sort(key=lambda x: x[0])
    # print(abList)
    s = [0]*(n+1)
    s[1] = abList[0][1]
    for i in range(1,n):
        s[i+1] = s[i] + abList[i][1]
    
    tokuhyoA = 0
    count = 0
    for i in range(n-1, -1, -1):
        tokuhyoA += abList[i][0] - abList[i][1]  # Ai + Bi
        count += 1
        if tokuhyoA > s[i]:
            return count

if __name__=='__main__':
    n,abList=readinput()
    ans=main(n,abList)
    print(ans)
