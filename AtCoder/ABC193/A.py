def readinput():
    a,b=map(int,input().split())
    return a,b

def main(a,b):
    nebiki = a - b
    waribiki = nebiki / a

    ans=waribiki * 100.0
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    printans(ans)
