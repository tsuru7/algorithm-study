import math
def myFactorization(n):
    '''nを素因数分解する

    戻り値: factDict = { prime1: exp1, prime2: exp2, ...} 
           n=(prime1)**exp1 * (prime2)**exp2 * ...
    '''

    factDict = {}
    temp=n
    cnt=0
    while(temp%2==0):
        temp=temp//2
        cnt+=1
    if(cnt>0):
        factDict[2] = cnt

    m=int(math.sqrt(n))+1
    for i in range(3,m+1,2):
        cnt=0
        while(temp%i==0):
            temp=temp//i
            cnt+=1
        if(cnt>0):
            factDict[i] = cnt
        if(temp==1):
            break
    if(temp>1):
        factDict[temp] = 1
    return factDict

def readinput():
    n = int(input())
    return n

def main(n):
    MOD = 10**9 + 7

    factorDict = {}
    for i in range(1, n+1):
        tempDict = myFactorization(i)
        for k, v in tempDict.items():
            if k in factorDict.keys():
                factorDict[k] += v
            else:
                factorDict[k] = v
    ans = 1
    for v in factorDict.values():
        ans = (ans * (v + 1))%MOD
    return ans

def printans(ans):
    print(ans)

if __name__ == '__main__':
    n = readinput()
    ans = main(n)
    printans(ans)
