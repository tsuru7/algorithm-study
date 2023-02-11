def readinput():
    x=int(input())
    return x

def main(x):
    ans = x % 100
    ans = 100 - ans
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    printans(ans)
