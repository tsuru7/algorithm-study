def readinput():
    a=[]
    for i in range(3):
        l=list(map(int,input().split()))
        a.append(l)
    n=int(input())
    b=[]
    for _ in range(n):
        b.append(int(input()))
    return n,a,b

def main(n,a,b):
    sheet=[]
    for i in range(3):
        sheet.append([0,0,0])
    
    for i in range(n):
        for j in range(3):
            for k in range(3):
                if a[j][k]==b[i]:
                    sheet[j][k]=1
    
    bingo=False
    for i in range(3):
        if sheet[i][0]==1 and sheet[i][1]==1 and sheet[i][2]==1:
            bingo=True
        elif sheet[0][i]==1 and sheet[1][i]==1 and sheet[2][i]==1:
            bingo=True
    if sheet[0][0]==1 and sheet[1][1]==1 and sheet[2][2]==1:
        bingo=True
    if sheet[0][2]==1 and sheet[1][1]==1 and sheet[2][0]==1:
        bingo=True
    return bingo

if __name__=='__main__':
    n,a,b=readinput()
    ans=main(n,a,b)
    if ans == True:
        print('Yes')
    else:
        print('No')

    