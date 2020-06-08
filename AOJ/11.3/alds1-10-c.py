import sys
sys.setrecursionlimit(2000)


def lcs(x,y):
    global c

    m=len(x)
    n=len(y)
    x='_'+x
    y='_'+y

    #for i in range(m+1):
    #    c[i][0] = 0
    c[:][0]=0
    #for j in range(n+1):
    #    c[0][j] = 0
    c[0]=[0]*(n+1)
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(x[i]==y[j]):
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]


n=int(input())

c=[]
for i in range(1001):
    cc = [0]*1001
    c.append(cc)

for i in range(n):
    x=input()
    y=input()
    print(lcs(x,y))

