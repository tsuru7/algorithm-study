def readinput():
    a=int(input())
    return a

def main(a):
    ans=a+a**2+a**3
    return ans

if __name__=='__main__':
    a=readinput()
    ans=main(a)
    print(ans)
